import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_bio_mhd_mesh(magnet_count, gap_width, pitch_angle, resolution=360):
    """
    Calculates the 3D positioning nodes for the internal double-helical 
    propulsion electrodes inside the bio-induction sleeve.
    Coils the electrical vectors to match the natural spiral of the blood.
    """
    propulsion_nodes = []
    pitch_rad = math.radians(pitch_angle)
    
    # Internal bore reference matching the atrial outlet boundary (22mm diameter)
    bore_diameter_mm = 22.0
    bore_radius_mm = bore_diameter_mm / 2.0
    
    # Total length of the MHD accelerator section is 30mm
    total_len_z = 30.0
    pitch_length_z = math.pi * bore_diameter_mm * math.tan(pitch_rad)
    
    for mag_idx in range(magnet_count):
        # Evenly map the 4 miniature N52 magnetic sectors along the Z-axis
        z_start = -(mag_idx * (total_len_z / magnet_count))
        z_mid = z_start - ((total_len_z / magnet_count) / 2.0)
        polarity = 1 if (mag_idx % 2 == 0) else -1
        
        for step in range(resolution):
            theta = (step * 2.0 * math.pi) / resolution
            
            # Double helix uses two starts offset by 180 degrees (Pi radians)
            helix_angle_1 = (abs(z_mid) / pitch_length_z) * 2.0 * math.pi
            helix_angle_2 = helix_angle_1 + math.pi
            
            is_helix_electrode = False
            for h_angle in [helix_angle_1, helix_angle_2]:
                wrapped_h_angle = h_angle % (2.0 * math.pi)
                if abs(theta - wrapped_h_angle) < (2.0 * math.pi / 36.0): # 10-degree tolerance band
                    is_helix_electrode = True
                    
            if is_helix_electrode:
                node_type = "MHD_Biocompatible_Glassy_Carbon_Electrode_Trace"
            else:
                node_type = f"Coaxial_N52_Magnetic_Field_Node_{'North' if polarity > 0 else 'South'}"
                
            x = bore_radius_mm * math.cos(theta)
            y = bore_radius_mm * math.sin(theta)
            
            propulsion_nodes.append({
                "magnet_index": mag_idx,
                "node_classification": node_type,
                "telemetry": {
                    "center_line_z_mm": round(z_mid, 4),
                    "local_polarity_factor": polarity,
                    "induction_angle_rad": round(theta, 4)
                },
                "vector_coordinate": (round(x, 4), round(y, 4), round(z_mid, 4))
            })
            
    return propulsion_nodes

def main():
    print("=" * 65)
    print("INITIALIZING: ARVH-02 MHD PROPULSION FIELD ENGINE")
    print("=" * 65)
    
    config_path = get_local_path("mhd-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        mag_count = config["electromagnetic_parameters"]["ring_magnets_count"]
        gap_width = config["electromagnetic_parameters"]["magnetic_gap_width_mm"]
        pitch_angle = config["harvesting_interface"]["helical_pitch_angle_deg"]
        material = config["manufacturing_profile"]["recommended_material"]
        print("[+] Medical Component ID ARVH-02 configuration card matched.")
    else:
        print("[⚠️] WARNING: mhd-config.json missing. Loading safe overrides.")
        mag_count = 4
        gap_width = 24.5
        pitch_angle = 35.0
        material = "Medical_PEEK"
        
    print(f"[*] Core Housing Material: {material}")
    print(f"[*] Electrode Geometry:    {pitch_angle}° Double Helical Track")
    print(f"[*] Compiling biocompatible Lorentz force propulsion fields...")
    
    propulsion_mesh = generate_bio_mhd_mesh(mag_count, gap_width, pitch_angle)
    audit_sample = [n for n in propulsion_mesh if n["node_classification"] == "MHD_Biocompatible_Glassy_Carbon_Electrode_Trace"][0]
    
    print("\n[+] SUCCESS: Electrodynamic propulsion matrix compiled cleanly.")
    print(f"[-] Total coordinated structural nodes logged: {len(propulsion_mesh)}")
    print(f"[-] ARVH-02 Optimized Node Balance Audit:")
    print(f"    ↳ Active Node Target:       {audit_sample['node_classification']}")
    print(f"    ↳ Target Field Centerline:  {audit_sample['telemetry']['center_line_z_mm']} mm")
    print("=" * 65)

if __name__ == "__main__":
    main()
  

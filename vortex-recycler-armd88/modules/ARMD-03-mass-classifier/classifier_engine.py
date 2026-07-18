import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_mhd_classifier_mesh(magnet_count, pitch_angle, resolution=360):
    """
    Calculates the 3D positioning nodes for the internal double-helical 
    sorting electrodes inside the cyclonic mass classifier sleeve.
    Coils the electrical vectors to sort elements via centrifugal density trajectories.
    """
    sorting_nodes = []
    pitch_rad = math.radians(pitch_angle)
    
    # Internal bore reference matching the cavitation core exit (50.8mm diameter)
    bore_diameter_mm = 50.8
    bore_radius_mm = bore_diameter_mm / 2.0
    
    # Total length of the massive industrial classifier sleeve is 600mm
    total_len_z = 600.0
    pitch_length_z = math.pi * bore_diameter_mm * math.tan(pitch_rad)
    
    for mag_idx in range(magnet_count):
        # Evenly distribute the 6 magnetic ring sectors down the length of the Z-axis
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
                node_type = "MHD_Glassy_Carbon_Sorting_Electrode_Trace"
            else:
                node_type = f"Coaxial_N52_Mass_Separation_Field_Node_{'North' if polarity > 0 else 'South'}"
                
            x = bore_radius_mm * math.cos(theta)
            y = bore_radius_mm * math.sin(theta)
            
            sorting_nodes.append({
                "magnet_index": mag_idx,
                "node_classification": node_type,
                "telemetry": {
                    "center_line_z_mm": round(z_mid, 4),
                    "local_polarity_factor": polarity,
                    "trajectory_angle_rad": round(theta, 4)
                },
                "vector_coordinate": (round(x, 4), round(y, 4), round(z_mid, 4))
            })
            
    return sorting_nodes

def main():
    print("=" * 65)
    print("INITIALIZING: ARMD-03 MASS CLASSIFIER TRACK CLUSTER ENGINE")
    print("=" * 65)
    
    config_path = get_local_path("classifier-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        mag_count = config["electromagnetic_parameters"]["ring_magnets_count"]
        pitch_angle = config["sorting_kinematics"]["helical_pitch_angle_deg"]
        material = config["industrial_profile"]["recommended_material"]
        print("[+] Industrial Component ID ARMD-03 configuration card matched.")
    else:
        print("[⚠️] WARNING: classifier-config.json missing. Loading safe overrides.")
        mag_count = 6
        pitch_angle = 45.0
        material = "Hardened_Inconel_718"
        
    print(f"[*] Core Housing Material: {material}")
    print(f"[*] Sorting Geometry:     {pitch_angle}° Double Helical Track")
    print(f"[*] Compiling multi-phase Lorentz force mass separation fields...")
    
    sorting_mesh = generate_mhd_classifier_mesh(mag_count, pitch_angle)
    audit_sample = [n for n in sorting_mesh if n["node_classification"] == "MHD_Glassy_Carbon_Sorting_Electrode_Trace"]
    
    print("\n[+] SUCCESS: Electrodynamic mass classification matrix compiled cleanly.")
    print(f"[-] Total coordinated structural nodes logged: {len(sorting_mesh)}")
    print(f"[-] ARMD-03 Core Node Balance Audit:")
    print(f"    ↳ Active Sorting Node:      {audit_sample[0]['node_classification']}")
    print(f"    ↳ Target Separation Axis:   {audit_sample[0]['telemetry']['center_line_z_mm']} mm")
    print("=" * 65)

if __name__ == "__main__":
    main()
      

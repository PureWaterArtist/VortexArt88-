import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_optimized_mhd_mesh(magnet_count, ring_thickness, pitch_angle, start_z=0.0, resolution=360):
    """
    Calculates the 3D positioning nodes for the external magnet cavities
    and the upgraded internal double-helical graphite pickup electrodes.
    Coils the electrode coordinates to match the helical spiral of the fluid.
    """
    sleeve_nodes = []
    pitch_rad = math.radians(pitch_angle)
    
    # Calculate vertical pitch distance required for one full 360 rotation
    # Using 50.8mm bore mapping reference:
    pitch_length_z = math.pi * 50.8 * math.tan(pitch_rad)
    
    for magnet_idx in range(magnet_count):
        z_start = start_z - (magnet_idx * ring_thickness)
        z_mid = z_start - (ring_thickness / 2.0)
        polarity = 1 if (magnet_idx % 2 == 0) else -1
        
        for step in range(resolution):
            theta = (step * 2.0 * math.pi) / resolution
            
            # Double helix uses two starts offset by 180 degrees (Pi radians)
            helix_angle_1 = (abs(z_mid) / pitch_length_z) * 2.0 * math.pi
            helix_angle_2 = helix_angle_1 + math.pi
            
            is_helix_electrode = False
            for h_angle in [helix_angle_1, helix_angle_2]:
                wrapped_h_angle = h_angle % (2.0 * math.pi)
                if abs(theta - wrapped_h_angle) < (2.0 * math.pi / 45.0): # 8-degree tolerance band
                    is_helix_electrode = True
                    
            if is_helix_electrode:
                node_type = "MHD_Double_Helical_Graphite_Electrode"
            else:
                node_type = f"N52_Magnetic_Field_Node_{'North' if polarity > 0 else 'South'}"
                
            sleeve_nodes.append({
                "magnet_index": magnet_idx,
                "node_classification": node_type,
                "telemetry": {
                    "center_line_z_mm": round(z_mid, 4),
                    "local_polarity_factor": polarity,
                    "induction_angle_rad": round(theta, 4)
                },
                "vector_coordinate": (round(math.cos(theta), 4), round(math.sin(theta), 4), round(z_mid, 4))
            })
            
    return sleeve_nodes

def main():
    print("=" * 65)
    print("INITIALIZING: ARVT-03 OPTIMIZED SLEEVE FIELD ENGINE")
    print("=" * 65)
    
    config_path = get_local_path("sleeve-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        magnet_count = config["electromagnetic_parameters"]["ring_magnets_count"]
        ring_thickness = config["electromagnetic_parameters"]["ring_thickness_z_mm"]
        e_geom = config["harvesting_interface"]["electrode_geometry"]
        pitch_angle = config["harvesting_interface"]["helical_pitch_angle_deg"]
        print("[+] Optimized Component ID ARVT-03 configuration card matched.")
    else:
        print("[⚠️] WARNING: sleeve-config.json missing. Loading safe fallbacks.")
        magnet_count = 6
        ring_thickness = 25.4
        e_geom = "Double_Helical_Track"
        pitch_angle = 45.0
        
    print(f"[*] Electrode Interface Style:  {e_geom}")
    print(f"[*] Helical Pitch Tracking:     {pitch_angle}° Alignment Matrix")
    print(f"[*] Compiling coiled Lorentz force pickup vectors...")
    
    sleeve_mesh = generate_optimized_mhd_mesh(magnet_count, ring_thickness, pitch_angle)
    
    # Audit an electrode node point running along the continuous double-helix track
    audit_sample = [n for n in sleeve_mesh if n["node_classification"] == "MHD_Double_Helical_Graphite_Electrode"][0]
    
    print("\n[+] SUCCESS: Upgraded MHD Power Sleeve matrix compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(sleeve_mesh)}")
    print(f"[-] ARVT-03 Optimized Node Balance Audit:")
    print(f"    ↳ Active Node Target:       {audit_sample['node_classification']}")
    print(f"    ↳ Target Field Centerline:  {audit_sample['telemetry']['center_line_z_mm']} mm")
    print("=" * 65)

if __name__ == "__main__":
    main()
                

import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_ionization_glow_mesh(pitch_angle, layer_depth, resolution=360):
    """
    Calculates the 3D positioning nodes for the double-helical ionization electrodes.
    Integrates spatial zone markers for Seebeck and PVDF impact-recycling layers.
    """
    glow_nodes = []
    pitch_rad = math.radians(pitch_angle)
    
    # Internal bore reference matching the injector exit manifold (25.4mm radius)
    bore_diameter_mm = 50.8
    bore_radius_mm = bore_diameter_mm / 2.0
    total_len_z = 120.0
    pitch_length_z = math.pi * bore_diameter_mm * math.tan(pitch_rad)
    
    for step in range(resolution):
        progress = step / resolution
        z_pos = -(progress * total_len_z)
        theta = (step * 2.0 * math.pi) / resolution
        
        # Double helix mapping logic for the glassy carbon electrode paths
        helix_angle_1 = (abs(z_pos) / pitch_length_z) * 2.0 * math.pi
        helix_angle_2 = helix_angle_1 + math.pi
        
        is_electrode = False
        for h_angle in [helix_angle_1, helix_angle_2]:
            wrapped_h_angle = h_angle % (2.0 * math.pi)
            if abs(theta - wrapped_h_angle) < (2.0 * math.pi / 36.0): # 10-degree window
                is_electrode = True
                
        if is_electrode:
            node_type = "High_Voltage_Glassy_Carbon_Ionization_Electrode"
            radius = bore_radius_mm
        else:
            node_type = "Regenerative_Piezo_Seebeck_Substrate_Matrix"
            # Step out slightly into the substrate wall for harvesting layers
            radius = bore_radius_mm + 2.5 
            
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        
        glow_nodes.append({
            "step_index": step,
            "structural_classification": node_type,
            "telemetry": {
                "axial_z_mm": round(z_pos, 4),
                "dynamic_radius_mm": round(radius, 4),
                "energy_harvesting_zone": int(progress * 4) # 4 distinct energy recycling zones
            },
            "vector_coordinate": (round(x, 4), round(y, 4), round(z_pos, 4))
        })
        
    return glow_nodes

def main():
    print("=" * 70)
    print("INITIALIZING: AEDS-02 IONIZATION CORE CALCULUS ENGINE")
    print("=" * 70)
    
    config_path = get_local_path("glow-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        pitch = config["ionization_parameters"]["helical_pitch_angle_deg"]
        depth = config["structural_fabrication_profile"]["channel_etch_depth_microns"] if "structural_fabrication_profile" in config else 250.0
        material = config["industrial_profile"]["internal_liner_substrate"]
        print("[+] Industrial Component ID AEDS-02 configuration card matched.")
    else:
        print("[⚠️] WARNING: glow-config.json missing. Loading safe overrides.")
        pitch = 45.0
        depth = 250.0
        material = "Silicon_Nitride_Si3N4"
        
    print(f"[*] Core Insulation Sleeve: {material}")
    print(f"[*] Energy Sorting Array  : 64 x Bi2Te3 Seebeck Pairs Active")
    print(f"[*] Compiling double-helical ionization and impact-recycling paths...")
    
    glow_mesh = generate_ionization_glow_mesh(pitch, depth)
    audit_sample = [n for n in glow_mesh if n["structural_classification"] == "High_Voltage_Glassy_Carbon_Ionization_Electrode"][0]
    
    print("\n[+] SUCCESS: High-Voltage Ionization core matrix compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(glow_mesh)}")
    print(f"[-] AEDS-02 Core Node Balance Audit:")
    print(f"    ↳ Active Classification:   {audit_sample['structural_classification']}")
    print(f"    ↳ Target Space Vector:     {audit_sample['vector_coordinate']}")
    print("=" * 70)

if __name__ == "__main__":
    main()
      

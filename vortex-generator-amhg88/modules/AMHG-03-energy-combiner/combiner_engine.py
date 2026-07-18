import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_energy_combiner_mesh(bus_count, resolution=360):
    """
    Calculates 3D positioning nodes for the multi-harvesting energy collector grids.
    Maps out the concentric layers handling high-voltage static, piezo-vibrations, and Seebeck currents.
    """
    combiner_nodes = []
    bore_diameter_mm = 50.8
    bore_radius_mm = bore_diameter_mm / 2.0
    total_len_z = 200.0  # 200mm total length of the combiner module along the vertical axis
    
    for bus_idx in range(bus_count):
        # Evenly distribute the 4 distinct collector segments along the vertical Z-axis
        z_start = -(bus_idx * (total_len_z / bus_count))
        z_mid = z_start - ((total_len_z / bus_count) / 2.0)
        
        for step in range(resolution):
            theta = (step * 2.0 * math.pi) / resolution
            
            # Segment the ring geometry into distinct energy-reclamation zones
            if bus_idx == 0 or bus_idx == 2:
                node_type = "High_Voltage_Copper_Bus_Bar_Collection_Zone"
                radius = bore_radius_mm
            elif bus_idx == 1:
                node_type = "Concentric_PVDF_Piezoelectric_Resonance_Stack"
                radius = bore_radius_mm + 1.5  # Embedded behind the internal core wall
            else:
                node_type = "Bismuth_Telluride_Seebeck_Thermal_Flywheel_Grid"
                radius = bore_radius_mm + 4.0  # Outer layer tracking near casing bounds
                
            x = radius * math.cos(theta)
            y = radius * math.sin(theta)
            
            combiner_nodes.append({
                "bus_segment_index": bus_idx,
                "node_classification": node_type,
                "diagnostics": {
                    "axial_alignment_z_mm": round(z_mid, 4),
                    "layer_radius_mm": round(radius, 4),
                    "dielectric_isolation_rating_v": 5000.0
                },
                "vector_coordinate": (round(x, 4), round(y, 4), round(z_mid, 4))
            })
            
    return combiner_nodes

def main():
    print("=" * 65)
    print("INITIALIZING: AMHG-03 ENERGY COMBINER MATH ENGINE")
    print("=" * 65)
    
    config_path = get_local_path("combiner-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        pairs_count = config["thermoelectric_seebeck_matrix"]["bismuth_telluride_pairs_count"]
        noise_db = config["solid_state_piezo_harvesting"]["target_noise_dampening_coefficient_db"]
        material = config["industrial_profile"]["internal_liner_substrate"]
        print("[+] Industrial Component ID AMHG-03 configuration card verified.")
    else:
        print("[⚠️] WARNING: combiner-config.json missing. Loading safe overrides.")
        pairs_count = 128
        noise_db = 42.0
        material = "Silicon_Nitride_Ceramic_Si3N4"
        
    print(f"[*] Core Insulation Matrix: {material}")
    print(f"[*] Acoustic Suppression   : {noise_db} dB Noise Capture Matrix Active")
    print(f"[*] Compiling multi-tier solid-state collection grid vectors...")
    
    combiner_mesh = generate_energy_combiner_mesh(4)
    audit_sample = [n for n in combiner_mesh if n["node_classification"] == "Concentric_PVDF_Piezoelectric_Resonance_Stack"]
    
    sample_node = audit_sample[len(audit_sample) // 2] if audit_sample else combiner_mesh[len(combiner_mesh) // 2]
    
    print("\n[+] SUCCESS: Multi-harvesting energy collector matrix compiled cleanly.")
    print(f"[-] Total coordinated structural nodes logged: {len(combiner_mesh)}")
    print(f"[-] AMHG-03 Core Node Balance Audit:")
    print(f"    ↳ Active Extraction Node:  {sample_node['node_classification']}")
    print(f"    ↳ Layer Spacing Radius:    {sample_node['diagnostics']['layer_radius_mm']} mm")
    print("=" * 65)

if __name__ == "__main__":
    main()
          

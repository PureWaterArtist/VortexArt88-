import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_magnetic_bottle_mesh(magnet_count, resolution=360):
    """
    Calculates the 3D positioning nodes for the coaxial N52 magnet arrays.
    Maps out the magnetic containment boundaries and Venturi shock-siphoning fields.
    """
    bottle_nodes = []
    bore_diameter_mm = 50.8
    bore_radius_mm = bore_diameter_mm / 2.0
    total_len_z = 150.0  # 150mm total longitudinal confinement sleeve height
    
    for mag_idx in range(magnet_count):
        # Evenly distribute the 6 magnetic ring sectors along the Z-axis
        z_start = -(mag_idx * (total_len_z / magnet_count))
        z_mid = z_start - ((total_len_z / magnet_count) / 2.0)
        polarity = 1 if (mag_idx % 2 == 0) else -1
        
        for step in range(resolution):
            theta = (step * 2.0 * math.pi) / resolution
            
            # Map out the asymmetric Venturi siphoning collar tracks near the upper output lip
            if abs(z_mid) < (total_len_z * 0.20):
                node_type = "Asymmetric_Venturi_Shock_Siphoning_Collar_Node"
                radius = bore_radius_mm - 1.5  # Constrict radius slightly to form the Venturi throat
            else:
                node_type = f"Coaxial_N52_Magnetic_Confinement_Node_{'North' if polarity > 0 else 'South'}"
                radius = bore_radius_mm + 3.0  # Positioned slightly back into the chassis track
                
            x = radius * math.cos(theta)
            y = radius * math.sin(theta)
            
            bottle_nodes.append({
                "magnet_index": mag_idx,
                "node_classification": node_type,
                "telemetry": {
                    "center_line_z_mm": round(z_mid, 4),
                    "local_polarity_factor": polarity,
                    "trajectory_angle_rad": round(theta, 4)
                },
                "vector_coordinate": (round(x, 4), round(y, 4), round(z_mid, 4))
            })
            
    return bottle_nodes

def main():
    print("=" * 65)
    print("INITIALIZING: AEDS-03 MAGNETIC BOTTLE FIELD ENGINE")
    print("=" * 65)
    
    config_path = get_local_path("bottle-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        mag_count = config["magnetic_containment"]["ring_magnets_count"]
        siphon_eff = config["venturi_shock_siphoning"]["pneumatic_siphoning_efficiency_pct"]
        material = config["industrial_profile"]["recommended_material"]
        print("[+] Industrial Component ID AEDS-03 configuration card matched.")
    else:
        print("[⚠️] WARNING: bottle-config.json missing. Loading safe fallbacks.")
        mag_count = 6
        siphon_eff = 94.5
        material = "Hardened_Inconel_718"
        
    print(f"[*] Core Housing Metallurgy: {material}")
    print(f"[*] Shock Siphoning Yield  : {siphon_eff}% Non-Mechanical Vacuum Lift")
    print(f"[*] Compiling multi-phase Lorentz force plasma confinement fields...")
    
    bottle_mesh = generate_magnetic_bottle_mesh(mag_count)
    audit_sample = [n for n in bottle_mesh if n["node_classification"] == "Asymmetric_Venturi_Shock_Siphoning_Collar_Node"]
    
    # Check if list is empty to provide safe fallback log printing
    sample_node = audit_sample if audit_sample else bottle_mesh[len(bottle_mesh) // 2]
    
    print("\n[+] SUCCESS: Coaxial magnetic bottle confinement matrix compiled cleanly.")
    print(f"[-] Total coordinated structural nodes logged: {len(bottle_mesh)}")
    print(f"[-] AEDS-03 Core Node Balance Audit:")
    print(f"    ↳ Active Containment Node:  {sample_node['node_classification']}")
    print(f"    ↳ Target Confinement Axis:  {sample_node['telemetry']['center_line_z_mm']} mm")
    print("=" * 65)

if __name__ == "__main__":
    main()
          

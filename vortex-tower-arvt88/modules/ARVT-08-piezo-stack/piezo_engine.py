import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_piezo_junction_vectors(rings, outer_dia, inner_dia, thickness, resolution=360):
    """
    Calculates 3D spatial vectors for the piezoelectric structural housings.
    Maps out the precise compression collars that sandwich the ceramic PZT rings
    directly at the inter-module high-vibration junction flanges.
    """
    housing_nodes = []
    r_out = outer_dia / 2.0
    r_in = inner_dia / 2.0
    
    for ring_idx in range(rings):
        # Position the stacks at alternating module junction thresholds vertically
        z_base = -(ring_idx * 500.0) # Stacked every 500mm down the tower
        
        for step in range(resolution):
            theta = (step * 2.0 * math.pi) / resolution
            
            # Formulate structural locking keyways every 90 degrees
            if step % 90 == 0:
                node_type = "Piezo_Chassis_Anti_Rotational_Keyway"
                radius = r_out + 3.0
            else:
                node_type = f"PZT_Ceramic_Compression_Seat_Ring_{ring_idx + 1}"
                radius = (r_out + r_in) / 2.0 # Concentric centerline
                
            x = radius * math.cos(theta)
            y = radius * math.sin(theta)
            
            housing_nodes.append({
                "ring_index": ring_idx,
                "node_classification": node_type,
                "telemetry": {
                    "junction_elevation_z_mm": round(z_base, 4),
                    "collar_clearance_mm": round(thickness, 2)
                },
                "vector": (round(x, 4), round(y, 4), round(z_base, 4))
            })
            
    return housing_nodes

def main():
    print("=" * 65)
    print("INITIALIZING: ARVT-08 PIEZOELECTRIC HYDRO-STACK ENGINE")
    print("=" * 65)
    
    config_path = get_local_path("piezo-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        rings = config["piezo_geometry"]["stack_rings_count"]
        outer_dia = config["piezo_geometry"]["ring_outer_diameter_mm"]
        inner_dia = config["piezo_geometry"]["ring_inner_diameter_mm"]
        thickness = config["piezo_geometry"]["ring_thickness_z_mm"]
        material = config["manufacturing_profile"]["recommended_material"]
        print("[+] Component ID ARVT-08 piezo parameters matched successfully.")
    else:
        print("[⚠️] WARNING: piezo-config.json missing. Loading safe overrides.")
        rings = 4
        outer_dia = 65.0
        inner_dia = 51.5
        thickness = 5.0
        material = "CF-PC"
        
    print(f"[*] Substrate Material Standard: {material}")
    print(f"[*] Piezo Active Array Ring:     {rings} x High-Strain PZT Crystals")
    print(f"[*] Compiling high-pressure compression junction ring meshes...")
    
    piezo_mesh = generate_piezo_junction_vectors(rings, outer_dia, inner_dia, thickness)
    
    # Audit a node directly inside the first structural compression seat ring
    audit_sample = [n for n in piezo_mesh if "PZT_Ceramic_Compression_Seat" in n["node_classification"]]
    
    print("\n[+] SUCCESS: Piezoelectric Hydro-Stack matrix compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(piezo_mesh)}")
    print(f"[-] ARVT-08 Optimized Node Balance Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['node_classification']}")
    print(f"    ↳ Geometric Vector Node:    {audit_sample['vector']}")
    print("=" * 65)

if __name__ == "__main__":
    main()
      

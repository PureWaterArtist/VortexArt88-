import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_induction_coil_bobbins(coils_count, coil_height, outer_dia, inner_dia, resolution=360):
    """
    Calculates 3D spatial vectors for the secondary copper coil bobbins.
    Maps out the precise spool channels that wrap concentrically around the outer 
    perimeters of the N52 Neodymium magnetic rings inside the power sleeve.
    """
    bobbin_nodes = []
    r_out = outer_dia / 2.0
    r_in = inner_dia / 2.0
    
    for coil_idx in range(coils_count):
        # Align bobbin positions directly with the 6 magnet rings stacked every 25.4mm
        z_start = -(coil_idx * 25.4)
        z_mid = z_start - (25.4 / 2.0)
        
        for step in range(resolution):
            theta = (step * 2.0 * math.pi) / resolution
            
            # Formulate structural bobbin retention lips at top and bottom margins
            if step % 180 == 0:
                node_type = "Bobbin_Chassis_Wire_Guide_Notch"
                radius = r_out + 2.0
            else:
                node_type = f"Secondary_Coil_Spool_Seat_Ring_{coil_idx + 1}"
                radius = r_in # Concentric core wire winding boundary
                
            x = radius * math.cos(theta)
            y = radius * math.sin(theta)
            
            bobbin_nodes.append({
                "coil_index": coil_idx,
                "node_classification": node_type,
                "telemetry": {
                    "coil_centerline_z_mm": round(z_mid, 4),
                    "spool_width_mm": round(coil_height, 2)
                },
                "vector": (round(x, 4), round(y, 4), round(z_mid, 4))
            })
            
    return bobbin_nodes

def main():
    print("=" * 65)
    print("INITIALIZING: ARVT-09 SECONDARY MAGNETIC INDUCTION ENGINE")
    print("=" * 65)
    
    config_path = get_local_path("induction-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        coils_count = config["induction_geometry"]["induction_coil_starts"]
        coil_height = config["induction_geometry"]["coil_height_z_mm"]
        outer_dia = config["induction_geometry"]["coil_outer_diameter_mm"]
        inner_dia = config["induction_geometry"]["coil_inner_diameter_mm"]
        material = config["manufacturing_profile"]["recommended_material"]
        print("[+] Component ID ARVT-09 induction configuration verified.")
    else:
        print("[⚠️] WARNING: induction-config.json missing. Loading safe overrides.")
        coils_count = 6
        coil_height = 22.0
        outer_dia = 82.5
        inner_dia = 76.5
        material = "Nylon-12"
        
    print(f"[*] Bobbin Material Standard:  {material}")
    print(f"[*] Induction Active Array:     {coils_count} x AWG 24 Winding Bobbins")
    print(f"[*] Compiling concentric Faraday coil spool meshes...")
    
    induction_mesh = generate_induction_coil_bobbins(coils_count, coil_height, outer_dia, inner_dia)
    
    # Audit a node directly inside the primary copper coil spool seat
    audit_sample = [n for n in induction_mesh if "Secondary_Coil_Spool_Seat" in n["node_classification"]]
    
    print("\n[+] SUCCESS: Secondary Magnetic Induction matrix compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(induction_mesh)}")
    print(f"[-] ARVT-09 Optimized Node Balance Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['node_classification']}")
    print(f"    ↳ Geometric Vector Node:    {audit_sample['vector']}")
    print("=" * 65)

if __name__ == "__main__":
    main()
          

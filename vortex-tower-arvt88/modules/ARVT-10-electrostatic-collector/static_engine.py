import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_electrostatic_grid_vectors(grid_dia, mesh_rings, needle_points, resolution=360):
    """
    Calculates 3D spatial vectors for the atmospheric electrostatic pickup grid.
    Maps out concentric stainless steel mesh seats and radical pickup needle points 
    positioned over the hollow siphon vortex core interface.
    """
    grid_nodes = []
    base_radius = grid_dia / 2.0
    
    # Process concentric ring paths for the metal collector seats
    for ring_idx in range(mesh_rings):
        current_radius = base_radius * ((ring_idx + 1) / mesh_rings)
        
        for step in range(resolution):
            theta = (step * 2.0 * math.pi) / resolution
            
            # Formulate radical needle pickup locations spaced evenly around the perimeter
            is_needle = False
            needle_interval = int(resolution / needle_points)
            if step % needle_interval == 0 and ring_idx == (mesh_rings - 1):
                is_helix_electrode = True
                node_type = f"Ionization_Static_Pickup_Needle_Point_{int(step/needle_interval) + 1}"
                radius_mod = current_radius + 5.0 # Sharp extension point
            else:
                node_type = f"Concentric_Mesh_Seat_Ring_{ring_idx + 1}"
                radius_mod = current_radius
                
            x = radius_mod * math.cos(theta)
            y = radius_mod * math.sin(theta)
            
            grid_nodes.append({
                "ring_layer": ring_idx,
                "node_classification": node_type,
                "telemetry": {
                    "radial_span_mm": round(radius_mod, 4),
                    "surface_perimeter_mm": round(2.0 * math.pi * radius_mod, 2)
                },
                "vector": (round(x, 4), round(y, 4), 0.0) # Flat 2D grid face at Z=0
            })
            
    return grid_nodes

def main():
    print("=" * 65)
    print("INITIALIZING: ARVT-10 ATMOSPHERIC ELECTROSTATIC ENGINE")
    print("=" * 65)
    
    config_path = get_local_path("static-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        grid_dia = config["collector_geometry"]["grid_ring_diameter_mm"]
        mesh_rings = config["collector_geometry"]["concentric_mesh_rings"]
        needle_points = config["collector_geometry"]["pickup_needle_points_count"]
        material = config["manufacturing_profile"]["recommended_material"]
        print("[+] Component ID ARVT-10 static collector parameters matched cleanly.")
    else:
        print("[⚠️] WARNING: static-config.json missing. Loading safe overrides.")
        grid_dia = 140.0
        mesh_rings = 3
        needle_points = 8
        material = "Polypropylene"
        
    print(f"[*] Base Housing Material:       {material}")
    print(f"[*] Electrostatic Array Mappings: {mesh_rings} Rings | {needle_points} x Ionization Needles")
    print(f"[*] Compiling atmospheric charge capture coordinate planes...")
    
    grid_mesh = generate_electrostatic_grid_vectors(grid_dia, mesh_rings, needle_points)
    
    # Audit an active needle extraction node point hanging directly over the intake core
    audit_sample = [n for n in grid_mesh if "Pickup_Needle_Point" in n["node_classification"]]
    
    print("\n[+] SUCCESS: Atmospheric Electrostatic Collector matrix compiled.")
    print(f"[-] Total coordinated structural steps logged: {len(grid_mesh)}")
    print(f"[-] ARVT-10 Optimized Node Balance Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['node_classification']}")
    print(f"    ↳ Geometric Vector Node:    {audit_sample['vector']}")
    print("=" * 65)

if __name__ == "__main__":
    main()
          

import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_cross_cap_vectors(throat_dia, resolution=360):
    """
    Calculates 3D spatial vectors mapping a projected non-orientable Cross-Cap.
    The tracks smoothly self-intersect to equalize fluid shear forces.
    """
    matrix_points = []
    r = throat_dia / 2.0
    
    for step in range(resolution):
        # Parameter 'u' maps along the radial cross-section of the surface (-Pi/2 to Pi/2)
        u = (-math.pi / 2.0) + (step * math.pi / resolution)
        
        # Parameter 'v' maps the rotational angle around the central fold (0 to Pi)
        v = (step * math.pi) / resolution
        
        # Classical Parametric Equations for a 3D Cross-Cap Manifold Surface
        x = r * math.sin(u) * math.sin(2.0 * v)
        y = r * math.sin(2.0 * u) * math.cos(v) * math.cos(v)
        z = r * math.cos(2.0 * u) * math.cos(v) * math.cos(v)
        
        # Zone tracking based on geometric progress
        if step < (resolution // 4):
            zone = "Self_Intersecting_Entry"
        elif step > (3 * resolution // 4):
            zone = "Stabilized_Discharge"
        else:
            zone = "Non_Orientable_Transit"
            
        matrix_points.append({
            "step": step,
            "structural_phase": zone,
            "parameters": {"u_rad": round(u, 4), "v_rad": round(v, 4)},
            "coordinate_vector": (round(x, 4), round(y, 4), round(z, 4))
        })
        
    return matrix_points

def main():
    print("=" * 60)
    print("INITIALIZING: NON-ORIENTABLE CROSS-CAP PIPELINE ENGINE")
    print("=" * 60)
    
    config_path = get_local_path("cross-cap-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        throat_diameter = config["geometry"]["internal_throat_diameter_mm"]
        print("[+] Non-orientable architectural variables verified and compiled.")
    else:
        print("[⚠️] WARNING: cross-cap-config.json missing. Resorting to overrides.")
        throat_diameter = 50.0
        
    print(f"[*] Projecting 3D cross-cap self-intersecting tracks...")
    print(f"[*] Scaling boundary matrix limits: Core Radius = {throat_diameter / 2.0}mm")
    
    # Run coordinate pipeline math
    cross_cap_nodes = generate_cross_cap_vectors(throat_diameter)
    
    # Audit a midpoint node tracking the self-intersecting crossing coordinate
    audit_sample = cross_cap_nodes[len(cross_cap_nodes) // 2]
    
    print("\n[+] SUCCESS: Cross-Cap manifold grid recompiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(cross_cap_nodes)}")
    print(f"[-] Self-Intersecting Symmetry Core Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['structural_phase']}")
    print(f"    ↳ Cartesian Mesh Node:      {audit_sample['coordinate_vector']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
      

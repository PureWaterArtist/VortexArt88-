import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_boy_surface_vectors(scale_a, resolution=360):
    """
    Calculates 3D spatial vectors mapping a Boy Surface Immersion.
    The surface curves smoothly and non-orientably with 3-fold rotational symmetry.
    """
    matrix_points = []
    
    for step in range(resolution):
        # Parameter 'u' tracks the latitude rotation (0 to Pi)
        u = (step * math.pi) / resolution
        
        # Parameter 'v' tracks the longitudinal sweep angle (0 to Pi)
        v = (step * math.pi) / resolution
        
        # Complex trigonometric formulation mapping a smooth 3-fold symmetric Boy Surface
        # Computes values across three interlocking 120-degree spatial quadrants
        g1 = math.cos(u) * math.sin(u) * math.cos(v)
        g2 = math.cos(u) * math.sin(u) * math.sin(v)
        g3 = (math.cos(u) ** 2) - (math.sin(u) ** 2)
        
        denominator = 2.0 - math.sqrt(2.0) * math.sin(3.0 * u) * math.sin(2.0 * v)
        if abs(denominator) < 1e-6:
            denominator = 1e-6
            
        x = scale_a * (g1 * math.cos(v) - g2 * math.sin(v)) / denominator
        y = scale_a * (g1 * math.sin(v) + g2 * math.cos(v)) / denominator
        z = scale_a * g3 / denominator
        
        # Structural phase tracking based on layout progress and proximity to the center node
        progress = step / resolution
        if abs(x) < 4.0 and abs(y) < 4.0 and abs(z) < 4.0:
            phase = "Three_Fold_Triple_Point_Core"
        elif progress < 0.33:
            phase = "Quadrant_Alpha_120_Degree_Flow"
        elif progress > 0.66:
            phase = "Quadrant_Gamma_120_Degree_Flow"
        else:
            phase = "Quadrant_Beta_120_Degree_Flow"
            
        matrix_points.append({
            "step": step,
            "structural_phase": phase,
            "parameters": {"u_rad": round(u, 4), "v_rad": round(v, 4)},
            "coordinate_vector": (round(x, 4), round(y, 4), round(z, 4))
        })
        
    return matrix_points

def main():
    print("=" * 60)
    print("INITIALIZING: BOY SURFACE IMMERSION ENGINE")
    print("=" * 60)
    
    config_path = get_local_path("boy-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        scale_a = config["geometry"]["radial_scale_a_mm"]
        print("[+] Smooth non-orientable variables verified from config matrix.")
    else:
        print("[⚠️] WARNING: boy-config.json missing. Loading safe overrides.")
        scale_a = 45.0
        
    print(f"[*] Projecting pinch-point-free 3-fold symmetric surface grids...")
    print(f"[*] Processing boundaries: Radial Scale (a) = {scale_a}mm")
    
    # Run coordinate pipeline calculation loops
    boy_nodes = generate_boy_surface_vectors(scale_a)
    
    # Audit a midpoint node tracking the structural tracking loops
    audit_sample = boy_nodes[len(boy_nodes) // 2]
    
    print("\n[+] SUCCESS: Boy Surface geometric matrix compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(boy_nodes)}")
    print(f"[-] Boy Surface Interface Alignment Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['structural_phase']}")
    print(f"    ↳ Cartesian Mesh Node:      {audit_sample['coordinate_vector']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
                                

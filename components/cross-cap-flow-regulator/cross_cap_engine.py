import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_cross_cap_vectors(base_radius, singular_len, resolution=360):
    """
    Calculates 3D spatial vectors mapping a Cross-Cap Immersion surface.
    The surface curves non-orientably to pass fluid tracks through their own axis.
    """
    matrix_points = []
    
    for step in range(resolution):
        # Parameter 'u' tracks the latitude sweep along the projective cap (0 to Pi/2)
        u = (step * math.pi) / (2.0 * resolution)
        
        # Parameter 'v' tracks the full longitudinal sweep rotation (0 to 2*Pi)
        v = (step * 2.0 * math.pi) / resolution
        
        # Classical Parametric Immersion Equations for a Cross-Cap Surface
        # Maps a continuous, single-sided self-intersecting coordinate grid
        x = base_radius * math.sin(u) * math.cos(2.0 * v)
        y = base_radius * math.sin(u) * math.sin(2.0 * v)
        z = singular_len * math.cos(u) * (math.cos(v) ** 2)
        
        # Structural phase tracking based on layout progress
        progress = step / resolution
        if progress < 0.20:
            phase = "Whitney_Branch_Point_Alpha"
        elif progress > 0.80:
            phase = "Whitney_Branch_Point_Beta"
        elif abs(x) < 2.0 and abs(y) < 2.0:
            phase = "Singular_Self_Intersection_Line"
        else:
            phase = "Projective_Cap_Boundary_Sweep"
            
        matrix_points.append({
            "step": step,
            "structural_phase": phase,
            "parameters": {"u_rad": round(u, 4), "v_rad": round(v, 4)},
            "coordinate_vector": (round(x, 4), round(y, 4), round(z, 4))
        })
        
    return matrix_points

def main():
    print("=" * 60)
    print("INITIALIZING: CROSS-CAP SURFACE IMMERSION ENGINE")
    print("=" * 60)
    
    config_path = get_local_path("cross-cap-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        base_radius = config["geometry"]["base_radius_r_mm"]
        singular_len = config["geometry"]["singular_line_length_mm"]
        print("[+] Non-orientable cross-cap variables parsed from configuration standard.")
    else:
        print("[⚠️] WARNING: cross-cap-config.json missing. Loading safe overrides.")
        base_radius = 35.0
        singular_len = 20.0
        
    print(f"[*] Projecting non-orientable self-intersecting surface grids...")
    print(f"[*] Processing boundaries: Base Radius = {base_radius}mm | Singular Line = {singular_len}mm")
    
    # Run coordinate pipeline calculation loops
    cross_cap_nodes = generate_cross_cap_vectors(base_radius, singular_len)
    
    # Audit a midpoint node tracking the structural tracking loops
    audit_sample = cross_cap_nodes[len(cross_cap_nodes) // 2]
    
    print("\n[+] SUCCESS: Cross-Cap geometric matrix compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(cross_cap_nodes)}")
    print(f"[-] Cross-Cap Intersection Interface Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['structural_phase']}")
    print(f"    ↳ Cartesian Mesh Node:      {audit_sample['coordinate_vector']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
          

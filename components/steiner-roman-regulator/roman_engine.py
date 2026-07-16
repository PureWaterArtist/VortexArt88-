import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_roman_surface_vectors(scale_a, resolution=360):
    """
    Calculates 3D spatial vectors mapping a Steiner Roman Surface Immersion.
    The surface curves non-orientably to pass fluid tracks through three perpendicular axes.
    """
    matrix_points = []
    
    for step in range(resolution):
        # Parameter 'u' tracks the latitude rotation (0 to Pi)
        u = (step * math.pi) / resolution
        
        # Parameter 'v' tracks the longitudinal sweep angle (0 to Pi)
        v = (step * math.pi) / resolution
        
        # Classical Parametric Immersion Equations for Steiner's Roman Surface
        # Maps a continuous, single-sided surface intersecting along X, Y, and Z planes
        x = (scale_a ** 2) * math.sin(2.0 * u) * (math.cos(v) ** 2)
        y = (scale_a ** 2) * math.sin(u) * math.sin(2.0 * v)
        z = (scale_a ** 2) * math.cos(u) * math.sin(2.0 * v)
        
        # Structural phase tracking based on layout progress and proximity to the center node
        progress = step / resolution
        if progress < 0.16 or progress > 0.84:
            phase = "Whitney_Branch_Point_Cluster"
        elif abs(x) < 5.0 and abs(y) < 5.0 and abs(z) < 5.0:
            phase = "Tri_Axial_Triple_Point_Core"
        else:
            phase = "Perpendicular_Lobe_Boundary_Sweep"
            
        matrix_points.append({
            "step": step,
            "structural_phase": phase,
            "parameters": {"u_rad": round(u, 4), "v_rad": round(v, 4)},
            "coordinate_vector": (round(x, 4), round(y, 4), round(z, 4))
        })
        
    return matrix_points

def main():
    print("=" * 60)
    print("INITIALIZING: STEINER ROMAN SURFACE IMMERSION ENGINE")
    print("=" * 60)
    
    config_path = get_local_path("roman-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        scale_a = config["geometry"]["radial_scale_a_mm"]
        print("[+] Non-orientable Roman variables parsed from configuration standard.")
    else:
        print("[⚠️] WARNING: roman-config.json missing. Loading safe overrides.")
        scale_a = 40.0
        
    print(f"[*] Projecting non-orientable tri-axial intersecting surface grids...")
    print(f"[*] Processing boundaries: Radial Scale (a) = {scale_a}mm")
    
    # Run coordinate pipeline calculation loops
    roman_nodes = generate_roman_surface_vectors(scale_a)
    
    # Audit a midpoint node tracking the structural tracking loops
    audit_sample = roman_nodes[len(roman_nodes) // 2]
    
    print("\n[+] SUCCESS: Roman Surface geometric matrix compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(roman_nodes)}")
    print(f"[-] Roman Core Intersection Interface Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['structural_phase']}")
    print(f"    ↳ Cartesian Mesh Node:      {audit_sample['coordinate_vector']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
  

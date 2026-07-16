import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_pseudosphere_vectors(radius_r, total_z, resolution=360):
    """
    Calculates 3D spatial vectors mapping a Pseudosphere shell.
    The surface curves tractricially to maintain constant negative curvature.
    """
    matrix_points = []
    
    for step in range(resolution):
        # Parameter 'u' tracks the tractrix arc profile (epsilon to Pi - epsilon)
        # Avoid zero to prevent log division limits at the asymptotic tips
        epsilon = 0.01
        u = epsilon + (step * (math.pi - 2 * epsilon) / resolution)
        
        # Rotational sweep angle 'v' maps the full 360-degree cylinder (0 to 2*Pi)
        v = (step * 2.0 * math.pi) / resolution
        
        # Classical Parametric Equations for a 3D Pseudosphere Surface
        x = radius_r * math.sin(u) * math.cos(v)
        y = radius_r * math.sin(u) * math.sin(v)
        z = radius_r * (math.cos(u) + math.log(math.tan(u / 2.0)))
        
        # Structural phase tracking based on progress
        progress = step / resolution
        if progress < 0.15 or progress > 0.85:
            phase = "Asymptotic_Spire_Zone"
        else:
            phase = "Equatorial_Expansion_Flare"
            
        matrix_points.append({
            "step": step,
            "structural_phase": phase,
            "parameters": {"u": round(u, 4), "v": round(v, 4)},
            "coordinate_vector": (round(x, 4), round(y, 4), round(z, 4))
        })
        
    return matrix_points

def main():
    print("=" * 60)
    print("INITIALIZING: PSEUDOSPHERE TRACTRIX MATRIX ENGINE")
    print("=" * 60)
    
    config_path = get_local_path("pseudosphere-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        radius_r = config["geometry"]["equatorial_radius_r_mm"]
        total_z = config["geometry"]["axial_length_z_mm"]
        print("[+] Constant negative curvature parameters successfully loaded.")
    else:
        print("[⚠️] WARNING: pseudosphere-config.json missing. Loading safe defaults.")
        radius_r = 40.0
        total_z = 120.0
        
    print(f"[*] Compiling hyperbolic tractrix curvature grids...")
    print(f"[*] Processing pseudosphere boundaries: Equatorial Radius = {radius_r}mm")
    
    # Run coordinate pipeline calculation loops
    pseudosphere_nodes = generate_pseudosphere_vectors(radius_r, total_z)
    
    # Audit a midpoint node tracking the equatorial flare area
    audit_sample = pseudosphere_nodes[len(pseudosphere_nodes) // 2]
    
    print("\n[+] SUCCESS: Pseudosphere boundary matrix compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(pseudosphere_nodes)}")
    print(f"[-] Pseudosphere Equator Balance Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['structural_phase']}")
    print(f"    ↳ Cartesian Mesh Node:      {audit_sample['coordinate_vector']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
  

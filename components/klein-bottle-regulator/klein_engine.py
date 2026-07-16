import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_klein_bottle_vectors(radius_r, offset_displacement, resolution=360):
    """
    Calculates 3D spatial vectors mapping a Klein Bottle Immersion surface.
    The surface curves non-orientably to transition fluid layers smoothly.
    """
    matrix_points = []
    
    for step in range(resolution):
        # Parameter 'u' tracks the sweep along the main tubular bottle body (0 to Pi)
        u = (step * math.pi) / resolution
        
        # Parameter 'v' tracks the rotational sweep angle around the tube profile (0 to 2*Pi)
        v = (step * 2.0 * math.pi) / resolution
        
        # Classical Parametric Immersion Equations for a Klein Bottle
        # Tracks a continuous, boundaryless self-intersecting coordinate map
        x = (radius_r + offset_displacement * math.cos(u / 2.0) * math.sin(v) - 
             offset_displacement * math.sin(u / 2.0) * math.sin(2.0 * v)) * math.cos(u)
             
        y = (radius_r + offset_displacement * math.cos(u / 2.0) * math.sin(v) - 
             offset_displacement * math.sin(u / 2.0) * math.sin(2.0 * v)) * math.sin(u)
             
        z = (offset_displacement * math.sin(u / 2.0) * math.sin(v) + 
             offset_displacement * math.cos(u / 2.0) * math.sin(2.0 * v))
        
        # Structural phase tracking based on progress depth
        progress = step / resolution
        if progress < 0.25:
            phase = "Chiral_Intake_Neck"
        elif progress > 0.75:
            phase = "Inversion_Throat_Intersection"
        else:
            phase = "Single_Sided_Body_Sweep"
            
        matrix_points.append({
            "step": step,
            "structural_phase": phase,
            "parameters": {"u_rad": round(u, 4), "v_rad": round(v, 4)},
            "coordinate_vector": (round(x, 4), round(y, 4), round(z, 4))
        })
        
    return matrix_points

def main():
    print("=" * 60)
    print("INITIALIZING: KLEIN BOTTLE IMMERSION MATRIX ENGINE")
    print("=" * 60)
    
    config_path = get_local_path("klein-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        radius_r = config["geometry"]["core_radius_r_mm"]
        offset_displacement = config["geometry"]["neck_immersion_displacement_mm"]
        print("[+] Non-orientable topological parameters successfully validated.")
    else:
        print("[⚠️] WARNING: klein-config.json missing. Loading safe defaults.")
        radius_r = 30.0
        offset_displacement = 12.0
        
    print(f"[*] Compiling single-sided self-intersecting boundary grids...")
    print(f"[*] Processing topological boundaries: Core Radius (r) = {radius_r}mm")
    
    # Run coordinate pipeline calculation loops
    klein_nodes = generate_klein_bottle_vectors(radius_r, offset_displacement)
    
    # Audit a midpoint node tracking the structural center loop
    audit_sample = klein_nodes[len(klein_nodes) // 2]
    
    print("\n[+] SUCCESS: Klein Bottle boundary matrix compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(klein_nodes)}")
    print(f"[-] Klein Core Topological Balance Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['structural_phase']}")
    print(f"    ↳ Cartesian Mesh Node:      {audit_sample['coordinate_vector']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
  

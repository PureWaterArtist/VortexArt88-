import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_saddle_vectors(scale_a, scale_b, limit_x, limit_y, resolution=360):
    """
    Calculates 3D spatial vectors mapping a Hyperbolic Paraboloid saddle shell.
    Saves coordinate nodes sweeping through the intersecting straight line paths.
    """
    matrix_points = []
    
    for step in range(resolution):
        # Progress parameter maps out the grid traversal across the X/Y spatial bounds
        progress = step / resolution
        
        # Symmetrically sweep parameters from negative limit to positive limit
        x = (-limit_x) + (progress * 2.0 * limit_x)
        
        # Rotational angle sweep maps a continuous parameter trace across the quadric layout
        theta = (step * 2.0 * math.pi) / resolution
        y = limit_y * math.sin(theta)
        
        # Classical Quadric Equation for a Hyperbolic Paraboloid Saddle:
        # z = (x^2 / a^2) - (y^2 / b^2)
        z = ((x ** 2) / (scale_a ** 2)) - ((y ** 2) / (scale_b ** 2))
        
        # Structural phase tracking based on layout progress
        if abs(x) < (limit_x * 0.20) and abs(y) < (limit_y * 0.20):
            phase = "Minimax_Saddle_Point_Core"
        elif x * y > 0:
            phase = "Ascending_Parabolic_Flange"
        else:
            phase = "Descending_Parabolic_Flange"
            
        matrix_points.append({
            "step": step,
            "structural_phase": phase,
            "parameters": {"x_pos_mm": round(x, 4), "y_pos_mm": round(y, 4)},
            "coordinate_vector": (round(x, 4), round(y, 4), round(z, 4))
        })
        
    return matrix_points

def main():
    print("=" * 60)
    print("INITIALIZING: HYPERBOLIC PARABOLOID SADDLE ENGINE")
    print("=" * 60)
    
    config_path = get_local_path("saddle-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        scale_a = config["geometry"]["parabola_a_scale_mm"]
        scale_b = config["geometry"]["parabola_b_scale_mm"]
        limit_x = config["geometry"]["spatial_limit_x_mm"]
        limit_y = config["geometry"]["spatial_limit_y_mm"]
        print("[+] Saddle-plane quadric variables successfully compiled.")
    else:
        print("[⚠️] WARNING: saddle-config.json missing. Loading safe defaults.")
        scale_a = 35.0
        scale_b = 35.0
        limit_x = 50.0
        limit_y = 50.0
        
    print(f"[*] Compiling doubly ruled saddle surface coordinate loops...")
    print(f"[*] Processing grid boundaries: Scaling Coefficients (a,b) = {scale_a}mm")
    
    # Run coordinate pipeline calculation loops
    saddle_nodes = generate_saddle_vectors(scale_a, scale_b, limit_x, limit_y)
    
    # Audit a midpoint node tracking the structural alignment close to the core center
    audit_sample = saddle_nodes[len(saddle_nodes) // 2]
    
    print("\n[+] SUCCESS: Hyperbolic paraboloid boundary matrix recompiled.")
    print(f"[-] Total coordinated structural steps logged: {len(saddle_nodes)}")
    print(f"[-] Saddle Minimax Center Balance Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['structural_phase']}")
    print(f"    ↳ Cartesian Mesh Node:      {audit_sample['coordinate_vector']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
  

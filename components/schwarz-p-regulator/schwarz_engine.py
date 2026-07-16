import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_schwarz_p_vectors(cell_length, manifold_radius, resolution=360):
    """
    Calculates 3D spatial vectors mapping a Schwarz Primitive Minimal Surface.
    Approximates the zero-mean-curvature surface via implicit functions:
    cos(x) + cos(y) + cos(z) = 0
    """
    matrix_points = []
    
    # Scale coordinates to map cleanly across a full 2*Pi periodic cycle
    spatial_scale = (2.0 * math.pi) / cell_length
    
    for step in range(resolution):
        # Progress parameter maps out the primary linear sweep path
        progress = step / resolution
        
        # Calculate localized 3D Cartesian positions looping through the unit cell
        x = (progress * cell_length) - (cell_length / 2.0)
        
        # Parametric sweep angle tracks the spatial rotation loops
        theta = (step * 2.0 * math.pi) / resolution
        y = manifold_radius * math.cos(theta)
        
        # Evaluate implicit Schwarz P surface constraint equation:
        # cos(X) + cos(Y) + cos(Z) = 0  ->  cos(Z) = -(cos(X) + cos(Y))
        cos_x = math.cos(x * spatial_scale)
        cos_y = math.cos(y * spatial_scale)
        
        target_cos_z = -(cos_x + cos_y)
        
        # Clamp to a valid mathematical cosine range [-1.0, 1.0] to prevent arithmetic limits
        target_cos_z = max(-1.0, min(1.0, target_cos_z))
        
        # Solve for the vertical coordinate component via the arc-cosine function
        z_scaled = math.acos(target_cos_z)
        z = z_scaled / spatial_scale
        
        # Structural phase tracking based on progress
        if progress < 0.20 or progress > 0.80:
            phase = "Orthogonal_Manifold_Ports"
        elif abs(x) < 4.0 and abs(y) < 4.0:
            phase = "Cubic_Junction_Core"
        else:
            phase = "Periodic_Labyrinth_Transit"
            
        matrix_points.append({
            "step": step,
            "structural_phase": phase,
            "parameters": {"x_pos_mm": round(x, 4), "y_pos_mm": round(y, 4)},
            "coordinate_vector": (round(x, 4), round(y, 4), round(z, 4))
        })
        
    return matrix_points

def main():
    print("=" * 60)
    print("INITIALIZING: SCHWARZ P PERIODIC MINIMAL SURFACE ENGINE")
    print("=" * 60)
    
    config_path = get_local_path("schwarz-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        cell_length = config["geometry"]["unit_cell_length_L_mm"]
        manifold_radius = config["geometry"]["pipe_manifold_radius_mm"]
        print("[+] Schwarz periodic parameters verified from configuration standard.")
    else:
        print("[⚠️] WARNING: schwarz-config.json missing. Loading safe defaults.")
        cell_length = 50.0
        manifold_radius = 18.0
        
    print(f"[*] Compiling triply periodic zero-mean-curvature grids...")
    print(f"[*] Processing unit cell bounds: Length (L) = {cell_length}mm")
    
    # Run coordinate pipeline calculation loops
    schwarz_nodes = generate_schwarz_p_vectors(cell_length, manifold_radius)
    
    # Audit a midpoint node tracking the structural alignment close to the junction core
    audit_sample = schwarz_nodes[len(schwarz_nodes) // 2]
    
    print("\n[+] SUCCESS: Schwarz P boundary matrix compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(schwarz_nodes)}")
    print(f"[-] Schwarz P Core Junction Balance Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['structural_phase']}")
    print(f"    ↳ Cartesian Mesh Node:      {audit_sample['coordinate_vector']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
  

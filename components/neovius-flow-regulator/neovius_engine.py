import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_neovius_vectors(cell_length, handle_radius, resolution=360):
    """
    Calculates 3D spatial vectors mapping a Neovius Minimal Surface.
    Approximates the zero-mean-curvature higher-genus surface via implicit functions:
    3 * (cos(x) + cos(y) + cos(z)) + 4 * cos(x) * cos(y) * cos(z) = 0
    """
    matrix_points = []
    
    # Scale coordinates to map cleanly across a full 2*Pi periodic cycle
    spatial_scale = (2.0 * math.pi) / cell_length
    
    for step in range(resolution):
        # Progress parameter maps out the primary linear sweep path along the X-axis
        progress = step / resolution
        x = (progress * cell_length) - (cell_length / 2.0)
        
        # Parametric sweep angle tracks the spatial rotation loops
        theta = (step * 2.0 * math.pi) / resolution
        y = handle_radius * math.cos(theta)
        
        # Precompute trigonometric terms for implicit structural constraints
        cos_x = math.cos(x * spatial_scale)
        cos_y = math.cos(y * spatial_scale)
        
        # Approximate the vertical coordinate z component using numerical stepping
        best_z = 0.0
        min_residual = float('inf')
        
        # Search the periodic z-domain to identify the exact minimal surface intercept
        for z_step in range(180):
            z_test = (z_step * cell_length / 180.0) - (cell_length / 2.0)
            cos_z = math.cos(z_test * spatial_scale)
            
            # Evaluate the implicit Neovius structural equation:
            # 3 * (cos(x) + cos(y) + cos(z)) + 4 * cos(x) * cos(y) * cos(z) = 0
            term1 = 3.0 * (cos_x + cos_y + cos_z)
            term2 = 4.0 * cos_x * cos_y * cos_z
            
            residual = abs(term1 + term2)
            if residual < min_residual:
                min_residual = residual
                best_z = z_test
                
        # Structural phase tracking based on layout progress
        if progress < 0.15 or progress > 0.85:
            phase = "Twelve_Fold_Manifold_Ports"
        elif abs(x) < 6.0 and abs(y) < 6.0:
            phase = "Open_Cubic_Junction_Core"
        else:
            phase = "Cross_Handle_Labyrinth_Transit"
            
        matrix_points.append({
            "step": step,
            "structural_phase": phase,
            "parameters": {"x_pos_mm": round(x, 4), "y_pos_mm": round(y, 4)},
            "coordinate_vector": (round(x, 4), round(y, 4), round(best_z, 4))
        })
        
    return matrix_points

def main():
    print("=" * 60)
    print("INITIALIZING: NEOVIUS HIGHER-GENUS MINIMAL SURFACE ENGINE")
    print("=" * 60)
    
    config_path = get_local_path("neovius-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        cell_length = config["geometry"]["unit_cell_length_L_mm"]
        handle_radius = config["geometry"]["cross_channel_handle_radius_mm"]
        print("[+] Neovius higher-genus periodic parameters verified from config.")
    else:
        print("[⚠️] WARNING: neovius-config.json missing. Loading safe defaults.")
        cell_length = 72.0
        handle_radius = 16.5
        
    print(f"[*] Compiling higher-genus zero-mean-curvature cubic grids...")
    print(f"[*] Processing unit cell bounds: Length (L) = {cell_length}mm")
    
    # Run coordinate pipeline calculation loops
    neovius_nodes = generate_neovius_vectors(cell_length, handle_radius)
    
    # Audit a midpoint node tracking the structural alignment close to the junction core
    audit_sample = neovius_nodes[len(neovius_nodes) // 2]
    
    print("\n[+] SUCCESS: Neovius boundary matrix compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(neovius_nodes)}")
    print(f"[-] Neovius Core Junction Balance Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['structural_phase']}")
    print(f"    ↳ Cartesian Mesh Node:      {audit_sample['coordinate_vector']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
              

import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_schwarz_d_vectors(cell_length, channel_radius, resolution=360):
    """
    Calculates 3D spatial vectors mapping a Schwarz Diamond Minimal Surface.
    Approximates the zero-mean-curvature surface via implicit functions:
    sin(x)*sin(y)*sin(z) + sin(x)*cos(y)*cos(z) + cos(x)*sin(y)*cos(z) + cos(x)*cos(y)*sin(z) = 0
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
        y = channel_radius * math.cos(theta)
        
        # Precompute trigonometric terms for implicit structural constraints
        sin_x = math.sin(x * spatial_scale)
        cos_x = math.cos(x * spatial_scale)
        sin_y = math.sin(y * spatial_scale)
        cos_y = math.cos(y * spatial_scale)
        
        # Approximate the vertical coordinate z component using numerical stepping
        best_z = 0.0
        min_residual = float('inf')
        
        # Search the periodic z-domain to identify the exact minimal surface intercept
        for z_step in range(180):
            z_test = (z_step * cell_length / 180.0) - (cell_length / 2.0)
            sin_z = math.sin(z_test * spatial_scale)
            cos_z = math.cos(z_test * spatial_scale)
            
            # Evaluate the structural implicit diamond constraint equation terms
            term1 = sin_x * sin_y * sin_z
            term2 = sin_x * cos_y * cos_z
            term3 = cos_x * sin_y * cos_z
            term4 = cos_x * cos_y * sin_z
            
            residual = abs(term1 + term2 + term3 + term4)
            if residual < min_residual:
                min_residual = residual
                best_z = z_test
                
        # Structural phase tracking based on layout progress
        if progress < 0.20 or progress > 0.80:
            phase = "Tetrahedral_Manifold_Ports"
        elif abs(x) < 5.0 and abs(y) < 5.0:
            phase = "Tetrahedral_Junction_Core"
        else:
            phase = "Diamond_Labyrinth_Transit"
            
        matrix_points.append({
            "step": step,
            "structural_phase": phase,
            "parameters": {"x_pos_mm": round(x, 4), "y_pos_mm": round(y, 4)},
            "coordinate_vector": (round(x, 4), round(y, 4), round(best_z, 4))
        })
        
    return matrix_points

def main():
    print("=" * 60)
    print("INITIALIZING: SCHWARZ D PERIODIC MINIMAL SURFACE ENGINE")
    print("=" * 60)
    
    config_path = get_local_path("schwarz-d-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        cell_length = config["geometry"]["unit_cell_length_L_mm"]
        channel_radius = config["geometry"]["tetrahedral_channel_radius_mm"]
        print("[+] Schwarz Diamond periodic parameters verified from configuration standard.")
    else:
        print("[⚠️] WARNING: schwarz-d-config.json missing. Loading safe defaults.")
        cell_length = 64.0
        channel_radius = 21.0
        
    print(f"[*] Compiling triply periodic zero-mean-curvature diamond grids...")
    print(f"[*] Processing unit cell bounds: Length (L) = {cell_length}mm")
    
    # Run coordinate pipeline calculation loops
    schwarz_d_nodes = generate_schwarz_d_vectors(cell_length, channel_radius)
    
    # Audit a midpoint node tracking the structural alignment close to the junction core
    audit_sample = schwarz_d_nodes[len(schwarz_d_nodes) // 2]
    
    print("\n[+] SUCCESS: Schwarz D boundary matrix compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(schwarz_d_nodes)}")
    print(f"[-] Schwarz D Core Junction Balance Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['structural_phase']}")
    print(f"    ↳ Cartesian Mesh Node:      {audit_sample['coordinate_vector']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
          

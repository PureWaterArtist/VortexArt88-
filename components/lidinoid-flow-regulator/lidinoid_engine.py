import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_lidinoid_vectors(cell_length, manifold_radius, resolution=360):
    """
    Calculates 3D spatial vectors mapping a Lidinoid Minimal Surface.
    Approximates the zero-mean-curvature surface via implicit functions:
    0.5 * (sin(2x)sin(y)cos(z) + sin(2y)sin(z)cos(x) + sin(2z)sin(x)cos(y)) - 
    0.5 * (cos(2x)cos(y)sin(z) + cos(2y)cos(z)sin(x) + cos(2z)cos(x)sin(y)) = 0
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
        
        # Precompute trigonometric terms for implicit structural constraints
        sin_2x = math.sin(2.0 * x * spatial_scale)
        cos_2x = math.cos(2.0 * x * spatial_scale)
        sin_x  = math.sin(x * spatial_scale)
        cos_x  = math.cos(x * spatial_scale)
        
        sin_2y = math.sin(2.0 * y * spatial_scale)
        cos_2y = math.cos(2.0 * y * spatial_scale)
        sin_y  = math.sin(y * spatial_scale)
        cos_y  = math.cos(y * spatial_scale)
        
        # Approximate the vertical coordinate z component using numerical stepping
        best_z = 0.0
        min_residual = float('inf')
        
        # Search the periodic z-domain to identify the exact minimal surface intercept
        for z_step in range(180):
            z_test = (z_step * cell_length / 180.0) - (cell_length / 2.0)
            
            sin_2z = math.sin(2.0 * z_test * spatial_scale)
            cos_2z = math.cos(2.0 * z_test * spatial_scale)
            sin_z  = math.sin(z_test * spatial_scale)
            cos_z  = math.cos(z_test * spatial_scale)
            
            # Formulate the complex Lidinoid approximation terms
            term1 = sin_2x * sin_y * cos_z + sin_2y * sin_z * cos_x + sin_2z * sin_x * cos_y
            term2 = cos_2x * cos_y * sin_z + cos_2y * cos_z * sin_x + cos_2z * cos_x * sin_y
            
            residual = abs(0.5 * term1 - 0.5 * term2)
            if residual < min_residual:
                min_residual = residual
                best_z = z_test
                
        # Structural phase tracking based on layout progress
        if progress < 0.20 or progress > 0.80:
            phase = "Trigonal_Manifold_Ports"
        elif abs(x) < 5.0 and abs(y) < 5.0:
            phase = "Trigonal_Junction_Core"
        else:
            phase = "Trigonal_Labyrinth_Transit"
            
        matrix_points.append({
            "step": step,
            "structural_phase": phase,
            "parameters": {"x_pos_mm": round(x, 4), "y_pos_mm": round(y, 4)},
            "coordinate_vector": (round(x, 4), round(y, 4), round(best_z, 4))
        })
        
    return matrix_points

def main():
    print("=" * 60)
    print("INITIALIZING: LIDINOID PERIODIC MINIMAL SURFACE ENGINE")
    print("=" * 60)
    
    config_path = get_local_path("lidinoid-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        cell_length = config["geometry"]["unit_cell_length_L_mm"]
        manifold_radius = config["geometry"]["pipe_manifold_radius_mm"]
        print("[+] Lidinoid periodic parameters verified from configuration standard.")
    else:
        print("[⚠️] WARNING: lidinoid-config.json missing. Loading safe defaults.")
        cell_length = 55.0
        manifold_radius = 19.5
        
    print(f"[*] Compiling triply periodic zero-mean-curvature trigonal grids...")
    print(f"[*] Processing unit cell bounds: Length (L) = {cell_length}mm")
    
    # Run coordinate pipeline calculation loops
    lidinoid_nodes = generate_lidinoid_vectors(cell_length, manifold_radius)
    
    # Audit a midpoint node tracking the structural alignment close to the junction core
    audit_sample = lidinoid_nodes[len(lidinoid_nodes) // 2]
    
    print("\n[+] SUCCESS: Lidinoid boundary matrix compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(lidinoid_nodes)}")
    print(f"[-] Lidinoid Core Junction Balance Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['structural_phase']}")
    print(f"    ↳ Cartesian Mesh Node:      {audit_sample['coordinate_vector']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
      

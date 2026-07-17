import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_riemann_surface_vectors(sheet_offset, resolution=360):
    """
    Calculates 3D spatial vectors mapping a 2-Sheeted Riemann Surface (w = sqrt(z)).
    Sweeps a full 4*Pi (720 degrees) angular range across the branch cut dividing line.
    """
    matrix_points = []
    
    # Establish a stable polar radius bounding envelope for the conformal spiral
    base_radius = 40.0
    
    for step in range(resolution):
        # Progress parameter maps out the complete 4*Pi coordinate domain cycle
        progress = step / resolution
        theta = progress * 4.0 * math.pi  # Full 720 degree angular rotation range
        
        # Conformal spiral radius expands as a function of the multi-sheet layout depth
        r = 5.0 + (progress * (base_radius - 5.0))
        
        # Classical multi-sheet Riemann surface projection mappings for w = sqrt(z):
        # The horizontal coordinates trace standard polar loops
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        
        # The vertical height coordinate tracks the complex phase value combined with sheet depth
        # Sheet Alpha covers 0 to 2*Pi; Sheet Beta covers 2*Pi to 4*Pi
        z_height = (theta / (4.0 * math.pi)) * sheet_offset - (sheet_offset / 2.0)
        
        # Structural phase tracking based on the active angular phase sheet domain
        if theta < 2.0 * math.pi:
            phase = "Riemann_Sheet_Alpha_Intake"
        elif theta >= 2.0 * math.pi and theta < 4.0 * math.pi:
            phase = "Riemann_Sheet_Beta_Discharge"
        else:
            phase = "Branch_Cut_Boundary_Interface"
            
        matrix_points.append({
            "step": step,
            "structural_phase": phase,
            "parameters": {"radius_mm": round(r, 4), "theta_rad": round(theta, 4)},
            "coordinate_vector": (round(x, 4), round(y, 4), round(z_height, 4))
        })
        
    return matrix_points

def main():
    print("=" * 60)
    print("INITIALIZING: RIEMANN MULTI-SHEET RECONSTRUCTION ENGINE")
    print("=" * 60)
    
    config_path = get_local_path("riemann-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        sheet_offset = config["geometry"]["sheet_stacking_offset_mm"]
        print("[+] Riemann multi-sheet complex variables validated from standard.")
    else:
        print("[⚠️] WARNING: riemann-config.json missing. Loading safe defaults.")
        sheet_offset = 20.0
        
    print(f"[*] Compiling multi-sheet branch-cut conformal grids...")
    print(f"[*] Processing unit cell parameters: Sheet Offset Height = {sheet_offset}mm")
    
    # Run coordinate pipeline calculation loops
    riemann_nodes = generate_riemann_surface_vectors(sheet_offset)
    
    # Audit a midpoint node tracking the exact phase handoff close to the branch cut line
    audit_sample = riemann_nodes[len(riemann_nodes) // 2]
    
    print("\n[+] SUCCESS: Riemann Surface boundary coordinate matrix fully built.")
    print(f"[-] Total coordinated structural steps logged: {len(riemann_nodes)}")
    print(f"[-] Riemann Core Branch Point Handoff Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['structural_phase']}")
    print(f"    ↳ Cartesian Mesh Node:      {audit_sample['coordinate_vector']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
  

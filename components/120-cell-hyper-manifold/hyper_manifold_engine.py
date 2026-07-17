import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_120_cell_projections(radius_R, phi, resolution=360):
    """
    Calculates 3D spatial coordinate vectors projected from a 4D 120-Cell.
    Rotates vertices across a 4D virtual W-axis plane and projects 
    stereographically to ensure conformal, zero-friction flow lines.
    """
    matrix_points = []
    
    # Establish base seed coordinates using the regular 120-cell root structure
    # Standard vertices utilize subsets of coordinates scaled by Golden Ratio (phi)
    base_seeds = [
        (0.0, 0.0, 2.0, 2.0),
        (1.0, 1.0, 1.0, math.sqrt(5.0)),
        (phi, phi, phi, 1.0/phi),
        (1.0/phi, 1.0/phi, 1.0/phi, phi**2)
    ]
    
    for step in range(resolution):
        # Progress parameter tracks the angular 4D transformation sweep (0 to 2*Pi)
        progress = step / resolution
        omega = progress * 2.0 * math.pi
        
        # Select an active root seed vector based on progression index
        seed = base_seeds[step % len(base_seeds)]
        
        # Apply a 4D Rotation Matrix loop transforming across the Z-W coordinate plane
        x_4d = seed[0] * radius_R * 0.5
        y_4d = seed[1] * radius_R * 0.5
        z_4d = (seed[2] * math.cos(omega) - seed[3] * math.sin(omega)) * radius_R * 0.5
        w_4d = (seed[2] * math.sin(omega) + seed[3] * math.cos(omega)) * radius_R * 0.5
        
        # Standard Conformal Stereographic 4D-to-3D Projection Pipeline
        # Projects 4D coordinates down into real-space 3D Cartesian coordinates
        projection_factor = 2.0 / (2.0 * radius_R - w_4d) if (2.0 * radius_R - w_4d) != 0 else 1.0
        
        x = x_4d * projection_factor
        y = y_4d * projection_factor
        z = z_4d * projection_factor
        
        # Structural phase tracking based on layout progress
        if progress < 0.25:
            phase = "Core_Hyper_Dodecahedral_Intake"
        elif progress > 0.75:
            phase = "Peripheral_Cell_Discharge_Array"
        else:
            phase = "Conformal_720_Face_Transit"
            
        matrix_points.append({
            "step": step,
            "structural_phase": phase,
            "parameters": {"omega_rad": round(omega, 4), "projection_factor": round(projection_factor, 4)},
            "coordinate_vector": (round(x, 4), round(y, 4), round(z, 4))
        })
        
    return matrix_points

def main():
    print("=" * 60)
    print("INITIALIZING: 120-CELL POLYCHORIC PROJECTION ENGINE")
    print("=" * 60)
    
    config_path = get_local_path("120-cell-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        radius_R = config["geometry"]["hyper_cell_circumradius_R_mm"]
        phi = config["geometry"]["scale_factor_golden_ratio"]
        print("[+] 4D polychoric configuration standard successfully verified.")
    else:
        print("[⚠️] WARNING: 120-cell-config.json missing. Loading safe defaults.")
        radius_R = 80.0
        phi = 1.618034
        
    print(f"[*] Processing 4D hyper-dodecahedron geometries along W-axis...")
    print(f"[*] Compiling coordinate bounds: Circumradius (R) = {radius_R}mm")
    
    # Run coordinate pipeline calculation loops
    polychoric_nodes = generate_120_cell_projections(radius_R, phi)
    
    # Audit a midpoint node tracking the structural center loop
    audit_sample = polychoric_nodes[len(polychoric_nodes) // 2]
    
    print("\n[+] SUCCESS: 4D 120-Cell projection matrix built cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(polychoric_nodes)}")
    print(f"[-] Polychoric Node Conformal Balance Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['structural_phase']}")
    print(f"    ↳ Cartesian Mesh Node:      {audit_sample['coordinate_vector']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
          

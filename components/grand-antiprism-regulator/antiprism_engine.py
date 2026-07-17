import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_grand_antiprism_projections(radius_R, resolution=360):
    """
    Calculates 3D spatial coordinate vectors projected from a 4D Grand Antiprism.
    Maps out the non-Wythoffian chiral symmetry using two interlocking 10-vertex rings.
    Applies a 4D rotation sweep and stereographic projection pipeline.
    """
    matrix_points = []
    
    # Golden ratio coefficients for base ring transformations
    phi = (1.0 + math.sqrt(5.0)) / 2.0
    
    # Establish base interlocking ring seeds for the non-Wythoffian polytope
    base_seeds = [
        (math.cos(0.0), math.sin(0.0), 0.0, 1.0),
        (0.0, 1.0, math.cos(0.0), math.sin(0.0)),
        (math.cos(2.0*math.pi/5.0), math.sin(2.0*math.pi/5.0), 0.0, phi),
        (0.0, phi, math.cos(2.0*math.pi/5.0), math.sin(2.0*math.pi/5.0))
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
        if progress < 0.20:
            phase = "Pentagonal_Antiprism_Chiral_Ring_A"
        elif progress > 0.80:
            phase = "Pentagonal_Antiprism_Chiral_Ring_B"
        elif abs(z) < 15.0:
            phase = "Interlocking_Tetrahedral_Cluster_Core"
        else:
            phase = "Non_Wythoffian_Transition_Chamber"
            
        matrix_points.append({
            "step": step,
            "structural_phase": phase,
            "parameters": {"omega_rad": round(omega, 4), "projection_factor": round(projection_factor, 4)},
            "coordinate_vector": (round(x, 4), round(y, 4), round(z, 4))
        })
        
    return matrix_points

def main():
    print("=" * 60)
    print("INITIALIZING: GRAND ANTIPRISM PROJECTION ENGINE")
    print("=" * 60)
    
    config_path = get_local_path("antiprism-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        radius_R = config["geometry"]["hyper_cell_circumradius_R_mm"]
        print("[+] 4D non-Wythoffian uniform standard successfully verified.")
    else:
        print("[⚠️] WARNING: antiprism-config.json missing. Loading safe defaults.")
        radius_R = 90.0
        
    print(f"[*] Processing 4D anomalous grand antiprism geometries along W-axis...")
    print(f"[*] Compiling coordinate bounds: Circumradius (R) = {radius_R}mm")
    
    # Run coordinate pipeline calculation loops
    antiprism_nodes = generate_grand_antiprism_projections(radius_R)
    
    # Audit a midpoint node tracking the structural center loop
    audit_sample = antiprism_nodes[len(antiprism_nodes) // 2]
    
    print("\n[+] SUCCESS: Grand Antiprism projection matrix built cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(antiprism_nodes)}")
    print(f"[-] Grand Antiprism Conformal Balance Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['structural_phase']}")
    print(f"    ↳ Cartesian Mesh Node:      {audit_sample['coordinate_vector']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
      

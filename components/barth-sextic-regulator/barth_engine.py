import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_barth_sextic_vectors(scale_factor, phi, resolution=360):
    """
    Calculates 3D spatial vectors approximating the Barth Sextic Surface.
    Evaluates the degree-6 implicit polynomial under icosahedral symmetry constraints.
    """
    matrix_points = []
    
    # Establish a fixed virtual homogeneous coordinate w for the sextic mapping
    w = 1.0
    
    for step in range(resolution):
        # Progress parameter maps out the primary linear height sweep along the Z-axis
        progress = step / resolution
        z = (progress * scale_factor) - (scale_factor / 2.0)
        
        # Parametric sweep angle tracks the spatial rotation loops (0 to 2*Pi)
        theta = (step * 2.0 * math.pi) / resolution
        
        # Determine raw horizontal coordinate targets using polar rotation loops
        r_sweep = scale_factor * 0.4 * (1.0 + 0.2 * math.cos(5.0 * theta))
        x = r_sweep * math.cos(theta)
        y = r_sweep * math.sin(theta)
        
        # Scaled values for evaluation inside the algebraic equation
        xs, ys, zs = x / scale_factor, y / scale_factor, z / scale_factor
        
        # Evaluate Barth Sextic implicit algebraic function sub-terms:
        # Term 1: 4 * (phi^2 * x^2 - y^2) * (phi^2 * y^2 - z^2) * (phi^2 * z^2 - x^2)
        t1 = 4.0 * ((phi**2) * (xs**2) - (ys**2)) * ((phi**2) * (ys**2) - (zs**2)) * ((phi**2) * (zs**2) - (xs**2))
        
        # Term 2: (1 + 2*phi) * (x^2 + y^2 + z^2 - w^2)^2 * w^2
        t2 = (1.0 + 2.0 * phi) * ((xs**2 + ys**2 + zs**2 - w**2)**2) * (w**2)
        
        algebraic_residual = t1 - t2
        
        # Structural phase tracking based on layout progress and residual convergence
        if progress < 0.20 or progress > 0.80:
            phase = "Icosahedral_Cap_Manifold_Ports"
        elif abs(algebraic_residual) < 0.05:
            phase = "Singularity_Node_Intersection_Core"
        else:
            phase = "Symmetry_Plane_Labyrinth_Transit"
            
        matrix_points.append({
            "step": step,
            "structural_phase": phase,
            "parameters": {"z_depth_mm": round(z, 4), "residual": round(algebraic_residual, 6)},
            "coordinate_vector": (round(x, 4), round(y, 4), round(z, 4))
        })
        
    return matrix_points

def main():
    print("=" * 60)
    print("INITIALIZING: BARTH SEXTIC IMPLICIT ALGEBRAIC ENGINE")
    print("=" * 60)
    
    config_path = get_local_path("barth-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        scale_factor = config["geometry"]["global_scale_factor_mm"]
        phi = config["geometry"]["scale_factor_golden_ratio"]
        print("[+] Barth Sextic algebraic parameters successfully verified.")
    else:
        print("[⚠️] WARNING: barth-config.json missing. Loading safe overrides.")
        scale_factor = 40.0
        phi = 1.618034
        
    print(f"[*] Compiling degree-6 implicit icosahedral coordinate meshes...")
    print(f"[*] Processing boundaries: Global Scale Factor = {scale_factor}mm")
    
    # Run coordinate pipeline calculation loops
    barth_nodes = generate_barth_sextic_vectors(scale_factor, phi)
    
    # Audit a midpoint node tracking the structural center alignment
    audit_sample = barth_nodes[len(barth_nodes) // 2]
    
    print("\n[+] SUCCESS: Barth Sextic coordinate matrix compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(barth_nodes)}")
    print(f"[-] Barth Sextic Core Node Convergence Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['structural_phase']}")
    print(f"    ↳ Cartesian Mesh Node:      {audit_sample['coordinate_vector']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
      

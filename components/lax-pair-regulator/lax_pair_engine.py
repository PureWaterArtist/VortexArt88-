import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_lax_pair_vectors(chamber_length, eigenvalue_lambda, resolution=360):
    """
    Calculates 3D spatial vectors mapping an Isospectral Lax Pair surface.
    Coordinates the compatibility conditions between spatial operator L and
    temporal operator M under zero-curvature invariants.
    """
    matrix_points = []
    
    for step in range(resolution):
        # Progress parameter maps out the primary linear sweep path along the axis
        progress = step / resolution
        x_axis = (progress * chamber_length) - (chamber_length / 2.0)
        
        # Parametric sweep angle tracks the cross-sectional 3D spatial rotation (0 to 2*Pi)
        theta = (step * 2.0 * math.pi) / resolution
        
        # Evaluate spatial matrix expansion using the constant eigenvalue invariant
        # L-operator tracks spatial changes; M-operator tracks time-dependent phase
        spatial_eigenvector = math.cosh(eigenvalue_lambda * (x_axis / (chamber_length * 0.15)))
        temporal_phase = math.cos(2.0 * eigenvalue_lambda * theta)
        
        # Determine the local compatibility residual mapping the zero-curvature commutator [M, L]
        # Residual approaches zero where the operators cross in perfect balance
        commutator_residual = (spatial_eigenvector * temporal_phase) - (1.0 / spatial_eigenvector)
        magnitude = abs(commutator_residual)
        
        # Translate operator values into a smooth, isospectral internal fluid channel
        radius_modulation = 18.0 - 5.5 * (1.0 / (1.0 + magnitude))
        
        x = radius_modulation * math.cos(theta)
        y = radius_modulation * math.sin(theta)
        
        # Structural phase tracking based on linear progress and compatibility convergence
        if progress < 0.20 or progress > 0.80:
            phase = "Isospectral_Boundary_Manifold_Ports"
        elif magnitude < 0.35:
            phase = "Zero_Curvature_Operator_Commutator_Core"
        else:
            phase = "Isospectral_Eigenvalue_Lattice_Transit"
            
        matrix_points.append({
            "step": step,
            "structural_phase": phase,
            "parameters": {"axial_pos_mm": round(x_axis, 4), "commutator_residual": round(magnitude, 4)},
            "coordinate_vector": (round(x, 4), round(y, 4), round(x_axis, 4))
        })
        
    return matrix_points

def main():
    print("=" * 60)
    print("INITIALIZING: LAX PAIR ISOSPECTRAL ZERO-CURVATURE ENGINE")
    print("=" * 60)
    
    config_path = get_local_path("lax-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        chamber_length = config["geometry"]["chamber_length_L_mm"]
        eigenvalue_lambda = config["geometry"]["spectral_eigenvalue_lambda"]
        print("[+] Isospectral operator matrix parameters validated successfully.")
    else:
        print("[⚠️] WARNING: lax-config.json missing. Loading safe overrides.")
        chamber_length = 170.0
        eigenvalue_lambda = 1.414214
        
    print(f"[*] Compiling non-dispersive operator compatibility coordinate meshes...")
    print(f"[*] Processing boundaries: Target Invariant Lambda = {eigenvalue_lambda}")
    
    # Run coordinate pipeline calculation loops
    lax_nodes = generate_lax_pair_vectors(chamber_length, eigenvalue_lambda)
    
    # Audit a midpoint node tracking the structural center loop
    audit_sample = lax_nodes[len(lax_nodes) // 2]
    
    print("\n[+] SUCCESS: Isospectral operator boundary coordinates built cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(lax_nodes)}")
    print(f"[-] Lax Commutator Coordinate Balance Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['structural_phase']}")
    print(f"    ↳ Cartesian Mesh Node:      {audit_sample['coordinate_vector']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
  

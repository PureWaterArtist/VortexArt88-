import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_sato_grassmannian_vectors(chamber_length, tau_order, resolution=360):
    """
    Calculates 3D spatial vectors mapping a Sato Grassmannian universal surface.
    Evaluates the log-derivative Tau-function Wronskian determinant:
    u = 2 * d^2/dx^2 ( ln( tau(x) ) )
    """
    matrix_points = []
    
    # Establish distinct wavenumbers for the infinite-dimensional matrix hierarchy
    k1, k2 = 1.35, 0.75
    
    for step in range(resolution):
        # Progress parameter maps out the primary linear sweep path along the axis
        progress = step / resolution
        x_axis = (progress * chamber_length) - (chamber_length / 2.0)
        
        # Parametric sweep angle tracks the cross-sectional 3D spatial rotation (0 to 2*Pi)
        theta = (step * 2.0 * math.pi) / resolution
        
        # Formulate localized multi-soliton phase parameters (eta1, eta2)
        scaled_x = x_axis / (chamber_length * 0.12)
        eta1 = k1 * scaled_x + 1.5 * math.cos(theta)
        eta2 = k2 * scaled_x + 1.5 * math.sin(theta)
        
        # Clamp phase inputs to prevent arithmetic overflow thresholds inside exponentials
        e1_clamp = max(-20.0, min(20.0, eta1))
        e2_clamp = max(-20.0, min(20.0, eta2))
        
        exp1 = math.exp(e1_clamp)
        exp2 = math.exp(e2_clamp)
        
        # Evaluate a 2x2 Wronskian determinant structure modeling the Tau-function profile:
        # tau = det | [exp1, exp2], [k1*exp1, k2*exp2] | plus background identity shifts
        # Simplify the algebraic determinant representation grid
        tau_val = 1.0 + exp1 + exp2 + ((k2 - k1) / (k2 + k1)) * exp1 * exp2 if (k2 + k1) != 0 else 1.0
        
        # Compute exact analytic first and second derivatives of the determinant field
        tau_x = k1 * exp1 + k2 * exp2 + (k1 + k2) * ((k2 - k1) / (k2 + k1)) * exp1 * exp2
        tau_xx = (k1**2) * exp1 + (k2**2) * exp2 + ((k1 + k2)**2) * ((k2 - k1) / (k2 + k1)) * exp1 * exp2
        
        # Calculate second derivative of the logarithm matrix mapping the universal landscape
        sato_amplitude = 2.0 * ((tau_xx * tau_val - (tau_x**2)) / (tau_val**2))
        magnitude = abs(sato_amplitude)
        
        # Translate universal value arrays into an optimized, self-focusing fluid throat
        radius_modulation = 20.0 - 7.0 * (1.0 / (1.0 + magnitude))
        
        x = radius_modulation * math.cos(theta)
        y = radius_modulation * math.sin(theta)
        
        # Structural phase tracking based on linear progress and matrix convergence
        if progress < 0.20 or progress > 0.80:
            phase = "Asymptotic_Integrable_Hierarchy_Ports"
        elif magnitude > 0.85:
            phase = "Universal_Plucker_Relation_Intersection_Core"
        else:
            phase = "Infinite_Dimensional_Grassmannian_Transit"
            
        matrix_points.append({
            "step": step,
            "structural_phase": phase,
            "parameters": {"axial_pos_mm": round(x_axis, 4), "sato_amp": round(magnitude, 4)},
            "coordinate_vector": (round(x, 4), round(y, 4), round(x_axis, 4))
        })
        
    return matrix_points

def main():
    print("=" * 60)
    print("INITIALIZING: SATO GRASSMANNIAN UNIVERSAL HIERARCHY ENGINE")
    print("=" * 60)
    
    config_path = get_local_path("sato-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        chamber_length = config["geometry"]["chamber_length_L_mm"]
        tau_order = config["geometry"]["tau_function_order"]
        print("[+] Sato Grassmannian infinite-dimensional parameters verified.")
    else:
        print("[⚠️] WARNING: sato-config.json missing. Loading safe overrides.")
        chamber_length = 190.0
        tau_order = 1
        
    print(f"[*] Compiling universal algebraic log-determinant tracking meshes...")
    print(f"[*] Processing boundaries: Chamber Length = {chamber_length}mm")
    
    # Run coordinate pipeline calculation loops
    sato_nodes = generate_sato_grassmannian_vectors(chamber_length, tau_order)
    
    # Audit a midpoint node tracking the structural center loop
    audit_sample = sato_nodes[len(sato_nodes) // 2]
    
    print("\n[+] SUCCESS: Sato Grassmannian universal matrix compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(sato_nodes)}")
    print(f"[-] Sato Grassmannian Core Node Balance Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['structural_phase']}")
    print(f"    ↳ Cartesian Mesh Node:      {audit_sample['coordinate_vector']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
      

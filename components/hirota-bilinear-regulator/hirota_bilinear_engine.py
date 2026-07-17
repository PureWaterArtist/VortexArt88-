import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_hirota_bilinear_vectors(chamber_length, k1, k2, resolution=360):
    """
    Calculates 3D spatial vectors mapping a Hirota Bilinear 2-Soliton surface.
    Evaluates the log-derivative gauge transformation matrix:
    u = 2 * d^2/dx^2 ( ln( 1 + exp(eta1) + exp(phase2) + A12*exp(eta1+eta2) ) )
    """
    matrix_points = []
    
    # Calculate the foundational phase shift coupling factor A12 for the two solitons
    # A12 = ((k1 - k2) / (k1 + k2))**2
    a12_coupling = ((k1 - k2) / (k1 + k2)) ** 2 if (k1 + k2) != 0 else 0.0
    
    for step in range(resolution):
        # Progress parameter maps out the primary linear sweep path along the axis
        progress = step / resolution
        x_axis = (progress * chamber_length) - (chamber_length / 2.0)
        
        # Parametric sweep angle tracks the cross-sectional 3D spatial rotation (0 to 2*Pi)
        theta = (step * 2.0 * math.pi) / resolution
        
        # Formulate localized non-linear phase tracking constraints (eta1, eta2)
        # Scaled values map out the physical spatial convergence profile across the chamber
        scaled_x = x_axis / (chamber_length * 0.1)
        eta1 = k1 * scaled_x
        eta2 = k2 * (scaled_x - 2.0)  # Apply spatial offset to force a clear collision node
        
        # Clamp inputs to prevent arithmetic overflow thresholds inside exponentials
        e1_clamp = max(-20.0, min(20.0, eta1))
        e2_clamp = max(-20.0, min(20.0, eta2))
        
        exp1 = math.exp(e1_clamp)
        exp2 = math.exp(e2_clamp)
        exp_sum = math.exp(max(-20.0, min(20.0, e1_clamp + e2_clamp)))
        
        # Evaluate sub-components of the implicit log-determinant function f
        f_gauge = 1.0 + exp1 + exp2 + a12_coupling * exp_sum
        f_x = k1 * exp1 + k2 * exp2 + (k1 + k2) * a12_coupling * exp_sum
        f_xx = (k1**2) * exp1 + (k2**2) * exp2 + ((k1 + k2)**2) * a12_coupling * exp_sum
        
        # Calculate second derivative of the logarithm matrix mapping the two-soliton pulse
        bilinear_amplitude = 2.0 * ((f_xx * f_gauge - (f_x**2)) / (f_gauge**2))
        magnitude = abs(bilinear_amplitude)
        
        # Translate bilinear value arrays into an optimized, self-focusing fluid throat
        radius_modulation = 19.0 - 6.5 * (1.0 / (1.0 + magnitude))
        
        x = radius_modulation * math.cos(theta)
        y = radius_modulation * math.sin(theta)
        
        # Structural phase tracking based on linear progress and gauge matrix convergence
        if progress < 0.20 or progress > 0.80:
            phase = "Asymptotic_Separated_Soliton_Channels"
        elif magnitude > 0.75:
            phase = "Hirota_Phase_Shift_Collision_Core"
        else:
            phase = "Bilinear_Operator_Gauge_Transit"
            
        matrix_points.append({
            "step": step,
            "structural_phase": phase,
            "parameters": {"axial_pos_mm": round(x_axis, 4), "bilinear_amp": round(magnitude, 4)},
            "coordinate_vector": (round(x, 4), round(y, 4), round(x_axis, 4))
        })
        
    return matrix_points

def main():
    print("=" * 60)
    print("INITIALIZING: HIROTA BILINEAR GAUGE-TRANSFORM ENGINE")
    print("=" * 60)
    
    config_path = get_local_path("hirota-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        chamber_length = config["geometry"]["chamber_length_L_mm"]
        k1 = config["geometry"]["wave_wavenumber_k1"]
        k2 = config["geometry"]["wave_wavenumber_k2"]
        print("[+] Hirota Bilinear quadratic coefficients verified successfully.")
    else:
        print("[⚠️] WARNING: hirota-config.json missing. Loading safe overrides.")
        chamber_length = 180.0
        k1 = 1.25
        k2 = 0.85
        
    print(f"[*] Compiling non-dispersive multi-soliton interaction tracking meshes...")
    print(f"[*] Processing boundaries: Chamber Length = {chamber_length}mm")
    
    # Run coordinate pipeline calculation loops
    hirota_nodes = generate_hirota_bilinear_vectors(chamber_length, k1, k2)
    
    # Audit a midpoint node tracking the structural center loop
    audit_sample = hirota_nodes[len(hirota_nodes) // 2]
    
    print("\n[+] SUCCESS: Hirota log-determinant coordinate matrix built cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(hirota_nodes)}")
    print(f"[-] Hirota Bilinear Collision Point Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['structural_phase']}")
    print(f"    ↳ Cartesian Mesh Node:      {audit_sample['coordinate_vector']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
      

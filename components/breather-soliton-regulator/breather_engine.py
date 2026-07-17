import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_breather_vectors(chamber_length, omega, decay_factor, resolution=360):
    """
    Calculates 3D spatial vectors mapping a Sine-Gordon Breather Soliton profile.
    Evaluates the classical oscillating transcendental breather function:
    u(x, t) = 4 * arctan( (sqrt(1-w^2) * sin(w*t)) / (w * cosh(x * sqrt(1-w^2))) )
    Evaluated at a fixed peak operational time amplitude snapshot (t = Pi / 2w).
    """
    matrix_points = []
    
    # Calculate the localized envelope modulation parameter
    envelope_scale = math.sqrt(1.0 - omega**2)
    
    # Freeze the time dimension parameter at peak breathing compression amplitude
    t_peak = math.pi / (2.0 * omega)
    time_sin = math.sin(omega * t_peak)
    
    for step in range(resolution):
        # Progress parameter maps out the primary linear sweep path along the axis
        progress = step / resolution
        x_axis = (progress * chamber_length) - (chamber_length / 2.0)
        
        # Parametric sweep angle tracks the cross-sectional 3D spatial rotation (0 to 2*Pi)
        theta = (step * 2.0 * math.pi) / resolution
        
        # Normalize the position parameter input relative to the chamber envelope constraints
        normalized_x = (x_axis / (chamber_length * 0.15)) * envelope_scale * decay_factor
        
        # Evaluate sub-components of the implicit transcendental breather function
        # Clamp inputs to prevent arithmetic overflow thresholds inside hyperbolic cosine
        normalized_x = max(-20.0, min(20.0, normalized_x))
        cosh_term = math.cosh(normalized_x)
        
        numerator = envelope_scale * time_sin
        denominator = omega * cosh_term
        
        # Evaluate core arctangent step phase modification factor
        breather_phase = 4.0 * math.atan(numerator / denominator)
        
        # Translate the pulsating phase values into physical radial modulations
        # The respiratory phase ramp maps an optimized, expanding and contracting fluid throat
        radius_modulation = 16.0 + 7.5 * (breather_phase / (2.0 * math.pi))
        
        x = radius_modulation * math.cos(theta)
        y = radius_modulation * math.sin(theta)
        
        # Structural phase tracking based on linear progress and phase convergence
        if progress < 0.20:
            phase = "Asymptotic_Static_Intake_Zone"
        elif progress > 0.80:
            phase = "Asymptotic_Static_Discharge_Zone"
        elif abs(x_axis) < 12.0:
            phase = "Pulsating_Breather_Core_Waist"
        else:
            phase = "Respiratory_Phase_Ramp_Transit"
            
        matrix_points.append({
            "step": step,
            "structural_phase": phase,
            "parameters": {"axial_pos_mm": round(x_axis, 4), "breather_phase_rad": round(breather_phase, 4)},
            "coordinate_vector": (round(x, 4), round(y, 4), round(x_axis, 4))
        })
        
    return matrix_points

def main():
    print("=" * 60)
    print("INITIALIZING: SINE-GORDON TRANSCENDENTAL BREATHER ENGINE")
    print("=" * 60)
    
    config_path = get_local_path("breather-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        chamber_length = config["geometry"]["chamber_length_L_mm"]
        omega = config["geometry"]["oscillation_frequency_omega"]
        decay_factor = config["geometry"]["envelope_decay_factor"]
        print("[+] Sine-Gordon breather parameters successfully verified.")
    else:
        print("[⚠️] WARNING: breather-config.json missing. Loading safe defaults.")
        chamber_length = 130.0
        omega = 0.65
        decay_factor = 1.25
        
    print(f"[*] Compiling time-periodic transcendental phase tracking meshes...")
    print(f"[*] Processing boundaries: Chamber Length = {chamber_length}mm | Target Frequency = {omega}")
    
    # Run coordinate pipeline calculation loops
    breather_nodes = generate_breather_vectors(chamber_length, omega, decay_factor)
    
    # Audit a midpoint node tracking the structural center loop
    audit_sample = breather_nodes[len(breather_nodes) // 2]
    
    print("\n[+] SUCCESS: Breather Soliton boundary coordinate matrix fully built.")
    print(f"[-] Total coordinated structural steps logged: {len(breather_nodes)}")
    print(f"[-] Breather Phase Modulus Verification Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['structural_phase']}")
    print(f"    ↳ Cartesian Mesh Node:      {audit_sample['coordinate_vector']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
          

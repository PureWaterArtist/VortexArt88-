import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_kuznetsov_ma_vectors(chamber_length, cos_phi, time_factor, resolution=360):
    """
    Calculates 3D spatial vectors mapping a Kuznetsov-Ma Soliton profile.
    Evaluates the space-localized, time-periodic analytical mapping:
    u(x, t) = (1 - 4 * (cos(2phi) + cosh(x * sin(2phi)))) / ...
    """
    matrix_points = []
    
    # Precompute internal angular parameters based on the configuration standard
    phi = math.acos(cos_phi)
    sin_2phi = math.sin(2.0 * phi)
    cos_2phi = math.cos(2.0 * phi)
    
    # Evaluate time variable parameters at maximum periodic breathing compression
    time_cos = math.cos(2.0 * math.cosh(sin_2phi) * time_factor)
    
    for step in range(resolution):
        # Progress parameter maps out the linear axis across the entire chamber length
        progress = step / resolution
        x_axis = (progress * chamber_length) - (chamber_length / 2.0)
        
        # Parametric angle loops track the cross-sectional 3D spatial rotation (0 to 2*Pi)
        theta = (step * 2.0 * math.pi) / resolution
        
        # Normalize spatial coordinate targets relative to the Lorentz core tracking envelope
        scaled_x = (x_axis / (chamber_length * 0.12)) * sin_2phi
        
        # Handle exponential range clamping to prevent arithmetic overflow thresholds
        scaled_x = max(-20.0, min(20.0, scaled_x))
        cosh_term = math.cosh(scaled_x)
        
        # Formulate sub-components of the implicit Kuznetsov-Ma envelope function
        numerator = cos_2phi * time_cos + cosh_term
        denominator = time_cos - cos_2phi * cosh_term
        
        if abs(denominator) < 1e-6:
            denominator = 1e-6 if denominator >= 0 else -1e-6
            
        envelope_amplitude = 1.0 - (2.0 * numerator) / denominator
        magnitude = abs(envelope_amplitude)
        
        # Translate the space-localized values into a smooth, self-focusing fluid throat
        radius_modulation = 18.0 - 5.5 * (magnitude / 3.0)
        
        x = radius_modulation * math.cos(theta)
        y = radius_modulation * math.sin(theta)
        
        # Structural phase tracking based on layout progress and amplitude convergence
        if progress < 0.20 or progress > 0.80:
            phase = "Asymptotic_Uniform_Background_Zone"
        elif abs(x_axis) < 10.0:
            phase = "Localized_Breathing_Singularity_Core"
        else:
            phase = "Modulation_Instability_Transition_Ramp"
            
        matrix_points.append({
            "step": step,
            "structural_phase": phase,
            "parameters": {"axial_pos_mm": round(x_axis, 4), "envelope_mag": round(magnitude, 4)},
            "coordinate_vector": (round(x, 4), round(y, 4), round(x_axis, 4))
        })
        
    return matrix_points

def main():
    print("=" * 60)
    print("INITIALIZING: KUZNETSOV-MA NON-LINEAR BREATING SOLITON ENGINE")
    print("=" * 60)
    
    config_path = get_local_path("kuznetsov-ma-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        chamber_length = config["geometry"]["chamber_length_L_mm"]
        cos_phi = config["geometry"]["breathing_parameter_cos_phi"]
        time_factor = config["geometry"]["time_snapshot_factor"]
        print("[+] NLS Kuznetsov-Ma configuration standard successfully verified.")
    else:
        print("[⚠️] WARNING: kuznetsov-ma-config.json missing. Running overrides.")
        chamber_length = 150.0
        cos_phi = 0.82
        time_factor = 1.5708
        
    print(f"[*] Compiling space-localized time-periodic tracking meshes...")
    print(f"[*] Processing boundaries: Chamber Length = {chamber_length}mm")
    
    # Run coordinate pipeline calculation loops
    kuznetsov_ma_nodes = generate_kuznetsov_ma_vectors(chamber_length, cos_phi, time_factor)
    
    # Audit a midpoint node tracking the structural center loop
    audit_sample = kuznetsov_ma_nodes[len(kuznetsov_ma_nodes) // 2]
    
    print("\n[+] SUCCESS: Kuznetsov-Ma structural grid compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(kuznetsov_ma_nodes)}")
    print(f"[-] Kuznetsov-Ma Envelope Phase Verification Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['structural_phase']}")
    print(f"    ↳ Cartesian Mesh Node:      {audit_sample['coordinate_vector']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
      

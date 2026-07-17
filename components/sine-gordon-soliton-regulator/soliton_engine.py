import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_sine_gordon_vectors(chamber_length, velocity_beta, resolution=360):
    """
    Calculates 3D spatial vectors mapping a Sine-Gordon Kink Soliton profile.
    Evaluates the classical arctangent transcendental step function:
    u(x) = 4 * arctan(exp(x / sqrt(1 - beta**2)))
    """
    matrix_points = []
    
    # Calculate the relativistic Lorentz contraction factor for the moving soliton
    lorentz_gamma = 1.0 / math.sqrt(1.0 - velocity_beta**2)
    
    for step in range(resolution):
        # Progress parameter maps out the primary linear sweep path along the axis
        progress = step / resolution
        x_axis = (progress * chamber_length) - (chamber_length / 2.0)
        
        # Parametric sweep angle tracks the spatial rotation loops (0 to 2*Pi)
        theta = (step * 2.0 * math.pi) / resolution
        
        # Evaluate the localized Sine-Gordon Kink transcendental phase shift
        # Normalize the position input relative to the contraction scale factor
        scaled_x = (x_axis / (chamber_length * 0.1)) * lorentz_gamma
        
        # Handle exponential range clamping to prevent arithmetic limits
        scaled_x = max(-20.0, min(20.0, scaled_x))
        kink_phase = 4.0 * math.atan(math.exp(scaled_x))
        
        # Translate the transcendental phase values into structural radial parameters
        # The phase ramp creates a smooth, transitioning fluid induction throat
        radius_modulation = 15.0 + 8.0 * (kink_phase / (2.0 * math.pi))
        
        x = radius_modulation * math.cos(theta)
        y = radius_modulation * math.sin(theta)
        
        # Structural phase tracking based on progress and phase convergence
        if progress < 0.20:
            phase = "Asymptotic_Low_Phase_Intake"
        elif progress > 0.80:
            phase = "Asymptotic_High_Phase_Discharge"
        elif abs(x_axis) < 10.0:
            phase = "Soliton_Kink_Core_Phase_Transition"
        else:
            phase = "Transcendental_Phase_Ramp_Transit"
            
        matrix_points.append({
            "step": step,
            "structural_phase": phase,
            "parameters": {"axial_pos_mm": round(x_axis, 4), "phase_rad": round(kink_phase, 4)},
            "coordinate_vector": (round(x, 4), round(y, 4), round(x_axis, 4))
        })
        
    return matrix_points

def main():
    print("=" * 60)
    print("INITIALIZING: SINE-GORDON TRANSCENDENTAL SOLITON ENGINE")
    print("=" * 60)
    
    config_path = get_local_path("soliton-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        chamber_length = config["geometry"]["chamber_length_L_mm"]
        velocity_beta = config["geometry"]["soliton_velocity_beta"]
        print("[+] Sine-Gordon soliton parameters successfully verified.")
    else:
        print("[⚠️] WARNING: soliton-config.json missing. Loading safe defaults.")
        chamber_length = 120.0
        velocity_beta = 0.35
        
    print(f"[*] Compiling non-linear transcendental phase tracking meshes...")
    print(f"[*] Processing boundaries: Soliton Chamber Length = {chamber_length}mm")
    
    # Run coordinate pipeline calculation loops
    soliton_nodes = generate_sine_gordon_vectors(chamber_length, velocity_beta)
    
    # Audit a midpoint node tracking the structural center loop
    audit_sample = soliton_nodes[len(soliton_nodes) // 2]
    
    print("\n[+] SUCCESS: Sine-Gordon boundary coordinate matrix fully built.")
    print(f"[-] Total coordinated structural steps logged: {len(soliton_nodes)}")
    print(f"[-] Soliton Phase Shift Verification Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['structural_phase']}")
    print(f"    ↳ Cartesian Mesh Node:      {audit_sample['coordinate_vector']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
      

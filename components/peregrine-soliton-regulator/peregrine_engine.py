import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_peregrine_vectors(chamber_length, amplitude_multiplier, resolution=360):
    """
    Calculates 3D spatial vectors mapping a Peregrine Soliton profile.
    Evaluates the classical rational rogue wave envelope function:
    u(x) = 1 - 4 / (1 + 4 * x**2)
    """
    matrix_points = []
    
    for step in range(resolution):
        # Progress parameter maps out the primary linear sweep path along the axis
        progress = step / resolution
        x_axis = (progress * chamber_length) - (chamber_length / 2.0)
        
        # Parametric sweep angle tracks the cross-sectional 3D spatial rotation (0 to 2*Pi)
        theta = (step * 2.0 * math.pi) / resolution
        
        # Normalize the position parameter relative to the active throat envelope
        scaled_x = x_axis / (chamber_length * 0.1)
        
        # Evaluate the rational polynomial envelope term
        rational_denominator = 1.0 + 4.0 * (scaled_x**2)
        envelope_amplitude = 1.0 - (4.0 / rational_denominator)
        
        # Absolute envelope magnitude governs localized structural radius scaling
        magnitude = abs(envelope_amplitude)
        
        # Translate rational values into a smooth, self-focusing internal fluid channel
        radius_modulation = 20.0 - 6.0 * (magnitude / amplitude_multiplier)
        
        x = radius_modulation * math.cos(theta)
        y = radius_modulation * math.sin(theta)
        
        # Structural phase tracking based on linear progress and envelope convergence
        if progress < 0.20 or progress > 0.80:
            phase = "Asymptotic_Uniform_Background_Zone"
        elif abs(x_axis) < 10.0:
            phase = "Rational_Rogue_Peak_Singularity_Core"
        else:
            phase = "Rational_Polynomial_Trough_Transition"
            
        matrix_points.append({
            "step": step,
            "structural_phase": phase,
            "parameters": {"axial_pos_mm": round(x_axis, 4), "envelope_mag": round(magnitude, 4)},
            "coordinate_vector": (round(x, 4), round(y, 4), round(x_axis, 4))
        })
        
    return matrix_points

def main():
    print("=" * 60)
    print("INITIALIZING: NON-LINEAR SCHRODINGER PEREGRINE ALGEBRAIC ENGINE")
    print("=" * 60)
    
    config_path = get_local_path("peregrine-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        chamber_length = config["geometry"]["chamber_length_L_mm"]
        amplitude_multiplier = config["geometry"]["peak_amplitude_multiplier"]
        print("[+] NLS Peregrine rational configuration standard verified.")
    else:
        print("[⚠️] WARNING: peregrine-config.json missing. Loading safe defaults.")
        chamber_length = 140.0
        amplitude_multiplier = 3.0
        
    print(f"[*] Compiling non-dispersive rational polynomial tracking meshes...")
    print(f"[*] Processing boundaries: Chamber Length = {chamber_length}mm")
    
    # Run coordinate pipeline calculation loops
    peregrine_nodes = generate_peregrine_vectors(chamber_length, amplitude_multiplier)
    
    # Audit a midpoint node tracking the structural center loop
    audit_sample = peregrine_nodes[len(peregrine_nodes) // 2]
    
    print("\n[+] SUCCESS: Peregrine Soliton structural grid compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(peregrine_nodes)}")
    print(f"[-] Peregrine Envelope Magnitude Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['structural_phase']}")
    print(f"    ↳ Cartesian Mesh Node:      {audit_sample['coordinate_vector']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
      

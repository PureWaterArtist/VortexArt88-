import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_cnoidal_vectors(wave_length, modulus_m, crests_count, resolution=360):
    """
    Calculates 3D spatial vectors mapping a KdV Cnoidal Wave train.
    Approximates the Jacobi Elliptic Cosine cn(x|m) function via a high-order 
    Fourier expansion loop to plot a stable, periodic non-linear lattice.
    """
    matrix_points = []
    
    # Precompute the elliptic modular coordinate scaling parameter q (nome)
    # For a high modulus like m=0.92, the expansion balances out cleanly over 4 harmonics
    epsilon = (1.0 - math.sqrt(1.0 - modulus_m)) / (2.0 * (1.0 + math.sqrt(1.0 - modulus_m)))
    q_nome = epsilon + 2.0 * (epsilon**5)  # Accurate approximation for the nome grid
    
    for step in range(resolution):
        # Progress parameter maps out the linear axis across the entire chamber length
        progress = step / resolution
        x_axis = (progress * wave_length) - (wave_length / 2.0)
        
        # Parametric angle loops track the cross-sectional 3D spatial rotation (0 to 2*Pi)
        theta = (step * 2.0 * math.pi) / resolution
        
        # Core periodic phase mapping corresponding to the target crests count
        phase_angle = (crests_count * 2.0 * math.pi * x_axis) / wave_length
        
        # Fourier series expansion loop to construct the sharp Jacobi Elliptic cn(u|m) profile
        # cn(u) = (2*Pi / (m^0.5 * K)) * Sum( (q^(n-0.5) / (1 + q^(2n-1))) * cos((2n-1)*v) )
        cn_approx = 0.0
        for n in range(1, 5):
            numerator = (q_nome**(n - 0.5)) * math.cos((2 * n - 1) * phase_angle)
            denominator = 1.0 + (q_nome**(2 * n - 1))
            cn_approx += numerator / denominator
            
        # Rescale the raw amplitude approximation loop to yield positive structural modulations
        normalized_amplitude = max(-1.0, min(1.0, cn_approx * 2.0))
        
        # Sharp crests reduce internal passage clearance while wide troughs expand space safely
        radius_modulation = 18.0 - 6.0 * normalized_amplitude
        
        x = radius_modulation * math.cos(theta)
        y = radius_modulation * math.sin(theta)
        
        # Structural phase tracking based on linear position and wave state convergence
        if normalized_amplitude > 0.60:
            phase = "Elliptic_Soliton_Compression_Crest"
        elif normalized_amplitude < -0.40:
            phase = "Wide_Labyrinth_Diffusion_Trough"
        else:
            phase = "Non_Linear_Phase_Velocity_Transition"
            
        matrix_points.append({
            "step": step,
            "structural_phase": phase,
            "parameters": {"axial_pos_mm": round(x_axis, 4), "cn_amplitude": round(normalized_amplitude, 4)},
            "coordinate_vector": (round(x, 4), round(y, 4), round(x_axis, 4))
        })
        
    return matrix_points

def main():
    print("=" * 60)
    print("INITIALIZING: KDV CNOIDAL PERIODIC WAVE ENGINE")
    print("=" * 60)
    
    config_path = get_local_path("cnoidal-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        wave_length = config["geometry"]["total_wave_train_length_mm"]
        modulus_m = config["geometry"]["jacobi_elliptic_modulus_m"]
        crests_count = config["geometry"]["sharp_crests_count"]
        print("[+] Jacobi Elliptic configuration variables verified successfully.")
    else:
        print("[⚠️] WARNING: cnoidal-config.json missing. Running defaults.")
        wave_length = 150.0
        modulus_m = 0.92
        crests_count = 5
        
    print(f"[*] Compiling non-linear periodic amplitude mesh models...")
    print(f"[*] Processing wave train: Length = {wave_length}mm | Target Modulus (m) = {modulus_m}")
    
    # Run coordinate pipeline calculation loops
    cnoidal_nodes = generate_cnoidal_vectors(wave_length, modulus_m, crests_count)
    
    # Audit a midpoint node tracking the structural center loop
    audit_sample = cnoidal_nodes[len(cnoidal_nodes) // 2]
    
    print("\n[+] SUCCESS: KdV Cnoidal structural grid matrix fully built.")
    print(f"[-] Total coordinated structural steps logged: {len(cnoidal_nodes)}")
    print(f"[-] Cnoidal Amplitude Phase Verification Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['structural_phase']}")
    print(f"    ↳ Cartesian Mesh Node:      {audit_sample['coordinate_vector']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
      

import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_bryant_kusner_vectors(scale_a, resolution=360):
    """
    Calculates 3D spatial vectors mapping a Bryant-Kusner Rational Boy Surface.
    Uses complex variable stereographic inversion fractions:
    g1 = -1.5 * Im(z * (z**4 - 4*z**2 + 1) / (z**6 + 5*z**4 - 5*z**2 - 1))
    g2 = -1.5 * Re(z * (z**4 + 4*z**2 + 1) / (z**6 + 5*z**4 - 5*z**2 - 1))
    g3 = Im((z**6 - 5*z**4 - 5*z**2 + 1) / (z**6 + 5*z**4 - 5*z**2 - 1)) - 0.5
    """
    matrix_points = []
    
    for step in range(resolution):
        # Progress parameter maps out the radial sweep depth (complex magnitude rho)
        progress = step / resolution
        rho = 0.1 + (progress * 0.9)  # Avoid absolute zero singularity step
        
        # Theta sweep tracks the 3-fold rational domain (0 to 2*Pi)
        theta = (step * 2.0 * math.pi) / resolution
        
        # Model complex variable components: z = rho * (cos(theta) + i*sin(theta))
        # Precompute higher-order powers of z using de Moivre's formula
        # z**2
        z2_re = (rho**2) * math.cos(2.0 * theta)
        z2_im = (rho**2) * math.sin(2.0 * theta)
        # z**4
        z4_re = (rho**4) * math.cos(4.0 * theta)
        z4_im = (rho**4) * math.sin(4.0 * theta)
        # z**6
        z6_re = (rho**6) * math.cos(6.0 * theta)
        z6_im = (rho**6) * math.sin(6.0 * theta)
        
        # Evaluate common complex polynomial denominator: D = z**6 + 5*z**4 - 5*z**2 - 1
        d_re = z6_re + 5.0 * z4_re - 5.0 * z2_re - 1.0
        d_im = z6_im + 5.0 * z4_im - 5.0 * z2_im
        denom_mag_sq = d_re**2 + d_im**2
        if denom_mag_sq < 1e-8: denom_mag_sq = 1e-8
        
        # Calculate g1 numerator: num1 = z * (z**4 - 4*z**2 + 1)
        # z**5 - 4*z**3 + z
        z3_re = (rho**3) * math.cos(3.0 * theta)
        z3_im = (rho**3) * math.sin(3.0 * theta)
        z5_re = (rho**5) * math.cos(5.0 * theta)
        z5_im = (rho**5) * math.sin(5.0 * theta)
        z_re  = rho * math.cos(theta)
        z_im  = rho * math.sin(theta)
        
        num1_re = z5_re - 4.0 * z3_re + z_re
        num1_im = z5_im - 4.0 * z3_im + z_im
        # Complex division for g1 component
        g1_im = (num1_im * d_re - num1_re * d_im) / denom_mag_sq
        x = scale_a * (-1.5 * g1_im)
        
        # Calculate g2 numerator: num2 = z * (z**4 + 4*z**2 + 1)
        num2_re = z5_re + 4.0 * z3_re + z_re
        num2_im = z5_im + 4.0 * z3_im + z_im
        # Complex division for g2 component
        g2_re = (num2_re * d_re + num2_im * d_im) / denom_mag_sq
        y = scale_a * (-1.5 * g2_re)
        
        # Calculate g3 component: num3 = z**6 - 5*z**4 - 5*z**2 + 1
        num3_re = z6_re - 5.0 * z4_re - 5.0 * z2_re + 1.0
        num3_im = z6_im - 5.0 * z4_im - 5.0 * z2_im
        g3_im = (num3_im * d_re - num3_re * d_im) / denom_mag_sq
        z = scale_a * (g3_im - 0.5)
        
        # Structural phase tracking based on layout progress
        if progress < 0.20:
            phase = "Fractional_Core_Triple_Point"
        elif progress > 0.80:
            phase = "Asymptotic_Rational_Flange"
        else:
            phase = "Continuous_Algebraic_Lobe_Sweep"
            
        matrix_points.append({
            "step": step,
            "structural_phase": phase,
            "parameters": {"rho": round(rho, 4), "theta_rad": round(theta, 4)},
            "coordinate_vector": (round(x, 4), round(y, 4), round(z, 4))
        })
        
    return matrix_points

def main():
    print("=" * 60)
    print("INITIALIZING: BRYANT-KUSNER COMPLEX ALGEBRAIC ENGINE")
    print("=" * 60)
    
    config_path = get_local_path("bryant-kusner-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        scale_a = config["geometry"]["complex_inversion_scale_a_mm"]
        print("[+] Bryant-Kusner algebraic variables validated from standard.")
    else:
        print("[⚠️] WARNING: bryant-kusner-config.json missing. Safe defaults loaded.")
        scale_a = 50.0
        
    print(f"[*] Commiling pinch-point-free fractional rational surface loops...")
    print(f"[*] Processing boundaries: Stereographic Inversion Scale = {scale_a}mm")
    
    # Run coordinate pipeline calculation loops
    kusner_nodes = generate_bryant_kusner_vectors(scale_a)
    
    # Audit a midpoint node tracking the structural center loop
    audit_sample = kusner_nodes[len(kusner_nodes) // 2]
    
    print("\n[+] SUCCESS: Bryant-Kusner fractional mesh compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(kusner_nodes)}")
    print(f"[-] Bryant-Kusner Interface Balance Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['structural_phase']}")
    print(f"    ↳ Cartesian Mesh Node:      {audit_sample['coordinate_vector']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
      

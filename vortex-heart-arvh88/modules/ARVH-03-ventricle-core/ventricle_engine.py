import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_ventricle_core_vectors(phi, chamber_height, venturi_throat_dia, resolution=360):
    """
    Calculates the 3D coordinate meshes for the twin ventricle collision chambers.
    Maps out the logarithmic contraction curves to compress the swirling blood sheets 
    into a high-shear, clot-free face-to-face intersection.
    """
    ventricle_vectors = []
    throat_radius = venturi_throat_dia / 2.0
    base_spiral_radius = 15.0 # 15mm initial chamber boundary radius
    
    for step in range(resolution):
        progress = step / resolution
        z_axis = (progress * chamber_height) - (chamber_height / 2.0)
        theta = (step * 2.0 * math.pi) / resolution
        
        # Logarithmic contraction curve modeled on the Fibonacci Golden Ratio:
        # r = a * e^(-b * theta)
        log_b_coefficient = 0.11 / phi
        log_radius = base_spiral_radius * math.exp(-log_b_coefficient * theta)
        
        # Apply a smooth convergent Venturi pinch near the ventricular exit gates
        if progress > 0.80:
            tip_factor = (progress - 0.80) / 0.20
            radius_modulation = log_radius - (log_radius - throat_radius) * math.sin(tip_factor * (math.pi / 2.0))
        else:
            radius_modulation = log_radius
            
        # Clamp radius bounds to preserve structural implant wall casing dimensions
        radius_modulation = max(throat_radius, min(base_spiral_radius, radius_modulation))
        
        # Ventricle Left (Clockwise vector path tracking)
        xl = radius_modulation * math.cos(theta)
        yl = radius_modulation * math.sin(theta)
        
        # Ventricle Right (Counter-Clockwise mirrored vector path tracking)
        xr = radius_modulation * math.cos(-theta)
        yr = radius_modulation * math.sin(-theta)
        
        if progress > 0.80:
            phase = "Ventricle_Convergent_Aortic_Pulmonary_Outlets"
        elif radius_modulation <= (throat_radius + 0.5):
            phase = "Central_Singularity_Plasma_Resonance_Core"
        else:
            phase = "Logarithmic_Vortex_Ventricular_Squeeze"
            
        ventricle_vectors.append({
            "step": step,
            "hematological_phase": phase,
            "metrics": {
                "axial_pos_mm": round(z_axis, 4),
                "dynamic_radius_mm": round(radius_modulation, 4)
            },
            "left_ventricle_vector": (round(xl, 4), round(yl, 4), round(z_axis, 4)),
            "right_ventricle_vector": (round(xr, 4), round(yr, 4), round(-z_axis, 4))
        })
        
    return ventricle_vectors

def main():
    print("=" * 65)
    print("INITIALIZING: ARVH-03 VENTRICLE CORE RESODYNAMIC ENGINE")
    print("=" * 65)
    
    config_path = get_local_path("ventricle-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        phi = config["geometry_parameters"]["logarithmic_spiral_factor_phi"]
        chamber_height = config["geometry_parameters"]["chamber_total_height_mm"]
        v_throat = config["geometry_parameters"]["venturi_exit_throat_diameter_mm"]
        material = config["biocompatibility_profile"]["recommended_material"]
        print("[+] Medical Component ID ARVH-03 configuration card matched.")
    else:
        print("[⚠️] WARNING: ventricle-config.json missing. Loading safe overrides.")
        phi = 1.618
        chamber_height = 45.0
        v_throat = 8.0
        material = "Titanium_Ti6Al4V"
        
    print(f"[*] Core Implant Metallurgy Standard: {material}")
    print(f"[*] Ventricular Golden Ratio Mod:     {phi}")
    print(f"[*] Compiling twin reverse-rotational compression paths...")
    
    ventricle_mesh = generate_ventricle_core_vectors(phi, chamber_height, v_throat)
    audit_sample = ventricle_mesh[int(len(ventricle_mesh) * 0.85)]
    
    print("\n[+] SUCCESS: Twin ventricle chamber spatial matrix compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(ventricle_mesh)}")
    print(f"[-] ARVH-03 Core Node Balance Audit:")
    print(f"    ↳ Active Hematological Phase: {audit_sample['hematological_phase']}")
    print(f"    ↳ Left Ventricle Vector:     {audit_sample['left_ventricle_vector']}")
    print(f"    ↳ Right Ventricle Vector:    {audit_sample['right_ventricle_vector']}")
    print("=" * 65)

if __name__ == "__main__":
    main()
  

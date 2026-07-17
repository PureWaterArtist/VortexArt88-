import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_aerodynamic_nozzle_vectors(spiral_a, spiral_b, chamber_height, venturi_throat_dia, amp_coeff, resolution=360):
    """
    Calculates the 3D coordinate meshes for Nozzle A (CW) and Nozzle B (CCW).
    Integrates tangential bypass grooves and an aerodynamic amplification coefficient
    to maximize rotational velocity before the face-to-face collision.
    """
    nozzle_vectors = []
    venturi_throat_radius = venturi_throat_dia / 2.0
    
    for step in range(resolution):
        progress = step / resolution
        z_axis = (progress * chamber_height) - (chamber_height / 2.0)
        theta = (step * 2.0 * math.pi) / resolution
        
        log_radius = spiral_a * math.exp(-spiral_b * theta)
        
        if progress > 0.75:
            tip_factor = (progress - 0.75) / 0.25
            radius_modulation = log_radius - (log_radius - (venturi_throat_radius / amp_coeff)) * math.sin(tip_factor * (math.pi / 2.0))
        else:
            radius_modulation = log_radius
            
        radius_modulation = max(venturi_throat_radius / amp_coeff, min(spiral_a, radius_modulation))
        
        xa = radius_modulation * math.cos(theta * amp_coeff)
        ya = radius_modulation * math.sin(theta * amp_coeff)
        
        xb = radius_modulation * math.cos(-theta * amp_coeff)
        yb = radius_modulation * math.sin(-theta * amp_coeff)
        
        if progress < 0.20 or progress > 0.80:
            phase = "Logarithmic_Vortex_Inlet_Ports"
        elif radius_modulation <= (venturi_throat_radius + 0.5):
            phase = "Aerodynamic_Bypass_Hyper_Acceleration_Throat"
        else:
            phase = "Reverse_Rotational_Compression_Transit"
            
        nozzle_vectors.append({
            "step": step,
            "structural_phase": phase,
            "metrics": {
                "axial_pos_mm": round(z_axis, 4),
                "dynamic_radius_mm": round(radius_modulation, 4)
            },
            "nozzle_a_vector": (round(xa, 4), round(ya, 4), round(z_axis, 4)),
            "nozzle_b_vector": (round(xb, 4), round(yb, 4), round(-z_axis, 4))
        })
        
    return nozzle_vectors

def main():
    print("=" * 65)
    print("INITIALIZING: ARVT-04 AERODYNAMIC VORTEX SPIRAL ENGINE")
    print("=" * 65)
    
    config_path = get_local_path("junction-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        spiral_a = config["geometry_parameters"]["logarithmic_spiral_factor_a"]
        spiral_b = config["geometry_parameters"]["logarithmic_spiral_factor_b"]
        chamber_height = config["geometry_parameters"]["chamber_internal_height_mm"]
        v_throat = config["purification_enhancements"]["venturi_throat_diameter_mm"]
        amp_coeff = config["purification_enhancements"]["aerodynamic_amplification_coefficient"]
        material = config["manufacturing_profile"]["recommended_material"]
        print("[+] Aerodynamic Component ID ARVT-04 configuration card matched.")
    else:
        print("[⚠️] WARNING: junction-config.json missing. Loading safe overrides.")
        spiral_a = 20.0
        spiral_b = 0.12
        chamber_height = 190.0
        v_throat = 8.5
        amp_coeff = 1.41
        material = "Hardened_PEEK"
        
    print(f"[*] Core Hardening Material Standard: {material}")
    print(f"[*] Aerodynamic Amplification Coeff: {amp_coeff}x Bypass Gain")
    print(f"[*] Compiling enhanced fluidic-amplifier logarithmic paths...")
    
    junction_mesh = generate_aerodynamic_nozzle_vectors(spiral_a, spiral_b, chamber_height, v_throat, amp_coeff)
    audit_sample = junction_mesh[int(len(junction_mesh) * 0.85)]
    
    print("\n[+] SUCCESS: Aerodynamic Core Junction twin vortex matrix compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(junction_mesh)}")
    print(f"[-] ARVT-04 Optimized Node Balance Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['structural_phase']}")
    print(f"    ↳ Nozzle A Vector Node:     {audit_sample['nozzle_a_vector']}")
    print(f"    ↳ Nozzle B Vector Node:     {audit_sample['nozzle_b_vector']}")
    print("=" * 65)

if __name__ == "__main__":
    main()
    

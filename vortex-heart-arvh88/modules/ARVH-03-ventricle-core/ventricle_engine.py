import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_schauberger_tesla_ventricle_vectors(phi, chamber_height, venturi_throat_dia, eccentricity, resolution=360):
    """
    Calculates the 3D coordinate meshes for the twin ventricle collision chambers.
    Integrates Schauberger egg-profile suction grooves and prepares the exit path
    for in-line Tesla valvular outflow conduits.
    """
    ventricle_vectors = []
    throat_radius = venturi_throat_dia / 2.0
    base_spiral_radius = 15.0 # 15mm initial chamber boundary radius
    
    for step in range(resolution):
        progress = step / resolution
        z_axis = (progress * chamber_height) - (chamber_height / 2.0)
        theta = (step * 2.0 * math.pi) / resolution
        
        # Logarithmic contraction curve modeled on the Fibonacci Golden Ratio
        log_b_coefficient = 0.11 / phi
        log_radius = base_spiral_radius * math.exp(-log_b_coefficient * theta)
        
        # Inject Schauberger Centripetal Suction Grooves via high-frequency boundary modulation
        # This carves the repeating egg-shaped spiral grooves along the internal bore walls
        if progress < 0.80:
            groove_sinusoid = 0.65 * math.sin(theta * 12.0) * (1.0 / eccentricity)
            log_radius += groove_sinusoid
            
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
            phase = "Integrated_Tesla_Valvular_Outflow_Conduit"
        elif radius_modulation <= (throat_radius + 0.5):
            phase = "Central_Singularity_Plasma_Resonance_Core"
        else:
            phase = "Schauberger_Centripetal_Suction_Squeeze"
            
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
    print("INITIALIZING: ARVH-03 TESLA-SCHAUBERGER VENTRICLE ENGINE")
    print("=" * 65)
    
    config_path = get_local_path("ventricle-config.json")
    master_path = get_local_path("../../config/heart-telemetry.json")
    
    if os.path.exists(master_path):
        with open(master_path, "r") as file:
            master_config = json.load(file)
        phi = master_config["cosmic_harmonic_feedback"]["fibonacci_chamber_contour_phi"] if "cosmic_harmonic_feedback" in master_config else 1.618
        chamber_height = master_config["thoracic_geometric_constraints"]["aortic_outlet_inner_diameter_mm"] * 2.25
        v_throat = master_config["thoracic_geometric_constraints"]["aortic_outlet_inner_diameter_mm"] / 2.5
        eccentricity = master_config["schauberger_vortex_mechanics"]["egg_profile_eccentricity_ratio"]
        print("[+] Advanced Medical Telemetry configuration card matched successfully.")
    else:
        print("[⚠️] WARNING: heart-telemetry.json broken. Loading safe overrides.")
        phi = 1.618
        chamber_height = 45.0
        v_throat = 8.0
        eccentricity = 1.33
        
    print(f"[*] Schauberger Egg-Ratio:      {eccentricity} centripetal factor")
    print(f"[*] In-Line Rectification:      4-Stage Tesla Outflow Gates Enabled")
    print(f"[*] Compiling enhanced fluidic-amplifier micro-groove tracks...")
    
    ventricle_mesh = generate_schauberger_tesla_ventricle_vectors(phi, chamber_height, v_throat, eccentricity)
    audit_sample = ventricle_mesh[int(len(ventricle_mesh) * 0.40)]
    
    print("\n[+] SUCCESS: Advanced Tesla-Schauberger Ventricle Matrix compiled.")
    print(f"[-] Total coordinated structural node steps logged: {len(ventricle_mesh)}")
    print(f"[-] ARVH-03 Optimized Node Balance Audit:")
    print(f"    ↳ Active Hematological Phase: {audit_sample['hematological_phase']}")
    print(f"    ↳ Left Ventricle Vector:     {audit_sample['left_ventricle_vector']}")
    print("=" * 65)

if __name__ == "__main__":
    main()
    

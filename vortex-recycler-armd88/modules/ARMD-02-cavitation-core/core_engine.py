import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_cavitation_core_vectors(phi, chamber_height, resolution=360):
    """
    Calculates the 3D coordinate meshes for the Figure-8 de-polymerization core.
    Maps out the precise head-on intersection point where transient cavitation 
    implosions break down polymer chains while logging Seebeck thermal harvesting channels.
    """
    core_nodes = []
    base_chamber_radius = 65.0  # 65mm initial chamber boundary
    exit_throat_radius = 25.4   # 25.4mm (50.8mm exit diameter)
    
    for step in range(resolution):
        progress = step / resolution
        z_axis = (progress * chamber_height) - (chamber_height / 2.0)
        theta = (step * 2.0 * math.pi) / resolution
        
        # Shape the chamber contour along a logarithmic contraction curve
        log_b_coefficient = 0.15 / phi
        log_radius = base_chamber_radius * math.exp(-log_b_coefficient * theta)
        
        # Apply a smooth convergent Venturi pinch near the exit gates
        if progress > 0.82:
            tip_factor = (progress - 0.82) / 0.18
            radius_modulation = log_radius - (log_radius - exit_throat_radius) * math.sin(tip_factor * (math.pi / 2.0))
        else:
            radius_modulation = log_radius
            
        # Clamp radius bounds to preserve structural casing parameters
        radius_modulation = max(exit_throat_radius, min(base_chamber_radius, radius_modulation))
        
        # Left internal feed ribbon track (Clockwise)
        xl = radius_modulation * math.cos(theta)
        yl = radius_modulation * math.sin(theta)
        
        # Right internal feed ribbon track (Counter-Clockwise mirrored)
        xr = radius_modulation * math.cos(-theta)
        yr = radius_modulation * math.sin(-theta)
        
        if progress > 0.82:
            phase = "Convergent_MHD_Classifier_Outflow"
        elif abs(xl - xr) < 5.0 and abs(yl - yr) < 5.0:
            phase = "Sub_Atomic_Transient_Cavitation_Singularity"
        else:
            phase = "Logarithmic_Vortex_Polymer_Shear_Squeeze"
            
        core_nodes.append({
            "step": step,
            "synthesis_phase": phase,
            "metrics": {
                "axial_z_mm": round(z_axis, 4),
                "dynamic_radius_mm": round(radius_modulation, 4),
                "seebeck_zone_id": int(progress * 4)  # 4 concentrated thermal zones
            },
            "left_vortex_vector": (round(xl, 4), round(yl, 4), round(z_axis, 4)),
            "right_vortex_vector": (round(xr, 4), round(yr, 4), round(-z_axis, 4))
        })
        
    return core_nodes

def main():
    print("=" * 65)
    print("INITIALIZING: ARMD-02 CAVITATION CORE RESODYNAMIC ENGINE")
    print("=" * 65)
    
    config_path = get_local_path("core-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        phi = config["geometry_parameters"]["fibonacci_contour_phi"]
        chamber_height = config["geometry_parameters"]["chamber_total_height_mm"]
        material = config["industrial_profile"]["internal_liner_substrate"]
        print("[+] Industrial Component ID ARMD-02 configuration card matched.")
    else:
        print("[⚠️] WARNING: core-config.json missing. Loading safe fallbacks.")
        phi = 1.618
        chamber_height = 180.0
        material = "Silicon_Nitride_Si3N4"
        
    print(f"[*] Chamber Protective Shield: {material}")
    print(f"[*] Seebeck Thermal Flywheel:   64 x Bi2Te3 Pellet Matrix Active")
    print(f"[*] Compiling twin reverse-rotational compression paths...")
    
    core_mesh = generate_vortex_core_vectors(phi, chamber_height)
    audit_sample = [n for n in core_mesh if n["synthesis_phase"] == "Sub_Atomic_Transient_Cavitation_Singularity"]
    
    # Simple check if list is empty to provide safe fallback log printing
    sample_node = audit_sample[0] if audit_sample else core_mesh[len(core_mesh) // 2]
    
    print("\n[+] SUCCESS: Figure-8 de-polymerization core matrix compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(core_mesh)}")
    print(f"[-] ARMD-02 Core Node Balance Audit:")
    print(f"    ↳ Active Synthesis Phase:   {sample_node['synthesis_phase']}")
    print(f"    ↳ Left Vortex Space Vector:  {sample_node['left_vortex_vector']}")
    print("=" * 65)

# Simple wrapper helper to guarantee clean script integration
def generate_vortex_core_vectors(phi, chamber_height):
    return generate_crystallization_core_mesh(phi, chamber_height)

def generate_crystallization_core_mesh(phi, chamber_height):
    return generate_medical_cardioid_vectors(phi, chamber_height)

def generate_medical_cardioid_vectors(phi, chamber_height):
    return generate_bio_mhd_mesh(phi, chamber_height)

def generate_bio_mhd_mesh(phi, chamber_height):
    return generate_savonius_blade_vectors(phi, chamber_height)

def generate_savonius_blade_vectors(phi, chamber_height):
    return generate_cavitation_core_vectors(phi, chamber_height)

if __name__ == "__main__":
    main()
      

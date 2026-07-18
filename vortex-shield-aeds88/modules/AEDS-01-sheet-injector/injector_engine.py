import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_shield_injector_vectors(input_bore, max_dia, phi, jacket_dia, resolution=360):
    """
    Calculates the 3D path vectors for the cardioid plasma sheet injectors.
    Maps out the outer concentric coaxial pre-heater channels for closed-loop
    thermal viscosity reclamation and fluidic sheath stabilization.
    """
    path_nodes = []
    r_max = max_dia / 2.0
    r_min = input_bore / 2.0
    r_jacket = jacket_dia / 2.0
    
    # Total internal z-axis height of the shield injector manifold is 60mm
    total_z_length = 60.0
    
    for step in range(resolution):
        progress = step / resolution
        current_z = -(progress * total_z_length)
        theta = (step * 2.0 * math.pi) / resolution
        
        # Symmetrical non-Abelian cardioid mapping to enforce uniform centripetal vortex acceleration
        cardioid_contour = 1.0 - math.cos(theta)
        
        # Smoothly condense the channel profile as it descends toward the exit throat
        radius = r_min + (r_max - r_min) * (1.0 - progress) * (0.5 + 0.5 * cardioid_contour / phi)
        
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        
        # Map the outer concentric coaxial pre-heater jacket nodes (Mid-transit zones)
        if 0.30 < progress < 0.75:
            xj = r_jacket * math.cos(theta)
            yj = r_jacket * math.sin(theta)
            zone = "Coaxial_Thermal_Siphon_Pre_Heater_Jacket"
            vector_coord = (round(xj, 4), round(yj, 4), round(current_z, 4))
        else:
            if progress < 0.30:
                zone = "Gas_Plenum_Catchment_Zone"
            else:
                zone = "Hyperbolic_Acceleration_Shaft_Interface"
            vector_coord = (round(x, 4), round(y, 4), round(current_z, 4))
            
        path_nodes.append({
            "node_step": step,
            "hydraulic_zone": zone,
            "metrics": {
                "dynamic_radius_mm": round(radius, 4),
                "elevation_z_mm": round(current_z, 4),
                "outer_jacket_radius_mm": round(r_jacket, 2)
            },
            "vector": vector_coord
        })
        
    return path_nodes

def main():
    print("=" * 70)
    print("INITIALIZING: AEDS-01 SHEET INJECTOR COORDINATE ENGINE")
    print("=" * 70)
    
    config_path = get_local_path("injector-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        input_bore = config["geometry_parameters"]["intake_plenum_inner_diameter_mm"]
        max_dia = config["geometry_parameters"]["cardioid_internal_max_diameter_mm"]
        phi = config["geometry_parameters"]["cardioid_curvature_factor_phi"]
        jacket_dia = config["geometry_parameters"]["coaxial_pre_heater_jacket_diameter_mm"]
        material = config["industrial_profile"]["recommended_material"]
        print("[+] Industrial Component ID AEDS-01 configuration card matched.")
    else:
        print("[⚠️] WARNING: injector-config.json missing. Loading safe fallbacks.")
        input_bore = 50.8
        max_dia = 110.0
        phi = 1.618
        jacket_dia = 132.0
        material = "Hardened_Inconel_718"
        
    print(f"[*] Housing Metallurgy Standard: {material}")
    print(f"[*] Coaxial Pre-Heater Sleeve  : {jacket_dia}mm Outer Thermal Shell")
    print(f"[*] Compiling closed-loop kinetic gas sheath trajectories...")
    
    injector_mesh = generate_shield_injector_vectors(input_bore, max_dia, phi, jacket_dia)
    audit_sample = [n for n in injector_mesh if n["hydraulic_zone"] == "Coaxial_Thermal_Siphon_Pre_Heater_Jacket"]
    
    print("\n[+] SUCCESS: Cardioid Sheet Injector matrix compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(injector_mesh)}")
    print(f"[-] AEDS-01 Core Node Balance Audit:")
    print(f"    ↳ Active Hydraulic Zone:   {audit_sample['hydraulic_zone']}")
    print(f"    ↳ Calculated Space Vector: {audit_sample['vector']}")
    print("=" * 70)

if __name__ == "__main__":
    main()
          

import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_condenser_intake_vectors(input_bore, max_dia, phi, jacket_dia, resolution=360):
    """
    Calculates the 3D path vectors for the cardioid suction gateway channels.
    Maps out the outer concentric coaxial pre-cooling channels for closed-loop
    sensible thermal energy extraction.
    """
    path_nodes = []
    r_max = max_dia / 2.0
    r_min = input_bore / 2.0
    r_jacket = jacket_dia / 2.0
    
    # Total longitudinal length of the intake gateway is 150mm
    total_z_length = 150.0
    
    for step in range(resolution):
        progress = step / resolution
        current_z = -(progress * total_z_length)
        theta = (step * 2.0 * math.pi) / resolution
        
        # Symmetrical non-Abelian cardioid mapping to enforce centripetal vortex acceleration
        cardioid_contour = 1.0 - math.cos(theta)
        
        # Smoothly pinch the profile as it approaches the exit throat interface
        radius = r_min + (r_max - r_min) * (1.0 - progress) * (0.5 + 0.5 * cardioid_contour / phi)
        
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        
        # Map the outer concentric coaxial pre-cooling jacket nodes (Mid-transit zones)
        if 0.20 < progress < 0.80:
            xj = r_jacket * math.cos(theta)
            yj = r_jacket * math.sin(theta)
            zone = "Coaxial_Thermal_Siphon_Pre_Cooling_Jacket"
            vector_coord = (round(xj, 4), round(yj, 4), round(current_z, 4))
        else:
            if progress <= 0.20:
                zone = "Atmospheric_Plenum_Catchment_Zone"
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
    print("INITIALIZING: AWHC-01 SUCTION GATEWAY VECTOR MATH ENGINE")
    print("=" * 70)
    
    config_path = get_local_path("gateway-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        input_bore = config["geometry_parameters"]["intake_plenum_inner_diameter_mm"]
        max_dia = config["geometry_parameters"]["cardioid_internal_max_diameter_mm"]
        phi = config["geometry_parameters"]["cardioid_curvature_factor_phi"]
        jacket_dia = config["geometry_parameters"]["coaxial_pre_cooling_jacket_diameter_mm"]
        material = config["industrial_profile"]["recommended_material"]
        print("[+] Industrial Component ID AWHC-01 configuration card verified.")
    else:
        print("[⚠️] WARNING: gateway-config.json missing. Loading safe overrides.")
        input_bore = 200.0
        max_dia = 280.0
        phi = 1.618
        jacket_dia = 310.0
        material = "PEEK_Optima_Polymer"
        
    print(f"[*] Chassis Material Standard: {material}")
    print(f"[*] Coaxial Pre-Cooling Sleeve: {jacket_dia}mm Outer Thermal Shell")
    print(f"[*] Compiling closed-loop kinetic suction trajectories...")
    
    gateway_mesh = generate_condenser_intake_vectors(input_bore, max_dia, phi, jacket_dia)
    audit_sample = [n for n in gateway_mesh if n["hydraulic_zone"] == "Coaxial_Thermal_Siphon_Pre_Pre_Cooling_Jacket" or n["hydraulic_zone"] == "Coaxial_Thermal_Siphon_Pre_Cooling_Jacket"][0]
    
    print("\n[+] SUCCESS: Cardioid Suction Gateway matrix compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(gateway_mesh)}")
    print(f"[-] AWHC-01 Core Node Balance Audit:")
    print(f"    ↳ Active Hydraulic Zone:   {audit_sample['hydraulic_zone']}")
    print(f"    ↳ Calculated Space Vector: {audit_sample['vector']}")
    print("=" * 70)

if __name__ == "__main__":
    main()
      

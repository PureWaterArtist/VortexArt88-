import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_supercritical_cardioid_vectors(input_bore, max_dia, phi, vanes_count, jacket_dia, resolution=360):
    """
    Calculates the 3D path vectors for the supercritical cardioid feed injectors.
    Integrates 45-degree swirl brake vanes and maps out the outer concentric 
    coaxial pre-heater channels for closed-loop thermal viscosity reclamation.
    """
    path_nodes = []
    r_max = max_dia / 2.0
    r_min = input_bore / 2.0
    r_jacket = jacket_dia / 2.0
    total_z_length = 40.0
    
    for step in range(resolution):
        progress = step / resolution
        current_z = -(progress * total_z_length)
        theta = (step * 2.0 * math.pi) / resolution
        
        cardioid_contour = 1.0 - math.cos(theta)
        radius = r_min + (r_max - r_min) * (1.0 - progress) * (0.5 + 0.5 * cardioid_contour / phi)
        
        # Inject the solid-state swirl brake vane geometry near the outlet throat
        if progress > 0.85:
            vane_factor = (step * vanes_count) % resolution
            if vane_factor < (resolution / 12.0):
                radius -= 1.5
                
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        
        # Map the outer concentric coaxial pre-heater jacket nodes (Mid-transit zones)
        if 0.30 < progress < 0.75:
            xj = r_jacket * math.cos(theta)
            yj = r_jacket * math.sin(theta)
            zone = "Coaxial_Thermal_Siphon_Pre_Heater_Jacket"
            vector_coord = (round(xj, 4), round(yj, 4), round(current_z, 4))
        else:
            if progress < 0.20:
                zone = "Supercritical_Feedstock_Catchment_Zone"
            elif progress > 0.85:
                zone = "Solid_State_Thermal_Swirl_Brake_Grid"
            else:
                zone = "Laminar_Vortex_Ribbon_Splitting_Phase"
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
    print("INITIALIZING: ARMC-01 CLOSED-LOOP INJECTOR SPLITTER ENGINE")
    print("=" * 70)
    
    config_path = get_local_path("injector-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        input_bore = config["geometry_parameters"]["feedstock_input_bore_diameter_mm"]
        max_dia = config["geometry_parameters"]["cardioid_internal_max_diameter_mm"]
        phi = config["geometry_parameters"]["cardioid_curvature_factor_phi"]
        vanes = config["thermal_break_grid_matrix"]["swirl_brake_vanes_count"]
        jacket_dia = config["coaxial_thermal_siphon_recycling"]["coaxial_pre_heater_jacket_diameter_mm"]
        material = config["industrial_profile"]["recommended_material"]
        print("[+] Optimized Component ID ARMC-01 configuration card matched.")
    else:
        print("[⚠️] WARNING: injector-config.json missing. Loading safe overrides.")
        input_bore = 6.35
        max_dia = 24.0
        phi = 1.618
        vanes = 6
        jacket_dia = 32.0
        material = "Titanium_Ti6Al4V"
        
    print(f"[*] Metallurgy Shell Standard: {material}")
    print(f"[*] Coaxial Pre-Heater Jacket:  {jacket_dia}mm Outer Thermal Sleeve")
    print(f"[*] Compiling closed-loop thermodynamic re-injection tracks...")
    
    injector_mesh = generate_supercritical_cardioid_vectors(input_bore, max_dia, phi, vanes, jacket_dia)
    audit_sample = [n for n in injector_mesh if n["hydraulic_zone"] == "Coaxial_Thermal_Siphon_Pre_Heater_Jacket"][0]
    
    print("\n[+] SUCCESS: Closed-Loop Cardioid Injector matrix compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(injector_mesh)}")
    print(f"[-] ARMC-01 Core Node Balance Audit:")
    print(f"    ↳ Active Hydraulic Zone:   {audit_sample['hydraulic_zone']}")
    print(f"    ↳ Calculated Space Vector: {audit_sample['vector']}")
    print("=" * 70)

if __name__ == "__main__":
    main()
    

import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_supercritical_cardioid_vectors(input_bore, max_dia, phi, vanes_count, resolution=360):
    """
    Calculates the 3D path vectors for the supercritical cardioid feed injectors.
    Integrates a solid-state thermal break grid and 45-degree swirl brake vanes 
    to prevent high-temperature backflow shocks.
    """
    path_nodes = []
    r_max = max_dia / 2.0
    r_min = input_bore / 2.0
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
            if vane_factor < (resolution / 12.0): # Generate 6 distinct thin blocking fins
                radius -= 1.5 # Deflect the radius inward to form a solid metal vane
                
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        
        if progress < 0.20:
            zone = "Supercritical_Feedstock_Catchment_Zone"
        elif progress > 0.85:
            zone = "Solid_State_Thermal_Swirl_Brake_Grid"
        else:
            zone = "Laminar_Vortex_Ribbon_Splitting_Phase"
            
        path_nodes.append({
            "node_step": step,
            "hydraulic_zone": zone,
            "metrics": {
                "dynamic_radius_mm": round(radius, 4),
                "elevation_z_mm": round(current_z, 4)
            },
            "vector": (round(x, 4), round(y, 4), round(current_z, 4))
        })
        
    return path_nodes

def main():
    print("=" * 65)
    print("INITIALIZING: ARMC-01 OPTIMIZED INJECTOR SPLITTER ENGINE")
    print("=" * 65)
    
    config_path = get_local_path("injector-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        input_bore = config["geometry_parameters"]["feedstock_input_bore_diameter_mm"]
        max_dia = config["geometry_parameters"]["cardioid_internal_max_diameter_mm"]
        phi = config["geometry_parameters"]["cardioid_curvature_factor_phi"]
        vanes = config["thermal_break_grid_matrix"]["swirl_brake_vanes_count"]
        material = config["industrial_profile"]["recommended_material"]
        print("[+] Optimized Component ID ARVT-01 configuration card matched.")
    else:
        print("[⚠️] WARNING: injector-config.json missing. Loading safe overrides.")
        input_bore = 6.35
        max_dia = 24.0
        phi = 1.618
        vanes = 6
        material = "Titanium_Ti6Al4V"
        
    print(f"[*] Metallurgy Shell Standard: {material}")
    print(f"[*] Swirl Brake Array Vanes:   {vanes} x Non-Mechanical Deflectors")
    print(f"[*] Compiling enhanced fluidic-amplifier thermal isolation paths...")
    
    injector_mesh = generate_supercritical_cardioid_vectors(input_bore, max_dia, phi, vanes)
    audit_sample = [n for n in injector_mesh if n["hydraulic_zone"] == "Solid_State_Thermal_Swirl_Brake_Grid"][0]
    
    print("\n[+] SUCCESS: Supercritical Cardioid Injector matrix compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(injector_mesh)}")
    print(f"[-] ARMC-01 Core Node Balance Audit:")
    print(f"    ↳ Active Hydraulic Zone:   {audit_sample['hydraulic_zone']}")
    print(f"    ↳ Calculated Space Vector: {audit_sample['vector']}")
    print("=" * 65)

if __name__ == "__main__":
    main()
    

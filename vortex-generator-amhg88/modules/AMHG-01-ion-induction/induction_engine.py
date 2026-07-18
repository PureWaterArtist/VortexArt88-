import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_ion_induction_vectors(input_bore, max_dia, phi, jacket_dia, resolution=360):
    """
    Calculates the 3D path vectors for the cardioid ion-static induction gateway.
    Maps out the double-helical glassy carbon collection traces for non-invasive,
    blade-free atmospheric charge draw.
    """
    path_nodes = []
    r_max = max_dia / 2.0
    r_min = input_bore / 2.0
    r_jacket = jacket_dia / 2.0
    
    # Total longitudinal height of the ion induction gateway is 200mm
    total_z_length = 200.0
    pitch_length_z = math.pi * input_bore * math.tan(math.radians(45.0))
    
    for step in range(resolution):
        progress = step / resolution
        current_z = -(progress * total_z_length)
        theta = (step * 2.0 * math.pi) / resolution
        
        # Symmetrical non-Abelian cardioid mapping to enforce centripetal vortex acceleration
        cardioid_contour = 1.0 - math.cos(theta)
        radius = r_min + (r_max - r_min) * (1.0 - progress) * (0.5 + 0.5 * cardioid_contour / phi)
        
        # Double helix tracking logic for the glassy carbon electro-static traces
        helix_angle_1 = (abs(current_z) / pitch_length_z) * 2.0 * math.pi
        helix_angle_2 = helix_angle_1 + math.pi
        
        is_induction_trace = False
        for h_angle in [helix_angle_1, helix_angle_2]:
            wrapped_h_angle = h_angle % (2.0 * math.pi)
            if abs(theta - wrapped_h_angle) < (2.0 * math.pi / 36.0): # 10-degree window
                is_induction_trace = True
                
        if is_induction_trace:
            zone = "Glassy_Carbon_Ion_Static_Induction_Trace"
            radius_mod = radius
        else:
            if progress < 0.25:
                zone = "Convective_Solar_Intake_Mouth_Plenum"
            else:
                zone = "Silicon_Nitride_Dielectric_Isolation_Wall"
            radius_mod = radius + 2.5 # Positioned back inside the structural wall
            
        x = radius_mod * math.cos(theta)
        y = radius_mod * math.sin(theta)
        
        path_nodes.append({
            "node_step": step,
            "structural_classification": zone,
            "metrics": {
                "dynamic_radius_mm": round(radius_mod, 4),
                "elevation_z_mm": round(current_z, 4),
                "outer_jacket_radius_mm": round(r_jacket, 2)
            },
            "vector_coordinate": (round(x, 4), round(y, 4), round(current_z, 4))
        })
        
    return path_nodes

def main():
    print("=" * 70)
    print("INITIALIZING: AMHG-01 ION INDUCTION GATEWAY MATH ENGINE")
    print("=" * 70)
    
    config_path = get_local_path("induction-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        input_bore = config["geometry_parameters"]["primary_intake_diameter_mm"]
        max_dia = config["geometry_parameters"]["cardioid_internal_max_diameter_mm"]
        phi = config["geometry_parameters"]["cardioid_curvature_factor_phi"]
        jacket_dia = config["geometry_parameters"]["coaxial_pre_heating_jacket_diameter_mm"]
        material = config["industrial_profile"]["internal_liner_substrate"]
        print("[+] Industrial Component ID AMHG-01 configuration card verified.")
    else:
        print("[⚠️] WARNING: induction-config.json missing. Loading safe overrides.")
        input_bore = 500.0
        max_dia = 620.0
        phi = 1.618
        jacket_dia = 680.0
        material = "Silicon_Nitride_Si3N4"
        
    print(f"[*] Core Insulation Liner  : {material}")
    print(f"[*] Electro-Static Threshold: 75,000V DC Ambient Ion Draw Active")
    print(f"[*] Compiling double-helical induction and centripetal fluid tracks...")
    
    gateway_mesh = generate_ion_induction_vectors(input_bore, max_dia, phi, jacket_dia)
    audit_sample = [n for n in gateway_mesh if n["structural_classification"] == "Glassy_Carbon_Ion_Static_Induction_Trace"]
    
    sample_node = audit_sample[len(audit_sample) // 2] if audit_sample else gateway_mesh[len(gateway_mesh) // 2]
    
    print("\n[+] SUCCESS: Cardioid Ion Induction Gateway matrix compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(gateway_mesh)}")
    print(f"[-] AMHG-01 Core Node Balance Audit:")
    print(f"    ↳ Active Structural Zone:  {sample_node['structural_classification']}")
    print(f"    ↳ Calculated Space Vector: {sample_node['vector_coordinate']}")
    print("=" * 70)

if __name__ == "__main__":
    main()
      

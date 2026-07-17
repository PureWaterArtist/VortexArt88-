import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_savonius_blade_vectors(stages, max_dia, twist_deg, resolution=180):
    """
    Calculates 3D spatial vectors for the suspended twisted Savonius turbine array.
    Maps out the precise aerodynamic helix geometry that captures the air core downdraft.
    """
    blade_nodes = []
    radius = max_dia / 2.0
    twist_rad = math.radians(twist_deg)
    
    # Each stage spans 100mm vertically down the central core
    stage_height_mm = 100.0
    
    for stage_idx in range(stages):
        z_start = -(stage_idx * stage_height_mm)
        
        for step in range(resolution):
            progress = step / resolution
            current_z = z_start - (progress * stage_height_mm)
            
            # Base rotational sweep angle (0 to Pi for a half-cylinder bucket)
            theta_base = progress * math.pi
            
            # Inject the helical twist offset based on vertical progression
            theta_twisted = theta_base + (progress * twist_rad)
            
            # Savonius S-shape scoop profile math
            # Two opposing semicircles offset from the center axis
            if step < (resolution / 2):
                # First bucket scoop loop
                x = (radius / 2.0) * (1.0 + math.cos(theta_twisted))
                y = (radius / 2.0) * math.sin(theta_twisted)
                node_type = f"Savonius_Scoop_Alpha_Stage_{stage_idx + 1}"
            else:
                # Second bucket scoop loop (Mirrored)
                x = -(radius / 2.0) * (1.0 + math.cos(theta_twisted))
                y = -(radius / 2.0) * math.sin(theta_twisted)
                node_type = f"Savonius_Scoop_Beta_Stage_{stage_idx + 1}"
                
            blade_nodes.append({
                "stage": stage_idx,
                "node_classification": node_type,
                "telemetry": {
                    "axial_pos_z_mm": round(current_z, 4),
                    "dynamic_theta_rad": round(theta_twisted, 4)
                },
                "vector": (round(x, 4), round(y, 4), round(current_z, 4))
            })
            
    return blade_nodes

def main():
    print("=" * 65)
    print("INITIALIZING: ARVT-11 AIR-CORE KINETIC TURBINE ENGINE")
    print("=" * 65)
    
    config_path = get_local_path("turbine-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        stages = config["turbine_geometry"]["impeller_stages_count"]
        max_dia = config["turbine_geometry"]["impeller_outer_diameter_mm"]
        twist_deg = config["turbine_geometry"]["blade_helical_twist_deg"]
        material = config["manufacturing_profile"]["recommended_material"]
        print("[+] Component ID ARVT-11 configuration card matched cleanly.")
    else:
        print("[⚠️] WARNING: turbine-config.json missing. Loading safe overrides.")
        stages = 3
        max_dia = 12.5
        twist_deg = 30.0
        material = "Carbon_Fiber_PLA"
        
    print(f"[*] Manufacturing Standard: {material} Ultra-Light Build")
    print(f"[*] Core Turbine Mapping:   {stages} Stages | {max_dia}mm Active Sweep Radius")
    print(f"[*] Calculating twisted aerodynamic helix space vectors...")
    
    turbine_mesh = generate_savonius_blade_vectors(stages, max_dia, twist_deg)
    
    # Audit a midpoint node tracking the structural scoop shape
    audit_sample = turbine_mesh[len(turbine_mesh) // 2]
    
    print("\n[+] SUCCESS: Air-Core Kinetic Turbine matrix compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(turbine_mesh)}")
    print(f"[-] ARVT-11 Optimized Node Balance Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['node_classification']}")
    print(f"    ↳ Cartesian Mesh Node:      {audit_sample['vector']}")
    print("=" * 65)

if __name__ == "__main__":
    main()
          

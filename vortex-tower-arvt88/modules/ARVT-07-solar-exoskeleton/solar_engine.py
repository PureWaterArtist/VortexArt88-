import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_solar_exoskeleton_mesh(height, clamp_dia, panels_count=4, resolution=360):
    """
    Calculates the 3D coordinate vectors for the clip-on solar exoskeleton.
    Maps out the outer facets required to mount flexible monocrystalline strips
    symmetrically around the main acceleration column casing.
    """
    chassis_nodes = []
    outer_radius = (clamp_dia / 2.0) + 5.0 # Account for material thickness
    
    # Process slices vertically down one 1-meter exoskeleton section
    slices_count = 10
    for slice_idx in range(slices_count):
        z_pos = -(slice_idx * (height / slices_count))
        
        for step in range(resolution):
            theta = (step * 2.0 * math.pi) / resolution
            
            # Divide the 360-degree perimeter into flat mounting facets (Panels)
            facet_angle = (2.0 * math.pi) / panels_count
            current_facet = int(theta / facet_angle)
            
            # Create structural snap-fit hinge regions at 0 and 180 degrees
            if abs(theta - 0.0) < 0.1 or abs(theta - math.pi) < 0.1:
                node_type = "Exoskeleton_Structural_Hinge_Snap"
                dynamic_radius = outer_radius + 4.0
            else:
                node_type = f"Photovoltaic_Facet_Mount_Zone_{current_facet + 1}"
                dynamic_radius = outer_radius
                
            x = dynamic_radius * math.cos(theta)
            y = dynamic_radius * math.sin(theta)
            
            chassis_nodes.append({
                "vertical_slice": slice_idx,
                "node_classification": node_type,
                "telemetry": {
                    "elevation_z_mm": round(z_pos, 4),
                    "radial_extension_mm": round(dynamic_radius, 2)
                },
                "vector": (round(x, 4), round(y, 4), round(z_pos, 4))
            })
            
    return chassis_nodes

def main():
    print("=" * 65)
    print("INITIALIZING: ARVT-07 SOLAR EXOSKELETON CHASSIS ENGINE")
    print("=" * 65)
    
    config_path = get_local_path("solar-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        height = config["structural_parameters"]["exoskeleton_height_mm"]
        clamp_dia = config["structural_parameters"]["internal_grip_diameter_mm"]
        p_type = config["photovoltaic_interface"]["panel_type"]
        wattage = config["photovoltaic_interface"]["peak_wattage_rating"]
        print("[+] Component ID ARVT-07 solar configuration card matched.")
    else:
        print("[⚠️] WARNING: solar-config.json missing. Loading safe overrides.")
        height = 1000.0
        clamp_dia = 80.0
        p_type = "Flexible_Monocrystalline"
        wattage = 150.0
        
    print(f"[*] Sourced Array Spec:    {wattage}W {p_type}")
    print(f"[*] Chassis Target Height: {height}mm Sleeve Length")
    print(f"[*] Compiling multi-facet structural armor vectors...")
    
    solar_mesh = generate_solar_exoskeleton_mesh(height, clamp_dia)
    
    # Audit a node point right on the primary sun-facing facet mount zone
    audit_sample = [n for n in solar_mesh if "Photovoltaic_Facet_Mount_Zone" in n["node_classification"]][0]
    
    print("\n[+] SUCCESS: Solar Exoskeleton chassis matrix compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(solar_mesh)}")
    print(f"[-] ARVT-07 Optimized Node Balance Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['node_classification']}")
    print(f"    ↳ Geometric Vector Node:    {audit_sample['vector']}")
    print("=" * 65)

if __name__ == "__main__":
    main()
          

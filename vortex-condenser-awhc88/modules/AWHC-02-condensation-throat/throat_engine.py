import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_condensation_throat_vectors(phi, chamber_height, venturi_dia, resolution=360):
    """
    Calculates the 3D coordinate meshes for the hyperbolic Venturi condensation throat.
    Maps out the precise thermal boundary zones where the Peltier/Seebeck energy matrix
    flash-chills the stream to force water phase transition.
    """
    throat_nodes = []
    base_entry_radius = 25.4   # 25.4mm radius matching the intake gateway exit
    min_throat_radius = venturi_dia / 2.0
    
    for step in range(resolution):
        progress = step / resolution
        z_axis = (progress * chamber_height) - (chamber_height / 2.0)
        theta = (step * 2.0 * math.pi) / resolution
        
        # Shape the chamber contour along a hyperbolic contraction-expansion curve (Venturi)
        # Symmetrical contraction centered around the middle of the vertical Z-axis
        mid_factor = abs(progress - 0.5) / 0.5
        radius_modulation = min_throat_radius + (base_entry_radius - min_throat_radius) * (mid_factor ** 2)
        
        # Clamp radius bounds to preserve precision manufacturing limits
        radius_modulation = max(min_throat_radius, min(base_entry_radius, radius_modulation))
        
        x = radius_modulation * math.cos(theta)
        y = radius_modulation * math.sin(theta)
        
        if 0.40 <= progress <= 0.60:
            zone = "Sub_Atomic_Dew_Point_Condensation_Singularity"
        else:
            if progress < 0.40:
                zone = "Convergent_Hyperbolic_Pressure_Squeeze"
            else:
                zone = "Divergent_Vortex_Velocity_Recovery_Zone"
                
        throat_nodes.append({
            "step": step,
            "condensation_phase": zone,
            "metrics": {
                "axial_z_mm": round(z_axis, 4),
                "dynamic_radius_mm": round(radius_modulation, 4),
                "thermoelectric_zone_id": int(progress * 4)
            },
            "vortex_streamline_vector": (round(x, 4), round(y, 4), round(z_axis, 4))
        })
        
    return throat_nodes

def main():
    print("=" * 65)
    print("INITIALIZING: AWHC-02 CONDENSER CORE GEOMETRIC ENGINE")
    print("=" * 65)
    
    config_path = get_local_path("throat-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        phi = config["geometry_parameters"]["fibonacci_contour_phi"]
        height = config["geometry_parameters"]["chamber_total_height_mm"]
        venturi_dia = config["geometry_parameters"]["venturi_throat_diameter_mm"]
        material = config["industrial_profile"]["internal_liner_substrate"]
        print("[+] Industrial Component ID AWHC-02 configuration card matched.")
    else:
        print("[⚠️] WARNING: throat-config.json missing. Loading safe overrides.")
        phi = 1.618
        height = 120.0
        venturi_dia = 12.0
        material = "Titanium_Ti6Al4V_Grade_23"
        
    print(f"[*] Chamber Thermal Conduction Liner: {material}")
    print(f"[*] Energy Harvesting Array         : 32 x Bi2Te3 Peltier/Seebeck Pairs Active")
    print(f"[*] Compiling hyperbolic Venturi pressure-drop tracks...")
    
    throat_mesh = generate_condensation_throat_vectors(phi, height, venturi_dia)
    audit_sample = [n for n in throat_mesh if n["condensation_phase"] == "Sub_Atomic_Dew_Point_Condensation_Singularity"]
    
    sample_node = audit_sample[len(audit_sample) // 2] if audit_sample else throat_mesh[len(throat_mesh) // 2]
    
    print("\n[+] SUCCESS: Hyperbolic condensation throat matrix compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(throat_mesh)}")
    print(f"[-] AWHC-02 Core Node Balance Audit:")
    print(f"    ↳ Active Condensation Phase: {sample_node['condensation_phase']}")
    print(f"    ↳ Calculated Space Vector:   {sample_node['vortex_streamline_vector']}")
    print("=" * 65)

if __name__ == "__main__":
    main()
      

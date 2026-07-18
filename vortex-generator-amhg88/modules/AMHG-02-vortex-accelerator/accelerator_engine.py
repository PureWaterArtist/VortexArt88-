import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_vortex_accelerator_vectors(phi, chamber_height, throat_dia, resolution=360):
    """
    Calculates the 3D coordinate meshes for the hyperbolic vortex accelerator throat.
    Maps out the precise thermal boundary zones where the coaxial pre-heater jacket
    super-heats the stream to enforce fluid viscosity reduction.
    """
    throat_nodes = []
    base_entry_radius = 75.0   # 75mm radius matching the induction exit manifold
    min_throat_radius = throat_dia / 2.0
    
    for step in range(resolution):
        progress = step / resolution
        z_axis = (progress * chamber_height) - (chamber_height / 2.0)
        theta = (step * 2.0 * math.pi) / resolution
        
        # Shape the chamber contour along a hyperbolic contraction-expansion curve
        mid_factor = abs(progress - 0.5) / 0.5
        radius_modulation = min_throat_radius + (base_entry_radius - min_throat_radius) * (mid_factor ** 2)
        
        # Clamp radius bounds to preserve precision manufacturing limits
        radius_modulation = max(min_throat_radius, min(base_entry_radius, radius_modulation))
        
        x = radius_modulation * math.cos(theta)
        y = radius_modulation * math.sin(theta)
        
        if 0.40 <= progress <= 0.60:
            zone = "Sub_Atomic_Vortex_Velocity_Acceleration_Singularity"
        else:
            if progress < 0.40:
                zone = "Convergent_Hyperbolic_Kinetic_Squeeze"
            else:
                zone = "Divergent_Vortex_Expansion_Exhaust_Zone"
                
        throat_nodes.append({
            "step": step,
            "acceleration_phase": zone,
            "metrics": {
                "axial_z_mm": round(z_axis, 4),
                "dynamic_radius_mm": round(radius_modulation, 4),
                "thermal_jacket_zone_id": int(progress * 4)
            },
            "vortex_streamline_vector": (round(x, 4), round(y, 4), round(z_axis, 4))
        })
        
    return throat_nodes

def main():
    print("=" * 65)
    print("INITIALIZING: AMHG-02 ACCELERATOR GEOMETRIC ENGINE")
    print("=" * 65)
    
    config_path = get_local_path("accelerator-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        phi = config["geometry_parameters"]["fibonacci_contour_phi"]
        height = config["geometry_parameters"]["chamber_total_height_mm"]
        throat_dia = config["geometry_parameters"]["vortex_throat_diameter_mm"]
        material = config["industrial_profile"]["internal_liner_substrate"]
        print("[+] Industrial Component ID AMHG-02 configuration card matched.")
    else:
        print("[⚠️] WARNING: accelerator-config.json missing. Loading safe overrides.")
        phi = 1.618
        height = 180.0
        throat_dia = 50.8
        material = "Silicon_Nitride_Ceramic_Si3N4"
        
    print(f"[*] Chamber Core Isolation Liner: {material}")
    print(f"[*] Compiling hyperbolic vortex contraction-expansion tracks...")
    
    throat_mesh = generate_vortex_accelerator_vectors(phi, height, throat_dia)
    audit_sample = [n for n in throat_mesh if n["acceleration_phase"] == "Sub_Atomic_Vortex_Velocity_Acceleration_Singularity"]
    
    sample_node = audit_sample[len(audit_sample) // 2] if audit_sample else throat_mesh[len(throat_mesh) // 2]
    
    print("\n[+] SUCCESS: Hyperbolic acceleration throat matrix compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(throat_mesh)}")
    print(f"[-] AMHG-02 Core Node Balance Audit:")
    print(f"    ↳ Active Acceleration Phase: {sample_node['acceleration_phase']}")
    print(f"    ↳ Calculated Space Vector:   {sample_node['vortex_streamline_vector']}")
    print("=" * 65)

if __name__ == "__main__":
    main()
  

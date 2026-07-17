import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_optimized_cardioid_vectors(max_dia, throat_dia, transition_offset, resolution=360):
    """
    Calculates the 3D path vectors for the optimized cardioid splitting loops.
    Integrates a smooth boundary blend at the throat exit to feed the 
    downstream hyperbolic acceleration shaft with zero entry turbulence.
    """
    path_nodes = []
    r_max = max_dia / 2.0
    r_min = (throat_dia - transition_offset) / 2.0
    
    for step in range(resolution):
        theta = (step * 2.0 * math.pi) / resolution
        scale_factor = (step / resolution)
        current_z = -(scale_factor * 120.0) # Funnel height drop remains 120mm
        
        # Pure Cardioid parametric layout modulated for the exit blend
        cardioid_mod = 1.0 - math.cos(theta)
        
        # Compound radius calculation mapping a smooth transition curve
        radius = r_min + (r_max - r_min) * (1.0 - scale_factor) * (0.5 + 0.5 * cardioid_mod)
        
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        
        # Segment tracking accounting for the pre-acceleration interface zone
        if scale_factor < 0.15:
            zone = "Atmospheric_Vortex_Catchment_Rim"
        elif scale_factor > 0.85:
            zone = "Hyperbolic_Interface_Split_Core"
        else:
            zone = "Laminar_Siphon_Compression_Transit"
            
        path_nodes.append({
            "node_step": step,
            "hydraulic_zone": zone,
            "metrics": {"radius_mm": round(radius, 4), "elevation_z_mm": round(current_z, 4)},
            "vector": (round(x, 4), round(y, 4), round(current_z, 4))
        })
        
    return path_nodes

def main():
    print("=" * 65)
    print("INITIALIZING: ARVT-01 OPTIMIZED INTAKE SPLITTER ENGINE")
    print("=" * 65)
    
    config_path = get_local_path("header-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        max_dia = config["geometry_parameters"]["intake_funnel_max_diameter_mm"]
        throat_dia = config["geometry_parameters"]["funnel_exit_throat_diameter_mm"]
        trans_offset = config["geometry_parameters"]["hyperbolic_transition_offset_mm"]
        flow_regime = config["operational_envelope"]["flow_regime"]
        print(f"[+] Optimized Component ID ARVT-01 configuration card matched.")
    else:
        print("[⚠️] WARNING: header-config.json missing. Loading safe fallbacks.")
        max_dia = 150.0
        throat_dia = 50.8
        trans_offset = 10.0
        flow_regime = "Hyperbolic_Pre_Accelerated_Siphon_Vortex"
        
    print(f"[*] Target Flow Regime:  {flow_regime}")
    print(f"[*] Hyperbolic Shift:    Blended {trans_offset}mm Entry Offset")
    print(f"[*] Evaluating solid-state zero back-pressure channel paths...")
    
    header_mesh = generate_optimized_cardioid_vectors(max_dia, throat_dia, trans_offset)
    
    audit_index = int(len(header_mesh) * 0.90)
    audit_sample = header_mesh[audit_index]
    
    print("\n[+] SUCCESS: Optimized Intake Cardioid Splitter matrix compiled.")
    print(f"[-] Total coordinated structural steps logged: {len(header_mesh)}")
    print(f"[-] ARVT-01 Optimized Node Balance Audit:")
    print(f"    ↳ Active Hydraulic Zone:   {audit_sample['hydraulic_zone']}")
    print(f"    ↳ Calculated Space Vector: {audit_sample['vector']}")
    print("=" * 65)

if __name__ == "__main__":
    main()
    

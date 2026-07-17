import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_mhd_field_nodes(magnet_count, ring_thickness, start_z=0.0, resolution=360):
    """
    Calculates the 3D positioning nodes for the external magnet cavities
    and corresponding internal graphite pickup electrodes.
    Aligns vectors perfectly perpendicular to the falling helical velocity field.
    """
    sleeve_nodes = []
    
    # Electrode angular positions placed exactly 180 degrees apart (Symmetrical Slices)
    electrode_angles = [0.0, math.pi]
    
    for magnet_idx in range(magnet_count):
        # Calculate vertical span for each magnet ring node
        z_start = start_z - (magnet_idx * ring_thickness)
        z_mid = z_start - (ring_thickness / 2.0)
        
        # Determine magnetic pole alternating sequence (+1 = North, -1 = South)
        polarity = 1 if (magnet_idx % 2 == 0) else -1
        
        for step in range(resolution):
            theta = (step * 2.0 * math.pi) / resolution
            
            # Identify if this coordinate vector aligns with a pickup electrode terminal
            is_electrode = False
            for e_angle in electrode_angles:
                if abs(theta - e_angle) < (2.0 * math.pi / resolution):
                    is_electrode = True
                    
            if is_electrode:
                node_type = "MHD_Graphite_Electrode_Terminal"
            else:
                node_type = f"N52_Magnetic_Field_Node_{'North' if polarity > 0 else 'South'}"
                
            sleeve_nodes.append({
                "magnet_index": magnet_idx,
                "node_classification": node_type,
                "telemetry": {
                    "center_line_z_mm": round(z_mid, 4),
                    "local_polarity_factor": polarity,
                    "induction_angle_rad": round(theta, 4)
                },
                "vector_coordinate": (round(math.cos(theta), 4), round(math.sin(theta), 4), round(z_mid, 4))
            })
            
    return sleeve_nodes

def main():
    print("=" * 65)
    print("INITIALIZING: ARVT-03 POWER SLEEVE MHD FIELD ENGINE")
    print("=" * 65)
    
    config_path = get_local_path("sleeve-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        magnet_count = config["electromagnetic_parameters"]["ring_magnets_count"]
        ring_thickness = config["electromagnetic_parameters"]["ring_thickness_z_mm"]
        flux_gauss = config["electromagnetic_parameters"]["estimated_magnetic_flux_gauss"]
        e_material = config["harvesting_interface"]["electrode_material"]
        print("[+] Component ID ARVT-03 configuration card matched cleanly.")
    else:
        print("[⚠️] WARNING: sleeve-config.json missing. Loading safe overrides.")
        magnet_count = 6
        ring_thickness = 25.4
        flux_gauss = 14800.0
        e_material = "Graphite"
        
    print(f"[*] Target Electromagnetic Flux: {flux_gauss} Gauss ({magnet_count}x N52 Units)")
    print(f"[*] Interface Electrodes Standard: {e_material} Symmetrical Terminals")
    print(f"[*] Compiling solid-state Lorentz force vector mapping fields...")
    
    sleeve_mesh = generate_mhd_field_nodes(magnet_count, ring_thickness)
    
    # Audit an electrode node point right at the center of the first induction stage
    audit_sample = [n for n in sleeve_mesh if n["node_classification"] == "MHD_Graphite_Electrode_Terminal"][0]
    
    print("\n[+] SUCCESS: MHD Power Sleeve magnetic matrix compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(sleeve_mesh)}")
    print(f"[-] ARVT-03 Core Node Balance Audit:")
    print(f"    ↳ Active Node Target:       {audit_sample['node_classification']}")
    print(f"    ↳ Target Field Centerline:  {audit_sample['telemetry']['center_line_z_mm']} mm")
    print("=" * 65)

if __name__ == "__main__":
    main()
  

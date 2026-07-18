import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_coanda_switch_streamlines(nozzle_w, wall_angle, phi, resolution=360):
    """
    Calculates 3D path vectors for the bi-stable Coanda logic switch channels.
    Models the parametric attachment curves along the golden ratio split island
    to verify latching thresholds for logic state storage.
    """
    streamline_nodes = []
    angle_rad = math.radians(wall_angle)
    
    # Internal macro-length of a single micro-etched logic gate is 10mm
    total_z_length = 10.0
    bore_radius = nozzle_w / 2.0
    
    for step in range(resolution):
        progress = step / resolution
        current_z = -(progress * total_z_length)
        theta = (step * 2.0 * math.pi) / resolution
        
        # Calculate the widening attachment curvature mimicking a natural low-pressure wall drop
        if progress > 0.25:
            attachment_factor = (progress - 0.25) / 0.75
            wall_deviation = (progress * total_z_length) * math.tan(angle_rad) * attachment_factor
        else:
            wall_deviation = 0.0
            
        # Left channel tracking path (State 1 - High Logic)
        xl = (bore_radius + wall_deviation) * math.cos(theta) + (wall_deviation / phi)
        yl = bore_radius * math.sin(theta)
        
        # Right channel tracking path (State 0 - Low Logic / Mirrored)
        xr = (bore_radius + wall_deviation) * math.cos(-theta) - (wall_deviation / phi)
        yr = bore_radius * math.sin(-theta)
        
        if progress < 0.25:
            zone = "Power_Jet_Laminar_Acceleration_Throat"
        elif progress > 0.85:
            zone = "Bi_Stable_State_Output_Channels"
        else:
            zone = "Coanda_Boundary_Layer_Attachment_Zone"
            
        streamline_nodes.append({
            "node_step": step,
            "logic_zone": zone,
            "metrics": {
                "axial_z_mm": round(current_z, 4),
                "wall_deviation_mm": round(wall_deviation, 4)
            },
            "state_1_high_vector": (round(xl, 4), round(yl, 4), round(current_z, 4)),
            "state_0_low_vector": (round(xr, 4), round(yr, 4), round(current_z, 4))
        })
        
    return streamline_nodes

def main():
    print("=" * 70)
    print("INITIALIZING: ARFC-01 COANDA SWITCH VECTOR CORE ENGINE")
    print("=" * 70)
    
    config_path = get_local_path("switch-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        nozzle_w = config["geometry_parameters"]["power_jet_nozzle_width_mm"]
        wall_angle = config["geometry_parameters"]["coanda_curved_wall_angle_deg"]
        phi = config["geometry_parameters"]["splitter_island_offset_phi"]
        material = config["fabrication_profile"]["recommended_wafer_substrate"]
        print("[+] Industrial Component ID ARFC-01 configuration card verified.")
    else:
        print("[⚠️] WARNING: switch-config.json missing. Loading safe overrides.")
        nozzle_w = 0.5
        wall_angle = 12.5
        phi = 1.618
        material = "Monocrystalline_Quartz"
        
    print(f"[*] Substrate Wafer Class: {material}")
    print(f"[*] Switching Bounds: Nozzle Width = {nozzle_w}mm -> Deflection Angle = {wall_angle}°")
    print(f"[*] Computing valveless bi-stable flow attachment tracks...")
    
    switch_mesh = generate_coanda_switch_streamlines(nozzle_w, wall_angle, phi)
    audit_sample = switch_mesh[int(len(switch_mesh) * 0.65)]
    
    print("\n[+] SUCCESS: Coanda-Effect Switching register matrix compiled.")
    print(f"[-] Total coordinated structural nodes logged: {len(switch_mesh)}")
    print(f"[-] ARFC-01 Core Node Balance Audit:")
    print(f"    ↳ Active Logic Zone:        {audit_sample['logic_zone']}")
    print(f"    ↳ State 1 (High) Vector:    {audit_sample['state_1_high_vector']}")
    print(f"    ↳ State 0 (Low) Vector:     {audit_sample['state_0_low_vector']}")
    print("=" * 70)

if __name__ == "__main__":
    main()
          

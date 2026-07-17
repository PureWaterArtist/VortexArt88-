import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_tesla_diode_vectors(stages, channel_width, loop_angle, resolution=360):
    """
    Calculates the 3D internal wall coordinates for the Tesla fluidic diode gate.
    Maps out the forward pass lanes and the interlocking reverse loops that 
    geometrically lock fluid backflow during a water hammer spike.
    """
    plenum_nodes = []
    angle_rad = math.radians(loop_angle)
    stage_length = channel_width * 3.5
    
    for stage_idx in range(stages):
        z_base = -(stage_idx * stage_length)
        
        for step in range(int(resolution / stages)):
            progress = step / (resolution / stages)
            current_z = z_base - (progress * stage_length)
            theta = (step * 2.0 * math.pi) / (resolution / stages)
            
            xf_left = -(channel_width / 2.0)
            xf_right = (channel_width / 2.0)
            
            loop_radius = channel_width * 1.2
            xl = loop_radius * math.sin(theta) + (channel_width * 0.7)
            yl = loop_radius * (1.0 - math.cos(theta)) * math.tan(angle_rad)
            
            if progress > 0.40 and progress < 0.80:
                phase = "Tesla_Diode_Reverse_Flow_Blocking_Pocket"
                vector_coord = (round(xl, 4), round(yl, 4), round(current_z, 4))
            else:
                phase = "Tesla_Diode_Forward_Laminar_Pass"
                vector_coord = (round(xf_left if step % 2 == 0 else xf_right, 4), 0.0, round(current_z, 4))
                
            plenum_nodes.append({
                "stage": stage_idx,
                "structural_phase": phase,
                "telemetry": {
                    "local_z_mm": round(current_z, 4),
                    "channel_clearance_mm": round(channel_width, 2)
                },
                "vector": vector_coord
            })
            
    return plenum_nodes

def main():
    print("=" * 65)
    print("INITIALIZING: ARVT-05 FEEDBACK PLENUM VALVE ENGINE")
    print("=" * 65)
    
    config_path = get_local_path("plenum-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        stages = config["feedback_geometry"]["tesla_diode_stages_count"]
        width = config["feedback_geometry"]["tesla_valve_internal_width_mm"]
        angle = config["feedback_geometry"]["tesla_loop_return_angle_deg"]
        material = config["manufacturing_profile"]["recommended_material"]
        print("[+] Component ID ARVT-05 configuration card matched cleanly.")
    else:
        print("[⚠️] WARNING: plenum-config.json missing. Loading safe overrides.")
        stages = 4
        width = 12.7
        angle = 34.0
        material = "CF-PC"
        
    print(f"[*] Manufacturing Standard: {material} Solid Infill")
    print(f"[*] Compiling {stages}-Stage Valvular Conduit loops at {angle}° returns...")
    
    plenum_mesh = generate_tesla_diode_vectors(stages, width, angle)
    audit_sample = [n for n in plenum_mesh if n["structural_phase"] == "Tesla_Diode_Reverse_Flow_Blocking_Pocket"]
    
    print("\n[+] SUCCESS: Feedback Plenum hydromechanical matrix compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(plenum_mesh)}")
    print(f"[-] ARVT-05 Core Node Balance Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['structural_phase']}")
    print(f"    ↳ Geometric Vector Node:    {audit_sample['vector']}")
    print("=" * 65)

if __name__ == "__main__":
    main()
    

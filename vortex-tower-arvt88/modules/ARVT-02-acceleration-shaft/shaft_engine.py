import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_micro_tesla_liner_mesh(segment_len, internal_dia, step_height, relief_angle, resolution=360):
    """
    Calculates 3D spatial vectors for the internal wall structure of the shaft.
    Engraves a repeating micro-Tesla step pattern to induce hydrodynamic boundary rollers.
    """
    matrix_points = []
    base_radius = internal_dia / 2.0
    angle_rad = math.radians(relief_angle)
    
    # Calculate step pitch based on the 15-degree relief angle and step height
    step_pitch_z = step_height / math.tan(angle_rad)
    
    # Process slices vertically down the length of the shaft segment
    vertical_slices = int(segment_len / 2.0) # 2mm vertical step slices
    
    for slice_idx in range(vertical_slices):
        z_pos = -(slice_idx * (segment_len / vertical_slices))
        
        # Determine the current localized position inside the repeating Tesla step profile
        z_offset_in_pitch = abs(z_pos) % step_pitch_z
        
        # Linear ramp profile creating the sharp downward-angled sawtooth relief
        dynamic_radius = base_radius + (step_height * (z_offset_in_pitch / step_pitch_z))
        
        for step in range(resolution):
            theta = (step * 2.0 * math.pi) / resolution
            
            x = dynamic_radius * math.cos(theta)
            y = dynamic_radius * math.sin(theta)
            
            # Identify active phase based on position relative to the step drop-off tip
            if z_offset_in_pitch > (step_pitch_z * 0.95):
                phase = "Tesla_Step_Vortex_Detachment_Tip"
            else:
                phase = "Boundary_Fluid_Roller_Cushion"
                
            matrix_points.append({
                "slice": slice_idx,
                "structural_phase": phase,
                "metrics": {"radius_mm": round(dynamic_radius, 4), "axial_pos_z_mm": round(z_pos, 4)},
                "vector": (round(x, 4), round(y, 4), round(z_pos, 4))
            })
            
    return matrix_points

def main():
    print("=" * 65)
    print("INITIALIZING: ARVT-02 ACCELERATION SHAFT LINER ENGINE")
    print("=" * 65)
    
    config_path = get_local_path("shaft-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        segment_len = config["geometry_parameters"]["shaft_segment_length_mm"]
        internal_dia = config["geometry_parameters"]["internal_bore_diameter_mm"]
        step_height = config["geometry_parameters"]["tesla_step_height_mm"]
        relief_angle = config["geometry_parameters"]["tesla_step_relief_angle_deg"]
        print("[+] Component ID ARVT-02 configuration card matched cleanly.")
    else:
        print("[⚠️] WARNING: shaft-config.json missing. Loading safe overrides.")
        segment_len = 500.0
        internal_dia = 50.8
        step_height = 1.2
        relief_angle = 15.0
        
    print(f"[*] Processing Bounds: Segment Length = {segment_len}mm | Bore Diameter = {internal_dia}mm")
    print(f"[*] Engraving micro-Tesla step profiles at {relief_angle}° angles...")
    
    shaft_mesh = generate_micro_tesla_liner_mesh(segment_len, internal_dia, step_height, relief_angle)
    
    # Audit a midpoint node tracking the boundary roller layer
    audit_sample = shaft_mesh[len(shaft_mesh) // 2]
    
    print("\n[+] SUCCESS: Acceleration Shaft internal matrix compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(shaft_mesh)}")
    print(f"[-] ARVT-02 Core Node Balance Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['structural_phase']}")
    print(f"    ↳ Cartesian Mesh Node:      {audit_sample['vector']}")
    print("=" * 65)

if __name__ == "__main__":
    main()
  

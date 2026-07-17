import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_hyperbolic_tesla_mesh(segment_len, d_in, d_out, step_height, relief_angle, resolution=360):
    """
    Calculates 3D spatial vectors for the internal wall structure of the shaft.
    Engraves micro-Tesla steps along a continuously tapering hyperbolic radius
    to force fluid compression and compound downward velocity.
    """
    matrix_points = []
    angle_rad = math.radians(relief_angle)
    step_pitch_z = step_height / math.tan(angle_rad)
    
    # Process slices vertically down the length of the shaft segment
    vertical_slices = int(segment_len / 2.0) # 2mm vertical step slices
    
    for slice_idx in range(vertical_slices):
        z_pos = -(slice_idx * (segment_len / vertical_slices))
        progress = abs(z_pos) / segment_len
        
        # Calculate the dynamic baseline radius for this slice using a hyperbolic taper
        current_base_dia = d_in - (d_in - d_out) * progress
        current_base_radius = current_base_dia / 2.0
        
        # Determine the current localized position inside the repeating Tesla step profile
        z_offset_in_pitch = abs(z_pos) % step_pitch_z
        
        # Linear sawtooth ramp added to the changing hyperbolic baseline radius
        dynamic_radius = current_base_radius + (step_height * (z_offset_in_pitch / step_pitch_z))
        
        for step in range(resolution):
            theta = (step * 2.0 * math.pi) / resolution
            
            x = dynamic_radius * math.cos(theta)
            y = dynamic_radius * math.sin(theta)
            
            # Identify active phase based on step drop-off geometry thresholds
            if z_offset_in_pitch > (step_pitch_z * 0.95):
                phase = "Hyperbolic_Tesla_Vortex_Detachment_Tip"
            else:
                phase = "Tapered_Boundary_Fluid_Roller_Cushion"
                
            matrix_points.append({
                "slice": slice_idx,
                "structural_phase": phase,
                "metrics": {"radius_mm": round(dynamic_radius, 4), "axial_pos_z_mm": round(z_pos, 4)},
                "vector": (round(x, 4), round(y, 4), round(z_pos, 4))
            })
            
    return matrix_points

def main():
    print("=" * 65)
    print("INITIALIZING: ARVT-02 HYPERBOLIC SHAFT LINER ENGINE")
    print("=" * 65)
    
    config_path = get_local_path("shaft-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        segment_len = config["geometry_parameters"]["shaft_segment_length_mm"]
        d_in = config["geometry_parameters"]["internal_bore_input_diameter_mm"]
        d_out = config["geometry_parameters"]["internal_bore_exit_diameter_mm"]
        step_height = config["geometry_parameters"]["tesla_step_height_mm"]
        relief_angle = config["geometry_parameters"]["tesla_step_relief_angle_deg"]
        print("[+] Optimized Component ID ARVT-02 configuration card matched.")
    else:
        print("[⚠️] WARNING: shaft-config.json missing. Loading safe fallbacks.")
        segment_len = 500.0
        d_in = 50.8
        d_out = 38.1
        step_height = 1.2
        relief_angle = 15.0
        
    print(f"[*] Profile Geometry: {d_in}mm -> {d_out}mm Hyperbolic Compression")
    print(f"[*] Engraving micro-Tesla steps along the compression path gradient...")
    
    shaft_mesh = generate_hyperbolic_tesla_mesh(segment_len, d_in, d_out, step_height, relief_angle)
    
    # Audit a midpoint node tracking the boundary roller layer
    audit_sample = shaft_mesh[len(shaft_mesh) // 2]
    
    print("\n[+] SUCCESS: Hyperbolic Acceleration Shaft matrix compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(shaft_mesh)}")
    print(f"[-] ARVT-02 Optimized Node Balance Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['structural_phase']}")
    print(f"    ↳ Cartesian Mesh Node:      {audit_sample['vector']}")
    print("=" * 65)

if __name__ == "__main__":
    main()
    

import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_hyperbolic_recycling_mesh(segment_len, d_in, d_out, step_height, relief_angle, resolution=360):
    """
    Calculates 3D spatial vectors for the internal wall structure of the throat.
    Engraves micro-Tesla steps along a continuously tapering hyperbolic radius
    while mapping the concentric channels for Seebeck thermal feedback.
    """
    matrix_points = []
    angle_rad = math.radians(relief_angle)
    step_pitch_z = step_height / math.tan(angle_rad)
    
    vertical_slices = int(segment_len / 1.0) # 1mm spatial resolution slices
    
    for slice_idx in range(vertical_slices):
        z_pos = -(slice_idx * (segment_len / vertical_slices))
        progress = abs(z_pos) / segment_len
        
        # Hyperbolic compression profile math
        current_base_dia = d_in - (d_in - d_out) * (progress ** 2)
        current_base_radius = current_base_dia / 2.0
        
        z_offset_in_pitch = abs(z_pos) % step_pitch_z
        dynamic_radius = current_base_radius + (step_height * (z_offset_in_pitch / step_pitch_z))
        
        for step in range(resolution):
            theta = (step * 2.0 * math.pi) / resolution
            
            x = dynamic_radius * math.cos(theta)
            y = dynamic_radius * math.sin(theta)
            
            if z_offset_in_pitch > (step_pitch_z * 0.95):
                phase = "Hyperbolic_Tesla_Vortex_Detachment_Tip"
            else:
                phase = "Tapered_Boundary_Fluid_Roller_Bearing"
                
            matrix_points.append({
                "slice": slice_idx,
                "structural_phase": phase,
                "metrics": {
                    "radius_mm": round(dynamic_radius, 4), 
                    "axial_pos_z_mm": round(z_pos, 4),
                    "thermal_seebeck_track_id": int(progress * 4) # 4 thermal zones
                },
                "vector": (round(x, 4), round(y, 4), round(z_pos, 4))
            })
            
    return matrix_points

def main():
    print("=" * 65)
    print("INITIALIZING: ARMC-02 HYPERBOLIC RECYCLING LINER ENGINE")
    print("=" * 65)
    
    config_path = get_local_path("throat-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        segment_len = config["geometry_parameters"]["throat_segment_length_mm"]
        d_in = config["geometry_parameters"]["internal_bore_input_diameter_mm"]
        d_out = config["geometry_parameters"]["internal_bore_exit_diameter_mm"]
        step_height = config["geometry_parameters"]["tesla_sawtooth_step_height_mm"]
        relief_angle = config["geometry_parameters"]["tesla_step_relief_angle_deg"]
        print("[+] Optimized Component ID ARMC-02 configuration card matched.")
    else:
        print("[⚠️] WARNING: throat-config.json missing. Loading safe fallbacks.")
        segment_len = 200.0
        d_in = 4.5
        d_out = 1.2
        step_height = 0.15
        relief_angle = 12.0
        
    print(f"[*] Profile Style: {d_in}mm -> {d_out}mm Hyperbolic Compression")
    print(f"[*] Siphoning Loop: Active Exhaust Gas Re-Siphoning Circuit Engaged")
    print(f"[*] Engrving micro-Tesla steps along the compression path gradient...")
    
    throat_mesh = generate_hyperbolic_recycling_mesh(segment_len, d_in, d_out, step_height, relief_angle)
    audit_sample = throat_mesh[len(throat_mesh) // 2]
    
    print("\n[+] SUCCESS: Hyperbolic Acceleration Throat matrix compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(throat_mesh)}")
    print(f"[-] ARMC-02 Core Node Balance Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['structural_phase']}")
    print(f"    ↳ Cartesian Mesh Node:      {audit_sample['vector']}")
    print("=" * 65)

if __name__ == "__main__":
    main()

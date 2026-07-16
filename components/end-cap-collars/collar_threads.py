import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_collar_thread_vectors(thread_dia, pitch, thickness, resolution=360):
    """
    Calculates the 3D helical spiral vectors for an internal metric thread 
    profile inside the End-Cap Compression Collar ring.
    """
    thread_nodes = []
    r_thread = thread_dia / 2.0
    
    # Calculate the total number of complete thread rotations based on thickness
    total_rotations = thickness / pitch
    total_steps = int(resolution * total_rotations)
    
    for step in range(total_steps):
        # Progress angle tracking the helical path loops
        angle = (step * 2 * math.pi) / resolution
        
        # Linear progression factor along the vertical compression axis (Z)
        progress = step / total_steps
        z_axis = progress * thickness
        
        # Simulate a trapezoidal thread profile groove
        # Alternates the radius slightly relative to the pitch angle to etch the thread teeth
        groove_depth = 1.5 * math.sin(angle * total_rotations)
        current_radius = r_thread + groove_depth
        
        x_thread = current_radius * math.cos(angle)
        y_thread = current_radius * math.sin(angle)
        
        # Isolate step entries to limit file size footprint in logs
        if step % 10 == 0:
            thread_nodes.append({
                "step": step,
                "rotation_angle_deg": round(math.degrees(angle), 2),
                "z_compression_mm": round(z_axis, 4),
                "internal_thread_vector": (round(x_thread, 4), round(y_thread, 4), round(z_axis, 4))
            })
            
    return thread_nodes

def main():
    print("=" * 60)
    print("INITIALIZING: END-CAP COLLAR THREAD ENGAGEMENT ENGINE")
    print("=" * 60)
    
    config_path = get_local_path("collars-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        thread_diameter = config["geometry"]["internal_thread_diameter_mm"]
        thread_pitch = config["geometry"]["thread_pitch_mm"]
        collar_thickness = config["geometry"]["collar_total_thickness_mm"]
        print("[+] Thread profiles and mechanical defaults successfully parsed.")
    else:
        print("[⚠️] WARNING: collars-config.json missing. Loading fallback constraints.")
        thread_diameter = 132.0
        thread_pitch = 3.0
        collar_thickness = 40.0
        
    print(f"[*] Simulating axial thrust loading tracks...")
    print(f"[*] Mapping ISO metric thread profile pitch: {thread_pitch}mm")
    
    # Run coordinate pipeline math
    helical_tracks = generate_collar_thread_vectors(thread_diameter, thread_pitch, collar_thickness)
    
    # Audit an active mid-thread engaged locking point coordinate
    thread_sample = helical_tracks[len(helical_tracks) // 2]
    
    print("\n[+] SUCCESS: Collar thread grid successfully compiled.")
    print(f"[-] Total structural locking nodes logged: {len(helical_tracks)}")
    print(f"[-] Thread Engagement Node Audit:")
    print(f"    ↳ Axial Z Compression Height: {thread_sample['z_compression_mm']}mm")
    print(f"    ↳ Geometric Helical Vector (X,Y,Z): {thread_sample['internal_thread_vector']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
  

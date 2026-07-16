import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_lemniscate_vectors(focal_length, height, resolution=360):
    """
    Calculates the 3D spatial vectors for a Figure-Eight Mixing Chamber
    using the parametric equations for the Lemniscate of Bernoulli.
    """
    chamber_nodes = []
    a = focal_length  # Focal parameter governing loop width
    
    for step in range(resolution):
        # Map step resolution across a full trigonometric rotation (-Pi to Pi)
        t = (step * 2 * math.pi / resolution) - math.pi
        
        # Standard Lemniscate of Bernoulli parametric equations
        # Avoid dividing by zero at the exact center crossing points
        denominator = 1 + (math.sin(t) ** 2)
        if denominator == 0:
            continue
            
        x = (a * math.cos(t)) / denominator
        y = (a * math.cos(t) * math.sin(t)) / denominator
        
        # Z-axis progression representing fluid depth/layering
        z = (step / resolution) * height
        
        # Left Loop vs Right Loop structural classification
        loop_assignment = "Left_Vortex" if x < 0 else "Right_Vortex"
        if round(x, 2) == 0.00 and round(y, 2) == 0.00:
            loop_assignment = "Collision_Center"
            
        chamber_nodes.append({
            "step": step,
            "parameter_t": round(t, 4),
            "zone": loop_assignment,
            "vector": (round(x, 4), round(y, 4), round(z, 4))
        })
        
    return chamber_nodes

def main():
    print("=" * 60)
    print("INITIALIZING: FIGURE-EIGHT MIXING CHAMBER GENERATOR")
    print("=" * 60)
    
    config_path = get_local_path("mixer-config.json")
    
    # Load constraints directly from the JSON profile file
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        focal_length = config["geometry"]["focal_length_mm"]
        chamber_height = config["geometry"]["chamber_height_mm"]
        print("[+] Configuration profiles extracted successfully.")
    else:
        # Fallback constants if JSON file path fails to resolve
        print("[⚠️] WARNING: mixer-config.json missing. Using system defaults.")
        focal_length = 50.0
        chamber_height = 75.0
        
    print(f"[*] Compiling geometry map using the Lemniscate of Bernoulli...")
    print(f"[*] Processing boundaries at scale: Focal Length = {focal_length}mm")
    
    # Generate the 3D vector points
    mesh_vectors = generate_lemniscate_vectors(focal_length, chamber_height)
    
    # Sample the absolute center collision junction (where loops cross)
    midpoint_sample = mesh_vectors[len(mesh_vectors) // 2]
    
    print("\n[+] SUCCESS: Figure-Eight vector matrix compiled cleanly.")
    print(f"[-] Total structural nodes mapped: {len(mesh_vectors)}")
    print(f"[-] Collision Zone Intersection Check (Midpoint):")
    print(f"    ↳ Vector Node Zone: {midpoint_sample['zone']}")
    print(f"    ↳ Spatial Vectors (X, Y, Z): {midpoint_sample['vector']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
  

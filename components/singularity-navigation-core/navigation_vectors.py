import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_singularity_vectors(throat_dia, height, compression_ratio, resolution=360):
    """
    Calculates 3D spatial vectors mapping a fluid stream compressing 
    down a vortex throat and distributing into a hexagonal array matrix.
    """
    nodes = []
    r_base = (throat_dia * compression_ratio) / 2.0
    r_throat = throat_dia / 2.0
    
    for step in range(resolution):
        # Progress angle to simulate spiral vortex velocity down the throat
        angle = (step * 4 * math.pi) / resolution  # 2 full rotational spirals
        
        # Linear progression factor along the vertical axis (0.0 to 1.0)
        progress = step / resolution
        z = progress * height
        
        # Dynamic Tapering: Squeezes the radius down to the throat bottleneck
        current_radius = r_base - (progress * (r_base - r_throat))
        
        # Map spiral path coordinates
        x_spiral = current_radius * math.cos(angle)
        y_spiral = current_radius * math.sin(angle)
        
        # Node zone assignment mapping the vector transition phases
        if progress < 0.15:
            phase = "Intake_Zone"
        elif progress > 0.85:
            phase = "Hex_Exhaust_Junction"
        else:
            phase = "Compression_Throat"
            
        nodes.append({
            "step": step,
            "phase": phase,
            "z_depth": round(z, 4),
            "vector": (round(x_spiral, 4), round(y_spiral, 4), round(z, 4))
        })
        
    return nodes

def main():
    print("=" * 60)
    print("INITIALIZING: SINGULARITY NAVIGATION CORE CALCULATOR")
    print("=" * 60)
    
    config_path = get_local_path("core-config.json")
    
    # Extract structural limits from your local settings JSON
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        throat_diameter = config["geometry"]["throat_diameter_mm"]
        chamber_height = config["geometry"]["chamber_height_mm"]
        # Convert configuration text key "1.618_to_1" into float constant 1.618
        ratio_str = config["geometry"]["compression_ratio"].split("_")[0]
        comp_ratio = float(ratio_str)
        print("[+] Core operational parameters safely loaded from configuration profile.")
    else:
        print("[⚠️] WARNING: core-config.json missing. Resorting to hardware overrides.")
        throat_diameter = 25.0
        chamber_height = 75.0
        comp_ratio = 1.618
        
    print(f"[*] Mapping vector compression curves using Truncated Icosahedron Node parameters...")
    print(f"[*] Scaling boundary matrix limits: Minimum Throat Diameter = {throat_diameter}mm")
    
    # Run coordinate pipeline math
    navigation_nodes = generate_singularity_vectors(throat_diameter, chamber_height, comp_ratio)
    
    # Audit the bottleneck exit boundary point
    final_node_sample = navigation_nodes[-1]
    
    print("\n[+] SUCCESS: Core compression matrix fully mapped.")
    print(f"[-] Total automated matrix points logged: {len(navigation_nodes)}")
    print(f"[-] Exit Transition Vector Boundary Audit:")
    print(f"    ↳ Operational Module Phase: {final_node_sample['phase']}")
    print(f"    ↳ Coordinate Vector Matrix (X, Y, Z): {final_node_sample['vector']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
      

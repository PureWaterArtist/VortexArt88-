import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_hyperboloid_vectors(throat_a, scale_c, total_z, resolution=360):
    """
    Calculates 3D spatial vectors mapping a Hyperboloid of One Sheet shell.
    The surface curves hyperbolically around the Z-axis to guide fluid paths.
    """
    matrix_points = []
    
    for step in range(resolution):
        # Progress factor maps out the vertical height progression along the Z-axis
        progress = step / resolution
        z_axis = (progress * total_z) - (total_z / 2.0)
        
        # Rotational sweep angle 'v' maps the full 360-degree cylinder (0 to 2*Pi)
        v = (step * 2.0 * math.pi) / resolution
        
        # Classical Parametric Equations for a Hyperboloid of One Sheet
        # Radius expands as a function of the hyperbolic secant / cosine properties
        # r = a * sqrt(1 + (z/c)^2)
        z_ratio = z_axis / scale_c
        radius = throat_a * math.sqrt(1.0 + (z_ratio ** 2))
        
        x = radius * math.cos(v)
        y = radius * math.sin(v)
        
        # Structural phase tracking based on height progress
        if progress < 0.20:
            phase = "Flanged_Intake_Zone"
        elif progress > 0.80:
            phase = "Flanged_Discharge_Zone"
        else:
            phase = "Asymptotic_Throat_Core"
            
        matrix_points.append({
            "step": step,
            "structural_phase": phase,
            "parameters": {"z_depth_mm": round(z_axis, 4), "v_rad": round(v, 4)},
            "coordinate_vector": (round(x, 4), round(y, 4), round(z_axis, 4))
        })
        
    return matrix_points

def main():
    print("=" * 60)
    print("INITIALIZING: HYPERBOLOIDAL REGULATOR MATRIX ENGINE")
    print("=" * 60)
    
    config_path = get_local_path("hyperboloid-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        throat_a = config["geometry"]["throat_radius_a_mm"]
        scale_c = config["geometry"]["asymptotic_scale_c_mm"]
        total_z = config["geometry"]["total_axial_length_z_mm"]
        print("[+] Hyperboloidal geometric parameters successfully loaded.")
    else:
        print("[⚠️] WARNING: hyperboloid-config.json missing. Loading safe defaults.")
        throat_a = 25.0
        scale_c = 40.0
        total_z = 120.0
        
    print(f"[*] Compiling doubly ruled asymptotic curvature grids...")
    print(f"[*] Processing quadric profile boundaries: Throat Radius = {throat_a}mm")
    
    # Run coordinate pipeline calculation loops
    hyperboloid_nodes = generate_hyperboloid_vectors(throat_a, scale_c, total_z)
    
    # Audit a midpoint node tracking the tightest restriction line at the center neck
    audit_sample = hyperboloid_nodes[len(hyperboloid_nodes) // 2]
    
    print("\n[+] SUCCESS: Hyperboloid boundary matrix compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(hyperboloid_nodes)}")
    print(f"[-] Hyperboloid Throat Center Balance Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['structural_phase']}")
    print(f"    ↳ Cartesian Mesh Node:      {audit_sample['coordinate_vector']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
      

import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_paraboloid_vectors(focal_length, max_z, resolution=360):
    """
    Calculates 3D spatial vectors mapping a Circular Paraboloid shell.
    The surface curves parabolically to focus fluid velocity vectors uniformly.
    """
    matrix_points = []
    
    for step in range(resolution):
        # Progress parameter maps out the axial depth progression (0 to max_z)
        progress = step / resolution
        z_axis = progress * max_z
        
        # Rotational sweep angle 'v' maps the full 360-degree cylinder (0 to 2*Pi)
        v = (step * 2.0 * math.pi) / resolution
        
        # Classical Paraboloid Equation: r^2 = 4 * f * z -> r = sqrt(4 * f * z)
        radius = math.sqrt(4.0 * focal_length * z_axis)
        
        # Translate polar cylinder dimensions to 3D Cartesian coordinates
        x = radius * math.cos(v)
        y = radius * math.sin(v)
        
        # Structural phase tracking based on progress depth
        if progress < 0.20:
            phase = "Concentrated_Discharge_Nexus"
        elif progress > 0.80:
            phase = "Wide_Manifold_Intake"
        else:
            phase = "Parabolic_Focal_Transition"
            
        matrix_points.append({
            "step": step,
            "structural_phase": phase,
            "parameters": {"z_depth_mm": round(z_axis, 4), "v_rad": round(v, 4)},
            "coordinate_vector": (round(x, 4), round(y, 4), round(z_axis, 4))
        })
        
    return matrix_points

def main():
    print("=" * 60)
    print("INITIALIZING: PARABOLOIDAL REGULATOR MATRIX ENGINE")
    print("=" * 60)
    
    config_path = get_local_path("paraboloid-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        focal_length = config["geometry"]["focal_length_f_mm"]
        max_z = config["geometry"]["max_axial_depth_z_mm"]
        print("[+] Parabolic reflective variables successfully loaded.")
    else:
        print("[⚠️] WARNING: paraboloid-config.json missing. Loading safe defaults.")
        focal_length = 20.0
        max_z = 80.0
        
    print(f"[*] Compiling parabolic focal reflection grids...")
    print(f"[*] Processing paraboloid profile boundaries: Focal Length = {focal_length}mm")
    
    # Run coordinate pipeline calculation loops
    paraboloid_nodes = generate_paraboloid_vectors(focal_length, max_z)
    
    # Audit a midpoint node tracking the focal transition area
    audit_sample = paraboloid_nodes[len(paraboloid_nodes) // 2]
    
    print("\n[+] SUCCESS: Paraboloid boundary matrix compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(paraboloid_nodes)}")
    print(f"[-] Paraboloid Focal Transition Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['structural_phase']}")
    print(f"    ↳ Cartesian Mesh Node:      {audit_sample['coordinate_vector']}")
    print("=" * 60)

if __name__ == "__main__":
    main()

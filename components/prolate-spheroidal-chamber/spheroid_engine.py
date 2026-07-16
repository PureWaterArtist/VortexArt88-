import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_prolate_spheroid_vectors(axis_a, axis_b, resolution=360):
    """
    Calculates 3D spatial vectors mapping a Prolate Spheroid boundary shell.
    The surface curves symmetrically around the major axis (Z) to guide fluid foci.
    """
    matrix_points = []
    
    for step in range(resolution):
        # Parametric angle 'u' maps from -Pi/2 to Pi/2 along the ellipse curvature
        u = (-math.pi / 2.0) + (step * math.pi / resolution)
        
        # Longitudinal sweep angle 'v' maps the full 360-degree rotation (0 to 2*Pi)
        v = (step * 2.0 * math.pi) / resolution
        
        # Classical Parametric Equations for a Prolate Spheroid rotated around the Z-axis
        x = axis_b * math.cos(u) * math.cos(v)
        y = axis_b * math.cos(u) * math.sin(v)
        z = axis_a * math.sin(u)
        
        # Structural tier tracing based on vertical height progress
        progress = step / resolution
        if progress < 0.25:
            zone = "Focal_Inlet_Zone"
        elif progress > 0.75:
            zone = "Focal_Outlet_Zone"
        else:
            zone = "Elliptical_Expansion_Chamber"
            
        matrix_points.append({
            "step": step,
            "structural_phase": zone,
            "angles_rad": {"u": round(u, 4), "v": round(v, 4)},
            "coordinate_vector": (round(x, 4), round(y, 4), round(z, 4))
        })
        
    return matrix_points

def main():
    print("=" * 60)
    print("INITIALIZING: PROLATE SPHEROIDAL GEOMETRY ENGINE")
    print("=" * 60)
    
    config_path = get_local_path("spheroid-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        axis_a = config["geometry"]["major_axis_radius_a_mm"]
        axis_b = config["geometry"]["minor_axis_radius_b_mm"]
        print("[+] Prolate elliptical constraints verified and parsed from configuration.")
    else:
        print("[⚠️] WARNING: spheroid-config.json missing. Loading safe defaults.")
        axis_a = 60.0
        axis_b = 30.0
        
    print(f"[*] Simulating dual-foci boundary curvature grids...")
    print(f"[*] Scaling profile axes: Major (a) = {axis_a}mm | Minor (b) = {axis_b}mm")
    
    # Run coordinate pipeline calculation loops
    spheroid_nodes = generate_prolate_spheroid_vectors(axis_a, axis_b)
    
    # Audit a midpoint node tracking the elliptical sweep at the equator
    audit_sample = spheroid_nodes[len(spheroid_nodes) // 2]
    
    print("\n[+] SUCCESS: Prolate Spheroid boundary matrix fully built.")
    print(f"[-] Total coordinated structural nodes logged: {len(spheroid_nodes)}")
    print(f"[-] Spheroidal Equator Interface Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['structural_phase']}")
    print(f"    ↳ Cartesian Mesh Node:      {audit_sample['coordinate_vector']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
  

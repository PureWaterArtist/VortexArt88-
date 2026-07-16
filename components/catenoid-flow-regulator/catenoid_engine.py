import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_catenoid_vectors(throat_c, total_z, resolution=360):
    """
    Calculates 3D spatial vectors mapping a Catenoid Minimal Surface shell.
    The surface curves hyperbolically to balance tension and compression fields.
    """
    matrix_points = []
    half_z = total_z / 2.0
    
    for step in range(resolution):
        # Parametric height parameter 'u' maps across the axial length (-half_z to +half_z)
        # Scaled to represent the standard hyperbolic input range
        u_scaled = -2.0 + (step * 4.0 / resolution)
        z_axis = throat_c * u_scaled
        
        # Rotational sweep angle 'v' maps the full 360-degree cylinder (0 to 2*Pi)
        v = (step * 2.0 * math.pi) / resolution
        
        # Classical Parametric Equations for a 3D Catenoid Surface
        # Radius expands as a function of the hyperbolic cosine of axial depth
        x = throat_c * math.cosh(u_scaled) * math.cos(v)
        y = throat_c * math.cosh(u_scaled) * math.sin(v)
        
        # Structural phase tracking based on height progress
        progress = step / resolution
        if progress < 0.20:
            phase = "Flanged_Intake_Zone"
        elif progress > 0.80:
            phase = "Flanged_Discharge_Zone"
        else:
            phase = "Hyperbolic_Throat_Core"
            
        matrix_points.append({
            "step": step,
            "structural_phase": phase,
            "parameters": {"u": round(u_scaled, 4), "v": round(v, 4)},
            "coordinate_vector": (round(x, 4), round(y, 4), round(z_axis, 4))
        })
        
    return matrix_points

def main():
    print("=" * 60)
    print("INITIALIZING: CATENOID MINIMAL SURFACE MATRIX ENGINE")
    print("=" * 60)
    
    config_path = get_local_path("catenoid-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        throat_c = config["geometry"]["throat_parameter_c_mm"]
        total_z = config["geometry"]["axial_length_z_mm"]
        print("[+] Minimal surface geometric parameters successfully loaded.")
    else:
        print("[⚠️] WARNING: catenoid-config.json missing. Loading safe overrides.")
        throat_c = 25.0
        total_z = 100.0
        
    print(f"[*] Compiling hyperbolic zero-mean-curvature grids...")
    print(f"[*] Processing catenary profile boundaries: Throat Constant = {throat_c}mm")
    
    # Run coordinate pipeline calculation loops
    catenoid_nodes = generate_catenoid_vectors(throat_c, total_z)
    
    # Audit a midpoint node tracking the tightest restriction line at the center neck
    audit_sample = catenoid_nodes[len(catenoid_nodes) // 2]
    
    print("\n[+] SUCCESS: Catenoid boundary matrix compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(catenoid_nodes)}")
    print(f"[-] Catenoid Throat Center Balance Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['structural_phase']}")
    print(f"    ↳ Cartesian Mesh Node:      {audit_sample['coordinate_vector']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
      

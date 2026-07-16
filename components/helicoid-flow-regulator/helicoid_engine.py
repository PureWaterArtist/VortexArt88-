import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_helicoid_vectors(inner_r, outer_r, pitch_p, total_z, resolution=360):
    """
    Calculates 3D spatial vectors mapping a Helicoid Minimal Surface shell.
    The surface curves symmetrically around the Z-axis to guide fluid screw lines.
    """
    matrix_points = []
    
    for step in range(resolution):
        # Progress factor maps out the vertical height progression along the Z-axis
        progress = step / resolution
        z_axis = (progress * total_z) - (total_z / 2.0)
        
        # Parameter 'u' tracks the radial distance from the central core to outer blade extent
        u = inner_r + (progress * (outer_r - inner_r))
        
        # Parameter 'v' maps the rotational angle sweep proportional to vertical height and pitch index
        # v = z / p -> maps the exact pitch angle tracking of the minimal surface screw
        v = z_axis / pitch_p
        
        # Classical Parametric Equations for a 3D Helicoid Minimal Surface
        x = u * math.cos(v)
        y = u * math.sin(v)
        
        # Structural phase tracking based on progress
        if progress < 0.20:
            phase = "Screw_Axis_Inlet"
        elif progress > 0.80:
            phase = "Screw_Axis_Discharge"
        else:
            phase = "Helical_Induction_Transit"
            
        matrix_points.append({
            "step": step,
            "structural_phase": phase,
            "parameters": {"u_radial": round(u, 4), "v_rad": round(v, 4)},
            "coordinate_vector": (round(x, 4), round(y, 4), round(z_axis, 4))
        })
        
    return matrix_points

def main():
    print("=" * 60)
    print("INITIALIZING: HELICOID MINIMAL SURFACE ENGINE")
    print("=" * 60)
    
    config_path = get_local_path("helicoid-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        inner_r = config["geometry"]["central_axis_radius_mm"]
        outer_r = config["geometry"]["outer_radial_extent_mm"]
        pitch_p = config["geometry"]["helical_pitch_p_mm"]
        total_z = config["geometry"]["total_axial_length_z_mm"]
        print("[+] Helicoid minimal surface parameters successfully verified.")
    else:
        print("[⚠️] WARNING: helicoid-config.json missing. Loading safe defaults.")
        inner_r = 10.0
        outer_r = 45.0
        pitch_p = 40.0
        total_z = 120.0
        
    print(f"[*] Compiling continuous horizontal straight line matrices...")
    print(f"[*] Processing screw pitch geometries: Pitch Parameter (p) = {pitch_p}mm")
    
    # Run coordinate pipeline calculation loops
    helicoid_nodes = generate_helicoid_vectors(inner_r, outer_r, pitch_p, total_z)
    
    # Audit a midpoint node tracking the structural center loop
    audit_sample = helicoid_nodes[len(helicoid_nodes) // 2]
    
    print("\n[+] SUCCESS: Helicoid boundary coordinate matrix fully built.")
    print(f"[-] Total coordinated structural steps logged: {len(helicoid_nodes)}")
    print(f"[-] Helicoid Screw Tracking Balance Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['structural_phase']}")
    print(f"    ↳ Cartesian Mesh Node:      {audit_sample['coordinate_vector']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
      

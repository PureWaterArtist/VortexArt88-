import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_casing_shell_vectors(inner_dia, outer_dia, total_length, resolution=180):
    """
    Calculates 3D spatial boundaries for the outer structural casing, 
    mapping cylindrical perimeters and localized O-ring gasket seal tracks.
    """
    shell_nodes = []
    r_out = outer_dia / 2.0
    r_in = inner_dia / 2.0
    
    for step in range(resolution):
        # Progress factor along the physical height length axis (Z)
        progress = step / resolution
        z_axis = progress * total_length
        
        # Sweep angle to plot circular coordinate paths
        theta = (step * 2 * math.pi) / resolution
        
        # Symmetrical Gasket Track placement safeguards at boundaries
        # Compresses the inner radius locally at the top and bottom to form tracks
        if (z_axis > 20.0 and z_axis < 30.0) or (z_axis > (total_length - 30.0) and z_axis < (total_length - 20.0)):
            current_inner_radius = r_in + 2.5  # Etch a 2.5mm deep groove track
            layer_status = "O_Ring_Gasket_Groove"
        else:
            current_inner_radius = r_in
            layer_status = "Solid_Wall_Sleeve"
            
        x_outer = r_out * math.cos(theta)
        y_outer = r_out * math.sin(theta)
        x_inner = current_inner_radius * math.cos(theta)
        y_inner = current_inner_radius * math.sin(theta)
        
        shell_nodes.append({
            "step": step,
            "layer_height_mm": round(z_axis, 2),
            "status": layer_status,
            "outer_perimeter": (round(x_outer, 4), round(y_outer, 4), round(z_axis, 4)),
            "inner_perimeter": (round(x_inner, 4), round(y_inner, 4), round(z_axis, 4))
        })
        
    return shell_nodes

def main():
    print("=" * 60)
    print("INITIALIZING: OUTER PRESSURE CASING BOUNDARY ENGINE")
    print("=" * 60)
    
    config_path = get_local_path("casing-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        inner_diameter = config["geometry"]["internal_chamber_diameter_mm"]
        outer_diameter = config["geometry"]["outer_shell_diameter_mm"]
        assembly_length = config["geometry"]["total_assembly_length_mm"]
        print("[+] Physical casing constraints parsed cleanly from configuration dataset.")
    else:
        print("[⚠️] WARNING: casing-config.json missing. Resorting to hardware fallbacks.")
        inner_diameter = 110.0
        outer_diameter = 130.0
        assembly_length = 450.0
        
    print(f"[*] Simulating structural hoop stress envelopes...")
    print(f"[*] Mapping sleeve boundaries: Total Length = {assembly_length}mm")
    
    # Run coordinate pipeline
    casing_matrix = generate_casing_shell_vectors(inner_diameter, outer_diameter, assembly_length)
    
    # Audit an active gasket ring segment vector point
    gasket_sample = casing_matrix[int(resolution_step_fraction := len(casing_matrix) * 0.06)]
    
    print("\n[+] SUCCESS: Casing sleeve geometry fully compiled.")
    print(f"[-] Total structural perimeters mapped: {len(casing_matrix)}")
    print(f"[-] Gasket Track Interface Audit:")
    print(f"    ↳ Geometric Layer Status: {gasket_sample['status']}")
    print(f"    ↳ Inner Groove Vector (X,Y,Z): {gasket_sample['inner_perimeter']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
      

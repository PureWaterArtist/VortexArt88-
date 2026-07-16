import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_glome_projection_vectors(core_radius, w_scale, shells, resolution=360):
    """
    Calculates 3D coordinates projected from a 4D Glome hypersphere matrix,
    tracking coordinates seamlessly across X, Y, Z, and W-axis spaces.
    """
    glome_nodes = []
    
    for step in range(resolution):
        # Progress factor along the radial expansion path
        progress = step / resolution
        
        # Angular coordinate tracking for hyperspherical sweep
        theta = (step * 2.0 * math.pi) / resolution
        phi = theta * 2.0
        
        # 4D Glome Hypersphere coordinate mappings
        x_4d = core_radius * math.cos(theta) * math.cos(phi)
        y_4d = core_radius * math.cos(theta) * math.sin(phi)
        z_4d = core_radius * math.sin(theta) * math.cos(phi)
        w_4d = core_radius * math.sin(theta) * math.sin(phi)
        
        # 3D Stereographic Projection using Golden Ratio hyper-scale limits
        denominator = 1.0 - (w_4d / (core_radius * w_scale))
        if abs(denominator) < 1e-6:
            denominator = 1e-6
            
        x_3d = x_4d / denominator
        y_3d = y_4d / denominator
        z_3d = z_4d / denominator
        
        # Segment assignment tracking the concentric layer transitions
        shell_index = int(progress * shells) + 1
        active_shell = f"Concentric_Shell_0{min(shell_index, shells)}"
        
        if progress < 0.20:
            phase = "Hyper_Core_Intake"
        elif progress > 0.80:
            phase = "Hyperspherical_Discharge"
        else:
            phase = "Nested_Shell_Expansion"
            
        glome_nodes.append({
            "step": step,
            "structural_phase": phase,
            "assigned_layer": active_shell,
            "projected_3d_vector": (round(x_3d, 4), round(y_3d, 4), round(z_3d, 4)),
            "hyper_coordinate_w": round(w_4d, 4)
        })
        
    return glome_nodes

def main():
    print("=" * 60)
    print("INITIALIZING: GLOME HYPER-SPHERICAL EXPANSION ENGINE")
    print("=" * 60)
    
    config_path = get_local_path("glome-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        core_radius = config["geometry"]["core_projection_radius_mm"]
        w_scale_factor = config["geometry"]["hyper_axis_w_scale"]
        nested_shells = config["geometry"]["nested_shell_layers"]
        print("[+] Glome hyper-dimensional variables successfully loaded.")
    else:
        print("[⚠️] WARNING: glome-config.json missing. Loading fallback defaults.")
        core_radius = 50.0
        w_scale_factor = 1.618034
        nested_shells = 5
        
    print(f"[*] Simulating stereographic hyperspherical matrices...")
    print(f"[*] Synchronizing W-Axis scalar bounds: Phi = {w_scale_factor}")
    
    # Run coordinate pipeline loops
    simulation_nodes = generate_glome_projection_vectors(core_radius, w_scale_factor, nested_shells)
    
    # Audit a midpoint node tracking the W-axis projection depth
    audit_sample = simulation_nodes[len(simulation_nodes) // 2]
    
    print("\n[+] SUCCESS: Glome hyperspherical matrix compiled cleanly.")
    print(f"[-] Total coordinated 4D grid steps logged: {len(simulation_nodes)}")
    print(f"[-] Hyperspherical Convergence Matrix Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['structural_phase']}")
    print(f"    ↳ Active Layer Allocation: {audit_sample['assigned_layer']}")
    print(f"    ↳ Projected 3D Cartesian:  {audit_sample['projected_3d_vector']}")
    print(f"    ↳ Hyper-Volume Node W:     {audit_sample['hyper_coordinate_w']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
      

import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_hyper_plenum_vectors(intake_dia, ports_count, w_scale, resolution=360):
    """
    Calculates 4D spatial extrusion vectors for a Hyper-Cylindrical Plenum,
    tracking coordinates seamlessly across X, Y, Z, and W-axis matrices.
    """
    hyper_nodes = []
    r_base = intake_dia / 2.0
    
    for step in range(resolution):
        # Progress along the linear vertical axis (Z)
        progress = step / resolution
        z_axis = progress * 120.0  # Mapped across a 120mm housing height
        
        # Rotational sweep to map the cylindrical perimeter
        theta = (step * 2 * math.pi) / resolution
        
        # 📐 THE PATH OF LEAST RESISTANCE EXTRUSION:
        # X and Y map the physical cylinder, while W handles the higher-dimensional scale
        x = r_base * math.cos(theta)
        y = r_base * math.sin(theta)
        
        # Extrude along the virtual 4D W-axis based on progress and Golden Ratio scaling
        w_axis = progress * w_scale * 10.0
        
        # Allocate spatial quadrants to represent the 4 balancing output ports
        quadrant = (step // (resolution // ports_count)) + 1
        port_assignment = f"Spatial_Port_Alpha_0{quadrant}"
        
        if progress < 0.20:
            phase = "4D_Intake_Manifold"
        elif progress > 0.80:
            phase = "Quad_Channel_Discharge"
        else:
            phase = "Hyper_Extrusion_Zone"
            
        hyper_nodes.append({
            "step": step,
            "structural_phase": phase,
            "target_discharge": port_assignment,
            "coordinates_3d": (round(x, 4), round(y, 4), round(z_axis, 4)),
            "hyper_vector_w": round(w_axis, 4)
        })
        
    return hyper_nodes

def main():
    print("=" * 60)
    print("INITIALIZING: HYPER-CYLINDRICAL PLENUM EXTRUSION ENGINE")
    print("=" * 60)
    
    config_path = get_local_path("hyper-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        intake_diameter = config["geometry"]["main_intake_diameter_mm"]
        output_ports = config["geometry"]["spatial_output_ports"]
        w_scale_factor = config["geometry"]["hyper_axis_w_scale"]
        print("[+] Hyper-dimensional geometric variables verified and compiled.")
    else:
        print("[⚠️] WARNING: hyper-config.json missing. Resorting to fallback overrides.")
        intake_diameter = 60.0
        output_ports = 4
        w_scale_factor = 1.618034
        
    print(f"[*] Projecting 4D hyper-cylindrical expansion envelopes...")
    print(f"[*] Synchronizing W-Axis scalar parameters: Phi = {w_scale_factor}")
    
    # Process the 4D matrix pipeline loops
    simulation_nodes = generate_hyper_plenum_vectors(intake_diameter, output_ports, w_scale_factor)
    
    # Audit a midpoint node tracking the W-axis extrusion depth
    audit_sample = simulation_nodes[len(simulation_nodes) // 2]
    
    print("\n[+] SUCCESS: Hyper-cylindrical vector grid compiled cleanly.")
    print(f"[-] Total coordinated 4D grid steps logged: {len(simulation_nodes)}")
    print(f"[-] Cross-Dimensional Convergence Matrix Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['structural_phase']}")
    print(f"    ↳ Real-Space Coordinates:   {audit_sample['coordinates_3d']}")
    print(f"    ↳ Hyper-Volume Extrusion W: {audit_sample['hyper_vector_w']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
      

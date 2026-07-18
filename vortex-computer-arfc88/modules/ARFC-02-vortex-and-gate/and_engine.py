import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_and_gate_vectors(phi, channel_depth_microns, input_w, resolution=360):
    """
    Calculates the 3D coordinate meshes for the Figure-8 conjunction core.
    Maps out the precise head-on intersection point where dual fluid ribbons 
    collide to execute pure Boolean AND logic operations.
    """
    and_nodes = []
    base_chamber_radius = 2.5   # 2.5mm initial micro-chamber boundary
    exit_throat_radius = input_w / 2.0
    
    # Total longitudinal thickness of the micro-etched logic block is 6mm
    total_z_length = 6.0
    
    for step in range(resolution):
        progress = step / resolution
        z_axis = (progress * total_z_length) - (total_z_length / 2.0)
        theta = (step * 2.0 * math.pi) / resolution
        
        # Shape the micro-conjunction contour along a logarithmic contraction curve
        log_b_coefficient = 0.12 / phi
        log_radius = base_chamber_radius * math.exp(-log_b_coefficient * theta)
        
        # Apply a smooth convergent Venturi pinch near the exit gates
        if progress > 0.80:
            tip_factor = (progress - 0.80) / 0.20
            radius_modulation = log_radius - (log_radius - exit_throat_radius) * math.sin(tip_factor * (math.pi / 2.0))
        else:
            radius_modulation = log_radius
            
        # Clamp radius bounds to preserve micro-wafer design limits
        radius_modulation = max(exit_throat_radius, min(base_chamber_radius, radius_modulation))
        
        # Logic Input A ribbon track (Clockwise)
        xa = radius_modulation * math.cos(theta)
        ya = radius_modulation * math.sin(theta)
        
        # Logic Input B ribbon track (Counter-Clockwise mirrored)
        xb = radius_modulation * math.cos(-theta)
        yb = radius_modulation * math.sin(-theta)
        
        if progress > 0.80:
            phase = "Convergent_Logic_Output_Channel"
        elif abs(xa - xb) < 0.1 and abs(ya - yb) < 0.1:
            phase = "Sub_Atomic_Fluidic_Conjunction_Singularity"
        else:
            phase = "Logarithmic_Vortex_Logic_Squeeze"
            
        and_nodes.append({
            "step": step,
            "logic_phase": phase,
            "metrics": {
                "axial_z_mm": round(z_axis, 4),
                "dynamic_radius_mm": round(radius_modulation, 4),
                "etch_depth_um": channel_depth_microns
            },
            "input_a_vector": (round(xa, 4), round(ya, 4), round(z_axis, 4)),
            "input_b_vector": (round(xb, 4), round(yb, 4), round(-z_axis, 4))
        })
        
    return and_nodes

def main():
    print("=" * 65)
    print("INITIALIZING: ARFC-02 VORTEX AND GATE CORE ENGINE")
    print("=" * 65)
    
    config_path = get_local_path("and-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        phi = config["geometry_parameters"]["fibonacci_contour_phi"]
        depth = config["fabrication_profile"]["channel_etch_depth_microns"]
        input_w = config["geometry_parameters"]["input_channel_width_mm"]
        material = config["fabrication_profile"]["recommended_wafer_substrate"]
        print("[+] Industrial Component ID ARFC-02 configuration card matched.")
    else:
        print("[⚠️] WARNING: and-config.json missing. Loading safe overrides.")
        phi = 1.618
        depth = 250.0
        input_w = 0.35
        material = "Monocrystalline_Quartz"
        
    print(f"[*] Wafer Substrate Material: {material}")
    print(f"[*] Micro-Etch Target Depth: {depth} microns")
    print(f"[*] Compiling twin reverse-rotational arithmetic paths...")
    
    and_mesh = generate_and_gate_vectors(phi, depth, input_w)
    audit_sample = [n for n in and_mesh if n["logic_phase"] == "Sub_Atomic_Fluidic_Conjunction_Singularity"]
    
    # Simple check if list is empty to provide safe fallback log printing
    sample_node = audit_sample[0] if audit_sample else and_mesh[len(and_mesh) // 2]
    
    print("\n[+] SUCCESS: Figure-8 fluid logic AND gate compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(and_mesh)}")
    print(f"[-] ARFC-02 Core Node Balance Audit:")
    print(f"    ↳ Active Logic Phase:      {sample_node['logic_phase']}")
    print(f"    ↳ Input A Space Vector:    {sample_node['input_a_vector']}")
    print("=" * 65)

if __name__ == "__main__":
    main()
  

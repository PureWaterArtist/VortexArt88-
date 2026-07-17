import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_twin_vortex_nozzle_vectors(spiral_a, spiral_b, chamber_height, resolution=360):
    """
    Calculates the 3D coordinate meshes for Nozzle A (CW) and Nozzle B (CCW).
    Maps out the logarithmic contraction curves to accelerate the fluid sheets 
    into a high-shear face-to-face collision.
    """
    nozzle_vectors = []
    
    for step in range(resolution):
        # Progress map tracking from the outer inlet to the high-shear tip
        progress = step / resolution
        z_axis = (progress * chamber_height) - (chamber_height / 2.0)
        
        # Parametric sweep angle tracks the cross-sectional 3D spatial rotation (0 to 2*Pi)
        theta = (step * 2.0 * math.pi) / resolution
        
        # Logarithmic contraction math modeling the golden-ratio spiral envelope:
        # r = a * e^(-b * theta)
        radius_modulation = spiral_a * math.exp(-spiral_b * theta)
        
        # Clamp radius to ensure a safe physical nozzle wall boundary thickness
        radius_modulation = max(5.0, min(spiral_a, radius_modulation))
        
        # Nozzle A (Clockwise vector path layout)
        xa = radius_modulation * math.cos(theta)
        ya = radius_modulation * math.sin(theta)
        
        # Nozzle B (Counter-Clockwise mirrored vector path layout)
        xb = radius_modulation * math.cos(-theta)
        yb = radius_modulation * math.sin(-theta)
        
        # Segment phase tracking based on linear progression through the core
        if progress < 0.20 or progress > 0.80:
            phase = "Logarithmic_Vortex_Inlet_Ports"
        elif radius_modulation < 10.0:
            phase = "Central_Singularity_High_Shear_Core"
        else:
            phase = "Reverse_Rotational_Compression_Transit"
            
        nozzle_vectors.append({
            "step": step,
            "structural_phase": phase,
            "metrics": {
                "axial_pos_mm": round(z_axis, 4),
                "dynamic_radius_mm": round(radius_modulation, 4)
            },
            "nozzle_a_vector": (round(xa, 4), round(ya, 4), round(z_axis, 4)),
            "nozzle_b_vector": (round(xb, 4), round(yb, 4), round(-z_axis, 4))
        })
        
    return nozzle_vectors

def main():
    print("=" * 65)
    print("INITIALIZING: ARVT-04 CORE JUNCTION VORTEX SPIRAL ENGINE")
    print("=" * 65)
    
    config_path = get_local_path("junction-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        spiral_a = config["geometry_parameters"]["logarithmic_spiral_factor_a"]
        spiral_b = config["geometry_parameters"]["logarithmic_spiral_factor_b"]
        chamber_height = config["geometry_parameters"]["chamber_internal_height_mm"]
        material = config["manufacturing_profile"]["recommended_material"]
        print("[+] Component ID ARVT-04 configuration card matched cleanly.")
    else:
        print("[⚠️] WARNING: junction-config.json missing. Loading safe overrides.")
        spiral_a = 20.0
        spiral_b = 0.12
        chamber_height = 190.0
        material = "Hardened_PEEK"
        
    print(f"[*] Core Hardening Material Standard: {material}")
    print(f"[*] Processing Bounds: Chamber Active Height Span = {chamber_height}mm")
    print(f"[*] Compiling reverse-rotational logarithmic mesh paths...")
    
    junction_mesh = generate_twin_vortex_nozzle_vectors(spiral_a, spiral_b, chamber_height)
    
    # Audit a midpoint node tracking the high-shear intersection core
    audit_sample = junction_mesh[len(junction_mesh) // 2]
    
    print("\n[+] SUCCESS: Core Junction twin vortex matrix compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(junction_mesh)}")
    print(f"[-] ARVT-04 Core Node Balance Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['structural_phase']}")
    print(f"    ↳ Nozzle A Vector Node:     {audit_sample['nozzle_a_vector']}")
    print(f"    ↳ Nozzle B Vector Node:     {audit_sample['nozzle_b_vector']}")
    print("=" * 65)

if __name__ == "__main__":
    main()
      

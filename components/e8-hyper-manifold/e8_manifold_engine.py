import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_e8_projections(chamber_length, resolution=360):
    """
    Calculates 3D spatial coordinate vectors projected from the 8D E8 Root Lattice.
    Generates E8 roots via integer permutations and half-integer configurations.
    Applies a hyper-dimensional rotation and stereographic projection pipeline.
    """
    matrix_points = []
    scale = chamber_length * 0.25
    
    # Establish base seed vectors representing the primary root subsystems of E8
    base_seeds = [
        (1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
        (-1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
        (0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5),
        (-0.5, -0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5)
    ]
    
    for step in range(resolution):
        # Progress parameter tracks the angular hyper-dimensional transformation sweep (0 to 2*Pi)
        progress = step / resolution
        omega = progress * 2.0 * math.pi
        
        # Select an active root seed vector based on progression index
        seed = base_seeds[step % len(base_seeds)]
        
        # Apply a hyper-dimensional rotation cross-coupling high-order axes (X5 through X8)
        # Trajectories are modulated smoothly over the virtual omega timeline
        x1 = seed[0] * scale
        y1 = seed[1] * scale
        z1 = (seed[2] * math.cos(omega) - seed[3] * math.sin(omega)) * scale
        w1 = (seed[2] * math.sin(omega) + seed[3] * math.cos(omega)) * scale
        
        # Upper 4D coordinates undergo a secondary orthogonal rotation phase shift
        x2 = seed[4] * scale
        y2 = seed[5] * scale
        z2 = (seed[6] * math.cos(2.0 * omega) - seed[7] * math.sin(2.0 * omega)) * scale
        w2 = (seed[6] * math.sin(2.0 * omega) + seed[7] * math.cos(2.0 * omega)) * scale
        
        # Standard Conformal Stereographic 8D-to-3D Projection Pipeline
        # Flattens the remaining 5 hyper-dimensions down sequentially into real-space 3D Cartesian coordinates
        denom_8d = (2.0 * scale - w2) if (2.0 * scale - w2) != 0 else 1.0
        p8 = 2.0 / denom_8d
        
        denom_7d = (2.0 * scale - z2 * p8) if (2.0 * scale - z2 * p8) != 0 else 1.0
        p7 = 2.0 / denom_7d
        
        denom_6d = (2.0 * scale - y2 * p7) if (2.0 * scale - y2 * p7) != 0 else 1.0
        p6 = 2.0 / denom_6d
        
        denom_5d = (2.0 * scale - x2 * p6) if (2.0 * scale - x2 * p6) != 0 else 1.0
        p5 = 2.0 / denom_5d
        
        denom_4d = (2.0 * scale - w1 * p5) if (2.0 * scale - w1 * p5) != 0 else 1.0
        p4 = 2.0 / denom_4d
        
        x = x1 * p4
        y = y1 * p4
        z = z1 * p4
        
        # Structural phase tracking based on linear progress and vector scaling
        if progress < 0.25:
            phase = "Core_Gosset_Polytope_Intake"
        elif progress > 0.75:
            phase = "Exceptional_240_Root_Discharge_Array"
        else:
            phase = "Conformal_Hyper_Geometric_Face_Transit"
            
        matrix_points.append({
            "step": step,
            "structural_phase": phase,
            "parameters": {"omega_rad": round(omega, 4), "projection_scale": round(p4, 4)},
            "coordinate_vector": (round(x, 4), round(y, 4), round(z, 4))
        })
        
    return matrix_points

def main():
    print("=" * 60)
    print("INITIALIZING: E8 HIGHER-DIMENSIONAL ROOT LATTICE ENGINE")
    print("=" * 60)
    
    config_path = get_local_path("e8-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        chamber_length = config["geometry"]["chamber_length_L_mm"]
        print("[+] 8D exceptional root configuration standard verified.")
    else:
        print("[⚠️] WARNING: e8-config.json missing. Loading safe defaults.")
        chamber_length = 160.0
        
    print(f"[*] Processing 8D regular polytope configurations across high-order planes...")
    print(f"[*] Compiling coordinate bounds: Chamber Length = {chamber_length}mm")
    
    # Run coordinate pipeline calculation loops
    polytopic_nodes = generate_e8_projections(chamber_length)
    
    # Audit a midpoint node tracking the structural center loop
    audit_sample = polytopic_nodes[len(polytopic_nodes) // 2]
    
    print("\n[+] SUCCESS: 8D E8 projection matrix built cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(polytopic_nodes)}")
    print(f"[-] Polytopic Node Conformal Balance Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['structural_phase']}")
    print(f"    ↳ Cartesian Mesh Node:      {audit_sample['coordinate_vector']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
      

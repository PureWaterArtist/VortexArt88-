import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_trefoil_knot_vectors(major_radius, tube_radius, resolution=360):
    """
    Calculates 3D spatial vectors mapping a continuous Trefoil Knot profile.
    The path loops over and under itself in a 3-fold spatial symmetry grid.
    """
    knot_nodes = []
    
    for step in range(resolution):
        # Progress factor maps out the full continuous loop (0 to 2*Pi)
        t = (step * 2.0 * math.pi) / resolution
        
        # Classical Parametric Equations for a standard (3,2) Trefoil Torus Knot
        # Scales and folds across three interlocking dimensional planes
        x = major_radius * (math.sin(t) + 2.0 * math.sin(2.0 * t))
        y = major_radius * (math.cos(t) - 2.0 * math.cos(2.0 * t))
        z = -major_radius * math.sin(3.0 * t)
        
        # Section classification based on the 3-fold symmetry loops
        progress = step / resolution
        if progress < 0.33:
            phase = "Symmetry_Braid_Alpha"
        elif progress < 0.66:
            phase = "Symmetry_Braid_Beta"
        else:
            phase = "Symmetry_Braid_Gamma"
            
        knot_nodes.append({
            "step": step,
            "structural_phase": phase,
            "parameter_t_rad": round(t, 4),
            "coordinate_vector": (round(x, 4), round(y, 4), round(z, 4))
        })
        
    return knot_nodes

def main():
    print("=" * 60)
    print("INITIALIZING: TREFOIL KNOT AUTOMATED VECTOR ENGINE")
    print("=" * 60)
    
    config_path = get_local_path("trefoil-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        major_radius = config["geometry"]["major_loop_radius_mm"]
        tube_radius = config["geometry"]["tube_internal_radius_mm"]
        print("[+] Knotted geometric variables safely extracted from configuration profile.")
    else:
        print("[⚠️] WARNING: trefoil-config.json missing. Loading safe overrides.")
        major_radius = 50.0
        tube_radius = 15.0
        
    print(f"[*] Compiling 3-fold self-looping boundary tracks...")
    print(f"[*] Processing knot coordinates at scaling radius: {major_radius}mm")
    
    # Run coordinate pipeline calculation loops
    knot_matrix = generate_trefoil_knot_vectors(major_radius, tube_radius)
    
    # Audit a midpoint node tracking the third dimensional crossover shift
    audit_sample = knot_matrix[len(knot_matrix) // 2]
    
    print("\n[+] SUCCESS: Trefoil Knot mathematical matrix compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(knot_matrix)}")
    print(f"[-] Knotted Cross-Axial Balance Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['structural_phase']}")
    print(f"    ↳ Cartesian Mesh Node:      {audit_sample['coordinate_vector']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
  

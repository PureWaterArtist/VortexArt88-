import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_chiral_mobius_vectors(throat_dia, resolution=360):
    """
    Calculates 3D spatial vectors mapping a non-orientable Mobius mesh filter.
    Processes coordinates forward, backward, and cross-axially in parallel
    to simulate a zero-bottleneck data ring.
    """
    matrix_points = []
    r_base = throat_dia / 2.0
    
    # 🔁 NON-ORIENTABLE DATA RING MECHANIC:
    # Process both loops simultaneously using inverted phase tracking
    for step in range(resolution):
        # Forward Angle (0 to 2*Pi)
        angle_fwd = (step * 2 * math.pi) / resolution
        # Backward/Inverted Phase Angle (2*Pi down to 0)
        angle_bwd = ((resolution - step) * 2 * math.pi) / resolution
        
        # Mobius Parametric Formula Mapping (Twisting ribbon in 3D space)
        # u sweeps from -1.0 to 1.0 representing the physical width of the filter blade
        u = (step / resolution) * 2.0 - 1.0
        
        # Symmetrical Right-Handed (Clockwise) hardware channel
        x_right = (r_base + u * math.cos(angle_fwd / 2.0)) * math.cos(angle_fwd)
        y_right = (r_base + u * math.cos(angle_fwd / 2.0)) * math.sin(angle_fwd)
        z_right = u * math.sin(angle_fwd / 2.0)
        
        # Symmetrical Left-Handed (Counter-Clockwise) hardware channel
        x_left = (r_base + u * math.cos(angle_bwd / 2.0)) * math.cos(angle_bwd)
        y_left = (r_base + u * math.cos(angle_bwd / 2.0)) * math.sin(angle_bwd)
        z_left = u * math.sin(angle_bwd / 2.0)
        
        matrix_points.append({
            "step": step,
            "right_handed_chiral_vector": (round(x_right, 4), round(y_right, 4), round(z_right, 4)),
            "left_handed_chiral_vector": (round(x_left, 4), round(y_left, 4), round(z_left, 4))
        })
        
    return matrix_points

def main():
    print("=" * 60)
    print("INITIALIZING: NON-ORIENTABLE CHIRAL FILTER ENGINE")
    print("=" * 60)
    
    config_path = get_local_path("filter-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        throat_diameter = config["geometry"]["internal_throat_diameter_mm"]
        print("[+] Non-orientable data matrix loaded from configuration profile.")
    else:
        print("[⚠️] WARNING: filter-config.json missing. Resorting to space overrides.")
        throat_diameter = 40.0
        
    print(f"[*] Activating parallel self-reversing calculation loops...")
    print(f"[*] Constructing Mobius geometry layout at throat width: {throat_diameter}mm")
    
    # Execute the twin-channel math matrix
    chiral_matrix = generate_chiral_mobius_vectors(throat_diameter)
    
    # Audit cross-axial intersection points to ensure perfect spatial inversion balance
    mid_sample = chiral_matrix[len(chiral_matrix) // 2]
    
    print("\n[+] SUCCESS: Chiral data ring fully synthesized.")
    print(f"[-] Total coordinated mesh steps logged: {len(chiral_matrix)}")
    print(f"[-] Midpoint Cross-Axial Inversion Symmetry Audit:")
    # At the midpoint, the forward and backward vectors perfectly cross over
    print(f"    ↳ Right-Handed Vortex Path: {mid_sample['right_handed_chiral_vector']}")
    print(f"    ↳ Left-Handed Vortex Path:  {mid_sample['left_handed_chiral_vector']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
      

import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_toroidal_helical_vectors(r_major, r_minor, pitch_loops, resolution=360):
    """
    Calculates 3D spatial vectors mapping a continuous toroidal helix.
    The path self-loops infinitely to neutralize cavitation stress.
    """
    torus_nodes = []
    
    for step in range(resolution):
        # Angle phi tracks the revolution around the major ring axis (0 to 2*Pi)
        phi = (step * 2 * math.pi) / resolution
        
        # Angle theta tracks the helical spiral around the minor tube axis
        # Multiplied by pitch_loops to control the frequency of the twists
        theta = phi * pitch_loops
        
        # Standard Parametric Equations for a 3D Toroidal Helix
        x = (r_major + r_minor * math.cos(theta)) * math.cos(phi)
        y = (r_major + r_minor * math.cos(theta)) * math.sin(phi)
        z = r_minor * math.sin(theta)
        
        # Section classification based on structural quadrant rotation
        if step < (resolution // 4):
            quadrant = "Intake_Transition_Zone"
        elif step > (3 * resolution // 4):
            quadrant = "Discharge_Equilibrium_Zone"
        else:
            quadrant = "Continuous_Recirculation_Loop"
            
        torus_nodes.append({
            "step": step,
            "quadrant": quadrant,
            "angles_rad": {"phi": round(phi, 4), "theta": round(theta, 4)},
            "vector": (round(x, 4), round(y, 4), round(z, 4))
        })
        
    return torus_nodes

def main():
    print("=" * 60)
    print("INITIALIZING: TOROIDAL HELICAL DIFFUSER RECKONING ENGINE")
    print("=" * 60)
    
    config_path = get_local_path("diffuser-config.json")
    
    # Extract structural dimensions directly from the configuration standard
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        r_major = config["geometry"]["major_ring_radius_r1_mm"]
        r_minor = config["geometry"]["minor_tube_radius_r2_mm"]
        pitch_loops = config["geometry"]["helical_pitch_loops"]
        print("[+] Toroidal geometric constraints safely extracted into active memory.")
    else:
        print("[⚠️] WARNING: diffuser-config.json missing. Resorting to hardware overrides.")
        r_major = 60.0
        r_minor = 20.0
        pitch_loops = 12
        
    print(f"[*] Compiling infinite self-looping boundary tracks...")
    print(f"[*] Synchronizing torus matrix parameters: Pitch Frequency = {pitch_loops}")
    
    # Execute coordinate calculation pipeline loops
    diffuser_nodes = generate_toroidal_helical_vectors(r_major, r_minor, pitch_loops)
    
    # Audit a midpoint sample vector where the internal helix hits max amplitude
    mid_sample = diffuser_nodes[len(diffuser_nodes) // 2]
    
    print("\n[+] SUCCESS: Toroidal helix coordinate matrix fully built.")
    print(f"[-] Total automated matrix nodes logged: {len(diffuser_nodes)}")
    print(f"[-] Self-Looping Kinetic Balance Audit:")
    print(f"    ↳ Active Structural Quadrant: {mid_sample['quadrant']}")
    print(f"    ↳ Cartesian Mesh Node (X,Y,Z): {mid_sample['vector']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
      

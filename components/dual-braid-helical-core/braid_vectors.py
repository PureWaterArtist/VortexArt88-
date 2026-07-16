import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_double_helix_vectors(core_dia, env_dia, pitch, total_length, resolution=360):
    """
    Calculates 3D spatial vectors mapping a synchronous, interlocking 
    double-helix track around a central core profile.
    """
    braid_nodes = []
    
    # Helix radius is the center distance from core to outer shell envelope
    r_helix = (core_dia + (env_dia - core_dia) / 2.0) / 2.0
    
    for step in range(resolution):
        # Progress factor along the linear vertical axis (Z)
        progress = step / resolution
        z_axis = progress * total_length
        
        # Calculate the rotational angle based on pitch and length
        total_turns = total_length / pitch
        theta_alpha = progress * total_turns * 2 * math.pi
        
        # Strand Beta is offset by exactly 180 degrees (Pi radians) to remain interlocking
        theta_beta = theta_alpha + math.pi
        
        # Strand Alpha parametric mapping (Clockwise spiral)
        x_alpha = r_helix * math.cos(theta_alpha)
        y_alpha = r_helix * math.sin(theta_alpha)
        
        # Strand Beta parametric mapping (Parallel interlocking spiral)
        x_beta = r_helix * math.cos(theta_beta)
        y_beta = r_helix * math.sin(theta_beta)
        
        # Section classification based on vertical progression
        if progress < 0.15:
            phase = "Intake_Braiding_Zone"
        elif progress > 0.85:
            phase = "Discharge_Manifold_Exit"
        else:
            phase = "Interlocked_Helix_Core"
            
        braid_nodes.append({
            "step": step,
            "structural_phase": phase,
            "z_height_mm": round(z_axis, 4),
            "strand_alpha_vector": (round(x_alpha, 4), round(y_alpha, 4), round(z_axis, 4)),
            "strand_beta_vector": (round(x_beta, 4), round(y_beta, 4), round(z_axis, 4))
        })
        
    return braid_nodes

def main():
    print("=" * 60)
    print("INITIALIZING: DUAL-BRAID HELICAL COUPLING ENGINE")
    print("=" * 60)
    
    config_path = get_local_path("core-config.json")
    
    # Extract structural dimensions directly from the configuration standard
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        core_diameter = config["geometry"]["core_diameter_mm"]
        envelope_diameter = config["geometry"]["outer_envelope_diameter_mm"]
        helical_pitch = config["geometry"]["helical_pitch_mm"]
        total_length = config["geometry"]["total_axial_length_mm"]
        print("[+] Double-helix variables safely extracted from local metadata.")
    else:
        print("[⚠️] WARNING: core-config.json missing. Loading fallback defaults.")
        core_diameter = 30.0
        envelope_diameter = 54.0
        helical_pitch = 50.0
        total_length = 150.0
        
    print(f"[*] Compiling intertwined synchronous vector tracks...")
    print(f"[*] Processing helical tracks at pitch frequency: {helical_pitch}mm")
    
    # Run coordinate calculation loops
    helix_nodes = generate_double_helix_vectors(core_diameter, envelope_diameter, helical_pitch, total_length)
    
    # Audit a midpoint node tracking the twin-strand offset symmetry
    audit_sample = helix_nodes[len(helix_nodes) // 2]
    
    print("\n[+] SUCCESS: Double-helix coordinate matrix fully built.")
    print(f"[-] Total automated matrix points logged: {len(helix_nodes)}")
    print(f"[-] Synchronous Braid Offset Symmetry Audit:")
    print(f"    ↳ Active Structural Phase: {audit_sample['structural_phase']}")
    print(f"    ↳ Strand Alpha Coordinates: {audit_sample['strand_alpha_vector']}")
    print(f"    ↳ Strand Beta Coordinates:  {audit_sample['strand_beta_vector']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
  

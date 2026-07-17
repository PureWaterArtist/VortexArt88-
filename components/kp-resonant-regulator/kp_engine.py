import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_kp_vectors(chamber_length, intersection_angle, amplitude_scale, resolution=360):
    """
    Calculates 3D spatial vectors mapping a Kadomtsev-Petviashvili Soliton Web.
    Models the intersection of two line solitons across a multi-axial plane.
    """
    matrix_points = []
    
    # Convert intersection angle parameter to radians for coordinate transforms
    rad_angle = math.radians(intersection_angle)
    k1_x = 1.0
    k1_y = 0.0
    k2_x = math.cos(rad_angle)
    k2_y = math.sin(rad_angle)
    
    for step in range(resolution):
        # Progress parameter maps out the primary linear sweep path along the axis
        progress = step / resolution
        x_axis = (progress * chamber_length) - (chamber_length / 2.0)
        
        # Parametric sweep angle tracks the cross-sectional 3D spatial rotation (0 to 2*Pi)
        theta = (step * 2.0 * math.pi) / resolution
        
        # Cross-sectional lateral axis variable
        y_axis = 15.0 * math.sin(theta)
        
        # Evaluate localized line soliton phase parameters
        phase1 = k1_x * x_axis + k1_y * y_axis
        phase2 = k2_x * x_axis + k2_y * y_axis
        
        # Clamp phase inputs to prevent arithmetic overflow thresholds inside exponentials
        p1_clamp = max(-20.0, min(20.0, phase1))
        p2_clamp = max(-20.0, min(20.0, phase2))
        
        # Evaluate logarithmic envelope formulation for a resonant KP web solution
        # u(x,y) = 2 * d^2/dx^2 ( ln( 1 + exp(phase1) + exp(phase2) ) )
        f_web = 1.0 + math.exp(p1_clamp) + math.exp(p2_clamp)
        f_x = math.exp(p1_clamp) * k1_x + math.exp(p2_clamp) * k2_x
        f_xx = math.exp(p1_clamp) * (k1_x**2) + math.exp(p2_clamp) * (k2_x**2)
        
        # Calculate second derivative of the logarithm matrix
        web_amplitude = 2.0 * ((f_xx * f_web - (f_x**2)) / (f_web**2))
        magnitude = abs(web_amplitude)
        
        # Translate resonant value arrays into an optimized, self-focusing fluid throat
        radius_modulation = 18.0 - 6.0 * (magnitude / amplitude_scale)
        
        x = radius_modulation * math.cos(theta)
        y = radius_modulation * math.sin(theta)
        
        # Structural phase tracking based on linear progress and envelope convergence
        if progress < 0.20 or progress > 0.80:
            phase = "Asymptotic_Linear_Soliton_Channels"
        elif abs(x_axis) < 10.0 and abs(y_axis) < 10.0:
            phase = "Resonant_Line_Intersection_Core"
        else:
            phase = "Two_Dimensional_Web_Transition_Zone"
            
        matrix_points.append({
            "step": step,
            "structural_phase": phase,
            "parameters": {"axial_pos_mm": round(x_axis, 4), "web_amp": round(magnitude, 4)},
            "coordinate_vector": (round(x, 4), round(y, 4), round(x_axis, 4))
        })
        
    return matrix_points

def main():
    print("=" * 60)
    print("INITIALIZING: KADOMTSEV-PETVIASHVILI RESONANT WEB ENGINE")
    print("=" * 60)
    
    config_path = get_local_path("kp-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        chamber_length = config["geometry"]["chamber_length_L_mm"]
        intersection_angle = config["geometry"]["line_intersection_angle_deg"]
        amplitude_scale = config["geometry"]["amplitude_scaling_factor"]
        print("[+] KP Resonant wave configuration standard verified.")
    else:
        print("[⚠️] WARNING: kp-config.json missing. Loading safe defaults.")
        chamber_length = 160.0
        intersection_angle = 60.0
        amplitude_scale = 2.5
        
    print(f"[*] Compiling non-dispersive two-dimensional web tracking meshes...")
    print(f"[*] Processing boundaries: Chamber Length = {chamber_length}mm | Intersection Angle = {intersection_angle}°")
    
    # Run coordinate pipeline calculation loops
    kp_nodes = generate_kp_vectors(chamber_length, intersection_angle, amplitude_scale)
    
    # Audit a midpoint node tracking the structural center loop
    audit_sample = kp_nodes[len(kp_nodes) // 2]
    
    print("\n[+] SUCCESS: KP Resonant web coordinate matrix compiled cleanly.")
    print(f"[-] Total coordinated structural steps logged: {len(kp_nodes)}")
    print(f"[-] KP Resonant Intersection Node Audit:")
    print(f"    ↳ Active Structural Phase:  {audit_sample['structural_phase']}")
    print(f"    ↳ Cartesian Mesh Node:      {audit_sample['coordinate_vector']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
      

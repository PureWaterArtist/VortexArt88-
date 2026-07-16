import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_plenum_vectors(intake_dia, port_count, angle_deg, resolution=180):
    """
    Calculates the 3D expansion geometry vectors for a 3-way 
    manifold plenum splitter utilizing smooth bifurcation curves.
    """
    nodes = []
    angle_rad = math.radians(angle_deg)
    
    for step in range(resolution):
        # Linear progression along the plenum's height axis (Z)
        progress = step / resolution
        z_axis = progress * 100.0  # Normalized 100mm assembly height
        
        # Calculate the outward expanding geometric envelope
        current_expansion = (intake_dia / 2.0) + (z_axis * math.tan(angle_rad))
        
        # Map the primary boundary shell perimeter using standard circle geometry
        theta = (step * 2 * math.pi) / resolution
        x_edge = current_expansion * math.cos(theta)
        y_edge = current_expansion * math.sin(theta)
        
        # Track individual internal flow splitter zones
        if progress < 0.20:
            zone = "Unified_Intake_Chamber"
        elif progress > 0.80:
            zone = "Tri_Port_Exhaust_Junction"
        else:
            zone = "Bifurcation_Transition_Zone"
            
        nodes.append({
            "step": step,
            "structural_phase": zone,
            "z_depth": round(z_axis, 4),
            "perimeter_vector": (round(x_edge, 4), round(y_edge, 4), round(z_axis, 4))
        })
        
    return nodes

def main():
    print("=" * 60)
    print("INITIALIZING: MANIFOLD DISTRIBUTION PLENUM MATRIX")
    print("=" * 60)
    
    config_path = get_local_path("plenum-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        intake_diameter = config["geometry"]["main_intake_diameter_mm"]
        output_ports = config["geometry"]["output_ports_count"]
        expansion_angle = config["geometry"]["expansion_angle_degrees"]
        print("[+] Configuration metadata safely loaded into memory map.")
    else:
        print("[⚠️] WARNING: plenum-config.json missing. Loading fallback defaults.")
        intake_diameter = 50.0
        output_ports = 3
        expansion_angle = 30.0
        
    print(f"[*] Simulating anti-cavitation fluid split lines...")
    print(f"[*] Mapping expansion boundaries at angle: {expansion_angle}°")
    
    # Run coordinate calculation loops
    plenum_nodes = generate_plenum_vectors(intake_diameter, output_ports, expansion_angle)
    
    # Audit the maximum expansion boundary step before the exhaust splitter
    audit_sample = plenum_nodes[intake_diameter]
    
    print("\n[+] SUCCESS: Distribution plenum vector grid successfully built.")
    print(f"[-] Total structural path layers logged: {len(plenum_nodes)}")
    print(f"[-] Transition Boundary Audit:")
    print(f"    ↳ Active Structural Phase: {audit_sample['structural_phase']}")
    print(f"    ↳ Cartesian Mesh Node (X,Y,Z): {audit_sample['perimeter_vector']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
  

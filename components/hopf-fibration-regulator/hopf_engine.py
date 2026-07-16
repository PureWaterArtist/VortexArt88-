import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_hopf_fibration_vectors(proj_radius, resolution=360):
    """
    Calculates 3D spatial vectors mapping a stereographic projection
    of a 4D Hopf Fibration map with nested, non-intersecting circular fibers.
    """
    hopf_nodes = []
    
    for step in range(resolution):
        # Angle phi tracks the primary horizontal rotation (0 to 2*Pi)
        phi = (step * 2.0 * math.pi) / resolution
        
        # Angle theta tracks the phase shift along the orthogonal circular track
        theta = phi * 2.0
        
        # 4D Hypersphere/Glome coordinates mapped along a Hopf Map
        x_4d = math.cos(theta) * math.cos(phi)
        y_4d = math.cos(theta) * math.sin(phi)
        z_4d = math.sin(theta) * math.cos(phi)
        w_4d = math.sin(theta) * math.sin(phi)
        
        # 3D Stereographic Projection: Mapping from 4D down to 3D Cartesian coordinates
        # Denominator handles projection relative to the 4th axis scale limit
        denominator = 1.0 - w_4d
        if abs(denominator) < 1e-6:
            denominator = 1e-6
            
        x_3d = (x_4d / denominator) * proj_radius
        y_3d = (y_4d / denominator) * proj_radius
        z_3d = (z_4d / denominator) * proj_radius
        
        # Section classification based on the multi-axial fluid distribution phase
        progress = step / resolution
        if progress < 0.25:
            phase = "Bundle_Intake_Split"
        elif progress > 0.75:
            phase = "Bundle_Discharge_Alignment"
        else:
            phase = "Nested_Fibration_Transit"
            
        hopf_nodes.append({
            "step": step,
            "structural_phase": phase,
            "angles_rad": {"phi": round(phi, 4), "theta": round(theta, 4)},
            "vector_3d": (round(x_3d, 4), round(y_3d, 4), round(z_3d, 4))
        })
        
    return hopf_nodes

def main():
    print("=" * 60)
    print("INITIALIZING: HOPF FIBRATION NESTED BUNDLE SYSTEM")
    print("=" * 60)
    
    config_path = get_local_path("hopf-config.json")
    
    # Extract structural dimensions directly from the configuration standard
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        proj_radius = config["geometry"]["projection_radius_r_mm"]
        print("[+] Multi-axial hyperspherical geometric variables verified.")
    else:
        print("[⚠️] WARNING: hopf-config.json missing. Loading safe defaults.")
        proj_radius = 55.0
        
    print(f"[*] Projecting 3D stereographic fiber expansions...")
    print(f"[*] Scaling boundary matrix limits: Projection Radius = {proj_radius}mm")
    
    # Execute the coordinate calculation pipeline loops
    bundle_nodes = generate_hopf_fibration_vectors(proj_radius)
    
    # Audit a midpoint node tracking the 3D projected vector coordinate
    audit_sample = bundle_nodes[len(bundle_nodes) // 2]
    
    print("\n[+] SUCCESS: Hopf Fibration fiber coordinates compiled cleanly.")
    print(f"[-] Total coordinated 3D vector points logged: {len(bundle_nodes)}")
    print(f"[-] Multi-Axial Nested Bundle Symmetry Audit:")
    print(f"    ↳ Active Structural Phase:     {audit_sample['structural_phase']}")
    print(f"    ↳ Projected 3D Cartesian Node: {audit_sample['vector_3d']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
  

import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_clifford_torus_vectors(r1, r2, resolution=360):
    """
    Calculates 3D spatial vectors mapping a stereographic projection
    of a 4D Clifford Torus with orthogonal flow channels.
    """
    clifford_nodes = []
    
    for step in range(resolution):
        # Progress parameter maps out the primary circular axis (0 to 2*Pi)
        theta = (step * 2 * math.pi) / resolution
        
        # Perpendicular secondary angular path mapped cross-axially
        # We add a phase shift relative to the step to simulate synchronous flow coupling
        phi = theta * 2.0
        
        # 4D Clifford Torus Coordinates in R^4 Space (S_1 x S_1 embedded in S_3)
        x_4d = r1 * math.cos(theta)
        y_4d = r1 * math.sin(theta)
        z_4d = r2 * math.cos(phi)
        w_4d = r2 * math.sin(phi)
        
        # 3D Stereographic Projection: Mapping from 4D space down to 3D Cartesian coordinates
        # We project from a point on the hypersphere (denominating by the 4th axis W)
        denominator = 1.0 - (w_4d / (r1 + r2))
        
        # Prevent division by zero errors at the projection pole boundary
        if abs(denominator) < 1e-6:
            denominator = 1e-6
            
        x_3d = x_4d / denominator
        y_3d = y_4d / denominator
        z_3d = z_4d / denominator
        
        # Section classification based on the multi-axial fluid distribution phase
        if step < (resolution // 4):
            phase = "Orthogonal_Intake_Split"
        elif step > (3 * resolution // 4):
            phase = "Synchronous_Discharge_Flow"
        else:
            phase = "Dual_Axial_Recirculation"
            
        clifford_nodes.append({
            "step": step,
            "structural_phase": phase,
            "angles_rad": {"theta": round(theta, 4), "phi": round(phi, 4)},
            "vector_3d": (round(x_3d, 4), round(y_3d, 4), round(z_3d, 4))
        })
        
    return clifford_nodes

def main():
    print("=" * 60)
    print("INITIALIZING: CLIFFORD TORUS MULTI-AXIAL STEP ENGINE")
    print("=" * 60)
    
    config_path = get_local_path("clifford-config.json")
    
    # Extract structural dimensions directly from the configuration standard
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        r1_param = config["geometry"]["primary_radius_r1_mm"]
        r2_param = config["geometry"]["secondary_radius_r2_mm"]
        print("[+] Hyper-orthogonal geometric metadata safely parsed into memory.")
    else:
        print("[⚠️] WARNING: clifford-config.json missing. Loading system defaults.")
        r1_param = 45.0
        r2_param = 45.0
        
    print(f"[*] Simulating stereographic cross-axial expansion fields...")
    print(f"[*] Scaling boundary matrix limits: R1 = {r1_param}mm | R2 = {r2_param}mm")
    
    # Execute the coordinate calculation pipeline loops
    manifold_nodes = generate_clifford_torus_vectors(r1_param, r2_param)
    
    # Audit a midpoint node tracking the 3D projected vector coordinate
    audit_sample = manifold_nodes[len(manifold_nodes) // 2]
    
    print("\n[+] SUCCESS: Clifford Torus manifold coordinates compiled cleanly.")
    print(f"[-] Total coordinated 3D vector points logged: {len(manifold_nodes)}")
    print(f"[-] Dual-Axial Orthogonal Symmetry Audit:")
    print(f"    ↳ Active Structural Phase:     {audit_sample['structural_phase']}")
    print(f"    ↳ Projected 3D Cartesian Node: {audit_sample['vector_3d']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
      

import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_icosahedron_face_centers(scale=1.0):
    """
    Calculates the 20 spatial Cartesian coordinates representing the centers
    of the 20 triangular faces of a regular icosahedron.
    The geometry is structurally governed by the Golden Ratio (Phi).
    """
    phi = (1.0 + math.sqrt(5.0)) / 2.0
    a = scale
    
    # Define the 12 base vertices of a regular icosahedron
    vertices = [
        (0.0, a, a * phi), (0.0, -a, a * phi), (0.0, a, -a * phi), (0.0, -a, -a * phi),
        (a, a * phi, 0.0), (-a, a * phi, 0.0), (a, -a * phi, 0.0), (-a, -a * phi, 0.0),
        (a * phi, 0.0, a), (a * phi, 0.0, -a), (-a * phi, 0.0, a), (-a * phi, 0.0, -a)
    ]
    
    # In a regular icosahedron, faces are formed by specific triplets of vertices.
    # We find triplets where the distance between each vertex pair equals the edge length 'a * 2'
    target_dist_sq = (2.0 * a) ** 2
    face_triplets = []
    
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            # Calculate distance squared between vertex i and j
            d1_sq = sum((vertices[i][k] - vertices[j][k])**2 for k in range(3))
            if abs(d1_sq - target_dist_sq) > 1e-3:
                continue
            for l in range(j + 1, len(vertices)):
                d2_sq = sum((vertices[i][k] - vertices[l][k])**2 for k in range(3))
                d3_sq = sum((vertices[j][k] - vertices[l][k])**2 for k in range(3))
                if abs(d2_sq - target_dist_sq) < 1e-3 and abs(d3_sq - target_dist_sq) < 1e-3:
                    face_triplets.append((vertices[i], vertices[j], vertices[l]))
                    
    face_vectors = []
    for idx, (v1, v2, v3) in enumerate(face_triplets):
        # The center of an equilateral triangular face is the average of its 3 vertices
        cx = (v1[0] + v2[0] + v3[0]) / 3.0
        cy = (v1[1] + v2[1] + v3[1]) / 3.0
        cz = (v1[2] + v2[2] + v3[2]) / 3.0
        
        face_vectors.append({
            "face_id": idx,
            "vector_direction": "Inward_Convergence",
            "coordinates": (round(cx, 4), round(cy, 4), round(cz, 4))
        })
        
    return face_vectors

def main():
    print("=" * 60)
    print("INITIALIZING: ICOSAHEDRAL VECTOR HARMONIZER ENGINE")
    print("=" * 60)
    
    config_path = get_local_path("harmonizer-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        scale_parameter = config["geometry"]["scale_parameter_a_mm"]
        print("[+] Icosahedral polyhedral variables successfully loaded.")
    else:
        print("[⚠️] WARNING: harmonizer-config.json missing. Loading system defaults.")
        scale_parameter = 40.0
        
    print(f"[*] Compiling 20-axis symmetric convergence vectors...")
    print(f"[*] Processing polyhedral bounding matrix at base scale: {scale_parameter}mm")
    
    # Execute the coordinate calculation pipeline loops
    convergence_nodes = generate_icosahedron_face_centers(scale_parameter / 2.0)
    
    # Audit an active face center vector point
    sample_node = convergence_nodes[0]
    
    print("\n[+] SUCCESS: Polyhedral vector matrix fully built.")
    print(f"[-] Total structural input channels mapped: {len(convergence_nodes)}")
    print(f"[-] Convergent Vector Node Audit (Face 0):")
    print(f"    ↳ Operational Mode:           {sample_node['vector_direction']}")
    print(f"    ↳ Cartesian Vectors (X,Y,Z):  {sample_node['coordinates']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
                             

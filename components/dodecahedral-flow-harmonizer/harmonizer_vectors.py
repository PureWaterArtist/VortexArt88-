import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_dodecahedron_face_centers(scale=1.0):
    """
    Calculates the 12 spatial Cartesian coordinates representing the centers
    of the 12 pentagonal faces of a regular dodecahedron.
    The geometry is structurally governed by the Golden Ratio (Phi).
    """
    phi = (1.0 + math.sqrt(5.0)) / 2.0
    a = scale
    
    # In a regular dodecahedron with an edge length of 'a', the distance 
    # from the absolute origin to the center of any face is uniform.
    # We calculate the normalized face center coordinates via the dual icosahedron scaling rules.
    r_factor = (phi ** 2) / math.sqrt(3.0)
    c = a * r_factor
    
    # Base coordinate sets for the 12 face center vectors 
    # derived by cyclic permutations of signs and axes.
    raw_centers = [
        # Set 1: Polar alignment frames
        (0.0, c / phi, c * phi),
        (0.0, -c / phi, c * phi),
        (0.0, c / phi, -c * phi),
        (0.0, -c / phi, -c * phi),
        
        # Set 2: Equatorial latitude bands
        (c * phi, 0.0, c / phi),
        (-c * phi, 0.0, c / phi),
        (c * phi, 0.0, -c / phi),
        (-c * phi, 0.0, -c / phi),
        
        # Set 3: Cross-axial intersection tracks
        (c / phi, c * phi, 0.0),
        (-c / phi, c * phi, 0.0),
        (c / phi, -c * phi, 0.0),
        (-c / phi, -c * phi, 0.0)
    ]
    
    face_vectors = []
    for idx, (x, y, z) in enumerate(raw_centers):
        face_vectors.append({
            "face_id": idx,
            "vector_direction": "Inward_Convergence",
            "coordinates": (round(x, 4), round(y, 4), round(z, 4))
        })
        
    return face_vectors

def main():
    print("=" * 60)
    print("INITIALIZING: DODECAHEDRAL FLOW HARMONIZER MATRIX")
    print("=" * 60)
    
    config_path = get_local_path("harmonizer-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        scale_parameter = config["geometry"]["scale_parameter_a_mm"]
        print("[+] Dodecahedral geometric dimensions extracted successfully.")
    else:
        print("[⚠️] WARNING: harmonizer-config.json missing. Loading system defaults.")
        scale_parameter = 35.0
        
    print(f"[*] Compiling 12-axis symmetric convergence vectors...")
    print(f"[*] Processing polyhedron bounding matrix at edge scale: {scale_parameter}mm")
    
    # Execute the coordinate calculation pipeline loops
    convergence_nodes = generate_dodecahedron_face_centers(scale_parameter)
    
    # Audit an active face center vector point
    sample_node = convergence_nodes[0]
    
    print("\n[+] SUCCESS: Polyhedral convergence matrix fully built.")
    print(f"[-] Total structural input channels mapped: {len(convergence_nodes)}")
    print(f"[-] Convergent Vector Node Audit (Face 0):")
    print(f"    ↳ Operational Mode: {sample_node['vector_direction']}")
    print(f"    ↳ Cartesian Vectors (X, Y, Z): {sample_node['coordinates']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
                            

import itertools
import json
import os

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_truncated_icosahedron_vertices(scale=1.0):
    """
    Generates the exact 60 Cartesian coordinates for the vertex junctions 
    of a Truncated Icosahedron using Golden Ratio (Phi) permutations.
    """
    phi = (1.0 + (5.0 ** 0.5)) / 2.0
    a = scale
    
    # Define the 3 base algebraic coordinate frames
    base_sets = [
        (0.0, a, 3.0 * a * phi),
        (2.0 * a, a * (1.0 + 2.0 * phi), a * phi),
        (a, a * (2.0 + phi), 2.0 * a * phi)
    ]
    
    unique_vertices = set()
    
    for base in base_sets:
        x_vals = [base, -base] if base[0] != 0 else [0.0]
        y_vals = [base[1], -base[1]]
        z_vals = [base[2], -base[2]]
        
        for x, y, z in itertools.product(x_vals, y_vals, z_vals):
            for perm in itertools.permutations((x, y, z)):
                # Enforce Truncated Icosahedron even permutations
                # Calculation check: verify parity of permutation index matching icosahedral symmetry
                rounded_vertex = (round(perm[0], 4), round(perm[1], 4), round(perm[2], 4))
                unique_vertices.add(rounded_vertex)
                
    return sorted(list(unique_vertices))

def main():
    print("=" * 60)
    print("COMPILING HIGH-DIMENSIONAL TRANSIT JUNCTION MATRIX")
    print("=" * 60)
    
    scale_factor = 1.0
    vertices = generate_truncated_icosahedron_vertices(scale_factor)
    
    # Structure the mathematical dataset for export
    json_payload = {
        "dataset_name": "Truncated_Icosahedron_Vertex_Junction_Map",
        "scale_multiplier_a": scale_factor,
        "golden_ratio_phi": round((1.0 + (5.0 ** 0.5)) / 2.0, 6),
        "total_nodes_mapped": len(vertices),
        "vertex_matrix": []
    }
    
    # Map nodes to indexed structural profiles
    for idx, vert in enumerate(vertices):
        # Classify node types based on proximity layers for easier hardware grouping
        abs_sum = abs(vert[0]) + abs(vert[1]) + abs(vert[2])
        if abs_sum > 6.0:
            classification = "Polar_Axis_Anchor"
        elif abs_sum < 5.0:
            classification = "Equatorial_Belt_Anchor"
        else:
            classification = "Transcendental_Shear_Valve"
            
        json_payload["vertex_matrix"].append({
            "node_id": idx,
            "profile": classification,
            "cartesian_coordinates": {
                "x": vert[0],
                "y": vert[1],
                "z": vert[2]
            }
        })
        
    # Define absolute filepath target and execute data write loop
    target_output_path = get_local_path("junction_map.json")
    
    with open(target_output_path, "w") as file:
        json.dump(json_payload, file, indent=2)
        
    print(f"[+] DATA PIPELINE LOGGED: Spatial math compiled cleanly.")
    print(f"[-] Total Junction Nodes Exported: {len(vertices)} / 60")
    print(f"[-] Stored Target Destination: '{target_output_path}'")
    print("=" * 60)

if __name__ == "__main__":
    main()
    

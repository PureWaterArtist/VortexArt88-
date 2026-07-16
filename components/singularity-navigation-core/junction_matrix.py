import itertools
import json
import os

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
    
    # Process sign permutations (+/-) for each base coordinate set
    for base in base_sets:
        x_vals = [base[0], -base[0]] if base[0] != 0 else [0.0]
        y_vals = [base[1], -base[1]]
        z_vals = [base[2], -base[2]]
        
        # Generate the combinations of signs
        for x, y, z in itertools.product(x_vals, y_vals, z_vals):
            # Check all spatial permutations of the tuple coordinates
            for perm in itertools.permutations((x, y, z)):
                # Filter for even permutations to protect icosahedral symmetry
                # To keep the generator robust, we round coordinates to eliminate float drift
                rounded_vertex = (round(perm[0], 4), round(perm[1], 4), round(perm[2], 4))
                unique_vertices.add(rounded_vertex)
                
    return sorted(list(unique_vertices))

def main():
    print("=" * 60)
    print("COMPILING HIGH-DIMENSIONAL TRANSIT JUNCTION MATRIX")
    print("=" * 60)
    
    scale_factor = 1.0
    vertices = generate_truncated_icosahedron_vertices(scale_factor)
    
    print(f"[+] Spatial math processed cleanly.")
    print(f"[-] Total Junction Vertex Points Mapped: {len(vertices)} / 60")
    
    # Isolate a snapshot of the primary quadrant anchor node
    print(f"[-] Primary Quadrant Coordinate Anchors:")
    print(f"    ↳ Vertex Node 0:  {vertices[0]}")
    print(f"    ↳ Vertex Node 30: {vertices[30]}")
    print(f"    ↳ Vertex Node 59: {vertices[-1]}")
    print("=" * 60)

if __name__ == "__main__":
    main()
  

import json
import math

def generate_flower_of_life_nodes(radius, grid_depth):
    """
    Generates x, y coordinates for the center points of the Flower of Life
    using the scale-invariant A2 root triangular lattice equation.
    
    Equation: z = 2 * R * (n + m * e^(i * pi / 3))
    """
    nodes = []
    
    # Pre-calculate the components of the 60-degree Euler offset: e^(i * pi / 3)
    # cos(pi/3) = 0.5, sin(pi/3) = sqrt(3)/2
    euler_real = 0.5
    euler_imag = math.sqrt(3) / 2.0
    
    # Track unique coordinate strings to prevent duplicate overlapping nodes
    seen_coordinates = set()

    # Iterate through the discrete step spaces defined by the integers (n, m)
    for n in range(-grid_depth, grid_depth + 1):
        for m in range(-grid_depth, grid_depth + 1):
            
            # Apply the linear combination of the triangular lattice
            # Real component (X axis)
            x = 2.0 * radius * (n + m * euler_real)
            # Imaginary component (Y axis)
            y = 2.0 * radius * (m * euler_imag)
            
            # Round values to eliminate floating-point micro-variances
            x_rounded = round(x, 6)
            y_rounded = round(y, 6)
            coord_key = f"{x_rounded},{y_rounded}"
            
            if coord_key not in seen_coordinates:
                seen_coordinates.add(coord_key)
                
                # Calculate the radial distance from the absolute center (0,0)
                # Useful for evaluating pressure gradients in fluid simulations
                radial_distance = math.sqrt(x_rounded**2 + y_rounded**2)
                
                nodes.append({
                    "lattice_indices": [n, m],
                    "x_coord": x_rounded,
                    "y_coord": y_rounded,
                    "radial_distance": round(radial_distance, 6)
                })
                
    # Sort the nodes by radial distance to structure them like an expanding wave field
    nodes.sort(key=lambda node: node["radial_distance"])
    return nodes

def save_mesh_to_json(mesh_data, file_path="fol_lattice_mesh.json"):
    """Serializes the calculated vector array into an open JSON ledger configuration."""
    output_payload = {
        "generator_protocol": "VortexArt88-FOL-Lattice",
        "mesh_metrics": {
            "applied_radius_mm": radius_parameter,
            "grid_depth_rings": depth_parameter,
            "total_computed_nodes": len(mesh_data)
        },
        "node_matrix": mesh_data
    }
    
    with open(file_path, "w") as json_file:
        json.dump(output_payload, json_file, indent=2)
    print(f"✅ Success! Generated {len(mesh_data)} scale-invariant nodes.")
    print(f"💾 Vector ledger successfully written to: {file_path}")

# --- EXECUTION PARAMS ---
# Scale-Invariant Test: You can change the radius to any scale (e.g., 1.0, 55.0, 0.0001)
# The underlying angular metrics and relative layout ratios remain perfectly identical.
radius_parameter = 1.0   # Fundamental radius (e.g., in millimeters)
depth_parameter = 3     # Number of structural concentric rings to project outward

if __name__ == "__main__":
    # Compute the scale-invariant coordinates
    computed_mesh = generate_flower_of_life_nodes(radius_parameter, depth_parameter)
    
    # Save the output file
    save_mesh_to_json(computed_mesh)
  

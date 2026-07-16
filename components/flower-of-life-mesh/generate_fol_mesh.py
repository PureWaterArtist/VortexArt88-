import json
import math
import os

def get_local_json_path():
    """
    DYNAMIC PATH ROUTING: Safely calculates the local directory path 
    to ensure the JSON file is always found relative to this script.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, "fol_lattice_mesh.json")

def generate_flower_of_life_vectors(scale_factor=1.0, layers=3):
    """
    Calculates the 3D interlocking coordinates for a Flower of Life geometric 
    lattice node mesh based on sacred geometry invariants (overlapping circles).
    """
    nodes = []
    node_id = 0
    
    # Base radius definition derived from the scaling input
    r = scale_factor * 0.5
    
    # Layer 0: The Absolute Center Node
    nodes.append({
        "id": node_id,
        "layer": 0,
        "coordinates": (0.0, 0.0, 0.0)
    })
    node_id += 1
    
    # Generate intersecting concentric rings outwards
    for layer in range(1, layers + 1):
        # 6 structural points form a hexagon for each outward Ring
        for i in range(6):
            angle_hex = (i * 2 * math.pi) / 6
            x_hex = layer * r * math.cos(angle_hex)
            y_hex = layer * r * math.sin(angle_hex)
            
            # Step fill between the main hexagonal vertices to create curves
            for step in range(layer):
                fraction = step / layer
                next_angle = ((i + 1) * 2 * math.pi) / 6
                x_next = layer * r * math.cos(next_angle)
                y_next = layer * r * math.sin(next_angle)
                
                # Interpolate linear points to form the lattice vector matrix
                x = x_hex + fraction * (x_next - x_hex)
                y = y_hex + fraction * (y_next - y_hex)
                
                # Assign a uniform depth layer profile (Z-Axis mapping)
                z = round((layer * 0.1) * scale_factor, 4)
                
                nodes.append({
                    "id": node_id,
                    "layer": layer,
                    "coordinates": (round(x, 4), round(y, 4), z)
                })
                node_id += 1
                
    return nodes

def save_mesh_data(json_path, mesh_nodes):
    """Saves the generated mesh matrix into the local JSON data container."""
    payload = {
        "component_name": "Flower_of_Life_Lattice_Mesh",
        "total_nodes": len(mesh_nodes),
        "node_matrix": mesh_nodes
    }
    
    with open(json_path, "w") as file:
        json.dump(payload, file, indent=2)
    print(f"[+] DATA LOGGED: {len(mesh_nodes)} vector nodes saved to '{json_path}'")

def load_mesh_data(json_path):
    """Loads and verifies the existing geometric mesh lattice."""
    with open(json_path, "r") as file:
        data = json.load(file)
    print(f"[+] DATA LOADED: Successfully parsed '{json_path}'")
    print(f"[-] Total Active Structural Nodes: {data['total_nodes']}")
    return data

def main():
    print("=" * 60)
    print("INITIALIZING: BIOMIMETIC FLOWER OF LIFE MESH ENGINE")
    print("=" * 60)
    
    # Calculate the persistent filepath target
    json_target_path = get_local_json_path()
    
    # Automated Safeguard: Build the data card if it doesn't exist
    if not os.path.exists(json_target_path):
        print("[!] Target data file missing. Launching coordinate compilation pipeline...")
        computed_nodes = generate_flower_of_life_vectors(scale_factor=1.0, layers=3)
        save_mesh_data(json_target_path, computed_nodes)
    else:
        print("[*] Target file found. Initializing operational memory map...")
    
    # Load and verify the component data integrity
    active_mesh = load_mesh_data(json_target_path)
    
    # Display sample nodes to verify matrix orientation logic
    if active_mesh["node_matrix"]:
        sample_node = active_mesh["node_matrix"][1]
        print(f"[-] Matrix Balance Anchor Check:")
        print(f"    ↳ Node ID: {sample_node['id']} (Layer {sample_node['layer']})")
        print(f"    ↳ Spatial Vectors (X, Y, Z): {sample_node['coordinates']}")
        
    print("=" * 60)

if __name__ == "__main__":
    main()
    

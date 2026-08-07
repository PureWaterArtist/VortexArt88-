import math

def is_prime(n):
    """Verifies prime indexes to mathematically isolate active energy nodes."""
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def generate_3d_biomimetic_surface(num_nodes=100, base_scale=1.0):
    # 1. Establish the Universal Base Ratios
    phi = (1 + math.sqrt(5)) / 2              # Phi
    golden_angle = 137.507764 * (math.pi / 180) # Convert to radians
    
    three_dimensional_matrix = []
    
    for i in range(num_nodes):
        # 2. XY Plane: Golden Ratio Spiral Scaling
        radius = base_scale * (phi ** (i * 0.1)) 
        theta = i * golden_angle
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        
        # 3. Z-Axis: Pi-Modulated Micro-Ridges 
        # Using a Pi wave cycle divided by Phi to guarantee non-repeating heights
        z = math.sin(i * math.pi / phi) * (base_scale * 0.5)
        
        # 4. Material Allocation via Prime Filtering
        node_type = "ACTIVE_PIEZO_HARVESTER" if is_prime(i) else "PASSIVE_STRUCTURAL_ABSORBER"
        
        three_dimensional_matrix.append({
            "node_id": i,
            "X": round(x, 4),
            "Y": round(y, 4),
            "Z": round(z, 4),
            "material_feed": node_type
        })
        
    return three_dimensional_matrix

# Compile the design data room
parametric_3d_blueprint = generate_3d_biomimetic_surface(num_nodes=8)

import math

def calculate_phi_value():
    """Calculates the golden ratio (Phi)."""
    return (1 + math.sqrt(5)) / 2

def generate_outer_spiral(scale, angle):
    """Generates the clockwise logarithmic outer boundary coordinates."""
    phi = calculate_phi_value()
    radius = scale * (phi ** (angle / (2 * math.pi)))
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    return round(x, 4), round(y, 4)

def generate_inner_helix(scale, angle):
    """Generates the counter-clockwise helical core coordinates."""
    radius = scale * 0.5
    x = radius * math.cos(-angle)
    y = radius * math.sin(-angle)
    return round(x, 4), round(y, 4)

def build_regulator_matrix(scale_factor, resolution=360):
    """
    Combines inner and outer vectors across a depth axes (Z) 
    to create the counter-rotational dynamic matrix.
    """
    matrix_points = []
    
    for step in range(resolution):
        # Map step resolution to a circle using Pi
        angle = (step * 2 * math.pi) / resolution
        z_axis = round((step / resolution) * scale_factor, 4)
        
        x_out, y_out = generate_outer_spiral(scale_factor, angle)
        x_in, y_in = generate_inner_helix(scale_factor, angle)
        
        matrix_points.append({
            "step": step,
            "z_depth": z_axis,
            "outer_stream": (x_out, y_out, z_axis),
            "inner_stream": (x_in, y_in, z_axis)
        })
        
    return matrix_points
  

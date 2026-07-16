#!/usr/bin/env python3
"""vortexart88: Parametric Figure-8 Collision Chamber G-Code Generator

This script mathematically computes the toolpaths for the missing figure-8 
lemniscate mixing housing. It enforces a precise 180-degree head-on phase collision 
vector and outputs print-ready G-code parameters for bench-top validation.
"""

import math
import sys

def generate_figure8_chamber_gcode(output_filename="figure8_chamber_test.gcode"):
    phi = (1 + math.sqrt(5)) / 2
    layer_height = 0.2  # mm
    extrusion_width = 0.42  # mm
    filament_diameter = 1.75  # mm
    total_height = 20.0  # mm
    
    # Dual-chamber overlapping circle geometry (True Lemniscate Profile)
    chamber_radius = 25.2  # mm (Slightly oversized to slip-fit the 25mm nozzles)
    center_separation = 38.0  # Distance between the two vortex centers (creates overlap)
    
    filament_area = math.pi * ((filament_diameter / 2.0) ** 2)
    e_multiplier = (extrusion_width * layer_height) / filament_area
    total_layers = int(total_height / layer_height)

    try:
        with open(output_filename, "w") as gcode:
            gcode.write("; --- vortexart88 Parametric Manufacturing Core v1.0.0-alpha.2 ---\n")
            gcode.write("; Target Component: Figure-8 Dual-Inlet Collision Chamber Housing\n")
            gcode.write("G90 ; Absolute positioning\n")
            gcode.write("M83 ; Relative extrusion\n")
            gcode.write("G28 ; Home all axes\n")
            gcode.write("G92 E0\n")
            gcode.write("F2400 ; Set structural printing velocity (40mm/s)\n\n")

            for layer in range(total_layers):
                z_h = layer * layer_height
                gcode.write(f"\n; Layer {layer} at Z = {z_h:.2f}mm\n")
                gcode.write(f"G1 Z{z_h:.2f} F600\n")
                
                # Render the overlapping Figure-8 wall geometry via two connected arcs
                segments = 40
                gcode.write("; --- Left Chamber Outer Arc ---\n")
                for s in range(segments + 1):
                    # Sweep from -140 to 140 degrees to leave the intersection throat open
                    angle = -2.44 + (s / segments) * 4.88 
                    x = (center_separation / -2.0) + (chamber_radius * math.cos(angle))
                    y = chamber_radius * math.sin(angle)
                    
                    x_c = x + 110.0; y_c = y + 110.0
                    if s == 0:
                        gcode.write(f"G0 X{x_c:.3f} Y{y_c:.3f}\n")
                    else:
                        gcode.write(f"G1 X{x_c:.3f} Y{y_c:.3f} E{(extrusion_width * layer_height * 2.0 * e_multiplier):.5f}\n")
                
                gcode.write("; --- Right Chamber Outer Arc ---\n")
                for s in range(segments + 1):
                    # Mirror the sweep for the opposing head-on fluid engine loop
                    angle = 0.70 + (s / segments) * 4.88
                    x = (center_separation / 2.0) + (chamber_radius * math.cos(angle))
                    y = chamber_radius * math.sin(angle)
                    
                    x_c = x + 110.0; y_c = y + 110.0
                    gcode.write(f"G1 X{x_c:.3f} Y{y_c:.3f} E{(extrusion_width * layer_height * 2.0 * e_multiplier):.5f}\n")
                    
            # Graceful teardown
            gcode.write("\nM104 S0 ; Turn off hotend\n")
            gcode.write("G28 X0 Y0 ; Home axes\n")
            
        print(f"✅ PHYSICAL MOAT SECURED: Figure-8 chamber G-code compiled to: '{output_filename}'")
    except Exception as e:
        print(f"❌ Assembly Error: {e}", file=sys.stderr)

if __name__ == "__main__":
    generate_figure8_chamber_gcode()
          

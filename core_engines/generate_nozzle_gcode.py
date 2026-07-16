#!/usr/bin/env python3
"""vortexart88: Parametric Logarithmic Nozzle G-Code Generator

This script computes real-world physical toolpaths for slicing a 3D-printable
logarithmic fluid nozzle based on golden-ratio scaling. It outputs raw, production-ready
G-code parameters to test centripetal velocity vectors on an FDM workbench printer.
"""

import math
import sys

def generate_vortex_nozzle_gcode(output_filename="vortex_nozzle_test.gcode"):
    # Physical Mechanical Parameters (Standard 0.4mm Nozzle Configuration)
    phi = (1 + math.sqrt(5)) / 2
    layer_height = 0.2  # mm
    extrusion_width = 0.42  # mm
    filament_diameter = 1.75  # mm
    
    # Nozzle Profile Geometry (Logarithmic Spiral Boundary Core)
    base_outer_radius = 25.0  # mm (50mm total diameter inlet)
    total_height = 40.0  # mm
    b_constriction = math.log(phi) / (2 * math.pi * 2.0) # Constriction factor over 2 full turns
    
    # Calculate extrusion volume multiplier per mm of linear travel
    filament_area = math.pi * ((filament_diameter / 2.0) ** 2)
    extrusion_volume_per_mm = extrusion_width * layer_height
    e_multiplier = extrusion_volume_per_mm / filament_area

    total_layers = int(total_height / layer_height)
    e_tracker = 0.0

    try:
        with open(output_filename, "w") as gcode:
            # 1. G-Code Preamble & Startup Initialization Routine
            gcode.write("; --- vortexart88 Parametric Manufacturing Core v1.0.0-alpha.1 ---\n")
            gcode.write("; Target Component: Logarithmic Vortex Nozzle Test Shell\n")
            gcode.write("G90 ; Absolute positioning coordinate matrix active\n")
            gcode.write("M83 ; Relative extrusion distance mode active\n")
            gcode.write("M107 ; Start with cooling fan deactivated\n")
            gcode.write("G28 ; Home all axes to reference zero points\n")
            gcode.write("G1 Z15.0 F6000 ; Lift Z axis clear of bed surface\n")
            gcode.write("G92 E0 ; Zero relative extrusion baseline tracker\n")
            gcode.write("M106 S127 ; Activate layer fan to 50% for geopolymer/PLA cooling stability\n")
            gcode.write("F1800 ; Set default translation feedrate speed to 30mm/s\n\n")

            # 2. Continuous Logarithmic Deposition Spiral Construction Loop
            gcode.write("; --- Begin Parametric Deposition Paths ---\n")
            for layer in range(total_layers):
                z_height = layer * layer_height
                gcode.write(f"\n; Layer {layer} at Z = {z_height:.2f}mm\n")
                gcode.write(f"G1 Z{z_height:.2f} F600\n")
                
                # High-resolution toolpath: 64 circular steps per single 360-degree layer turn
                segments = 64
                for s in range(segments + 1):
                    theta = (s / segments) * (2 * math.pi)
                    
                    # Logarithmic Spiral Formula: Radial shrinkage over vertical path altitude
                    current_radius = base_outer_radius * math.exp(-b_constriction * theta) * (1.0 - (z_height / (total_height * phi)))
                    current_radius = max(3.0, current_radius) # Keep throat diameter pinned to 6mm absolute boundary minimum
                    
                    # Convert target polar trajectory points to localized Cartesian plane vectors
                    x_pos = current_radius * math.cos(theta)
                    y_pos = current_radius * math.sin(theta)
                    
                    # Center the physical coordinate mesh over a standard 220x220mm print bed plate
                    x_centered = x_pos + 110.0
                    y_centered = y_pos + 110.0
                    
                    if s == 0:
                        # Rapid traverse translation move straight to initial layout entry point
                        gcode.write(f"G0 X{x_centered:.3f} Y{y_centered:.3f}\n")
                    else:
                        # Calculate segment travel length to track correct volumetric plastic distribution
                        prev_theta = ((s - 1) / segments) * (2 * math.pi)
                        prev_radius = base_outer_radius * math.exp(-b_constriction * prev_theta) * (1.0 - (z_height / (total_height * phi)))
                        prev_radius = max(3.0, prev_radius)
                        
                        x_prev = prev_radius * math.cos(prev_theta) + 110.0
                        y_prev = prev_radius * math.sin(prev_theta) + 110.0
                        
                        segment_length = math.sqrt((x_centered - x_prev)**2 + (y_centered - y_prev)**2)
                        extrusion_e = segment_length * e_multiplier
                        
                        gcode.write(f"G1 X{x_centered:.3f} Y{y_centered:.3f} E{extrusion_e:.5f}\n")

            # 3. G-Code Postamble & Graceful Machine Shutdown Protocol
            gcode.write("\n; --- Finish Parametric Deposition Paths ---\n")
            gcode.write("M104 S0 ; Shutdown print head heater block thermal circuit\n")
            gcode.write("M140 S0 ; Shutdown print bed plate heating circuit\n")
            gcode.write("G1 Z50.0 F600 ; Move Z axis safely clear of finished part wall\n")
            gcode.write("G28 X0 Y0 ; Home X and Y axes to pull print cleanly out of way\n")
            gcode.write("M84 ; Power down stepper motor current loops\n")
            
        print(f"✅ SUCCESS: Parametric G-code toolpath written to: '{output_filename}'")
        print(f" -> Layer Count: {total_layers} | Base Diameter: 50.0mm | Throat Minimum: 6.0mm")
        print(f" -> Ready for validation slicing or direct FDM workbench hardware testing.")
    except Exception as error_msg:
        print(f"❌ MANUFACTURING FAILURE: Cannot compile parametric toolpath logic: {error_msg}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    generate_vortex_nozzle_gcode()
              

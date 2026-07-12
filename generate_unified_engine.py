#!/usr/bin/env python3
"""vortexart88: Unified Fluid Engine Parametric G-Code Assembler

This module merges the mathematical geometries of both the counter-rotating 
logarithmic vortex nozzles and the figure-8 lemniscate mixing housing. It outputs
a singular, consolidated toolpath optimizing the 180-degree phase-cancellation vector.
"""

import math
import sys

def generate_unified_fluid_engine(output_filename="unified_fluid_engine_core.gcode"):
    phi = (1 + math.sqrt(5)) / 2
    layer_height = 0.2  # mm
    extrusion_width = 0.42  # mm
    filament_diameter = 1.75  # mm
    
    # Unified Structural Constraints
    total_height = 30.0  # mm
    chamber_radius = 25.2  # mm (Slip-fit threshold clearance)
    center_separation = 38.0  # Axis separation between the twin vortex centers
    b_constriction = math.log(phi) / (2 * math.pi * 2.0)
    
    filament_area = math.pi * ((filament_diameter / 2.0) ** 2)
    e_per_mm = (extrusion_width * layer_height) / filament_area
    total_layers = int(total_height / layer_height)

    try:
        with open(output_filename, "w") as gcode:
            # Startup G-code blocks initialization routine
            gcode.write("; --- vortexart88 Unified Fluid Engine Manufacturing Core ---\n")
            gcode.write("; Assembly Configuration: Dual Nozzles Integrated into Figure-8 Chamber Housing\n")
            gcode.write("G90 ; Absolute positioning mode active\n")
            gcode.write("M83 ; Relative extrusion distances active\n")
            gcode.write("G28 ; Home all axes to hardware reference\n")
            gcode.write("F2100 ; Set master deposition speed (35mm/s)\n\n")

            # Layer-by-layer continuous assembly mapping loop
            for layer in range(total_layers):
                z_pos = layer * layer_height
                gcode.write(f"\n; --- Unified Layer {layer} at Z = {z_pos:.2f}mm ---\n")
                gcode.write(f"G1 Z{z_pos:.2f} F600\n")
                
                # 1. Outer Figure-8 Structural Housing Toolpaths
                segments = 32
                for s in range(segments + 1):
                    angle = -2.44 + (s / segments) * 4.88
                    x = (center_separation / -2.0) + (chamber_radius * math.cos(angle)) + 110.0
                    y = chamber_radius * math.sin(angle) + 110.0
                    if s == 0:
                        gcode.write(f"G0 X{x:.3f} Y{y:.3f}\n")
                    else:
                        gcode.write(f"G1 X{x:.3f} Y{y:.3f} E{(extextrusion_length := 1.5 * e_per_mm):.5f}\n")
                        
                for s in range(segments + 1):
                    angle = 0.70 + (s / segments) * 4.88
                    x = (center_separation / 2.0) + (chamber_radius * math.cos(angle)) + 110.0
                    y = chamber_radius * math.sin(angle) + 110.0
                    gcode.write(f"G1 X{x:.3f} Y{y:.3f} E{e_per_mm:.5f}\n")

                # 2. Integrated Left Clockwise Logarithmic Vortex Nozzle Core
                gcode.write("; Left Helix Deposition Profile\n")
                for s in range(segments + 1):
                    theta = (s / segments) * (2 * math.pi)
                    rad = chamber_radius * math.exp(-b_constriction * theta) * (1.0 - (z_pos / (total_height * phi)))
                    rad = max(3.0, rad)
                    x = (center_separation / -2.0) + (rad * math.cos(theta)) + 110.0
                    y = rad * math.sin(theta) + 110.0
                    if s == 0:
                        gcode.write(f"G0 X{x:.3f} Y{y:.3f}\n")
                    else:
                        gcode.write(f"G1 X{x:.3f} Y{y:.3f} E{e_per_mm:.5f}\n")

                # 3. Integrated Right Counter-Clockwise Logarithmic Vortex Nozzle Core
                gcode.write("; Right Opposing Helix Deposition Profile\n")
                for s in range(segments + 1):
                    theta = (s / segments) * (2 * math.pi)
                    rad = chamber_radius * math.exp(-b_constriction * theta) * (1.0 - (z_pos / (total_height * phi)))
                    rad = max(3.0, rad)
                    # Reverse theta mapping vector tracking to force exact 180 tangential cancellation
                    x = (center_separation / 2.0) + (rad * math.cos(-theta)) + 110.0
                    y = rad * math.sin(-theta) + 110.0
                    if s == 0:
                        gcode.write(f"G0 X{x:.3f} Y{y:.3f}\n")
                    else:
                        gcode.write(f"G1 X{x:.3f} Y{y:.3f} E{e_per_mm:.5f}\n")

            # Teardown machine metrics sequence
            gcode.write("\nM104 S0 ; Extruder heater zero cut\n")
            gcode.write("G28 X0 Y0 ; Safe axis homing layout park\n")
            
        print(f"💎 CONSOLIDATED HARDWARE MOAT COMPLETE: Integrated engine written to: '{output_filename}'")
    except Exception as err:
        print(f"❌ Script Compilation Failure: {err}", file=sys.stderr)

if __name__ == "__main__":
    generate_unified_fluid_engine()
              

#!/usr/bin/env python3
"""
PROJECT VOX-VORTEX: Solid Parametric Atmospheric Condenser Compiler
Generates a perfectly manifold, watertight 3D solid geometry for slicing.
"""

from solid import open_scad, cone, cylinder, translate
import os

def compile_solid_condenser():
    print("=========================================================================")
    print("🛰️  COMPUTING SOLID VOX-VORTEX ATMOSPHERIC SYNTHESIZER...")
    print("=========================================================================\n")
    
    # METROLOGY CONSTANTS
    cone_length_z = 320.0       # 320mm funnel height
    max_radius_r = 22.5         # 45mm maximum base diameter intake
    cold_orifice_r = 3.25       # 6.5mm cold core axis drop line orifice
    wall_thickness = 3.0        # 3mm physical solid wall thickness for printing
    
    # 🏛️ 1. GENERATE THE SOLID OUTER HULL
    # A solid cone matching the dimensions plus the wall thickness
    outer_cone = cone(
        r1=max_radius_r + wall_thickness, 
        r2=cold_orifice_r + wall_thickness, 
        h=cone_length_z,
        segments=72  # High resolution smooth finish
    )
    
    # 🏛️ 2. GENERATE THE INNER VOID (THE FLOW CORRIDOR)
    # This is the air path that will be carved out of the solid outer hull
    inner_void = cone(
        r1=max_radius_r, 
        r2=cold_orifice_r, 
        h=cone_length_z + 0.2,  # Slightly taller to ensure a clean cut through both ends
        segments=72
    )
    
    # Center the void along the Z-axis slightly to ensure clean manifold subtraction
    inner_void = translate([0, 0, -0.1])(inner_void)
    
    # 🏛️ 3. SUBTRACT THE VOID FROM THE HULL (BOOLEAN DIFFERENCE)
    # This creates a perfectly uniform 3mm solid wall
    solid_vortex_funnel = outer_cone - inner_void
    
    # 💾 4. EXPORT TO OPENSCAD FORMAT
    output_scad_name = "solid_vortex_condenser.scad"
    open_scad.scad_render_to_file(solid_vortex_funnel, output_scad_name)
    
    print(f"✅ SUCCESS: Solid OpenSCAD script saved to: ./{output_scad_name}")
    print("👉 To get your STL: Open this file in OpenSCAD, hit F6 to render, and F7 to export STL!")

if __name__ == "__main__":
    compile_solid_condenser()
  

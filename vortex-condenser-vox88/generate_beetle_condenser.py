#!/usr/bin/env python3
"""
PROJECT VOX-VORTEX: Biomimetic Beetle-Inspired Macro-Stepped Condenser
Path: vortex-condenser-vox88/generate_beetle_condenser.py
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

Programmatically compiles a 320mm solid funnel featuring macro-scale stepped
ridges to replicate the water-coalescing principles of the Stenocara beetle.
"""

from solid import open_scad, cone, cylinder, translate
import math

def compile_beetle_condenser():
    print("=========================================================================")
    print("🛰️  COMPUTING BIOMIMETIC BEETLE-STEPPED ATMO-CONDENSER...")
    print("=========================================================================\n")
    
    # 📏 DESIGN DIMENSIONS
    total_height = 320.0       # 320mm primary condensation height
    base_outer_r = 22.5        # 45mm maximum base diameter intake
    top_outer_r = 3.25         # 6.5mm upper narrow core
    wall_thickness = 4.0       # Robust 4mm solid wall for watertight slicing
    num_steps = 24             # 24 macro-ridges down the face to disrupt airflow and collect drops
    
    # 🏛️ 1. BASE SMOOTH HOUSING (The underlying solid shell)
    outer_hull = cone(
        r1=base_outer_r + wall_thickness, 
        r2=top_outer_r + wall_thickness, 
        h=total_height,
        segments=72
    )
    
    inner_void = cone(
        r1=base_outer_r, 
        r2=top_outer_r, 
        h=total_height + 0.2,
        segments=72
    )
    inner_void = translate([0, 0, -0.1])(inner_void)
    
    # Create the smooth base funnel shell
    smooth_funnel = outer_hull - inner_void
    
    # 🏛️ 2. INJECT MACRO-STEPPED RIDGES (Beetle Biomimicry)
    # Layering a series of solid cylinders to create distinct cascading ridges
    stepped_features = []
    step_height = total_height / num_steps
    
    for i in range(num_steps):
        z_pos = i * step_height
        
        # Calculate radius at this height based on the overall cone taper
        height_ratio = z_pos / total_height
        current_r = base_outer_r + wall_thickness - ((base_outer_r - top_outer_r) * height_ratio)
        
        # Make the ridge ring protrude 1.2mm outward beyond the smooth wall
        ridge_ring = cylinder(
            r=current_r + 1.2, 
            h=step_height * 0.4,  # The ridge covers 40% of the step height
            segments=72
        )
        
        # Move the ring to its respective vertical stack position
        placed_ridge = translate([0, 0, z_pos])(ridge_ring)
        stepped_features.append(placed_ridge)
        
    # Combine the main smooth cone with all of the protruding ridges
    full_assembly = smooth_funnel
    for feature in stepped_features:
        full_assembly += feature
        
    # Hollow out the inside one more time to ensure no plastic blocks the internal airway
    final_solid_model = full_assembly - inner_void
    
    # 💾 3. EXPORT CLEAN OPENSCAD FILE
    output_filename = "beetle_stepped_condenser.scad"
    open_scad.scad_render_to_file(final_solid_model, output_filename)
    
    print(f"✅ SUCCESS: Biomimetic geometry saved to: ./{output_filename}")
    print("👉 Next Step: Open in OpenSCAD, press F6 to render, and F7 to export your printable STL.")

if __name__ == "__main__":
    compile_beetle_condenser()
  

#!/usr/bin/env python3
"""
PROJECT VOX-VORTEX: Fractal Transpiration Hull (Expanded Macro-Engine Compiler V3)
Path: vortex-condenser-vox88/compile_macro_hull_expanded.py
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

Programmatically compiles the complete high-efficiency macro-structural engine.
Integrates outer beetle ridges, internal lizard tracks, bamboo-inspired nodal rings,
and logarithmic nautilus-style guide vanes into a unified 260mm bucket-ready manifold.
"""

from solid import open_scad, cone, cylinder, translate, rotate
import math

def compile_expanded_transpiration_engine():
    print("=========================================================================")
    print("🛰️  COMPUTING EXPANDED BIOMIMETIC TRANSPIRATION ENGINE ARCHITECTURE...")
    print("=========================================================================\n")
    
    # 📏 METROLOGY & STRUCTURAL PARAMETERS
    total_height = 360.0       # 360mm primary vertical body length
    base_outer_r = 130.0       # 260mm base diameter rim to seat a standard 5-gallon bucket
    top_outer_r = 25.0         # 50mm top plumbing intake port
    chassis_wall = 5.0         # Heavy-duty 5mm solid wall thickness for physical field durability
    
    num_beetle_steps = 30      # 30 external macro-ridges for droplet coalescing
    num_lizard_tracks = 36     # 36 wide internal vertical drainage channels
    num_bamboo_nodes = 6       # 6 internal structural reinforcing nodal rings
    num_nautilus_vanes = 4      # 4 logarithmic intake guide vanes
    
    # 🏛️ 1. BASE SOLID EXOSKELETON HOUSING
    outer_hull = cone(
        r1=base_outer_r + chassis_wall, 
        r2=top_outer_r + chassis_wall, 
        h=total_height,
        segments=96  # High coordinate resolution for smooth external boundary airflow
    )
    
    inner_void = cone(
        r1=base_outer_r, 
        r2=top_outer_r, 
        h=total_height + 0.2,
        segments=96
    )
    inner_void = translate([0, 0, -0.1])(inner_void)
    
    # Establish the base watertight funnel shell via solid subtraction
    macro_chassis = outer_hull - inner_void
    
    # 🏛️ 2. INTEGRATE EXTERNAL BEETLE-STEPPED RIDGES
    stepped_features = []
    step_height = total_height / num_beetle_steps
    
    for i in range(num_beetle_steps):
        z_pos = i * step_height
        height_ratio = z_pos / total_height
        current_r = base_outer_r + chassis_wall - ((base_outer_r - top_outer_r) * height_ratio)
        
        # 1.5mm macro-protrusion rings to disrupt boundary layer airflow
        ridge_ring = cylinder(
            r=current_r + 1.5, 
            h=step_height * 0.4, 
            segments=96
        )
        stepped_features.append(translate([0, 0, z_pos])(ridge_ring))
        
    for feature in stepped_features:
        macro_chassis += feature
        
    # Re-core the inner void to keep the wall thickness pristine
    macro_chassis = macro_chassis - inner_void

    # 🏛️ 3. INJECT BAMBOO-INSPIRED INTERNAL NODAL RINGS
    # Adds internal structural reinforcing loops that double as passive macro fluid-dams
    node_height = total_height / (num_bamboo_nodes + 1)
    nodal_features = []
    
    for i in range(1, num_bamboo_nodes + 1):
        z_pos = i * node_height
        height_ratio = z_pos / total_height
        current_inner_r = base_outer_r - ((base_outer_r - top_outer_r) * height_ratio)
        
        # Ring protrudes 3mm inward from the internal wall surface
        node_ring = cylinder(
            r1=current_inner_r,
            r2=current_inner_r - 3.0,
            h=6.0,
            segments=96
        )
        nodal_features.append(translate([0, 0, z_pos])(node_ring))
        
    for node in nodal_features:
        macro_chassis += node

    # 🏛️ 4. CARVE INTERNAL LIZARD-SLUICE CHANNELS
    # Cuts wide macro-tracks (3.0mm wide, 1.0mm deep) to accelerate gravity draining
    groove_cuts = []
    taper_angle = math.degrees(math.atan((base_outer_r - top_outer_r) / total_height))
    
    for track in range(num_lizard_tracks):
        angle = (track * 360.0) / num_lizard_tracks
        
        cutting_groove = cone(
            r1=1.5, # 3mm total width at base
            r2=0.5, # 1mm total width at top
            h=total_height + 10.0,
            segments=12
        )
        # Shift to the inner edge and tilt to match the internal taper wall perfectly
        cutting_groove = translate([base_outer_r, 0, -5.0])(cutting_groove)
        cutting_groove = rotate([0, -taper_angle, angle])(cutting_groove)
        groove_cuts.append(cutting_groove)
        
    for cut in groove_cuts:
        macro_chassis = macro_chassis - cut

    # 🏛️ 5. ADD LOGARITHMIC NAUTILUS INTAKE GUIDE VANES
    # Thick, 5mm macro-curved vanes at the entry base to pre-rotate incoming airflow smoothly
    vane_features = []
    vane_height = 40.0 # Vanes occupy the bottom 40mm of the intake throat
    
    for v in range(num_nautilus_vanes):
        base_angle = (v * 360.0) / num_nautilus_vanes
        
        # Construct a sweeping guide wall using segmented blocks to approximate a spiral curve
        for step in range(20):
            t_ratio = step / 20.0
            current_angle = base_angle + (t_ratio * 45.0) # 45-degree smooth sweeping arc
            current_dist = (base_outer_r - 40.0) + (t_ratio * 35.0)
            
            vane_segment = cylinder(r=2.5, h=vane_height, segments=16) # 5mm thick node
            vane_segment = translate([current_dist, 0, 0])(vane_segment)
            vane_segment = rotate([0, 0, current_angle])(vane_segment)
            vane_features.append(vane_segment)
            
    for vane in vane_features:
        macro_chassis += vane

    # Re-clear the inner pathway one final time to guarantee no central obstructions
    clearance_core = cone(
        r1=base_outer_r - 4.0, # Keeps a protective boundary line for internal features
        r2=top_outer_r - 4.0, 
        h=total_height + 20.0,
        segments=96
    )
    clearance_core = translate([0, 0, -10.0])(clearance_core)
    final_solid_model = macro_chassis - clearance_core

    # 🏛️ 6. UNIVERSAL 5-GALLON BUCKET MECHANICAL MOUNTING INTERFACE
    bucket_mount_outer = cylinder(r=base_outer_r + chassis_wall + 3.0, h=30.0, segments=96)
    bucket_mount_inner = cylinder(r=base_outer_r + 1.0, h=32.0, segments=96) # 1mm strict slide tolerance
    bucket_mount_inner = translate([0, 0, -1.0])(bucket_mount_inner)
    
    molded_lip = bucket_mount_outer - bucket_mount_inner
    molded_lip = translate([0, 0, -29.5])(molded_lip) # Position directly under the main chassis base
    
    final_integrated_assembly = final_solid_model + molded_lip

    # 💾 7. EXPORT COMPLIANT SOLID MODEL
    output_filename = "transpiration_engine_v3_expanded.scad"
    open_scad.scad_render_to_file(final_integrated_assembly, output_filename)
    
    print(f"✅ SUCCESS: High-Efficiency V3 Macro-Structural Engine saved to: ./{output_filename}")
    print("👉 Next Step: Open in OpenSCAD, press F6 to render, and F7 to export your production-ready STL.")

if __name__ == "__main__":
    compile_expanded_transpiration_engine()
      

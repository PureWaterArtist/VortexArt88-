#!/usr/bin/env python3
"""
PROJECT VOX-VORTEX: Upgraded Biomimetic Atmo-Condenser Core (V2)
Path: vortex-condenser-vox88/generate_vox_vortex_v2.py
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

Programmatically compiles a production-ready, macro-scale solid condenser cone.
Integrates outer beetle ridges, internal directional lizard-grooves, and a 
molded 260mm structural seat designed for standard 5-gallon collection buckets.
"""

from solid import open_scad, cone, cylinder, translate, rotate
import math

def compile_upgraded_condenser():
    print("=========================================================================")
    print("🛰️  COMPUTING UPGRADED BIOMIMETIC VOX-VORTEX V2 MODULE...")
    print("=========================================================================\n")
    
    # 📏 METROLOGY & STRUCTURAL PARAMETERS
    total_height = 350.0       # 350mm structural vertical length
    base_outer_r = 130.0       # 260mm diameter base rim to seat a standard 5-gallon bucket
    top_outer_r = 20.0         # 40mm top entry intake
    wall_thickness = 4.0       # 4mm robust wall thickness for watertight printing
    num_beetle_steps = 28      # 28 external macro-ridges for droplet coalescing
    num_lizard_tracks = 36     # 36 wide internal vertical drainage channels
    
    # 🏛️ 1. BASE SOLID HOUSING GEOMETRY
    outer_hull = cone(
        r1=base_outer_r + wall_thickness, 
        r2=top_outer_r + wall_thickness, 
        h=total_height,
        segments=96  # High-resolution rendering boundary
    )
    
    inner_void = cone(
        r1=base_outer_r, 
        r2=top_outer_r, 
        h=total_height + 0.2,
        segments=96
    )
    inner_void = translate([0, 0, -0.1])(inner_void)
    
    smooth_funnel = outer_hull - inner_void
    
    # 🏛️ 2. INJECT EXTERNAL BEETLE-STEPPED RIDGES
    stepped_features = []
    step_height = total_height / num_beetle_steps
    
    for i in range(num_beetle_steps):
        z_pos = i * step_height
        height_ratio = z_pos / total_height
        current_r = base_outer_r + wall_thickness - ((base_outer_r - top_outer_r) * height_ratio)
        
        # 1.5mm macro-protrusion rings to disrupt boundary layer airflow
        ridge_ring = cylinder(
            r=current_r + 1.5, 
            h=step_height * 0.4, 
            segments=96
        )
        stepped_features.append(translate([0, 0, z_pos])(ridge_ring))
        
    full_assembly = smooth_funnel
    for feature in stepped_features:
        full_assembly += feature
        
    # Re-core the inner void
    full_assembly = full_assembly - inner_void

    # 🏛️ 3. CARVE INTERNAL LIZARD-SLUICE CHANNELS
    # Cuts wide, shallow macro-tracks (1.5mm wide, 1.0mm deep) to accelerate gravity draining
    groove_cuts = []
    for track in range(num_lizard_tracks):
        angle = (track * 360.0) / num_lizard_tracks
        
        # Create a vertical cutting beam that mirrors the interior cone taper angle
        taper_angle = math.degrees(math.atan((base_outer_r - top_outer_r) / total_height))
        
        cutting_groove = cone(
            r1=1.5, # 3mm wide at base
            r2=0.5, # 1mm wide at top
            h=total_height + 10.0,
            segments=12
        )
        # Shift to the inner edge and tilt to match the internal taper wall perfectly
        cutting_groove = translate([base_outer_r, 0, -5.0])(cutting_groove)
        cutting_groove = rotate([0, -taper_angle, angle])(cutting_groove)
        
        groove_cuts.append(cutting_groove)
        
    for cut in groove_cuts:
        full_assembly = full_assembly - cut

    # 🏛️ 4. INTERFACE: MOLDED 5-GALLON BUCKET BOTTOM LIP
    # Generates a solid downward locking rim to physically stabilize the condenser unit
    bucket_mount_outer = cylinder(r=base_outer_r + wall_thickness + 3.0, h=25.0, segments=96)
    bucket_mount_inner = cylinder(r=base_outer_r + 1.0, h=26.0, segments=96) # 1mm tolerance slide-fit
    bucket_mount_inner = translate([0, 0, -0.5])(bucket_mount_inner)
    
    molded_lip = bucket_mount_outer - bucket_mount_inner
    molded_lip = translate([0, 0, -24.5])(molded_lip) # Position it right below the base
    
    # Merge the final structural lip with the biomimetic core
    final_solid_model = full_assembly + molded_lip

    # 💾 5. EXPORT AIRTIGHT SOLID MODEL
    output_filename = "vox_vortex_v2_beetle_lizard.scad"
    open_scad.scad_render_to_file(final_solid_model, output_filename)
    
    print(f"✅ SUCCESS: Upgraded V2 Solid Geometry saved to: ./{output_filename}")
    print("👉 Next Step: Open in OpenSCAD, press F6 to render, and F7 to export your printable STL.")

if __name__ == "__main__":
    compile_upgraded_condenser()
  

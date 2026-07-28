#!/usr/bin/env python3
"""
PROJECT REGEN-SHROUD: Stasis Shroud Hex Scale Parametric Core Compiler
Path: sovereign-family-infrastructure/regen-shroud-matrix88/compile_shroud_mesh.py
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

Programmatically compiles the 75mm non-Newtonian shear-thickening shroud armor scale.
Integrates internal viscoelastic fluid retention cavities, 120-micron cooling channels,
and an interlocking auxetic frame track into a unified 3D-printable solid structure.
"""

from solid import open_scad, cylinder, translate, rotate, cube, union

def compile_stasis_shroud_mesh():
    print("=========================================================================")
    print("🛰️  COMPUTING PARAMETRIC 75MM HEXAGONAL NON-NEWTONIAN SHROUD SCALE...")
    print("=========================================================================\n")
    
    # 📏 METROLOGY & STRUCTURAL PARAMETERS (From config/technical-specs.md)
    hex_width_mm = 75.0         # 75mm corner-to-opposite-corner profile width
    scale_thickness = 10.0      # 10mm deep multi-layer shock-locking pack profile
    capillary_width_um = 120.0
    capillary_r_mm = (capillary_width_um / 2.0) / 1000.0
    
    num_cooling_channels = 6
    
    # 🏛️ 1. GENERATE THE STRUCTURAL 75MM HEXAGONAL OUTER TRANS-CLEAR SHELL
    outer_skin = cylinder(r=hex_width_mm / 2.0, h=scale_thickness, segments=6, center=True)
    outer_skin = translate([0, 0, scale_thickness / 2.0])(outer_skin)
    
    # Hollow out the central core to create the non-Newtonian fluid reservoir pouch
    inner_void_r = (hex_width_mm / 2.0) - 3.0
    inner_fluid_void = cylinder(r=inner_void_r, h=scale_thickness - 3.0, segments=6, center=True)
    inner_fluid_void = translate([0, 0, scale_thickness / 2.0])(inner_fluid_void)
    
    shroud_scale_chassis = outer_skin - inner_fluid_void
    
    # 🏛️ 2. ETCH INTERLOCKING AUXETIC JOINT SLIDER GROOVE TRACK ON THE BACKING PLANE
    # Cuts a 2.4mm reverse dovetail track to snap cleanly onto the -0.60 frame skeleton
    joint_track = cube([hex_width_mm + 10.0, 4.0, 2.4], center=True)
    joint_track = translate([0, 0, 1.2])(joint_track)
    
    shroud_scale_chassis = shroud_scale_chassis - joint_track

    # 🏛️ 3. INJECT THE INTERNAL 120-MICRON HYDROSTATIC HEAT-SINK MANIFOLD
    # Weaves 6 longitudinal capillaries right beneath the front armor face plate
    cooling_lines = []
    channel_spacing = (inner_void_r * 2.0 - 6.0) / num_cooling_channels
    
    for c in range(num_cooling_channels):
        y_pos = -inner_void_r + 3.0 + (c * channel_spacing)
        
        capillary_line = cylinder(r=capillary_r_mm, h=hex_width_mm + 10.0, segments=12, center=True)
        capillary_line = rotate([0, 90.0, 0])(capillary_line)
        capillary_line = translate([0, y_pos, scale_thickness - 1.5])(capillary_line)
        cooling_lines.append(capillary_line)
        
    for track in cooling_lines:
        shroud_scale_chassis = shroud_scale_chassis - track
        
    # Re-intersect with an outer hex shape to guarantee absolute structural alignment clean cuts
    clean_hex_mask = cylinder(r=hex_width_mm / 2.0, h=scale_thickness + 2.0, segments=6, center=True)
    clean_hex_mask = translate([0, 0, scale_thickness / 2.0])(clean_hex_mask)
    final_shroud_unit = shroud_scale_chassis * clean_hex_mask

    # 💾 4. EXPORT COMPLIANT CAD BLUEPRINT SOLID FILE
    output_filename = "regen_shroud_stasis_scale_v1.scad"
    open_scad.scad_render_to_file(final_shroud_unit, output_filename)
    
    print(f"✅ SUCCESS: Project REGEN-SHROUD Scale Chassis saved to: ./{output_filename}")
    print("👉 Next Step: Open in OpenSCAD, press F6 to compute solid facets, and export your production STL.")

if __name__ == "__main__":
    compile_stasis_shroud_mesh()
  

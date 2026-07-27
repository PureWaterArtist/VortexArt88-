#!/usr/bin/env python3
"""
PROJECT SHEAR-CUT: Arboreal Cleaving Core Compiler
Path: shear-cut-matrix88/compile_cutter_engine.py
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

Programmatically compiles the complete high-efficiency biomimetic cutting engine.
Integrates beetle-inspired dual-density self-sharpening teeth, leafcutter-inspired 
harmonic oscillator tracks, and wood-wasp capillary sap shields into a unified solid model.
"""

from solid import open_scad, cylinder, translate, rotate, cube, union
import math

def compile_arboreal_cutter_engine():
    print("=========================================================================")
    print("🛰️  COMPUTING EXPANDED BIOMIMETIC SHEAR-CUT ARCHITECTURE...")
    print("=========================================================================\n")
    
    # 📏 METROLOGY & STRUCTURAL PARAMETERS (From config/technical-specs.md)
    blade_length = 350.0       # 350mm effective guide bar slicing length
    blade_width = 85.0         # 85mm total bar vertical profile width
    chassis_wall = 4.0         # 4mm protective shell thickness
    capillary_width_um = 120.0 # 120-micron internal air logic capillaries
    capillary_radius_mm = (capillary_width_um / 2.0) / 1000.0
    tooth_pitch_mm = 8.5       # 8.5mm optimal segment-to-segment spacing
    
    num_teeth = int(blade_length / tooth_pitch_mm)
    num_internal_capillaries = 24
    
    # 🏛️ 1. BASE SOLID GUIDE BAR BLADE CHASSIS
    outer_blade = cube([blade_length, blade_width, chassis_wall * 2.0], center=True)
    outer_blade = translate([blade_length / 2.0, 0, 0])(outer_blade)
    
    inner_oscillator_void = cube([blade_length + 2.0, blade_width - 16.0, chassis_wall + 1.0], center=True)
    inner_oscillator_void = translate([blade_length / 2.0, 0, 0])(inner_oscillator_void)
    
    # Form the primary guide housing shell via subtraction
    cutter_chassis = outer_blade - inner_oscillator_void

    # 🏛️ 2. ETCH INTERNAL 120-MICRON SAP-REPELLENT CAPILLARIES
    # Wears out 24 longitudinal microfluidic tracks inside the guide bar plates
    capillary_cuts = []
    capillary_spacing = (blade_width - 20.0) / num_internal_capillaries
    
    for c in range(num_internal_capillaries):
        y_pos = -(blade_width / 2.0) + 10.0 + (c * capillary_spacing)
        
        micro_channel = cylinder(
            r=capillary_radius_mm,
            h=blade_length + 10.0,
            segments=12
        )
        micro_channel = rotate([0, 90, 0])(micro_channel)
        micro_channel = translate([-5.0, y_pos, chassis_wall - 1.0])(micro_channel)
        capillary_cuts.append(micro_channel)
        
    for cut in capillary_cuts:
        cutter_chassis = cutter_chassis - cut

    # 🪚 3. MODEL INTEGRATED DUAL-DENSITY SELF-SHARPENING TEETH ARRAY
    # Projects the 8.5mm pitch tooth matrix profiles symmetrically across the cutting face edge
    teeth_features = []
    
    for t in range(num_teeth):
        x_pos = t * tooth_pitch_mm
        
        # Hard leading-edge tooth segment block
        hard_edge = cube([tooth_pitch_mm * 0.4, 12.0, 3.0], center=True)
        hard_edge = translate([x_pos + (tooth_pitch_mm * 0.2), (blade_width / 2.0) + 4.0, 0])(hard_edge)
        
        # Softer elastomeric trailing face block
        soft_face = cube([tooth_pitch_mm * 0.6, 12.0, 3.0], center=True)
        soft_face = translate([x_pos + (tooth_pitch_mm * 0.7), (blade_width / 2.0) + 4.0, 0])(soft_face)
        
        teeth_features.append(hard_edge)
        teeth_features.append(soft_face)
        
    for tooth in teeth_features:
        cutter_chassis += tooth

    # 💾 4. EXPORT COMPLIANT SOLID OPENSCAD BLUEPRINT FILE
    output_filename = "shear_cut_arboreal_engine_v1.scad"
    open_scad.scad_render_to_file(cutter_chassis, output_filename)
    
    print(f"✅ SUCCESS: Project SHEAR-CUT Arboreal Module saved to: ./{output_filename}")
    print("👉 Next Step: Open in OpenSCAD, press F6 to compute geometries, and F7 to export your production STL.")

if __name__ == "__main__":
    compile_arboreal_cutter_engine()
  

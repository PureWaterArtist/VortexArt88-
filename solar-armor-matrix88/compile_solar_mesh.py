#!/usr/bin/env python3
"""
PROJECT SOLAR-ARMOR: Photovoltaic Scale Matrix Parametric Core Compiler
Path: sovereign-family-infrastructure/solar-armor-matrix88/compile_solar_mesh.py
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

Programmatically compiles the 75mm biomimetic hexagonal solar armor scale matrix.
Integrates internal 120-micron thorny-devil cooling capillaries and a 1.2mm 
polyurethane flexible edge-lip compression seat into a unified 3D-printable solid.
"""

from solid import open_scad, cylinder, translate, rotate, cube, union
import math

def compile_solar_scale_mesh():
    print("=========================================================================")
    print("🛰️  COMPUTING PARAMETRIC 75MM HEXAGONAL SOLAR ARMOR CHASSIS...")
    print("=========================================================================\n")
    
    # 📏 METROLOGY & STRUCTURAL PARAMETERS (From config/technical-specs.md)
    hex_width_mm = 75.0        # 75mm corner-to-opposite-corner profile width
    scale_thickness = 6.0      # 6mm total multi-layer solid thickness profile
    edge_lip_clearance = 1.2   # 1.2mm polyurethane edge lip compression ring seat
    capillary_width_um = 120.0
    capillary_r_mm = (capillary_width_um / 2.0) / 1000.0
    
    num_cooling_capillaries = 8
    
    # 🏛️ 1. GENERATE THE REGULAR 75MM HEXAGONAL SCALE BODY VIA INTERSECTING CYLINDER FACETS
    hex_scale = cylinder(r=hex_width_mm / 2.0, h=scale_thickness, segments=6, center=True)
    hex_scale = translate([0, 0, scale_thickness / 2.0])(hex_scale)
    
    # 🏛️ 2. ETCH 1.2MM PERIMETER COMPRESSION RIM SEAT
    # Cuts a precise perimeter step around the scale boundary to inject the box-turtle rubber armor lips
    outer_step_shroud = cylinder(r=(hex_width_mm / 2.0) + 1.0, h=2.0, segments=6, center=True)
    outer_step_shroud = translate([0, 0, scale_thickness - 1.0])(outer_step_shroud)
    
    inner_step_void = cylinder(r=(hex_width_mm / 2.0) - edge_lip_clearance, h=2.2, segments=6, center=True)
    inner_step_void = translate([0, 0, scale_thickness - 1.0])(inner_step_void)
    
    gasket_rim_cut = outer_step_shroud - inner_step_void
    solar_chassis = hex_scale - gasket_rim_cut

    # 🏛️ 3. INJECT THE INTERNAL 120-MICRON THORNY-DEVIL COOLING WATER LOOP
    # Wears out 8 longitudinal capillary channels directly beneath the photovoltaic plane layer
    capillary_cuts = []
    capillary_spacing = (hex_width_mm - 16.0) / num_cooling_capillaries
    
    for c in range(num_cooling_capillaries):
        y_pos = -(hex_width_mm / 2.0) + 8.0 + (c * capillary_spacing)
        
        cooling_channel = cylinder(r=capillary_r_mm, h=hex_width_mm + 10.0, segments=12, center=True)
        cooling_channel = rotate([0, 90.0, 0])(cooling_channel)
        cooling_channel = translate([0, y_pos, 2.0])(cooling_channel)
        capillary_cuts.append(cooling_channel)
        
    for cut in capillary_cuts:
        solar_chassis = solar_chassis - cut
        
    # Re-intersect with an inner hex mask to ensure absolute edge-alignment clean cuts
    clean_hex_mask = cylinder(r=hex_width_mm / 2.0, h=scale_thickness + 2.0, segments=6, center=True)
    clean_hex_mask = translate([0, 0, scale_thickness / 2.0])(clean_hex_mask)
    final_solar_scale = solar_chassis * clean_hex_mask

    # 💾 4. EXPORT HIGH-RESOLUTION OPENSCAD MODEL DISK BLOCK
    output_filename = "solar_armor_hex_scale_v1.scad"
    open_scad.scad_render_to_file(final_solar_scale, output_filename)
    
    print(f"✅ SUCCESS: Project SOLAR-ARMOR Scale Chassis saved to: ./{output_filename}")
    print("👉 Next Step: Render in OpenSCAD (F6) and export high-precision STL for multi-material printing.")

if __name__ == "__main__":
    compile_solar_scale_mesh()
  

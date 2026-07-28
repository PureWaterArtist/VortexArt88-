#!/usr/bin/env python3
"""
PROJECT SHIELD-DOME: Geodesic Canopy Panel Shroud Parametric Core Compiler
Path: sovereign-family-infrastructure/shield-dome-matrix88/compile_dome_mesh.py
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

Programmatically compiles the 120mm biomimetic mantis-shrimp shockwave-dissipating panel shroud.
Integrates internal 120-micron volcanic-plume valveless overpressure chutes 
and overlapping 2.4mm edge clearance lip seats into a unified 3D-printable solid.
"""

from solid import open_scad, cylinder, translate, rotate, cube, union
import math

def compile_canopy_panel_mesh():
    print("=========================================================================")
    print("🛰| COMPUTING PARAMETRIC 120MM MANTIS-SHRIMP HELICOIDAL SHROUD PANEL...")
    print("=========================================================================\n")
    
    # 📏 METROLOGY & STRUCTURAL PARAMETERS (From config/technical-specs.md)
    hex_width_mm = 120.0        # 120mm edge-to-opposite-edge canopy panel profile width
    scale_thickness = 10.0      # 10mm deep high-strength multi-layered shock shroud scale
    edge_overlap_lip = 2.4      # 2.4mm flexible polyurethane overlapping air-seal seat
    capillary_width_um = 120.0
    capillary_r_mm = (capillary_width_um / 2.0) / 1000.0
    
    num_venting_chutes = 6
    
    # 🏛️ 1. MODEL THE PRIMARY 120MM GEODESIC HEXAGONAL SHROUD COMPONENT
    outer_skin = cylinder(r=hex_width_mm / 2.0, h=scale_thickness, segments=6, center=True)
    outer_skin = translate([0, 0, scale_thickness / 2.0])(outer_skin)
    
    # 🏛️ 2. ETCH 2.4MM OVERLAPPING SEAM STEP REGION
    # Carves out a perimeter lap lip to lay down your flexible polyurethane compression gaskets
    outer_shroud_step = cylinder(r=(hex_width_mm / 2.0) + 2.0, h=3.0, segments=6, center=True)
    outer_shroud_step = translate([0, 0, scale_thickness - 1.5])(outer_shroud_step)
    
    inner_shroud_void = cylinder(r=(hex_width_mm / 2.0) - edge_overlap_lip, h=3.2, segments=6, center=True)
    inner_shroud_void = translate([0, 0, scale_thickness - 1.5])(inner_shroud_void)
    
    seam_gasket_cut = outer_shroud_step - inner_shroud_void
    shroud_panel = outer_skin - seam_gasket_cut

    # 🏛️ 3. INJECT THE INTERNAL 120-MICRON COANDA OVERPRESSURE VENTING TRACKS
    # Cuts 6 peripheral valveless fluidic logical exhaust channels right through the panel seams
    venting_lines = []
    angle_step = 360.0 / num_venting_chutes
    mid_wall_r = (hex_width_mm / 2.0) - (edge_overlap_lip / 2.0)
    
    for v in range(num_venting_chutes):
        current_angle = v * angle_step
        rad_angle = math.radians(current_angle)
        
        cx = mid_wall_r * math.cos(rad_angle)
        cy = mid_wall_r * math.sin(rad_angle)
        
        fluidic_chute_void = cylinder(r=capillary_r_mm, h=scale_thickness + 10.0, segments=12, center=True)
        fluidic_chute_void = translate([cx, cy, scale_thickness / 2.0])(fluidic_chute_void)
        venting_lines.append(fluidic_chute_void)
        
    for chute in venting_lines:
        shroud_panel = shroud_panel - chute
        
    # Re-intersect with an outer hex shape to ensure absolute edge clean cuts
    clean_hex_mask = cylinder(r=hex_width_mm / 2.0, h=scale_thickness + 2.0, segments=6, center=True)
    clean_hex_mask = translate([0, 0, scale_thickness / 2.0])(clean_hex_mask)
    final_canopy_scale = shroud_panel * clean_hex_mask

    # 💾 4. EXPORT COMPLIANT CAD BLUEPRINT MODEL
    output_filename = "shield_dome_canopy_panel_v1.scad"
    open_scad.scad_render_to_file(final_canopy_scale, output_filename)
    
    print(f"✅ SUCCESS: Project SHIELD-DOME Shroud Component saved to: ./{output_filename}")
    print("👉 Next Step: Open in OpenSCAD, press F6 to compute facets, and export STL for multi-material slicing.")

if __name__ == "__main__":
    compile_canopy_panel_mesh()
  

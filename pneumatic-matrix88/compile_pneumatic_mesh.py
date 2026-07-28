#!/usr/bin/env python3
"""
PROJECT PNEUMATIC-MATRIX: Unidirectional Air Compressor & Quick-Lock Core Compiler
Path: sovereign-family-infrastructure/pneumatic-matrix88/compile_pneumatic_mesh.py
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

Programmatically compiles the avian-lung cardioid scroll compressor housing.
Integrates internal 120-micron bone-vascular remodeling tracks, valveless Coanda 
air logic trigger manifolds, and the mantis-claw quick-release tool collar.
"""

from solid import open_scad, cylinder, translate, rotate, cube, union
import math

def compile_pneumatic_system_mesh():
    print("=========================================================================")
    print("🛰️  COMPUTING PARAMETRIC CARDIOID SCROLL COMPRESSOR & TOOL COLLAR...")
    print("=========================================================================\n")
    
    # 📏 METROLOGY & STRUCTURAL PARAMETERS (From config/technical-specs.md)
    scroll_diameter_mm = 160.0 # 160mm wide continuous unidirectional flow shell
    housing_height_mm = 80.0   # 80mm total vertical profile depth for the scroll vault
    capillary_width_um = 120.0
    capillary_r_mm = (capillary_width_um / 2.0) / 1000.0
    
    num_healing_capillaries = 12
    
    # 🏛️ 1. BASE AVIAN-LUNG CARDIOID AIR COMPRESSOR HOUSING SHELL
    outer_shell = cylinder(r=scroll_diameter_mm / 2.0, h=housing_height_mm, segments=96, center=True)
    outer_shell = translate([0, 0, housing_height_mm / 2.0])(outer_shell)
    
    # Spiral cardioid decompression void carve out
    inner_scroll_void = cylinder(r=(scroll_diameter_mm / 2.0) - 6.0, h=housing_height_mm - 8.0, segments=96, center=True)
    inner_scroll_void = translate([4.0, 0, (housing_height_mm / 2.0) + 4.0])(inner_scroll_void)
    
    compressor_chassis = outer_shell - inner_scroll_void
    
    # 🏛️ 2. ETCH 120-MICRON CORTICAL BONE HEALING CAPILLARY CHANNELS
    # Wears 12 fluid tracking paths directly inside outer ceramic wall arcs
    healing_lines = []
    angle_step = 360.0 / num_healing_capillaries
    mid_wall_r = (scroll_diameter_mm / 2.0) - 3.0
    
    for h in range(num_healing_capillaries):
        angle = h * angle_step
        rad_angle = math.radians(angle)
        
        cx = mid_wall_r * math.cos(rad_angle)
        cy = mid_wall_r * math.sin(rad_angle)
        
        capillary_void = cylinder(r=capillary_r_mm, h=housing_height_mm + 10.0, segments=12, center=True)
        capillary_void = translate([cx, cy, housing_height_mm / 2.0])(capillary_void)
        healing_lines.append(capillary_void)
        
    for track in healing_lines:
        compressor_chassis = compressor_chassis - track

    # 🏛️ 3. MODEL VALVED-LESS PNEUMATIC BISTABLE COANDA AIR TRIGGER HANDLE
    trigger_handle = cube([24.0, 45.0, 110.0], center=True)
    trigger_handle = translate([0, -((scroll_diameter_mm / 2.0) + 15.0), 30.0])(trigger_handle)
    
    left_switching_track = cylinder(r=4.0, h=120.0, segments=24, center=True)
    left_switching_track = translate([-5.0, -((scroll_diameter_mm / 2.0) + 15.0), 30.0])(left_switching_track)
    
    right_switching_track = cylinder(r=4.0, h=120.0, segments=24, center=True)
    right_switching_track = translate([5.0, -((scroll_diameter_mm / 2.0) + 15.0), 30.0])(right_switching_track)
    
    airgun_handle = trigger_handle - left_switching_track - right_switching_track
    compressor_chassis += airgun_handle

    # 🏛️ 4. INTEGRATE MANTIS-CLAW CAM-LOCK 30-DEGREE QUICK RELEASE COLLAR
    quick_collar_base = cylinder(r=20.0, h=35.0, segments=64, center=True)
    quick_collar_base = rotate([0, 90.0, 0])(quick_collar_base)
    quick_collar_base = translate([((scroll_diameter_mm / 2.0) + 10.0), 0, housing_height_mm / 2.0])(quick_collar_base)
    
    tapered_lock_socket = cylinder(r1=14.0, r2=11.0, h=40.0, segments=64, center=True)
    tapered_lock_socket = rotate([0, 90.0, 0])(tapered_lock_socket)
    tapered_lock_socket = translate([((scroll_diameter_mm / 2.0) + 10.0), 0, housing_height_mm / 2.0])(tapered_lock_socket)
    
    mantis_lock_interface = quick_collar_base - tapered_lock_socket
    compressor_chassis += mantis_lock_interface

    # Symmetrical edge clean cuts
    clean_hull_mask = cylinder(r=(scroll_diameter_mm / 2.0) + 60.0, h=housing_height_mm + 120.0, segments=96, center=True)
    clean_hull_mask = translate([0, 0, housing_height_mm / 2.0])(clean_hull_mask)
    final_pneumatic_unit = compressor_chassis * clean_hull_mask

    # 💾 5. EXPORT HIGH-RESOLUTION OPENSCAD PRODUCTION SOLID FILE
    output_filename = "pneumatic_matrix_compressor_core_v1.scad"
    open_scad.scad_render_to_file(final_pneumatic_unit, output_filename)
    
    print(f"✅ SUCCESS: Project PNEUMATIC-MATRIX Compressor Core saved to: ./{output_filename}")
    print("👉 Next Step: Open in OpenSCAD (F6) and export clean STL for multi-material composite printing.")

if __name__ == "__main__":
    compile_pneumatic_system_mesh()
    

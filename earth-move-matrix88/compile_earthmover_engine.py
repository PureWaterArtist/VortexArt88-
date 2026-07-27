#!/usr/bin/env python3
"""
PROJECT EARTH-MOVE: Subterranean Transit Core Compiler
Path: earth-move-matrix88/compile_earthmover_engine.py
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

Programmatically compiles the complete high-efficiency biomimetic digging engine.
Integrates cicada-inspired acoustic cavitation heads, radial root-expansion shells,
and an internal peristaltic earthworm propulsion tube into a unified solid model.
"""

from solid import open_scad, cylinder, translate, rotate, cube, union
import math

def compile_subterranean_earthmover_engine():
    print("=========================================================================")
    print("🛰️  COMPUTING EXPANDED BIOMIMETIC EARTH-MOVE ARCHITECTURE...")
    print("=========================================================================\n")
    
    # 📏 METROLOGY & STRUCTURAL PARAMETERS (From config/technical-specs.md)
    chassis_length = 400.0     # 400mm modular block tunnel segment length
    nose_diameter_mm = 120.0   # 120mm primary acoustic cavitation head diameter
    expansion_shell_r = 80.0   # 160mm base radial expansion outer profile radius
    chassis_wall = 5.0         # 5mm solid elastomeric wall boundary depth
    capillary_width_um = 120.0 # 120-micron internal air logic capillaries
    capillary_radius_mm = (capillary_width_um / 2.0) / 1000.0
    
    num_piezo_nodes = 12       # 12 high-intensity 40.0 kHz transducer blocks in head
    num_internal_capillaries = 36 # 36 hollow air tracks embedded inside expansion walls
    
    # 🏛️ 1. BASE SOLID RADIAL ROOT-TIP EXPANSION HOUSING
    outer_shell = cylinder(
        r=expansion_shell_r + chassis_wall,
        h=chassis_length,
        segments=96  # High coordinate resolution for seamless wall sliding
    )
    
    inner_core_void = cylinder(
        r=expansion_shell_r,
        h=chassis_length + 0.2,
        segments=96
    )
    inner_core_void = translate([0, 0, -0.1])(inner_core_void)
    
    # Establish the hollow expansion shell boundary via solid subtraction
    earthmover_chassis = outer_shell - inner_core_void

    # 🏛️ 2. ETCH INTERNAL 120-MICRON COMPRESSED AIR LINES
    # Wears out 36 vertical microfluidic tracks inside the 5mm outer walls
    capillary_cuts = []
    angle_step = 360.0 / num_internal_capillaries
    mid_wall_radius = expansion_shell_r + (chassis_wall / 2.0)
    
    for c in range(num_internal_capillaries):
        current_angle = c * angle_step
        rad_angle = math.radians(current_angle)
        
        cx = mid_wall_radius * math.cos(rad_angle)
        cy = mid_wall_radius * math.sin(rad_angle)
        
        micro_channel = cylinder(
            r=capillary_radius_mm,
            h=chassis_length + 10.0,
            segments=12
        )
        micro_channel = translate([cx, cy, -5.0])(micro_channel)
        capillary_cuts.append(micro_channel)
        
    for cut in capillary_cuts:
        earthmover_chassis = earthmover_chassis - cut

    # 🪱 3. INTEGRATE THE PERISTALTIC EARTHWORM TRANSPORT CORE
    # Embeds the central 80mm inner pumping tube to squeeze loose sand slurry backward
    transport_core_void = cylinder(r=40.0, h=chassis_length + 2.0, segments=96)
    transport_core_void = translate([0, 0, -1.0])(transport_core_void)
    
    # Create internal segment ring flaps that pulse sequentially to trap slurry flow
    internal_flaps = []
    for ring in range(8):
        z_pos = (ring * (chassis_length / 8.0)) + 25.0
        flap_ring = cylinder(r1=44.0, r2=40.0, h=4.0, segments=96)
        internal_flaps.append(translate([0, 0, z_pos])(flap_ring))
        
    for flap in internal_flaps:
        earthmover_chassis += flap
        
    # Re-clear the main central transportation void
    earthmover_chassis = earthmover_chassis - transport_core_void

    # 🦔 4. MODEL ACOUSTIC NOSE CONE INTERFACE & HOUSING
    # Position mounting rings for the 12 high-intensity 40.0 kHz piezoelectric blocks
    piezo_mounts = []
    for p in range(num_piezo_nodes):
        piezo_angle = p * (360.0 / num_piezo_nodes)
        mount_block = cube([12.0, 12.0, 20.0], center=True)
        mount_block = translate([expansion_shell_r + chassis_wall, 0, chassis_length - 15.0])(mount_block)
        mount_block = rotate([0, -15.0, piezo_angle])(mount_block) # Angle forward to cross focal line
        piezo_mounts.append(mount_block)
        
    for mount in piezo_mounts:
        earthmover_chassis += mount

    # 💾 5. EXPORT COMPLIANT SOLID OPENSCAD BLUEPRINT FILE
    output_filename = "earth_move_transit_engine_v1.scad"
    open_scad.scad_render_to_file(earthmover_chassis, output_filename)
    
    print(f"✅ SUCCESS: Project EARTH-MOVE Subterranean Module saved to: ./{output_filename}")
    print("👉 Next Step: Open in OpenSCAD, press F6 to compute geometries, and F7 to export your production STL.")

if __name__ == "__main__":
    compile_subterranean_earthmover_engine()
  

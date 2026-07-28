#!/usr/bin/env python3
"""
PROJECT WATER-RECLAIM: Mangrove-Biomimetic Graywater Filter Core Compiler
Path: sovereign-family-infrastructure/water-reclaim-matrix88/compile_filter_engine.py
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

Programmatically compiles the complete multi-stage cascade gravity filtration cabinet.
Integrates 20nm absolute graphene sieve slide tracks, a perforated carbon pack bed,
and a passive solar parabolic UV-sanitization fluid track.
"""

from solid import open_scad, cylinder, translate, rotate, cube, union

def compile_mangrove_filter_chassis():
    print("=========================================================================")
    print("🛰️  COMPUTING PARAMETRIC CLOSED-LOOP MANGROVE SIFT CABINET...")
    print("=========================================================================\n")
    
    # 📏 METROLOGY & STRUCTURAL PARAMETERS (From config/technical-specs.md)
    cabinet_h = 600.0          # 600mm multi-stage processing vertical axis
    cabinet_w = 250.0          # 250mm modular compact footprint width
    wall_thickness = 4.0       # 4mm sturdy structural PLA boundary plates
    
    # 🏛️ 1. STRUCTURAL FILTRATION CABINET SHELL BOUNDARY
    outer_hull = cube([cabinet_w, cabinet_w, cabinet_h], center=True)
    outer_hull = translate([0, 0, cabinet_h / 2.0])(outer_hull)
    
    inner_chamber_void = cube([cabinet_w - (wall_thickness*2.0), cabinet_w - (wall_thickness*2.0), cabinet_h + 2.0], center=True)
    inner_chamber_void = translate([0, 0, cabinet_h / 2.0])(inner_chamber_void)
    
    filter_chassis = outer_hull - inner_chamber_void
    
    # 🏛️ 2. INJECT MULTI-STAGE SLIDE CHANNELS FOR THE 20nm GRAPHENE MEMBRANES
    # Cuts matching 2mm deep perimeter grooves to slide filter plates without screws
    graphene_slot_1 = cube([cabinet_w + 2.0, cabinet_w - 6.0, 3.0], center=True)
    graphene_slot_1 = translate([0, 0, 400.0])(graphene_slot_1)
    
    graphene_slot_2 = cube([cabinet_w + 2.0, cabinet_w - 6.0, 3.0], center=True)
    graphene_slot_2 = translate([0, 0, 200.0])(graphene_slot_2)
    
    filter_chassis = filter_chassis - graphene_slot_1 - graphene_slot_2
    
    # 🏛️ 3. INTEGRATE THE LOWER PARABOLIC SOLAR UV-REFLECTOR CHUTE
    # Projects the borosilicate fluid path under the base plane exit lines
    uv_chute_outer = cylinder(r=30.0, h=cabinet_w - 10.0, segments=64)
    uv_chute_outer = rotate([0, 90, 0])(uv_chute_outer)
    uv_chute_outer = translate([-cabinet_w/2.0 + 5.0, 0, 35.0])(uv_chute_outer)
    
    uv_chute_inner = cylinder(r=26.0, h=cabinet_w + 20.0, segments=64)
    uv_chute_inner = rotate([0, 90, 0])(uv_chute_inner)
    uv_chute_inner = translate([-cabinet_w/2.0 - 10.0, 0, 35.0])(uv_chute_inner)
    
    parabolic_reflector = uv_chute_outer - uv_chute_inner
    filter_chassis += parabolic_reflector
    
    # 💾 4. EXPORT COMPLIANT CAD BLUEPRINT MODEL
    output_filename = "water_reclaim_mangrove_sieve_v1.scad"
    open_scad.scad_render_to_file(filter_chassis, output_filename)
    
    print(f"✅ SUCCESS: Project WATER-RECLAIM Sieve Chassis saved to: ./{output_filename}")
    print("👉 Next Step: Slice file with zero-void infill parameters for watertight durability.")

if __name__ == "__main__":
    compile_mangrove_filter_chassis()
  

#!/usr/bin/env python3
"""
PROJECT MAKER-UTILITY: Three-Tier Multi-Product Solid Core Compiler
Path: sovereign-family-infrastructure/maker-utility88/compile_utility_mesh.py
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

Programmatically compiles the 30-product solid-state mesh layout boundaries.
Delineates Section 1 (Moms), Section 2 (Working Dads), and Section 3 (Whole House)
with hard-locked 0.35mm print-in-place mechanical air gaps.
"""

from solid import open_scad, cylinder, translate, rotate, cube, union

def compile_three_tier_catalog_mesh():
    print("=========================================================================")
    print("🛰️  COMPUTING PARAMETRIC PROGRAMMATIC WORKSHOP THREE-TIER MESHES...")
    print("=========================================================================\n")
    
    # 📏 GENERAL METROLOGY CONSTRAINTS (From config/technical-specs.md)
    base_diameter_mm = 50.0
    thickness_mm = 12.0
    clearance_gap_mm = 0.35  # 0.35mm mechanical moving air gap
    
    # 🤱 SUITE 01 ELEMENT: THE CRAB-CLAW JUICE BOX PROTECTIVE BLOCK CORE (UTL-01)
    mom_outer_shield = cylinder(r=base_diameter_mm / 2.0, h=thickness_mm, segments=64)
    mom_inner_box_void = cube([22.0, 32.0, thickness_mm + 4.0], center=True)
    mom_inner_box_void = translate([0, 0, thickness_mm / 2.0])(mom_inner_box_void)
    
    section_1_mesh = mom_outer_shield - mom_inner_box_void
    
    # 🔨 SUITE 02 ELEMENT: THE HAMMER-HEAD SHOCK-ABSORBING SLEEVE HUB (UTL-11)
    dad_grip_outer = cylinder(r=(base_diameter_mm / 2.0) - 2.0, h=thickness_mm * 2.0, segments=64)
    dad_internal_handle_void = cylinder(r=12.5, h=thickness_mm * 2.0 + 4.0, segments=64)
    
    # Etch 6 micro-lattice glass-sponge shock absorber grooves inside the wall
    for i in range(6):
        angle = i * 60.0
        groove = cube([4.0, (base_diameter_mm / 2.0), thickness_mm * 2.0 + 2.0], center=True)
        groove = rotate([0, 0, angle])(groove)
        groove = translate([0, 0, thickness_mm])(groove)
        dad_grip_outer = dad_grip_outer - groove
        
    section_2_mesh = dad_grip_outer - dad_internal_handle_void
    
    # 🏡 SUITE 03 ELEMENT: THE CARDIOID NAUTILUS WIRE ORGANIZER CORE (UTL-21)
    house_base = cylinder(r=base_diameter_mm / 2.0, h=thickness_mm, segments=64)
    
    # Mechanical Print-in-Place moving lock track clearance channels
    hinge_housing = cylinder(r=5.0, h=thickness_mm, segments=32)
    hinge_housing = translate([18.0, 0, 0])(hinge_housing)
    hinge_clearance = cylinder(r=3.5 + clearance_gap_mm, h=thickness_mm + 2.0, segments=32)
    hinge_clearance = translate([18.0, 0, -1.0])(hinge_clearance)
    hinge_pin = cylinder(r=3.5, h=thickness_mm, segments=32)
    hinge_pin = translate([18.0, 0, 0])(hinge_pin)
    
    moving_latch = (hinge_housing - hinge_clearance) + hinge_pin
    section_3_mesh = house_base + moving_latch
    
    # UNIFY THREE-TIER SHOWROOM PATTERN INTO A SINGLE COMPILED SCAD FILE
    compiled_catalog = (
        translate([-60.0, 0, 0])(section_1_mesh) + 
        translate([0, 0, 0])(section_2_mesh) + 
        translate([60.0, 0, 0])(section_3_mesh)
    )
    
    # 💾 EXPORT HIGH-RESOLUTION SCAD PRODUCTION SOLID BLUEPRINT
    output_filename = "maker_utility_three_tier_catalog_v2.scad"
    open_scad.scad_render_to_file(compiled_catalog, output_filename)
    
    print(f"✅ SUCCESS: Restructured Three-Tier Slicers Core saved to: ./{output_filename}")
    print("👉 Next Step: Open in OpenSCAD (F6) and click to view the side-by-side solid-state layout prints.")

if __name__ == "__main__":
    compile_three_tier_catalog_mesh()
    

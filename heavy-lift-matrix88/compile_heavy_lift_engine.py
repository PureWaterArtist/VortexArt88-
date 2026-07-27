#!/usr/bin/env python3
"""
PROJECT HEAVY-LIFT: Muscular Hydrostat & Auxetic Truss Core Compiler
Path: vortex-heavy-lift-vox88/compile_heavy_lift_engine.py
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

Programmatically compiles the complete high-efficiency biomimetic mass-handling engine.
Integrates banyan-inspired auxetic lattices, elephant-trunk muscular hydrostat chambers,
and a modular gecko setae base pad mounting interface into a unified 3D-printable solid model.
"""

from solid import open_scad, cylinder, translate, rotate, cube, union
import math

def compile_heavy_lift_actuator_engine():
    print("=========================================================================")
    print("🛰️  COMPUTING EXPANDED BIOMIMETIC HEAVY-LIFT ENGINE ARCHITECTURE...")
    print("=========================================================================\n")
    
    # 📏 METROLOGY & STRUCTURAL PARAMETERS (From config/technical-specs.md)
    arm_segment_height = 500.0  # 500mm height per modular structural block segment
    base_outer_r = 90.0        # 180mm base actuator core outer diameter profile
    chassis_wall = 6.0         # 6mm thick solid structural boundary shell wall
    capillary_width_um = 120.0 # 120-micron internal microfluidic air logic tracking lines
    capillary_radius_mm = (capillary_width_um / 2.0) / 1000.0
    
    num_auxetic_cells = 6       # 6 symmetrical banyan star cell rows per face
    num_vascular_sectors = 4    # 4 distinct quadrant chambers for elephant-trunk flexion
    num_internal_capillaries = 36 # 36 hollow air logic tracks embedded in muscle walls
    
    # 🏛️ 1. BASE SOLID ELEPHANT-TRUNK HYDROSTAT CASING
    outer_skin = cylinder(
        r=base_outer_r + chassis_wall,
        h=arm_segment_height,
        segments=96  # High coordinate resolution for flawless structural flow
    )
    
    inner_core_void = cylinder(
        r=base_outer_r,
        h=arm_segment_height + 0.2,
        segments=96
    )
    inner_core_void = translate([0, 0, -0.1])(inner_core_void)
    
    # Establish the hollow muscular hydrostat cylinder profile shell via solid subtraction
    hydrostat_chassis = outer_skin - inner_core_void

    # 🏛️ 2. ETCH INTERNAL 120-MICRON AIR LOGIC CAPILLARY TRACKS
    # Wears out 36 separate vertical void tracks inside the 6mm flexible polymer walls
    capillary_cuts = []
    angle_step = 360.0 / num_internal_capillaries
    mid_wall_radius = base_outer_r + (chassis_wall / 2.0)
    
    for c in range(num_internal_capillaries):
        current_angle = c * angle_step
        rad_angle = math.radians(current_angle)
        
        # Position the microfluidic channel directly at the center axis of the wall
        cx = mid_wall_radius * math.cos(rad_angle)
        cy = mid_wall_radius * math.sin(rad_angle)
        
        micro_channel = cylinder(
            r=capillary_radius_mm,
            h=arm_segment_height + 10.0,
            segments=12
        )
        micro_channel = translate([cx, cy, -5.0])(micro_channel)
        capillary_cuts.append(micro_channel)
        
    for cut in capillary_cuts:
        hydrostat_chassis = hydrostat_chassis - cut

    # 🏛️ 3. INTEGRATE THE INVERTED AUXETIC BANYAN SKELETON TRUSS
    # Builds an external cardioid star matrix structure that hardens automatically under load tension
    auxetic_features = []
    cell_height = arm_segment_height / num_auxetic_cells
    
    for layer in range(num_auxetic_cells):
        z_pos = layer * cell_height
        
        for face in range(4): # Project structural star cells symmetrically across 4 outer faces
            face_angle = face * 90.0
            
            # Form an inverted auxetic cardioid star profile out of interlocking diamond cubes
            star_node_1 = cube([15.0, 15.0, cell_height * 0.5], center=True)
            star_node_1 = rotate([0, 0, 45])(star_node_1)
            star_node_1 = translate([base_outer_r + chassis_wall + 5.0, 0, z_pos + (cell_height * 0.25)])(star_node_1)
            star_node_1 = rotate([0, 0, face_angle])(star_node_1)
            
            star_node_2 = cube([15.0, 15.0, cell_height * 0.5], center=True)
            star_node_2 = rotate([0, 0, 45])(star_node_2)
            star_node_2 = translate([base_outer_r + chassis_wall + 5.0, 0, z_pos + (cell_height * 0.75)])(star_node_2)
            star_node_2 = rotate([0, 0, face_angle])(star_node_2)
            
            auxetic_features.append(star_node_1)
            auxetic_features.append(star_node_2)
            
    for star in auxetic_features:
        hydrostat_chassis += star

    # Re-core the central void one final time to keep the internal inner track pristine
    hydrostat_chassis = hydrostat_chassis - inner_core_void

    # 🏛️ 4. MODEL INTERNAL REINFORCING SECTOR FLAP CHAMBERS
    # Divides the arm into 4 distinct quadrants for directional elephant-trunk flexion
    sector_walls = []
    for s in range(num_vascular_sectors):
        sector_angle = s * 90.0
        divider_wall = cube([base_outer_r * 2.0, 4.0, arm_segment_height], center=True)
        divider_wall = translate([0, 0, arm_segment_height / 2.0])(divider_wall)
        divider_wall = rotate([0, 0, sector_angle])(divider_wall)
        sector_walls.append(divider_wall)
        
    # Hollow out the dividers slightly so air logic can pass internally between quadrants
    for wall in sector_walls:
        hydrostat_chassis += (wall - cylinder(r=base_outer_r - 20.0, h=arm_segment_height + 2.0, segments=96))

    # 🏛️ 5. UNIVERSAL MODULAR GECKO SETAE MOUNTING INTERFACE (BASE LINK)
    # Forms a strict, 1mm-tolerance slide rim that lets the arm segment lock flat onto the carbon nanotube feet pads
    base_mount_outer = cylinder(r=base_outer_r + chassis_wall + 10.0, h=40.0, segments=96)
    base_mount_inner = cylinder(r=base_outer_r + 1.0, h=42.0, segments=96) # 1mm strict slide seat tolerance
    base_mount_inner = translate([0, 0, -1.0])(base_mount_inner)
    
    molded_interlock_lip = base_mount_outer - base_mount_inner
    molded_interlock_lip = translate([0, 0, -39.5])(molded_interlock_lip) # Position directly beneath base plane
    
    final_integrated_assembly = hydrostat_chassis + molded_interlock_lip

    # 💾 6. EXPORT COMPLIANT SOLID OPENSCAD SCRIPT
    output_filename = "heavy_lift_actuator_v1_expanded.scad"
    open_scad.scad_render_to_file(final_integrated_assembly, output_filename)
    
    print(f"✅ SUCCESS: Heavy-Lift V1 Biomimetic Actuator Module saved to: ./{output_filename}")
    print("👉 Next Step: Open in OpenSCAD, press F6 to compute full geometry, and F7 to export your production STL.")

if __name__ == "__main__":
    compile_heavy_lift_actuator_engine()
          

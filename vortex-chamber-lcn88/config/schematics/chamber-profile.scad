// =========================================================================
// PROJECT LCN-88: LEMNISCATE COLLISION NODE (FIGURE-8 CHAMBER)
// Schematics Module: Scale-Invariant Parametric Fluid Engine v1.0.0
// Licensed under CERN-OHL-S-2.0 (Strongly Reciprocal Open Hardware)
// =========================================================================

$fn = 120; // High-resolution layout factor for cleanroom slicing metrics

// --- UNALTERABLE SPATIAL ORIGIN ---
origin_x = 0.00;
origin_y = 0.00;
origin_z = 0.00;

// --- PARAMETRIC INPUT ATTRIBUTES (Keyed to hardware-bom.json) ---
nozzle_od = 25.4;        // Baseline outer diameter of the nozzle exit throat (mm)
print_clearance = 0.18;  // Slip-fit tolerance uniform air gap boundary (mm)
wall_thickness = 4.5;    // Structural wall loop container thickness for high pressure
chamber_radius = 22.0;   // Internal radius of the overlapping fluid rollers
focal_distance = 18.5;   // X-axis offset from origin to centerline of internal vortices
port_diameter = 12.0;    // Induction and drainage track bore diameter
chamber_height = 44.0;   // Total vertical volume height of the mixing core

receiver_id = nozzle_od + (print_clearance * 2);

module InternalFluidCore() {
    // Left Fluid Roller Cylinder (Nozzle B Matrix Loop)
    translate([-focal_distance, 0, 0])
        cylinder(h=chamber_height, r=chamber_radius, center=true);
    
    // Right Fluid Roller Cylinder (Nozzle A Matrix Loop)
    translate([focal_distance, 0, 0])
        cylinder(h=chamber_height, r=chamber_radius, center=true);
        
    // High-Velocity Tangential Inlet Receivers
    // Nozzle A Receiver: Positive X-Axis Vector (1,0,0) entering toward origin
    translate([focal_distance + chamber_radius, -chamber_radius, 0])
        rotate([0, 90, 0])
            cylinder(h=40, r=receiver_id/2, center=true);
            
    // Nozzle B Receiver: Negative X-Axis Vector (-1,0,0) entering toward origin
    translate([-(focal_distance + chamber_radius), chamber_radius, 0])
        rotate([0, 90, 0])
            cylinder(h=40, r=receiver_id/2, center=true);

    // Z-Axis Inflow Continuum Path (Atmospheric Port)
    translate([0, 0, chamber_height/2])
        cylinder(h=20, r=port_diameter/2, center=true);

    // Z-Axis Outflow Continuum Path (Discharge Drainage Port)
    translate([0, 0, -chamber_height/2])
        cylinder(h=20, r=port_diameter/2, center=true);
}

module ExternalHousingShell() {
    // Outer Protective Boundary Layer Container
    hull() {
        translate([-focal_distance, 0, 0])
            cylinder(h=chamber_height + (wall_thickness * 2), r=chamber_radius + wall_thickness, center=true);
        translate([focal_distance, 0, 0])
            cylinder(h=chamber_height + (wall_thickness * 2), r=chamber_radius + wall_thickness, center=true);
    }
}

// --- MASTER DIFFERENCE COMPILATION ---
difference() {
    ExternalHousingShell();
    InternalFluidCore();
    
    // Cleanroom Alignment Keyways (To prevent rotational displacement during torque setup)
    translate([0, chamber_radius + (wall_thickness/2), 0])
        cube([3.0, 3.0, chamber_height + 20], center=true);
    translate([0, -(chamber_radius + (wall_thickness/2)), 0])
        cube([3.0, 3.0, chamber_height + 20], center=true);
}


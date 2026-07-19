// =========================================================================
// PROJECT ARMW-88: PARAMECTRIC modular ARM SLEEVE ENGINE
// Modules Subsystem: Forearm Slider Tracks, Bicep Cuffs, & TPU Joints v1.0.0
// Licensed under CERN-OHL-S-2.0 (Strongly Reciprocal Open Hardware)
// =========================================================================

$fn = 120; // High-resolution layout factor for cleanroom circular components

// --- PARAMETRIC INPUT ATTRIBUTES (Keyed to hardware-bom.json) ---
forearm_id = 95.0;         // Inner clearance width for forearm protection (mm)
bicep_id = 125.0;          // Inner clearance width for bicep cuff protection (mm)
rail_width = 14.0;         // Linear rail track groove width for wing joint (mm)
rail_depth = 10.0;         // Linear rail track groove depth for wing joint (mm)
arm_total_length = 420.0;  // Total longitudinal span of the limb framework (mm)
shoulder_pin_bore = 16.0;  // Sizing for torso-mating connection rods (mm)
shell_wall = 5.5;          // Structural wall thickness of the carbon shell (mm)

module ForearmChassisSleeve() {
    // Rigid outer forearm block housing the linear slider tracks
    difference() {
        cylinder(h=arm_total_length*0.55, r=(forearm_id/2) + shell_wall, center=true);
        cylinder(h=(arm_total_length*0.55) + 10, r=forearm_id/2, center=true);
        
        // Carve the external continuous linear sliding guide rail tracks
        translate([(forearm_id/2) + shell_wall - (rail_depth/2), 0, 0])
            cube([rail_depth + 2.0, rail_width, (arm_total_length*0.55) + 5], center=true);
    }
}

module BicepCuffChassis() {
    // Upper bicep structural collar featuring the torso tongue attachment joint
    difference() {
        cylinder(h=arm_total_length*0.30, r=(bicep_id/2) + shell_wall, center=true);
        cylinder(h=(arm_total_length*0.30) + 10, r=bicep_id/2, center=true);
        
        // Transverse shoulder detent pin integration bore
        translate([0, 0, (arm_total_length*0.12)])
            rotate([0, 90, 0])
                cylinder(h=bicep_id + 40, r=shoulder_pin_bore/2, center=true);
    }
}

module ElbowAccordionBellowsWell() {
    // Intermediate pleated section placeholder allowing multi-axial flex paths
    difference() {
        cylinder(h=45, r=((forearm_id + bicep_id)/4) + shell_wall + 2.0, center=true);
        cylinder(h=55, r=((forearm_id + bicep_id)/4) - 2.0, center=true);
        
        // Micro-fluidic bus loops cuts for liquid gallium wire simulation
        for (i = [-12, 0, 12]) {
            translate([0, 0, i])
                rotate_extrude(angle=360)
                    translate([((forearm_id + bicep_id)/4) + 1.0, 0, 0])
                        circle(r=1.5);
        }
    }
}

// --- MASTER MODULAR ARM ASSEMBLAGE COMPILATION ---
union() {
    // Position the forearm tracking mass block
    translate([0, 0, -(arm_total_length*0.22)])
        ForearmChassisSleeve();
        
    // Position the flexible elbow core well (Printed out of TPU-95A)
    translate([0, 0, 15])
        %ElbowAccordionBellowsWell();
        
    // Position the upper shoulder bicep assembly joint
    translate([0, 0, (arm_total_length*0.32)])
        BicepCuffChassis();
}

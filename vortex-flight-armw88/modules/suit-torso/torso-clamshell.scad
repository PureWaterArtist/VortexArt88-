// =========================================================================
// PROJECT ARMW-88: MODULAR TORSO FLIGHT CHASSIS ENGINE
// Modules Subsystem: Interlocking Clamshell & Toroidal Vortex Shield v1.0.0
// Licensed under CERN-OHL-S-2.0 (Strongly Reciprocal Open Hardware)
// =========================================================================

$fn = 120; // High-resolution layout factor for cleanroom resodynamic arcs

// --- PARAMETRIC INPUT ATTRIBUTES (Keyed to hardware-bom.json) ---
torso_width_inner = 340.0;     // Internal clearance width for pilot's chest ribs (mm)
torso_depth_inner = 260.0;     // Internal front-to-back clearance depth (mm)
torso_height = 580.0;          // Total vertical length of the torso chassis (mm)
armor_thickness = 12.0;       // Thickness of carbon-fiber composite armor shielding (mm)
vortex_ring_radius = 45.0;     // Radius of collarbone vortex resonator chambers (mm)
vortex_throat_width = 3.5;    // Jet pinch exit gap for kinetic shield boundary (mm)
jet_intake_diameter = 95.0;    // Diameter of rear squid ram-air induction ports (mm)
shoulder_pin_bore = 16.0;      // Bore sizing for modular arm socket connection rods (mm)
central_dial_radius = 35.0;    // Structural footprint of center chest locking dial (mm)

module TorsoOuterArmorMass() {
    // Generates the base aerodynamic exterior torso-shield geometry
    resize([torso_width_inner + (armor_thickness*2), torso_depth_inner + (armor_thickness*2), torso_height])
        cylinder(h=1, r=10, center=true);
}

module InternalTorsoCavity() {
    // Hollow inner chamber carved out for pilot chassis seating and liner loops
    resize([torso_width_inner, torso_depth_inner, torso_height - 16])
        cylinder(h=1, r=10, center=true);
}

module ToroidalVortexResonatorChambers() {
    // Concentric collarbone cavities that spin ram-air to project the kinetic shield
    for (i = [-1, 1]) {
        translate([i * (torso_width_inner/3), 0, (torso_height/2) - 30]) {
            // Hollow internal toroidal vortex ring
            rotate_extrude(angle=360)
                translate([vortex_ring_radius, 0, 0])
                    circle(r=12.0);
            
            // Continuous micro-Venturi jet pinch slit pointing upward/outward
            rotate_extrude(angle=360)
                translate([vortex_ring_radius + 4.0, 0, 0])
                    square([vortex_throat_width, 15.0], center=true);
        }
    }
}

module RearSquidRamAirIntakes() {
    // Twin rear induction channels routing compressed air to fluid systems and nozzles
    for (i = [-1, 1]) {
        translate([i * 75, -(torso_depth_inner/2) - armor_thickness/2, 60])
            rotate([90, 0, 0]) {
                cylinder(h=armor_thickness + 20, r=jet_intake_diameter/2, center=true);
                // Internal spiral pathway compression layout indicator
                %cylinder(h=armor_thickness + 22, r=(jet_intake_diameter/2) - 4, center=true);
            }
    }
}

module ShoulderSocketArmAnchors() {
    // Heavy-duty upper side bores for arm sleeve quick-release detent bars
    for (i = [-1, 1]) {
        translate([i * ((torso_width_inner/2) + armor_thickness/2), 0, (torso_height/2) - 80])
            rotate([0, 90, 0])
                cylinder(h=armor_thickness + 30, r=shoulder_pin_bore/2, center=true);
    }
}

module CentralChestLockingDialRegistry() {
    // Center front cutout cavity housing the mechanical interlocking link bars
    translate([0, (torso_depth_inner/2) + armor_thickness/2, 20])
        rotate([90, 0, 0])
            cylinder(h=armor_thickness + 10, r=central_dial_radius, center=true);
}

module ClamshellHingedSplitLine() {
    // Lateral structural plane separating the chassis into distinct Front and Back plates
    translate()
        cube([torso_width_inner + (armor_thickness * 3), torso_depth_inner + (armor_thickness * 3), 1.5], center=true);
}

// --- MASTER COMPONENT COMPILATION ---
// Slicers differ front/back by running standard solid intersection/difference flags
difference() {
    TorsoOuterArmorMass();
    InternalTorsoCavity();
    ToroidalVortexResonatorChambers();
    RearSquidRamAirIntakes();
    ShoulderSocketArmAnchors();
    CentralChestLockingDialRegistry();
    
    // Superior neck collar boundary cut
    translate([0, 0, (torso_height/2) + 5])
        cylinder(h=40, r=90.0, center=true);
        
    // Inferior waist exit boundary flare cut
    translate([0, 0, -(torso_height/2) - 5])
        cylinder(h=40, r1=180.0, r2=150.0, center=true);
}

// Visual Indicator: Maps the lateral clamshell mating split line for the developer
%rotate([0, 90, 0]) ClamshellHingedSplitLine();

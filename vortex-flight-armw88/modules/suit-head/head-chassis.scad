// =========================================================================
// PROJECT ARMW-88: MODULAR FLIGHT HELMET CHASSIS ENGINE
// Modules Subsystem: Two-Piece Faraday-Cage Head Shield v1.0.0
// Licensed under CERN-OHL-S-2.0 (Strongly Reciprocal Open Hardware)
// =========================================================================

$fn = 120; // High-resolution layout factor for cleanroom structural arcs

// --- PARAMETRIC INPUT ATTRIBUTES (Keyed to hardware-bom.json) ---
head_width_inner = 165.0;     // Internal clearance width for skull comfort (mm)
head_length_inner = 210.0;    // Internal clearance length from brow to occipital (mm)
helmet_height = 240.0;        // Total vertical height of the helmet unit (mm)
shell_thickness = 8.0;        // Thickness of carbon-fiber composite shielding shell (mm)
visor_width = 140.0;          // Horizontal span of the front flat optics visor window (mm)
visor_height = 75.0;          // Vertical span of the front flat optics visor window (mm)
armo_lens_thick = 2.5;        // Thickness of integrated ARMO-88 substrate flange (mm)
detent_pin_bore = 8.0;        // Sizing for mechanical jawline quick-release pins (mm)

module HelmetOuterMass() {
    // Generates the base aerodynamic exterior head-shield geometry
    resize([head_width_inner + (shell_thickness*2), head_length_inner + (shell_thickness*2), helmet_height])
        cylinder(h=1, r=10, center=true);
}

module InternalSkullCavity() {
    // Hollow inner chamber carved out for pilot comfort and padding integration
    resize([head_width_inner, head_length_inner, helmet_height - 12])
        cylinder(h=1, r=10, center=true);
}

module PassiveVisorRetentionWell() {
    // Carves the front viewport and steps a precise seat flange for ARMO-88 metalenses
    translate([0, (head_length_inner/2) + shell_thickness/2, 20]) {
        // Main view-through cutout hole
        cube([visor_width - 6, shell_thickness + 10, visor_height - 6], center=true);
        
        // Step flange shelf to secure the sub-wavelength optics plates
        translate([0, -(shell_thickness/2) + (armo_lens_thick/2), 0])
            cube([visor_width, armo_lens_thick + 0.1, visor_height], center=true);
    }
}

module AcousticTemporalWaveguides() {
    // Left and right sub-millimeter spiral channels matching the ear arrays
    for (i = [-1, 1]) {
        translate([i * ((head_width_inner/2) + shell_thickness/2), -15, -20])
            rotate([0, 90 * i, 0])
                cylinder(h=shell_thickness + 10, r=12.0, center=true);
    }
}

module JawlineQuickReleaseDetents() {
    // Transverse anchoring channels for spring-loaded locking pins at the base rim
    translate([0, 0, -(helmet_height/2) + 20]) {
        translate([-((head_width_inner/2) + shell_thickness/2), 0, 0])
            rotate([0, 90, 0]) cylinder(h=40, r=detent_pin_bore/2, center=true);
        translate([((head_width_inner/2) + shell_thickness/2), 0, 0])
            rotate([0, 90, 0]) cylinder(h=40, r=detent_pin_bore/2, center=true);
    }
}

module FaradayInterlockingSeam() {
    // Tongue-and-groove slicing block to split the helmet into clean front/rear halves
    translate([0, 0, 0])
        cube([head_width_inner + (shell_thickness * 3), 1.5, helmet_height + 20], center=true);
}

// --- MASTER COMPONENT COMPILATION ---
// To output a distinct half, wrap a section in an intersection or difference block
difference() {
    HelmetOuterMass();
    InternalSkullCavity();
    PassiveVisorRetentionWell();
    AcousticTemporalWaveguides();
    JawlineQuickReleaseDetents();
    
    // Bottom opening throat entry flare relief
    translate([0, 0, -(helmet_height/2) - 10])
        cylinder(h=40, r1=head_width_inner/1.2, r2=head_width_inner/2, center=true);
}

// Visual Indicator: Showcase the split seam layout route for the fabricator
%FaradayInterlockingSeam();
// --- BIOMIMETIC KINETIC & THERMAL LINER ARRAY SUBSYSTEM ---
// Mimics woodpecker endocranial sponge structures and desert ant thermal conduits

liner_thickness = 14.0; // Thickness of the compliant, energy-absorbing liner layer (mm)

module BiomimeticSpongeLiner() {
    // 3D printed out of variable durometer flexible TPU to damp high G-force acceleration
    difference() {
        // Outer layer contours exactly to the internal skull cavity bounds
        resize([head_width_inner - 0.2, head_length_inner - 0.2, helmet_height - 12.2])
            cylinder(h=1, r=10, center=true);
            
        // Inner clearance envelope facing the pilot's padded head sock
        resize([head_width_inner - (liner_thickness*2), head_length_inner - (liner_thickness*2), helmet_height - 12 - liner_thickness])
            cylinder(h=1, r=10, center=true);
            
        // Passive micro-fluidic thermal cooling channels (Sahara Ant template)
        for (y = [-head_length_inner/2 : 12 : head_length_inner/2]) {
            translate([0, y, 0])
                rotate([90, 0, 0])
                    cylinder(h=3.5, r=1.2, center=true);
        }
    }
}

module LinerSnapRetentionAnchors() {
    // Cylindrical push-pin tabs to mechanically lock the liner into the shell without glue
    for (i = [0 : 90 : 270]) {
        rotate([0, 0, i])
            translate([(head_width_inner/2) - 2, 0, 0])
                cylinder(h=8, r=3.0, center=true);
    }
}

// NOTE FOR FABRICATOR: Print this independent block out of elastic, variable-density 
// flexible filament to secure full multi-axial shock and thermal management.
// To view or render the liner isolated, uncomment the line below:
// BiomimeticSpongeLiner();

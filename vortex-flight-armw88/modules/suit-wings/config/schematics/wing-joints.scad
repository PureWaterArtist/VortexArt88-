// =========================================================================
// PROJECT ARMW-88: PARAMETRIC MODULAR FLIGHT WING-JOINT ENGINE
// Modules Subsystem: Spine Root, Folding Hinges, & Slotted Vortextips v1.0.0
// Licensed under CERN-OHL-S-2.0 (Strongly Reciprocal Open Hardware)
// =========================================================================

$fn = 120; // High-resolution layout factor for cleanroom aerodynamic profiles

// --- PARAMETRIC INPUT ATTRIBUTES (Keyed to hardware-bom.json) ---
max_span = 2400.0;          // Maximum extended wingspan target (mm)
root_chord = 650.0;         // Wing root chord length width (mm)
jettison_travel = 120.0;    // Mechanical safety release cable pull depth (mm)
vortextip_slots = 4;        // Number of active slotted eagle wingtip segments
spine_wall = 12.0;          // Central spine mounting box reinforcement thickness (mm)
wing_thickness = 42.0;      // Maximum profile thickness of primary structural spars (mm)
hinge_pin_bore = 10.0;      // Sizing for multi-segmented wing section pivot pins (mm)

module CentralSpineRootBox() {
    // Rigid central root box interfacing directly with the torso harness frame
    difference() {
        // Main mounting block outer mass
        cube([180.0, 120.0, 220.0], center=true);
        
        // Internal hollow channel matching torso spine alignment rails
        cube([180.0 - (spine_wall * 2), 130.0, 220.0 - 24.0], center=true);
        
        // Transverse emergency jettison safety slide-rod release channels
        translate([0, 0, 45])
            rotate([0, 90, 0])
                cylinder(h=210, r=6.0, center=true);
        translate([0, 0, -45])
            rotate([0, 90, 0])
                cylinder(h=210, r=6.0, center=true);
    }
}

module MorphingHingeLinkages() {
    // Multi-segmented folding joints allowing real-time aspect ratio manipulation
    for (i = [-1, 1]) {
        translate([i * 110.0, 0, 0])
            difference() {
                // Outer joint hinge protective ear cuff
                cylinder(h=wing_thickness + 12.0, r=22.0, center=true);
                
                // Clearances for opposite morphing section pivot tongue
                cylinder(h=wing_thickness + 2.0, r=22.2, center=true);
                
                // Hardened structural pivot pin locking bore
                cylinder(h=wing_thickness + 30.0, r=hinge_pin_bore/2, center=true);
            }
    }
}

module PrimaryAirfoilSpars() {
    // High-tensile continuous lift-bearing wing rib spars (3K continuous filaments)
    for (i = [-1, 1]) {
        translate([i * (max_span / 4), 0, 0])
            rotate([0, i * 12, 0])
                difference() {
                    // Outer tapered wing profile representation block
                    resize([max_span / 2.2, root_chord, wing_thickness])
                        cylinder(h=1, r=10, center=true);
                    
                    // Internal micro-fluidic EGaIn static power bus tracking conduits
                    translate([0, 0, (wing_thickness/2) - 3.5])
                        rotate_extrude(angle=360)
                            circle(r=2.0);
                }
    }
}

module SlottedEagleVortextips() {
    // Flexible TPU tip slats that twist under high shear to break drag vortices
    for (i = [1 : vortextip_slots]) {
        translate([(max_span/2) - 80.0 + (i * 15.0), -(root_chord/4) + (i * 30.0), 0])
            rotate([0, i * 4, i * -8])
                difference() {
                    // Aerodynamic feather-profile curved trailing slat
                    resize([45.0, 180.0, 6.0])
                        cylinder(h=1, r=10, center=true);
                    
                    // Lightening reduction slot matching natural contouring density
                    resize([25.0, 140.0, 10.0])
                        cylinder(h=1, r=10, center=true);
                }
    }
}

// --- MASTER MODULAR WING ASSEMBLAGE COMPILATION ---
union() {
    // Secure centralized emergency-jettison spine root mounting block
    CentralSpineRootBox();
    
    // Position dynamic morphing joint pivot intersections
    MorphingHingeLinkages();
    
    // Materialize continuous lift-bearing high-aspect airfoil wing spars
    intersection() {
        PrimaryAirfoilSpars();
        // Restrict structural output profile clear of central torso mating zones
        cube([max_span + 20, root_chord + 20, wing_thickness + 40], center=true);
    }
    
    // Append left-side slotted eagle-wingtip passive drag vortex scatter arrays
    SlottedEagleVortextips();
    
    // Mirror and append right-side slotted vortex-shedding wingtip configurations
    mirror([1, 0, 0])
        SlottedEagleVortextips();
}

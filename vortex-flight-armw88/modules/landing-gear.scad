// =========================================================================
// PROJECT ARMW-88: BIOMIMETIC KINETIC DECELERATION LANDING EXOSKELETON
// Modules Subsystem: Kangaroo-Tendon Leaf-Spring Shock Absorber v1.0.0
// Licensed under CERN-OHL-S-2.0 (Strongly Reciprocal Open Hardware)
// =========================================================================

$fn = 120; // High-resolution layout factor for cleanroom structural arcs

// --- PARAMETRIC INPUT ATTRIBUTES (Keyed to hardware-bom.json) ---
leaf_travel_clearance = 150.0; // Structural compression travel buffer space (mm)
shin_sleeve_id = 110.0;        // Inner diameter to fit leg protective gear securely (mm)
spring_thickness = 12.0;       // Thickness profile of the carbon fiber leaf bands (mm)
detent_pin_bore = 12.0;        // Bore sizing for inox stainless quick-release pins (mm)
exoskeleton_height = 380.0;    // Total vertical length of the lower leg frame (mm)
chassis_wall = 6.0;            // Protective containment loop structural wall thickness (mm)

module ShinSleeveChassis() {
    // Rigid load-bearing upper collar wrapping the lower leg
    difference() {
        cylinder(h=80, r=(shin_sleeve_id/2) + chassis_wall, center=true);
        cylinder(h=90, r=shin_sleeve_id/2, center=true);
        
        // Locking pin mounting channels
        rotate([90, 0, 0])
            cylinder(h=shin_sleeve_id + 40, r=detent_pin_bore/2, center=true);
    }
}

module KangarooTendonLeafSprings() {
    // High-elasticity curved leaf loops that bend to absorb vertical touchdown impacts
    difference() {
        // Outer loop envelope geometry
        resize([shin_sleeve_id + 40, leaf_travel_clearance, exoskeleton_height/2])
            cylinder(h=1, r=10, center=true);
            
        // Hollow interior core defining the spring rate flex gap
        resize([shin_sleeve_id + 40 - (spring_thickness*2), leaf_travel_clearance - spring_thickness, exoskeleton_height/2 + 10])
            cylinder(h=1, r=10, center=true);
    }
}

module AnkleInterfaceSleeve() {
    // Lower foot anchor plate translating forces safely into ground contact surfaces
    translate([0, 0, -(exoskeleton_height/2) + 20])
        difference() {
            cylinder(h=40, r=(shin_sleeve_id/2) - 8, center=true);
            cylinder(h=50, r=(shin_sleeve_id/2) - 14, center=true);
        }
}

// --- MASTER LANDING EXOSKELETON ASSEMBLAGE ---
union() {
    // Position upper attachment cuff
    translate([0, 0, (exoskeleton_height/2) - 40])
        ShinSleeveChassis();
        
    // Position active kinetic spring loop elements
    translate([0, 0, -10])
        intersection() {
            KangarooTendonLeafSprings();
            // Restrict spring layout to flat side-band arrays
            cube([shin_sleeve_id + 60, spring_thickness * 3, exoskeleton_height], center=true);
        }
        
    // Position lower structural ankle connector
    AnkleInterfaceSleeve();
}

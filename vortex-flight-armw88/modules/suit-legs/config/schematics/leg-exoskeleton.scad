// =========================================================================
// PROJECT ARMW-88: PARAMETRIC MODULAR LEG CHASSIS ENGINE
// Modules Subsystem: Thigh Guards, Shin Sleeves, & Leaf-Spring Shock Absorber v1.0.0
// Licensed under CERN-OHL-S-2.0 (Strongly Reciprocal Open Hardware)
// =========================================================================

$fn = 120; // High-resolution layout factor for cleanroom structural arcs

// --- PARAMETRIC INPUT ATTRIBUTES (Keyed to hardware-bom.json) ---
thigh_id = 180.0;             // Inner clearance width for upper thigh guards (mm)
shin_id = 110.0;              // Inner clearance width for shin protection sleeves (mm)
leaf_travel_clearance = 150.0; // Structural compression travel buffer space (mm)
spring_thickness = 12.0;       // Thickness profile of the carbon fiber leaf bands (mm)
hip_pin_bore = 14.0;          // Bore sizing for torso-mating connection rods (mm)
leg_total_length = 760.0;     // Total longitudinal length of lower exoskeleton (mm)
chassis_wall = 6.0;            // Protective containment structural wall thickness (mm)

module ThighGuardChassis() {
    // Upper protective thigh collar featuring the hip locking attachment interface
    difference() {
        cylinder(h=leg_total_length*0.35, r=(thigh_id/2) + chassis_wall, center=true);
        cylinder(h=(leg_total_length*0.35) + 10, r=thigh_id/2, center=true);
        
        // Transverse hip quick-release detent pin connector bore
        translate([0, 0, (leg_total_length*0.12)])
            rotate([0, 90, 0])
                cylinder(h=thigh_id + 40, r=hip_pin_bore/2, center=true);
    }
}

module ShinSleeveChassis() {
    // Rigid load-bearing lower casing surrounding the calf muscles
    difference() {
        cylinder(h=leg_total_length*0.45, r=(shin_id/2) + chassis_wall, center=true);
        cylinder(h=(leg_total_length*0.45) + 10, r=shin_id/2, center=true);
        
        // Micro-etched active camouflage retention rows (1.5mm macro-groove profile)
        for (angle = [0 : 15 : 360]) {
            rotate([0, 0, angle])
                translate([(shin_id/2) + chassis_wall - 1.0, 0, 0])
                    cube([3.0, 1.2, leg_total_length*0.40], center=true);
        }
    }
}

module KangarooTendonLeafSprings() {
    // High-elasticity curved leaf loops that bend to absorb vertical touchdowns
    difference() {
        // Outer loop envelope geometry matching the 125,000 N/m flex target
        resize([shin_id + 50, leaf_travel_clearance, leg_total_length*0.25])
            cylinder(h=1, r=10, center=true);
            
        // Hollow interior core mapping the operational travel clearance bounds
        resize([shin_id + 50 - (spring_thickness*2), leaf_travel_clearance - spring_thickness, (leg_total_length*0.25) + 10])
            cylinder(h=1, r=10, center=true);
    }
}

module AnkleInterfacePlate() {
    // Lower foot lock-anchor plate translating structural forces to the boot array
    translate([0, 0, -(leg_total_length*0.48)])
        difference() {
            cylinder(h=35, r=(shin_id/2) + 2.0, center=true);
            cylinder(h=45, r=(shin_id/2) - 6.0, center=true);
        }
}

// --- MASTER MODULAR LEG ASSEMBLAGE COMPILATION ---
union() {
    // Position upper hip and thigh armor cell
    translate([0, 0, (leg_total_length*0.30)])
        ThighGuardChassis();
        
    // Position lower load-bearing shin and calibration loop tracks
    translate([0, 0, -(leg_total_length*0.15)])
        ShinSleeveChassis();
        
    // Position active kinetic leaf spring loop elements (Molded Pre-Preg Carbon Array)
    translate([0, 0, -(leg_total_length*0.30)])
        intersection() {
            KangarooTendonLeafSprings();
            // Restrict carbon spring layouts exclusively to vertical heel-stride bands
            cube([shin_id + 70, spring_thickness * 3.5, leg_total_length*0.30], center=true);
        }
        
    // Position lower structural boot attachment interface plate
    AnkleInterfacePlate();
}

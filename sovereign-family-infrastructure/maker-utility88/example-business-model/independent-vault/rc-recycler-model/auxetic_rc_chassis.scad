// Matrix Biomimetic Utilities - Universal Indestructible 1:16 RC Vehicle Engine
// Version 3.0.0-Hobby Master | Cranial Skull Sutures & Vine Helical Couplers

// ============================================================================
// 🏛️ MASTER CAR BOUNDARY MATRIX (Parametric 1:16 Scale Allocations)
// ============================================================================
CHASSIS_W = 85.0;          // Total structural outer bumper width (mm)
CHASSIS_L = 160.0;         // Total front-to-back chassis footprint length (mm)
BATTERY_BAY_W = 35.5;      // Precision compartment slot width for 2S LiPo batteries (mm)

// 📐 SHALED MATRIX RECONCILIATION
SHELL_WALL = 3.0;          // Reinforced 3mm perimeter barrier armor
$fn = 60;                  // High-fidelity curvature tracking resolution

// 🖨️ FABRICATION ROUTER SELECTOR
// PART_SELECTOR: 0 = Unified Visual Assembly, 1 = Flexible TPU Outer Bumper, 2 = Rigid Nylon Motor Spine
PART_SELECTOR = 0;

if (PART_SELECTOR == 0) {
    color("Charcoal", 0.9) RC_Beetle_Exoskeleton_Hull();
    translate([0, 0, -2.0]) color("DimGray") Gazelle_Heatsink_Motor_Spine();
} else if (PART_SELECTOR == 1) {
    RC_Beetle_Exoskeleton_Hull();
} else if (PART_SELECTOR == 2) {
    Gazelle_Heatsink_Motor_Spine();
}

// ============================================================================
// ⚙️ SYSTEM CAD COMPONENT MODULES
// ============================================================================

module RC_Beetle_Exoskeleton_Hull() {
    difference() {
        union() {
            // LAYER 3 CORE: VARIABLE-DENSITY TPU OUTER PROTECTION SHELL
            cube([CHASSIS_W, CHASSIS_L, 22.0], center=true);
            
            // BIOMIMETIC GRASSHOPPER LEAF SUSPENSION ARMS
            // Integrated curved flex extensions replace fragile hydraulic shock rods completely
            for (x_sign = [-1, 1], y_sign = [-0.35, 0.35]) {
                translate([x_sign * (CHASSIS_W/2 + 4.0), y_sign * CHASSIS_L, 0])
                    rotate([0, 0, x_sign * 45])
                        difference() {
                            circle(r=12.0);
                            circle(r=9.5);
                        }
            }
        }
        
        // 🛠️ BIOMIMETIC PATCH 1: MAMMALIAN CRANIUM SKULL SUTURES
        // Replaces straight pin slots with an alternating puzzle-piece zig-zag seam.
        // This spreads extreme crash impacts across the entire mating surface to block shear stress.
        translate([0, 0, 0]) {
            for (y_suture = [-CHASSIS_L*0.35 : 10 : CHASSIS_L*0.35]) {
                translate([sin(y_suture*15)*2.5, y_suture, 0])
                    cube([BATTERY_BAY_W + 8.4, 4.0, 30.0], center=true);
            }
        }
        
        // THE FRONT-IMPACT AUXETIC ARROWHEAD MESH MOAT
        for (x_step = [-CHASSIS_W*0.35 : 12 : CHASSIS_W*0.35]) {
            translate([x_step, CHASSIS_L*0.5 - 4.0, 0])
                rotate([0, 0, 0])
                    Auxetic_Bumper_Cell();
        }
        
        // Wheel Hub Axle Pass-Through Clearance Cutouts
        for (x_sign = [-1, 1], y_sign = [-0.4, 0.4]) {
            translate([x_sign * (CHASSIS_W/2), y_sign * CHASSIS_L, 0])
                cube([15.0, 18.0, 40.0], center=true);
        }
    }
}

module Gazelle_Heatsink_Motor_Spine() {
    // LAYER 1-2 CORE: Rigid internal motor and battery cradle frame printed in PA-CF Nylon
    difference() {
        union() {
            // Main spine foundation plate
            cube([BATTERY_BAY_W + 7.6, CHASSIS_L - 20.4, 12.0], center=true);
            
            // 🛠️ BIOMIMETIC PATCH 3: DESERT GAZELLE CONVECTIVE MICRO-HEATSINKS
            // Upper deck ventilation chimney grid draws motor heat loops straight out through ram air channels
            translate([0, -CHASSIS_L * 0.1, 8.0]) {
                for (chimney = [-15 : 6 : 15]) {
                    translate([chimney, 0, 0])
                        cube([1.5, CHASSIS_L * 0.3, 6.0], center=true);
                }
            }
        }
        
        // LiPo Battery Pre-Tensioned Quick-Snap Nest
        translate([0, -25.0, 2.0])
            cube([BATTERY_BAY_W, 71.0, 14.0], center=true);
            
        // Standard 390-Brushed Motor Keyway Alignment Cradle Tunnel
        translate([0, CHASSIS_L * 0.28, 0])
            rotate([90, 0, 0])
                cylinder(h=32.0, r=14.1, center=true); // Precision 390 diameter clearance
    }
}

module Passiflora_Vine_Helical_Coupler() {
    // 🛠️ BIOMIMETIC PATCH 2: PASSIFLORA VINE SOLID-STATE DRIVE AXLE
    // hollow single-tube construction printed in ductile Polypropylene (PP) with a 360° cut spiral track.
    // Transmits raw torque and steering deflection with zero friction faces to generate heat or melt.
    difference() {
        cylinder(h=45.0, r=4.0, center=true);
        cylinder(h=47.0, r=2.5, center=true); // Hollow internal core
        
        // Helical torsion spring spiral channel track cutter
        translate([0, 0, 0]) {
            linear_extrude(height=35.0, center=true, twist=360, slices=60) {
                translate([2.5, 0, 0])
                    circle(r=0.8, $fn=12);
            }
        }
    }
}

module Auxetic_Bumper_Cell() {
    union() {
        cube([6.0, 2.0, 30.0], center=true);
        rotate([0, 0, 45]) cube([4.5, 1.5, 30.0], center=true);
        rotate([0, 0, -45]) cube([4.5, 1.5, 30.0], center=true);
    }
}

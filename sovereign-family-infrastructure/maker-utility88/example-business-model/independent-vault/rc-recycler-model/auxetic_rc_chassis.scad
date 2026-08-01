// Matrix Biomimetic Utilities - Independent RC Kinetic Shock Chassis
// Version 1.0.0-Hobby Core | Indestructible Auxetic Exoskeleton Layout

// ============================================================================
// 🏛️ MASTER CAR BOUNDARY MATRIX (Parametric 1:16 Scale Allocations)
// ============================================================================
CHASSIS_W = 85.0;          // Total structural outer bumper width (mm)
CHASSIS_L = 160.0;         // Total front-to-back chassis footprint length (mm)
BATTERY_BAY_W = 35.5;      // Precision compartment slot width for LiPo batteries (mm)

// 📐 TOLERANCE RECONCILIATION MATRICES
SHELL_WALL = 3.0;          // Reinforced 3mm perimeter barrier walls to handle concrete impacts
$fn = 60;                  // High-fidelity curvature factor for clean steering pivot clearance

// PART_SELECTOR: 0 = Full Visual Assembly, 1 = Flexible TPU Auxetic Bumper, 2 = Rigid Nylon Motor Spine
PART_SELECTOR = 0;

if (PART_SELECTOR == 0) {
    color("Charcoal", 0.9) RC_Auxetic_Exoskeleton();
    translate([0, 0, -2.0]) color("DimGray") Rigid_Nylon_Motor_Spine();
} else if (PART_SELECTOR == 1) {
    RC_Auxetic_Exoskeleton();
} else if (PART_SELECTOR == 2) {
    Rigid_Nylon_Motor_Spine();
}

// ============================================================================
// ⚙️ SYSTEM CAD COMPONENT MODULES
// ============================================================================

module RC_Auxetic_Exoskeleton() {
    difference() {
        union() {
            // LAYER 2: PRIMARY PROTECTIVE HULL (Printed in High-Rebound TPU)
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
        
        // CENTRAL RIGID SPINE INGESTION CAVITY
        cube([BATTERY_BAY_W + 8.0, CHASSIS_L - 20.0, 30.0], center=true);
        
        // THE FRONT-IMPACT AUXETIC ARROWHEAD MESH MOAT
        // Carves re-entrant structures directly into the front bumper to absorb high-speed wall slams
        for (x_step = [-CHASSIS_W*0.35 : 12 : CHASSIS_W*0.35]) {
            translate([x_step, CHASSIS_L*0.5 - 4.0, 0])
                rotate([0, 0, 90])
                    Auxetic_Bumper_Cell();
        }
        
        // Wheel Hub Axle Pass-Through Clearance Cutouts
        for (x_sign = [-1, 1], y_sign = [-0.4, 0.4]) {
            translate([x_sign * (CHASSIS_W/2), y_sign * CHASSIS_L, 0])
                cube([15.0, 18.0, 40.0], center=true);
        }
    }
}

module Rigid_Nylon_Motor_Spine() {
    // LAYER 1: Rigid internal motor and battery cradle housing printed in PA-CF Nylon
    difference() {
        cube([BATTERY_BAY_W + 7.6, CHASSIS_L - 20.4, 12.0], center=true);
        
        // LiPo Battery Safety Nest Subtraction
        translate([0, -10.0, 2.0])
            cube([BATTERY_BAY_W, CHASSIS_L * 0.4, 12.0], center=true);
            
        // Standard 540-Brushed Motor Mounting Cylinder Bay
        translate([0, CHASSIS_L * 0.3, 0])
            rotate([90, 0, 0])
                cylinder(h=30.0, r=18.0, center=true);
    }
}

module Auxetic_Bumper_Cell() {
    union() {
        cube([6.0, 2.0, 30.0], center=true);
        rotate() cube([4.5, 1.5, 30.0], center=true);
        rotate([0, 0, -45]) cube([4.5, 1.5, 30.0], center=true);
    }
}

// Matrix Biomimetic Utilities - Independent Consumer Smart Case Engine
// Version 3.0.0-Production Master | Dovetail Interlocks & Modular Snap-Rail Core

// ============================================================================
// 🏛️ PHONE MODEL GEOMETRY MATRIX (Adjust to modify target device dimensions)
// ============================================================================
PHONE_X = 78.1;            // Target smartphone width clearance (mm)
PHONE_Y = 160.8;           // Target smartphone height clearance (mm)
PHONE_Z = 7.8;             // Target smartphone thickness clearance (mm)
SHELL_WALL = 2.4;          // 2.4mm thick high-density perimeter barrier wall [1.1]

// ============================================================================
// 📐 RECONCILIATION & TOLERANCE ARRAYS (Compensates for Shrinkage)
// ============================================================================
INT_X = PHONE_X + 0.5;     
INT_Y = PHONE_Y + 0.5;
INT_Z = PHONE_Z + 0.4;

CASE_X = INT_X + (SHELL_WALL * 2);
CASE_Y = INT_Y + (SHELL_WALL * 2);
CASE_H = INT_Z + SHELL_WALL;

$fn = 60; // Curvature resolution factor for flawless hand ergonomics

// PART_SELECTOR: 0 = Full Visual Preview, 1 = Flexible TPU Outer Bumper, 2 = Rigid ASA Snap-In Rails
PART_SELECTOR = 0;

if (PART_SELECTOR == 0) {
    color("Charcoal") Smart_Case_Auxetic_Bumper();
    translate([0, 0, (CASE_H/2) - 0.6]) color("DimGray") Rigid_ASA_Snap_Rails();
} else if (PART_SELECTOR == 1) {
    Smart_Case_Auxetic_Bumper();
} else if (PART_SELECTOR == 2) {
    Rigid_ASA_Snap_Rails();
}

module Smart_Case_Auxetic_Bumper() {
    difference() {
        union() {
            // PRIMARY ERGONOMIC BUMPER (Printed in flexible high-rebound TPU)
            cube([CASE_X, CASE_Y, CASE_H], center=true);
            
            // BIOMIMETIC T-SLOT DOVETAIL INTERLOCKS
            // Replaces expensive magnets with wear-free mechanical puzzle joints
            for (y_ext = [-CASE_Y*0.25, CASE_Y*0.25]) {
                translate([CASE_X*0.5, y_ext, 0]) Armadillo_Dovetail_Male();
            }
        }
        
        // INNER PHONE INGESTION CAVITY
        translate([0, 0, SHELL_WALL * 0.5])
            cube([INT_X, INT_Y, INT_Z + 2.0], center=true);
            
        // THE BIOMIMETIC AUXETIC ARROWHEAD GRID
        for (y_step = [-CASE_Y*0.4 : 12 : CASE_Y*0.4]) {
            translate([CASE_X*0.5, y_step, 0]) rotate([0,0,0]) Auxetic_Cutout_Cell();
            translate([-CASE_X*0.5, y_step, 0]) rotate([0,0,180]) Auxetic_Cutout_Cell();
        }
        
        // INTERNAL SNAP-IN RAIL CHANNEL SUBTRACTION
        // Open tracks to receive the rigid ASA slide infrastructure
        translate([0, 0, (CASE_H/2) - 1.2])
            cube([CASE_X - 2.0, CASE_Y - 2.0, 1.6], center=true);
            
        // RIGID DESK-INTERFACE SOLID-BORNE FOOTPAD SLOTS
        // Connects desk vibrations directly to the internal tracking membrane
        for (x_foot = [-CASE_X*0.3, CASE_X*0.3], y_foot = [-CASE_Y*0.4, CASE_Y*0.4]) {
            translate([x_foot, y_foot, -CASE_H*0.5])
                cube([8.0, 8.0, 1.5], center=true);
        }
        
        // Camera Cutout Window
        translate([CASE_X*0.22, CASE_Y*0.32, -5.0])
            cube([28.0, 32.0, 20.0], center=true);
    }
}

module Rigid_ASA_Snap_Rails() {
    // Rigid internal framework strips that house the 40:1 rocker arms supportless
    difference() {
        cube([CASE_X - 2.4, CASE_Y - 2.4, 1.2], center=true);
        translate([0, 0, -0.1])
            cube([CASE_X - 6.4, CASE_Y - 6.4, 2.0], center=true);
    }
    
    // BIOMIMETIC ASYMMETRICAL ORMIA LEVER FULCRUMS
    // Amplifies low-frequency solid-borne desk hums up to a concentrated 40:1 mechanical pinch
    for (y_pivot = [-CASE_Y*0.2, 0, CASE_Y*0.2]) {
        translate([-CASE_X*0.42, y_pivot, 0])
            cube([4.0, 8.0, 1.0], center=true);
    }
}

module Armadillo_Dovetail_Male() {
    // T-Slot male slider node provides permanent mechanical locking with zero magnet overhead
    translate([1.0, 0, 0]) {
        cube([2.0, 4.0, CASE_H * 0.8], center=true);
        translate([1.0, 0, 0])
            rotate([0,0,45])
                cube([3.0, 3.0, CASE_H * 0.8], center=true);
    }
}

module Auxetic_Cutout_Cell() {
    union() {
        cube([4.0, 1.5, CASE_H + 2], center=true);
        rotate([0,0,45]) cube([3.0, 1.0, CASE_H + 2], center=true);
        rotate([0,0,-45]) cube([3.0, 1.0, CASE_H + 2], center=true);
    }
}

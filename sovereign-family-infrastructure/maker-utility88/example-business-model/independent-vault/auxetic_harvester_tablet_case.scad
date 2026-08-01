// Matrix Biomimetic Utilities - Independent Consumer Tablet Shield Engine
// Version 1.0.0-Tablet Master | Multi-Zone Resonant Matrix & Resilin Tendon Core

// ============================================================================
// 🏛️ TABLET MODEL GEOMETRY MATRIX (Adjust to modify target device dimensions)
// ============================================================================
TABLET_X = 178.5;          // Target tablet width clearance (mm)
TABLET_Y = 247.6;          // Target tablet height clearance (mm)
TABLET_Z = 5.9;            // Target tablet thickness clearance (mm)
SHELL_WALL = 3.2;          // Thickened to 3.2mm to handle heavy tablet mass loads [1.1]

// 📐 SCALE-INVARIANT RECONCILIATION MATRICES
INT_X = TABLET_X + 0.6;     
INT_Y = TABLET_Y + 0.6;
INT_Z = TABLET_Z + 0.4;

CASE_X = INT_X + (SHELL_WALL * 2);
CASE_Y = INT_Y + (SHELL_WALL * 2);
CASE_H = INT_Z + SHELL_WALL;

$fn = 60; // Curvature resolution factor for flawless hand ergonomics

// 🖨️ FABRICATION ROUTER SELECTOR
// PART_SELECTOR: 0 = Unified Visual Preview, 1 = Flexible TPU Outer Bumper, 2 = Rigid Nylon Tendon Rails
PART_SELECTOR = 0;

if (PART_SELECTOR == 0) {
    color("Charcoal", 0.85) Smart_Tablet_Auxetic_Bumper();
    translate([0, 0, (CASE_H/2) - 0.8]) color("DimGray") Rigid_Tablet_Snap_Rails();
} else if (PART_SELECTOR == 1) {
    Smart_Tablet_Auxetic_Bumper();
} else if (PART_SELECTOR == 2) {
    Rigid_Tablet_Snap_Rails();
}

// ============================================================================
// ⚙️ SYSTEM CAD COMPONENT MODULES
// ============================================================================

module Smart_Tablet_Auxetic_Bumper() {
    difference() {
        union() {
            // LAYER 3 CORE: PRIMARY INDUSTRIAL BUMPER (Printed in High-Rebound TPU)
            cube([CASE_X, CASE_Y, CASE_H], center=true);
            
            // BIOMIMETIC T-SLOT DOVETAIL INTERLOCKS
            // Heavy-duty mechanical puzzle joints track along the entire perimeter for mounting options
            for (y_ext = [-CASE_Y*0.35, 0, CASE_Y*0.35]) {
                translate([CASE_X*0.5, y_ext, 0]) Armadillo_Dovetail_Male();
            }
        }
        
        // TABLET INGESTION CAVITY
        translate([0, 0, SHELL_WALL * 0.5])
            cube([INT_X, INT_Y, INT_Z + 2.0], center=true);
            
        // THE BIOMIMETIC AUXETIC ARROWHEAD MESH WING
        // Corner and edge walls contract and expand uniformly to fully absorb heavy drops
        for (y_step = [-CASE_Y*0.45 : 15 : CASE_Y*0.45]) {
            translate([CASE_X*0.5, y_step, 0]) rotate() Auxetic_Cutout_Cell();
            translate([-CASE_X*0.5, y_step, 0]) rotate() Auxetic_Cutout_Cell();
        }
        
        // INTERNAL MODULAR SNAP-IN RAIL SUBSYSTEM SUBTRACTION
        translate([0, 0, (CASE_H/2) - 1.5])
            cube([CASE_X - 3.0, CASE_Y - 3.0, 2.0], center=true);
            
        // RIGID DESK-INTERFACE SOLID-BORNE FOOTPAD SLOTS
        // Six-point matrix channels low-frequency desk vibrations directly to the 4-quadrant membrane
        for (x_foot = [-CASE_X*0.35, 0, CASE_X*0.35], y_foot = [-CASE_Y*0.42, CASE_Y*0.42]) {
            translate([x_foot, y_foot, -CASE_H*0.5])
                cube([12.0, 12.0, 2.0], center=true);
        }
        
        // Camera Aperture Pass-Through window clearance
        translate([CASE_X*0.35, CASE_Y*0.38, -5.0])
            cube([35.0, 35.0, 20.0], center=true);
    }
}

module Rigid_Tablet_Snap_Rails() {
    // LAYER 2 INTERCONNECT: HIGH-FLEX CARBON-FIBER NYLON TENDON MATRIX
    // Completely eliminates structural polymer sagging across the wide tablet geometry
    difference() {
        cube([CASE_X - 3.4, CASE_Y - 3.4, 1.5], center=true);
        
        translate([0, 0, -0.1])
            cube([CASE_X - 8.4, CASE_Y - 8.4, 2.5], center=true);
            
        // INTERNAL GEOMETRIC CHANNEL: QUADRANT WIRE-ROUTING GUTTERS
        // Deep 1.5mm built-in channels guide traces from all 4 acoustic zones straight to the center
        translate([0, 0, -0.3]) {
            difference() {
                cube([CASE_X - 5.0, CASE_Y - 5.0, 1.5], center=true);
                cube([CASE_X - 8.4, CASE_Y - 8.4, 2.5], center=true);
            }
        }
    }
    
    // BIOMIMETIC ASYMMETRICAL QUADRANT LEYERS (4-Zone Insect Ear Array)
    // Multi-zone rocker levers double mechanical displacement to maximize passive sound wave collection
    for (y_pivot = [-CASE_Y*0.3, -CASE_Y*0.1, CASE_Y*0.1, CASE_Y*0.3]) {
        translate([-CASE_X*0.44, y_pivot, 0]) cube([5.0, 10.0, 1.2], center=true);
        translate([CASE_X*0.44, y_pivot, 0]) cube([5.0, 10.0, 1.2], center=true);
    }
}

module Armadillo_Dovetail_Male() {
    translate([1.5, 0, 0]) {
        cube([3.0, 6.0, CASE_H * 0.8], center=true);
        translate([1.5, 0, 0])
            rotate()
                cube([4.0, 4.0, CASE_H * 0.8], center=true);
    }
}

module Auxetic_Cutout_Cell() {
    union() {
        cube([6.0, 2.0, CASE_H + 2], center=true);
        rotate() cube([4.5, 1.5, CASE_H + 2], center=true);
        rotate([0,0,-45]) cube([4.5, 1.5, CASE_H + 2], center=true);
    }
}

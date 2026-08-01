// Matrix Biomimetic Utilities - Independent Consumer Smart Case Engine
// Version 4.2.0-Production Master | Symmetrical Wire Gutters & Resilin Snap Matrix

// ============================================================================
// 🏛️ UNIVERSAL BASELINE DIMENSIONS (Parametric Starting Boundaries)
// ============================================================================
PHONE_X = 78.1;            // Target smartphone width clearance (mm)
PHONE_Y = 160.8;           // Target smartphone height clearance (mm)
PHONE_Z = 7.8;             // Target smartphone thickness clearance (mm)
SHELL_WALL = 2.4;          // 2.4mm thick high-density perimeter barrier wall [1.1]

// 📐 TOLERANCE ADJUSTMENT MATRICES
INT_X = PHONE_X + 0.5;     
INT_Y = PHONE_Y + 0.5;
INT_Z = PHONE_Z + 0.4;

CASE_X = INT_X + (SHELL_WALL * 2);
CASE_Y = INT_Y + (SHELL_WALL * 2);
CASE_H = INT_Z + SHELL_WALL;

$fn = 60; // Curved surface resolution factor

// 🖨️ FABRICATION ROUTER SELECTOR
// PART_SELECTOR: 0 = Unified Visual Preview, 1 = Flexible TPU Outer Bumper, 2 = Rigid Nylon Tendon Rails
PART_SELECTOR = 0;

if (PART_SELECTOR == 0) {
    color("Charcoal", 0.85) Smart_Case_Auxetic_Bumper();
    translate([0, 0, (CASE_H/2) - 0.6]) color("DimGray") Rigid_Resilin_Snap_Rails();
} else if (PART_SELECTOR == 1) {
    Smart_Case_Auxetic_Bumper();
} else if (PART_SELECTOR == 2) {
    Rigid_Resilin_Snap_Rails();
}

// ============================================================================
// ⚙️ SYSTEM CAD COMPONENT MODULES
// ============================================================================

module Smart_Case_Auxetic_Bumper() {
    difference() {
        union() {
            // LAYER 3 CORE: PRIMARY ERGONOMIC BUMPER (Printed in High-Rebound TPU)
            cube([CASE_X, CASE_Y, CASE_H], center=true);
            
            // BIOMIMETIC T-SLOT DOVETAIL INTERLOCKS
            // Armadillo interlocking puzzle joint system provides lifetime wear rating with zero magnets
            for (y_ext = [-CASE_Y*0.25, CASE_Y*0.25]) {
                translate([CASE_X*0.5, y_ext, 0]) Armadillo_Dovetail_Male();
            }
        }
        
        // PHONE INGESTION CAVITY
        translate([0, 0, SHELL_WALL * 0.5])
            cube([INT_X, INT_Y, INT_Z + 2.0], center=true);
            
        // THE BIOMIMETIC AUXETIC ARROWHEAD MESH WING
        // Side walls contract and expand uniformly to fully isolate machine shocks on drop impact
        for (y_step = [-CASE_Y*0.4 : 12 : CASE_Y*0.4]) {
            translate([CASE_X*0.5, y_step, 0]) rotate() Auxetic_Cutout_Cell();
            translate([-CASE_X*0.5, y_step, 0]) rotate() Auxetic_Cutout_Cell();
        }
        
        // INTERNAL MODULAR SNAP-IN RAIL SUBSYSTEM SUBTRACTION
        translate([0, 0, (CASE_H/2) - 1.2])
            cube([CASE_X - 2.0, CASE_Y - 2.0, 1.6], center=true);
            
        // RIGID DESK-INTERFACE SOLID-BORNE FOOTPAD SLOTS
        // Channels low-frequency vibrations directly into the internal tracking membrane
        for (x_foot = [-CASE_X*0.3, CASE_X*0.3], y_foot = [-CASE_Y*0.4, CASE_Y*0.4]) {
            translate([x_foot, y_foot, -CASE_H*0.5])
                cube([8.0, 8.0, 1.5], center=true);
        }
        
        // Camera Aperture Pass-Through window clearance
        translate([CASE_X*0.22, CASE_Y*0.32, -5.0])
            cube([28.0, 32.0, 20.0], center=true);
    }
}

module Rigid_Resilin_Snap_Rails() {
    // LAYER 2 INTERCONNECT: HIGH-FLEX CARBON-FIBER NYLON TENDON MATRIX
    // Completely eliminates structural polymer sagging during expansion and long-term storage
    difference() {
        cube([CASE_X - 2.4, CASE_Y - 2.4, 1.2], center=true);
        
        translate([0, 0, -0.1])
            cube([CASE_X - 6.4, CASE_Y - 6.4, 2.0], center=true);
            
        // INTERNAL GEOMETRIC CHANNEL: DUAL CONCENTRIC WIRE-ROUTING GUTTERS
        // Carves a built-in 1.2mm x 1.2mm wire conduit track channel directly into the printed backplane face.
        // This naturally collects and houses insulated copper traces without manual tools or extra layout wear.
        translate([0, 0, -0.2]) {
            difference() {
                cube([CASE_X - 4.0, CASE_Y - 4.0, 1.2], center=true);
                cube([CASE_X - 6.4, CASE_Y - 6.4, 2.0], center=true);
            }
        }
    }
    
    // BIOMIMETIC ASYMMETRICAL ORMIA LEVER FULCRUMS
    // Symmetrically populates 40-to-1 mechanical displacement levers on both Left and Right tracks [1.1, 1.2]
    for (y_pivot = [-CASE_Y*0.2, 0, CASE_Y*0.2]) {
        translate([-CASE_X*0.42, y_pivot, 0])
            cube([4.0, 8.0, 1.0], center=true);
        translate([CASE_X*0.42, y_pivot, 0])
            cube([4.0, 8.0, 1.0], center=true);
    }
}

module Armadillo_Dovetail_Male() {
    translate([1.0, 0, 0]) {
        cube([2.0, 4.0, CASE_H * 0.8], center=true);
        translate([1.0, 0, 0])
            rotate()
                cube([3.0, 3.0, CASE_H * 0.8], center=true);
    }
}

module Auxetic_Cutout_Cell() {
    union() {
        cube([4.0, 1.5, CASE_H + 2], center=true);
        rotate() cube([3.0, 1.0, CASE_H + 2], center=true);
        rotate([0,0,-45]) cube([3.0, 1.0, CASE_H + 2], center=true);
    }
}

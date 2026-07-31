// Matrix Biomimetic Utilities - Simplified Parametric Solar-Scale Engine
// Version 2.0.0-Optimized Core | Flat-Face Supportless Manufacturing CAD

TILE_WIDTH = 150.0;        // Flat-to-flat distance of hexagonal scale (mm)
BASE_HEIGHT = 8.0;         // Structural base thickness (mm)
CAP_HEIGHT = 4.0;          // Optical shield thickness (mm)
WALL_THICKNESS = 3.0;

SNAP_RADIUS = TILE_WIDTH * 0.08;
PRISM_SIZE = 1.5;

$fn = 60;

// Set to "base" to render the ASA chassis, or "cap" to render the clear lens shield
RENDER_TARGET = "base"; 

module Execution_Router() {
    if (RENDER_TARGET == "base") {
        Parametric_Base_Chassis();
    } else if (RENDER_TARGET == "cap") {
        Parametric_Optical_Cap();
    }
}

// ============================================================================
// 🏛️ COMPONENT 1: VASCULAR BASE CHASSIS (Print in Matte Weatherproof ASA)
// ============================================================================
module Parametric_Base_Chassis() {
    difference() {
        union() {
            // Main structural carrier hex block
            cylinder(h=BASE_HEIGHT, r=TILE_WIDTH * 0.57, $fn=6);
            
            // Radially arrayed male interlocking snap tabs (3 faces)
            for (face =) {
                rotate([0, 0, face])
                    translate([TILE_WIDTH * 0.5, 0, 0])
                        cylinder(h=BASE_HEIGHT * 0.6, r=SNAP_RADIUS);
            }
        }
        
        // Reciprocating female interlocking slots (alternate 3 faces)
        for (face =) {
            rotate([0, 0, face])
                translate([TILE_WIDTH * 0.5, 0, 0])
                    translate([0, 0, -1])
                        cylinder(h=BASE_HEIGHT + 2, r=SNAP_RADIUS + 0.2);
        }
        
        // Main internal equipment bay for the Solar/Seebeck hardware sandwich
        translate([0, 0, WALL_THICKNESS])
            cylinder(h=BASE_HEIGHT, r=TILE_WIDTH * 0.48, $fn=6);
            
        // Vascular cooling channels running beneath the equipment floor
        for (vent = [-TILE_WIDTH*0.4 : 9 : TILE_WIDTH*0.4]) {
            translate([vent, -TILE_WIDTH*0.6, WALL_THICKNESS/2])
                rotate([-90, 0, 0])
                    cylinder(h=TILE_WIDTH * 1.2, r=1.2);
        }
    }
}

// ============================================================================
// 🏛️ COMPONENT 2: OPTICAL ARMOR SHIELD (Print in Transparent PC or PETG)
// ============================================================================
module Parametric_Optical_Cap() {
    difference() {
        // Main protective lens volume
        cylinder(h=CAP_HEIGHT, r=TILE_WIDTH * 0.56, $fn=6);
        
        // Internal Auxetic Impact Web (Machined into the underside of the clear cap)
        translate([0, 0, -0.1]) {
            intersection() {
                cylinder(h=CAP_HEIGHT * 0.5, r=TILE_WIDTH * 0.52, $fn=6);
                for (x = [-TILE_WIDTH : 10 : TILE_WIDTH]) {
                    for (y = [-TILE_WIDTH : 10 : TILE_WIDTH]) {
                        translate([x, y, 0]) {
                            cube([1.0, 7.0, CAP_HEIGHT], center=true);
                            cube([7.0, 1.0, CAP_HEIGHT], center=true);
                        }
                    }
                }
            }
        }
    }
    
    // External Micro-Prism Light Trap face (Lays flat on the build plate)
    translate([0, 0, CAP_HEIGHT]) {
        intersection() {
            cylinder(h=PRISM_SIZE, r=TILE_WIDTH * 0.56, $fn=6);
            for (x = [-TILE_WIDTH : PRISM_SIZE : TILE_WIDTH]) {
                for (y = [-TILE_WIDTH : PRISM_SIZE : TILE_WIDTH]) {
                    translate([x, y, 0])
                        polyhedron(
                            points=[[0,0,PRISM_SIZE], [PRISM_SIZE/2,PRISM_SIZE/2,0], [PRISM_SIZE/2,-PRISM_SIZE/2,0], [-PRISM_SIZE/2,-PRISM_SIZE/2,0], [-PRISM_SIZE/2,PRISM_SIZE/2,0]],
                            faces=[[0,1,2], [0,2,3], [0,3,4], [0,4,1], [1,4,3,2]]
                        );
                }
            }
        }
    }
}

Execution_Router();

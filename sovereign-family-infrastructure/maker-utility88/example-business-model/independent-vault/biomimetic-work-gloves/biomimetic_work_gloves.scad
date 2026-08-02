// Matrix Biomimetic Utilities - Resonant-Class High-Dexterity Work Gloves
// Version 1.0.0-Glove Core | Shark-Skin & Auxetic Metamaterial Matrix
// System Core: Directional Friction Matrix + Print-in-Place Interlocking Strap

// ============================================================================
// 🏛️ GLOBAL PARAMETRIC VARIABLES & HAND PROFILE BOUNDARIES
// ============================================================================
HAND_WIDTH = 90.0;        // Flat palm width across the four knuckle joints (mm)
GLOVE_LENGTH = 210.0;     // Total vertical distance from middle finger tip to cuff base (mm)
WALL_THICKNESS = 1.60;    // Standardized wall footprint for optimal toolpaths (mm)
SCALE_SIZE = 1.80;        // Base footprint dimension of individual placoid skin scales (mm)

// 🖨️ WORKBENCH VISUAL ROUTER
// PREVIEW_MODE: 0 = Full Flat Print-in-Place Layout, 1 = Palm Texture Micro-Audit Only
PREVIEW_MODE = 0;

if (PREVIEW_MODE == 0) {
    Full_Biomimetic_Glove_Assembly();
} else if (PREVIEW_MODE == 1) {
    intersection() {
        Full_Biomimetic_Glove_Assembly();
        translate([0, 0, WALL_THICKNESS*0.5]) cube([30.0, 30.0, WALL_THICKNESS*4], center=true);
    }
}

// ============================================================================
// ⚙️ BIOMIMETIC GLOVE PLATFORM CORE MODULES
// ============================================================================

module Full_Biomimetic_Glove_Assembly() {
    union() {
        // Foundation Skin Template
        difference() {
            // Main hand contour envelope base block
            cube([HAND_WIDTH, GLOVE_LENGTH, WALL_THICKNESS], center=true);
            
            // 🧬 AUXETIC DRAGONFLY-WING KNUCKLES
            // Carves localized diamond expansion cells over the finger joint planes
            // to allow zero-resistance hand clenching while thickening under load.
            translate([0, GLOVE_LENGTH*0.15, 0])
                Auxetic_Flex_Grid(w=HAND_WIDTH*0.9, l=45.0);
        }
        
        // 🦈 SHARK-SKIN PLACOID SCALES MATRIX (Grip Surface Layer)
        // Generates an array of overlapping, swept-back V-shaped dermal structures
        // that channel away liquids and interlock when fingers curl inward.
        translate([0, -GLOVE_LENGTH*0.12, WALL_THICKNESS*0.5]) {
            intersection() {
                cube([HAND_WIDTH*0.95, GLOVE_LENGTH*0.5, SCALE_SIZE*2], center=true);
                union() {
                    for (x = [-HAND_WIDTH*0.5 : SCALE_SIZE*1.2 : HAND_WIDTH*0.5]) {
                        for (y = [-GLOVE_LENGTH*0.25 : SCALE_SIZE*1.5 : GLOVE_LENGTH*0.25]) {
                            // Alternating brick pattern spacing layout
                            translate([x + (mod(floor(y/SCALE_SIZE), 2) * SCALE_SIZE*0.6), y, 0])
                                Placoid_Dermal_Denticle();
                        }
                    }
                }
            }
        }
        
        // 🔒 120-DEGREE ASYMMETRICAL HERRINGBONE WRIST STRAP
        // Print-in-place toolless mechanical wrist fastening bands
        translate([0, -GLOVE_LENGTH*0.44, 0])
            Herringbone_Wrist_Closure_Strap();
    }
}

module Placoid_Dermal_Denticle() {
    // Sharp, swept-back aerodynamic scale geometry optimized for 3D extrusion
    rotate([14, 0, 0]) // Built-in hydrodynamic attack tilt angle profile
        polyhedron(
            points=[
                [0, SCALE_SIZE*0.8, SCALE_SIZE*0.4],             // Peak Keel Ridge Point
                [SCALE_SIZE*0.5, -SCALE_SIZE*0.4, 0],            // Flanking Right Wing
                [0, -SCALE_SIZE*0.6, 0],                         // Deep Recessed Center Channel V
                [-SCALE_SIZE*0.5, -SCALE_SIZE*0.4, 0],           // Flanking Left Wing
                [0, SCALE_SIZE*0.7, 0]                           // Leading Entry Anchor Point
            ],
            faces=[, [0,2,3], [0,3,4], [0,4,1],              // Upper Swept Ridges
                [1,4,3,2]                                        // Flat Bed Interface Face
            ]
        );
}

module Auxetic_Flex_Grid(w, l) {
    // Tessellating auxetic geometric cutouts to eliminate hand movement fatigue
    for (gx = [-w*0.5 : 8.0 : w*0.5]) {
        for (gy = [-l*0.5 : 8.0 : l*0.5]) {
            translate([gx, gy, 0])
                rotate([0, 0, 45])
                    cube([1.4, 6.5, WALL_THICKNESS*1.2], center=true);
        }
    }
}

module Herringbone_Wrist_Closure_Strap() {
    // Extrudes wrap-around locking arms containing asymmetrical ridges
    union() {
        // Main Band Arm Core
        cube([HAND_WIDTH*1.4, 25.0, WALL_THICKNESS*0.8], center=true);
        
        // 120-Degree Gripping Chevron Ridges
        for (r_offset = [-HAND_WIDTH*0.6 : 4.0 : HAND_WIDTH*0.6]) {
            translate([r_offset, 0, WALL_THICKNESS*0.4])
                rotate([0, 0, 30])
                    cube([1.0, 12.0, 0.8], center=true);
            translate([r_offset, 0, WALL_THICKNESS*0.4])
                rotate([0, 0, -30])
                    cube([1.0, 12.0, 0.8], center=true);
        }
    }
}

function mod(a, b) = a - floor(a/b)*b;

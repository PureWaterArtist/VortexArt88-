// Matrix Biomimetic Utilities - Resonant-Class High-Dexterity Work Gloves
// Version 1.3.0-Glove Core | Magnetically Arrayed Hardened Stomatal Matrix
// System Core: Continuous Chevron Rib Grip + Press-Fit Magnet Compartments

// ============================================================================
// 🏛️ GLOBAL PARAMETRIC VARIABLES & HAND PROFILE BOUNDARIES
// ============================================================================
HAND_WIDTH = 90.0;        // Flat palm width across the four knuckle joints (mm)
GLOVE_LENGTH = 210.0;     // Total vertical distance from middle finger tip to cuff base (mm)
WALL_THICKNESS = 1.40;    // Optimized: Thinned wall for maximum hand tactility (mm)
CHEVRON_PITCH = 2.40;     // Optimized: Simplified print-line toolpath track pitch (mm)

// 🧲 NEODYMIUM COMPARTMENT METRICS (Sized for Standard 8mm x 2mm Discs)
MAG_DIAMETER = 8.0;       // Nominal outer diameter of the magnet disc (mm)
MAG_THICKNESS = 2.0;      // Nominal depth thickness of the magnet disc (mm)
FIT_TOLERANCE = 0.20;     // 🛠️ Press-fit compression reduction loop for flexible TPU

Full_Biomimetic_Glove_Assembly();

// ============================================================================
// ⚙️ BIOMIMETIC GLOVE PLATFORM MASTER CORE MODULE
// ============================================================================

module Full_Biomimetic_Glove_Assembly() {
    union() {
        // Foundation Skin Template
        difference() {
            // Main hand contour envelope base block
            cube([HAND_WIDTH, GLOVE_LENGTH, WALL_THICKNESS], center=true);
            
            // AUXETIC DRAGONFLY-WING KNUCKLES & STOMATAL PORE ARRAY
            translate([0, GLOVE_LENGTH*0.15, 0])
                Kinetic_Stomatal_Flex_Grid(w=HAND_WIDTH*0.85, l=45.0);
                
            // 🛠️ HARDWARE UPGRADE 1: INDEX FINGER PRESS-FIT MAGNET COMPARTMENT
            // Carves an exact cylindrical pocket into the upper index tip plane.
            // Sized with a tight sub-micron compression ring so the magnet snaps inside 
            // flushly without messy shop adhesives or metallic fasteners.
            translate([HAND_WIDTH*0.32, GLOVE_LENGTH*0.42, 0])
                cylinder(h=MAG_THICKNESS + 0.2, r=(MAG_DIAMETER - FIT_TOLERANCE)*0.5, center=true, $fn=40);
                
            // 🛠️ HARDWARE UPGRADE 2: BACK-OF-HAND STAGING MAGNET ARRAY
            // Carves a dual-cylinder landing pocket across the main structural back plate
            // to hold loose hex nuts, driver bits, and steel screws hands-free on the bench.
            translate([-HAND_WIDTH*0.22, GLOVE_LENGTH*0.02, 0])
                cylinder(h=MAG_THICKNESS + 0.2, r=(MAG_DIAMETER - FIT_TOLERANCE)*0.5, center=true, $fn=40);
            translate([0, GLOVE_LENGTH*0.02, 0])
                cylinder(h=MAG_THICKNESS + 0.2, r=(MAG_DIAMETER - FIT_TOLERANCE)*0.5, center=true, $fn=40);
        }
        
        // 🦈 STREAMLINED SHARK-SKIN PALM CORE (Continuous Toolpath Ribs)
        translate([0, -GLOVE_LENGTH*0.12, WALL_THICKNESS*0.5]) {
            intersection() {
                cube([HAND_WIDTH*0.95, GLOVE_LENGTH*0.5, 1.2], center=true);
                union() {
                    for (y_row = [-GLOVE_LENGTH*0.25 : CHEVRON_PITCH : GLOVE_LENGTH*0.25]) {
                        translate([0, y_row, 0])
                            Continuous_Swept_Chevron_Rib();
                    }
                }
            }
        }
        
        // 120-DEGREE ASYMMETRICAL HERRINGBONE WRIST STRAP
        translate([0, -GLOVE_LENGTH*0.44, 0])
            Herringbone_Wrist_Closure_Strap();
    }
}

module Continuous_Swept_Chevron_Rib() {
    stroke_w = 1.0;
    linear_extrude(height=0.8, scale=0.8) {
        union() {
            rotate()
                translate([HAND_WIDTH*0.25, 0, 0])
                    square([HAND_WIDTH*0.6, stroke_w], center=true);
            rotate([0, 0, -25])
                translate([-HAND_WIDTH*0.25, 0, 0])
                    square([HAND_WIDTH*0.6, stroke_w], center=true);
        }
    }
}

module Kinetic_Stomatal_Flex_Grid(w, l) {
    for (gx = [-w*0.5 : 8.0 : w*0.5]) {
        for (gy = [-l*0.5 : 6.0 : l*0.5]) {
            translate([gx, gy, 0]) {
                cube([0.4, 4.5, WALL_THICKNESS*1.5], center=true);
                translate([0.3, 0, -WALL_THICKNESS*0.4])
                    rotate()
                        cube([0.2, 4.5, 0.6], center=true);
            }
        }
    }
}

module Herringbone_Wrist_Closure_Strap() {
    union() {
        cube([HAND_WIDTH*1.4, 25.0, WALL_THICKNESS*0.8], center=true);
        for (r_offset = [-HAND_WIDTH*0.6 : 4.0 : HAND_WIDTH*0.6]) {
            translate([r_offset, 0, WALL_THICKNESS*0.4])
                rotate()
                    cube([1.0, 12.0, 0.8], center=true);
            translate([r_offset, 0, WALL_THICKNESS*0.4])
                rotate([0, 0, -30])
                    cube([1.0, 12.0, 0.8], center=true);
        }
    }
}

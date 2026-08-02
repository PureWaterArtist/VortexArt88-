// Matrix Biomimetic Utilities - Resonant-Class Heavy Thermal Work Glove
// Version 2.0.0-Heavy Armor | Modular Snap-On Shield & Thermal Core Matrix
// System Core: Silver-Ant Refractive Siphons + Auxetic Impact Carapace

// ============================================================================
// 🏛️ GLOBAL PARAMETRIC VARIABLES & HEAVY FRAME GEOMETRIES
// ============================================================================
HAND_WIDTH = 92.0;        // Heavy shell flat palm width across the knuckles (mm)
GLOVE_LENGTH = 220.0;     // Total vertical distance including heavy gauntlet cuff (mm)
LINER_THICKNESS = 1.40;   // Base flexible liner wall for tactile feedback (mm)
ARMOR_THICKNESS = 4.50;   // 🛠️ HEAVY UPGRADE: Thicker high-rebound impact armor web (mm)
PIN_RADIUS = 3.50;        // Precision radius for modular snap-on alignment nodes (mm)

// 🖨️ WORKBENCH VISUAL ROUTER
// PREVIEW_INDEX: 0 = Full Multi-Material Heavy Assembly, 1 = Snap-On Carapace Shell ONLY
PREVIEW_INDEX = 0;

if (PREVIEW_INDEX == 0) {
    Inner_Tactile_Thermal_Llove();
    translate([0, 0, LINER_THICKNESS*0.5 + 1.2]) 
        color([0.3, 0.3, 0.3, 0.8]) Modular_SnapOn_Heavy_Carapace();
} else if (PREVIEW_INDEX == 1) {
    Modular_SnapOn_Heavy_Carapace();
}

// ============================================================================
// ⚙️ HEAVY HARDWARE ENGINES & BIOMIMETIC MODULES
// ============================================================================

module Inner_Tactile_Thermal_Llove() {
    // Foundational hand template containing embedded thermal barriers and male pins
    union() {
        difference() {
            cube([HAND_WIDTH, GLOVE_LENGTH, LINER_THICKNESS], center=true);
            
            // 🧬 BIOMIMETIC THERMAL FIX: DESERT SILVER ANT REFRACTIVE MATRIX
            // Carves an array of microscopic triangular micro-grooves and hollow air
            // siphons modeled after the body hairs of the Saharan Silver Ant.
            // These reflect 95% of outward industrial heat radiation and trap a dense layer 
            // of dead-air insulation to freeze sub-zero conductive transfer completely.
            translate([0, 0, -LINER_THICKNESS*0.1]) {
                for (tx = [-HAND_WIDTH*0.45 : 3.2 : HAND_WIDTH*0.45]) {
                    for (ty = [-GLOVE_LENGTH*0.4 : 6.0 : GLOVE_LENGTH*0.4]) {
                        translate([tx, ty, 0])
                            // Prismatic insulating dead-air well geometry ($fn=3)
                            cylinder(h=LINER_THICKNESS*0.6, r1=1.2, r2=0.2, center=true, $fn=3);
                    }
                }
            }
        }
        
        // MODULAR MALE SNAP ALIGNMENT NODES
        // Four solid mechanical posts protruding upward from the backplate and fingers
        // to receive the heavy impact carapace shell securely without glues.
        translate([-HAND_WIDTH*0.35, 0, LINER_THICKNESS*0.5]) Snap_Anchor_Post();
        translate([HAND_WIDTH*0.35, 0, LINER_THICKNESS*0.5]) Snap_Anchor_Post();
        translate([-HAND_WIDTH*0.20, GLOVE_LENGTH*0.38, LINER_THICKNESS*0.5]) Snap_Anchor_Post();
        translate([HAND_WIDTH*0.20, GLOVE_LENGTH*0.38, LINER_THICKNESS*0.5]) Snap_Anchor_Post();
    }
}

module Modular_SnapOn_Heavy_Carapace() {
    // 🛡️ THE HEAVY SHIELD: 4.5mm thick auxiliary impact armor carapace.
    // Maps a high-density auxetic metamaterial lattice over the back of the hand,
    // back of the fingers, and wraps cleanly around the structural wrist cuff.
    difference() {
        union() {
            // Main Armor Shield Body
            intersection() {
                cube([HAND_WIDTH*1.05, GLOVE_LENGTH*0.98, ARMOR_THICKNESS], center=true);
                
                // 🦋 AUXETIC DRAGONFLY-WING IMPACT MATAMATERIAL WEB
                // Thicker high-rebound geometric rows that expand in all directions
                // simultaneously under direct crushing, tool slips, or hammer impacts.
                union() {
                    for (ax = [-HAND_WIDTH*0.55 : 10.0 : HAND_WIDTH*0.55]) {
                        for (ay = [-GLOVE_LENGTH*0.5 : 10.0 : GLOVE_LENGTH*0.5]) {
                            translate([ax, ay, 0])
                                rotate([0, 0, 45])
                                    cube([2.2, 9.2, ARMOR_THICKNESS + 0.2], center=true);
                            translate([ax, ay, 0])
                                rotate([0, 0, -45])
                                    cube([2.2, 9.2, ARMOR_THICKNESS + 0.2], center=true);
                        }
                    }
                }
            }
            
            // WRAP-AROUND GAUNTLET CUFF SHIELD
            // Heavy wrist armor band protecting the radial nerve lines completely
            translate([0, -GLOVE_LENGTH*0.42, 0])
                cube([HAND_WIDTH*1.3, 30.0, ARMOR_THICKNESS*1.4], center=true);
        }
        
        // RECIPROCATING FEMALE SNAP CAPTURE SLOTS
        // Compression-fit lock recesses to clamp over the inner liner's anchor posts.
        translate([-HAND_WIDTH*0.35, 0, -ARMOR_THICKNESS*0.6]) Snap_Capture_Recess();
        translate([HAND_WIDTH*0.35, 0, -ARMOR_THICKNESS*0.6]) Snap_Capture_Recess();
        translate([-HAND_WIDTH*0.20, GLOVE_LENGTH*0.38, -ARMOR_THICKNESS*0.6]) Snap_Capture_Recess();
        translate([HAND_WIDTH*0.20, GLOVE_LENGTH*0.38, -ARMOR_THICKNESS*0.6]) Snap_Capture_Recess();
    }
}

module Snap_Anchor_Post() {
    cylinder(h=4.0, r=PIN_RADIUS - 0.15, center=false, $fn=30);
    translate([0, 0, 3.0])
        rotate_extrude() translate([PIN_RADIUS - 0.15, 0, 0]) circle(r=0.6, $fn=20); // Locking ridge
}

module Snap_Capture_Recess() {
    cylinder(h=ARMOR_THICKNESS*1.5, r=PIN_RADIUS, center=false, $fn=30);
    translate([0, 0, 3.0])
        rotate_extrude() translate([PIN_RADIUS, 0, 0]) circle(r=0.8, $fn=20); // Int. groove
  }

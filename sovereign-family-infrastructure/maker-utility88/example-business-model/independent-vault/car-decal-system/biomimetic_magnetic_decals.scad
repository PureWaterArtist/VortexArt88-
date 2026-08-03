// Matrix Biomimetic Utilities - Interlocking National Flag Decal Matrix
// Version 1.2.0-Decal Master | Absolute Non-Scalable Suture Tolerance Lock
// System Core: Fade-Proof Tri-Color Strata + Fixed Zero-Slop Hardware Gaps

// ============================================================================
// 🏛️ GLOBAL PARAMETRIC VARIABLES & GEOMETRIC CONSTANTS
// ============================================================================
TILE_WIDTH = 120.0;       // Flat-to-flat distance of individual mosaic hex tile (mm)
BASE_HEIGHT = 2.20;       // Low-profile thickness to permanently crush highway drag (mm)
SUTURE_L = 10.0;          // Length scale of individual ironclad jigsaw teeth (mm)
SUTURE_W = 6.0;           // Waist width of the interlocking jigsaw tooth (mm)

// 📐 ABSOLUTE HARDWARE OVERRIDE: FIXED CLEARANCE CEILING
// Stripped out of the scaling loops to remain an absolute constant across custom models.
// Prevents loose flapping seams when scaling up to massive commercial truck sizes.
SUTURE_GAP = 0.15;        // Fixed non-scalable assembly tolerance gap limit (mm)

// 🧲 NEODYMIUM COMPARTMENT METRICS (Sized for Standard 10mm x 2mm Discs)
MAG_DIAMETER = 10.0;
MAG_THICKNESS = 2.0;
FIT_TOLERANCE = 0.20;

Full_National_Flag_Decal_Matrix();

// ============================================================================
// ⚙️ BIOMIMETIC HARDWARE ENGINES & STRUCTURAL MODULES
// ============================================================================

module Full_National_Flag_Decal_Matrix() {
    difference() {
        union() {
            // LAYER 1: TREE-FROG SUCTION GASKET BASE (Flexible 95A TPU Liner)
            color([0.1, 0.1, 0.1])
                difference() {
                    cylinder(h=BASE_HEIGHT * 0.5, r=TILE_WIDTH * 0.55, $fn=6);
                    
                    // Tree-Frog Hexagonal Suction Grip Grid
                    for (sx = [-TILE_WIDTH*0.45 : 8.0 : TILE_WIDTH*0.45]) {
                        for (sy = [-TILE_WIDTH*0.45 : 8.0 : TILE_WIDTH*0.45]) {
                            translate([sx, sy, -0.2])
                                cylinder(h=0.4, r=3.0, $fn=6);
                        }
                    }
                }
                
            // LAYER 2: THE CHAMELEON ATOMIC NATIONAL FLAG STRATA (Weather-Proof ASA/PC)
            translate([0, 0, BASE_HEIGHT * 0.25])
                National_Flag_TriColor_Skin();
            
            // 🪲 BIOMIMETIC INTERLOCK: PARAMETRIC IRONCLAD JIGSAW SUTURES
            for (face = [0 : 120 : 359]) {
                rotate([0, 0, face])
                    translate([TILE_WIDTH * 0.51, 0, -BASE_HEIGHT * 0.25])
                        Ironclad_Jigsaw_Male_Pin();
            }
        }
        
        // RECIPROCATING FEMALE SUTURE KEYWAY SLOTS
        for (face = [60 : 120 : 359]) {
            rotate([0, 0, face])
                translate([TILE_WIDTH * 0.51, 0, -BASE_HEIGHT * 0.25 - 0.1])
                    Ironclad_Jigsaw_Female_Slot();
        }
        
        // 🌊 SCALLOP FLUID DRAINAGE GUTTERS
        for (border = [0 : 60 : 359]) {
            rotate([0, 0, border])
                translate([TILE_WIDTH * 0.52, 0, BASE_HEIGHT * 0.25])
                    cube([1.2, TILE_WIDTH * 0.6, 0.4], center=true);
        }
        
        // 🧲 COUNTERSUNK NON-SCRATCH MAGNET POCKETS
        for (mag_node = [30 : 60 : 359]) {
            rotate([0, 0, mag_node])
                translate([TILE_WIDTH * 0.32, 0, -BASE_HEIGHT * 0.5 + 0.1])
                    cylinder(h=MAG_THICKNESS + 0.1, r=(MAG_DIAMETER - FIT_TOLERANCE)*0.5, $fn=40);
        }
        
        // 🌊 PARABOLIC FALCON-WING AIRFOIL BEZEL
        difference() {
            translate([0, 0, BASE_HEIGHT*0.5]) cylinder(h=2.0, r=TILE_WIDTH*0.65, center=true, $fn=6);
            translate([0, 0, BASE_HEIGHT*0.5]) cylinder(h=2.2, r1=TILE_WIDTH*0.54, r2=TILE_WIDTH*0.46, center=true, $fn=6);
        }
    }
}

module National_Flag_TriColor_Skin() {
    stripe_h = TILE_WIDTH / 3.0; 
    intersection() {
        cylinder(h=BASE_HEIGHT * 0.5, r=TILE_WIDTH * 0.53, $fn=6);
        union() {
            color([0.8, 0.1, 0.1])
                translate([0, -stripe_h, 0]) cube([TILE_WIDTH * 1.5, stripe_h, BASE_HEIGHT], center=true);
            color([0.9, 0.9, 0.9])
                cube([TILE_WIDTH * 1.5, stripe_h, BASE_HEIGHT], center=true);
            color([0.1, 0.2, 0.5])
                translate([0, stripe_h, 0]) cube([TILE_WIDTH * 1.5, stripe_h, BASE_HEIGHT], center=true);
        }
    }
}

module Ironclad_Jigsaw_Male_Pin() {
    linear_extrude(height=BASE_HEIGHT) {
        union() {
            translate([-SUTURE_L*0.2, 0, 0]) square([SUTURE_L*0.5, SUTURE_W*0.8], center=true);
            translate([SUTURE_L*0.2, 0, 0]) rotate() circle(r=SUTURE_W*0.6, $fn=6);
        }
    }
}

module Ironclad_Jigsaw_Female_Slot() {
    // 🛠️ HARDWARE UPGRADE: Utilizes the absolute SUTURE_GAP constant
    linear_extrude(height=BASE_HEIGHT + 0.4) {
        union() {
            translate([-SUTURE_L*0.2, 0, 0]) square([SUTURE_L*0.5 + SUTURE_GAP, SUTURE_W*0.8 + SUTURE_GAP], center=true);
            translate([SUTURE_L*0.2, 0, 0]) rotate() circle(r=SUTURE_W*0.6 + SUTURE_GAP, $fn=6);
        }
    }
}

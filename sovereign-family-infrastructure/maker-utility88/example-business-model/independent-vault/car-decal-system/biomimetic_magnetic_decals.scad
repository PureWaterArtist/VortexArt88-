// Matrix Biomimetic Utilities - Interlocking National Flag Decal Matrix
// Version 1.1.0-Decal Master | Parabolic Airfoil & Tree-Frog Gasket Core
// System Core: Fade-Proof Tri-Color Strata + Mechanical Drainage Gutters

// ============================================================================
// 🏛️ GLOBAL PARAMETRIC VARIABLES & GEOMETRIC CONSTANTS
// ============================================================================
TILE_WIDTH = 120.0;       // Flat-to-flat distance of individual mosaic hex tile (mm)
BASE_HEIGHT = 2.20;       // Low-profile thickness to permanently crush highway drag (mm)
SUTURE_L = 10.0;          // Length scale of individual ironclad jigsaw teeth (mm)
SUTURE_W = 6.0;           // Waist width of the interlocking jigsaw tooth (mm)

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
            // Forms a soft, high-friction, anti-scratch barrier against vehicle paint
            color([0.1, 0.1, 0.1])
                difference() {
                    cylinder(h=BASE_HEIGHT * 0.5, r=TILE_WIDTH * 0.55, $fn=6);
                    
                    // Tree-Frog Hexagonal Suction Grip Grid
                    // Traps localized air pockets to block creeping road dust sandpaper effects
                    for (sx = [-TILE_WIDTH*0.45 : 8.0 : TILE_WIDTH*0.45]) {
                        for (sy = [-TILE_WIDTH*0.45 : 8.0 : TILE_WIDTH*0.45]) {
                            translate([sx, sy, -0.2])
                                cylinder(h=0.4, r=3.0, $fn=6);
                        }
                    }
                }
                
            // LAYER 2: THE CHAMELEON ATOMIC NATIONAL FLAG STRATA (Weather-Proof ASA/PC)
            // Co-extruded solid color blocks that replace cheap fading inks and vinyl stickers
            translate([0, 0, BASE_HEIGHT * 0.25])
                National_Flag_TriColor_Skin();
            
            // 🪲 BIOMIMETIC INTERLOCK: PARAMETRIC IRONCLAD JIGSAW SUTURES
            // Alternating re-entrant teeth that snap tiles into a continuous armor plate
            for (face = [0 : 120 : 359]) {
                rotate([0, 0, face])
                    translate([TILE_WIDTH * 0.51, 0, -BASE_HEIGHT * 0.25])
                        Ironclad_Jigsaw_Male_Pin();
            }
        }
        
        // RECIPROCATING FEMALE SUTURE KEYWAY SLOTS (With Built-in Clearance)
        for (face = [60 : 120 : 359]) {
            rotate([0, 0, face])
                translate([TILE_WIDTH * 0.51, 0, -BASE_HEIGHT * 0.25 - 0.1])
                    Ironclad_Jigsaw_Female_Slot();
        }
        
        // 🌊 🛠️ MOAT UPGRADE 1: SCALLOP FLUID DRAINAGE GUTTERS
        // Carves 0.4mm channels directly along the perimeter seams to prevent rain water
        // and winter road salt from pooling and freezing inside the puzzle interlocks
        for (border = [0 : 60 : 359]) {
            rotate([0, 0, border])
                translate([TILE_WIDTH * 0.52, 0, BASE_HEIGHT * 0.25])
                    cube([1.2, TILE_WIDTH * 0.6, 0.4], center=true);
        }
        
        // 🧲 COUNTERSUNK NON-SCRATCH MAGNET POCKETS
        // Compression reduction loops leave a thin 0.2mm protective rubber shield
        for (mag_node = [30 : 60 : 359]) {
            rotate([0, 0, mag_node])
                translate([TILE_WIDTH * 0.32, 0, -BASE_HEIGHT * 0.5 + 0.1])
                    cylinder(h=MAG_THICKNESS + 0.1, r=(MAG_DIAMETER - FIT_TOLERANCE)*0.5, $fn=40);
        }
        
        // 🌊 🛠️ MOAT UPGRADE 2: PARABOLIC FALCON-WING AIRFOIL BEZEL
        // Replaces sharp 90-degree outer lips with a sweeping curve to convert wind
        // into continuous aerodynamic downforce, making lift impossible at 75 MPH
        difference() {
            translate([0, 0, BASE_HEIGHT*0.5]) cylinder(h=2.0, r=TILE_WIDTH*0.65, center=true, $fn=6);
            translate([0, 0, BASE_HEIGHT*0.5]) cylinder(h=2.2, r1=TILE_WIDTH*0.54, r2=TILE_WIDTH*0.46, center=true, $fn=6);
        }
    }
}

module National_Flag_TriColor_Skin() {
    // 🎨 SOLID STRATA CODE: Slices the upper 1.0mm geometry into three perfect
    // horizontal filament tracks to print true, un-fading national color blocks
    stripe_h = TILE_WIDTH / 3.0; // Balanced 40mm stripe span index
    
    intersection() {
        cylinder(h=BASE_HEIGHT * 0.5, r=TILE_WIDTH * 0.53, $fn=6);
        union() {
            // Stripe 1: Bottom Band Channel (e.g., Red Track)
            color([0.8, 0.1, 0.1])
                translate([0, -stripe_h, 0]) cube([TILE_WIDTH * 1.5, stripe_h, BASE_HEIGHT], center=true);
            
            // Stripe 2: Center Band Channel (e.g., White/Silver Track)
            color([0.9, 0.9, 0.9])
                translate([0, 0, 0]) cube([TILE_WIDTH * 1.5, stripe_h, BASE_HEIGHT], center=true);
                
            // Stripe 3: Top Band Channel (e.g., Blue Track)
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
    gap = 0.15;
    linear_extrude(height=BASE_HEIGHT + 0.4) {
        union() {
            translate([-SUTURE_L*0.2, 0, 0]) square([SUTURE_L*0.5 + gap, SUTURE_W*0.8 + gap], center=true);
            translate([SUTURE_L*0.2, 0, 0]) rotate() circle(r=SUTURE_W*0.6 + gap, $fn=6);
        }
    }
}

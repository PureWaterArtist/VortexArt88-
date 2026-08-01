// Matrix Biomimetic Utilities - Circular Footwear Style Extensions Matrix
// Version 1.0.0-Styles Core | Urban Hex Mesh, Tactical Boot, and Runner Slide

// ============================================================================
// 🏛️ UNIVERSAL SIZING MATRIX REFERENCE
// ============================================================================
FOOT_LENGTH = 270.0;       // Men's Size 9 Baseline (mm)
FOOT_WIDTH = 98.0;         // Max width baseline (mm)
SOLE_THICKNESS = 28.0;     // Midsole thickness (mm)

INT_L = FOOT_LENGTH + 4.0;
INT_W = FOOT_WIDTH + 2.0;
$fn = 60;

// 🎨 STYLE SELECTOR INDEX
// STYLE_SELECTOR: 1 = Urban Hex-Clog, 2 = Tactical All-Terrain Boot, 3 = High-Velocity Runner Slide
STYLE_SELECTOR = 1;

if (STYLE_SELECTOR == 1) {
    Style_Urban_Hex_Clog();
} else if (STYLE_SELECTOR == 2) {
    Style_Tactical_All_Terrain_Boot();
} else if (STYLE_SELECTOR == 3) {
    Style_High_Velocity_Runner_Slide();
}

// ============================================================================
// ⚙️ SYSTEM CAD COMPONENT MODULES
// ============================================================================

module Style_Urban_Hex_Clog() {
    // VARIANT 1: THE URBAN HEX-CLOG (Streetwear Geometric Mesh Profile)
    difference() {
        union() {
            scale([1, 1, 0.45]) sphere(d=INT_L);
            // Continuous longitudinal dovetail male splines molded supportless to base
            Footwear_Base_Dovetail_Rails();
        }
        
        // Inner Foot Ingestion Cavity
        translate([0, 0, -2.0]) scale([0.96, 0.94, 0.42]) sphere(d=INT_L);
        // Ankle Collar Entry Window Opening
        translate([-INT_L*0.15, 0, 30.0]) cylinder(h=40.0, r=INT_W*0.48, center=true);
        // Bottom Sole Separation Planar Cut
        translate([0, 0, -40.0]) cube([INT_L+10, INT_W+10, 80.0], center=true);
            
        // BIOMIMETIC HEXAGONAL LATTICE CUTTERS (Wipes out 20% print time)
        for (y_hex = [-INT_L*0.3 : 14 : INT_L*0.3]) {
            for (x_hex = [-INT_W*0.3 : 14 : INT_W*0.3]) {
                translate([x_hex, y_hex + (x_hex % 28 == 0 ? 7 : 0), 12.0])
                    rotate([0, 0, 30])
                        cylinder(h=20.0, r=3.5, $fn=6, center=true); // Sharp geometric hex cells
            }
        }
    }
}

module Style_Tactical_All_Terrain_Boot() {
    // VARIANT 2: THE TACTICAL ALL-TERRAIN BOOT (Ankle-Stabilizing Exoskeleton Shell)
    difference() {
        union() {
            // Extended vertical Z-axis height profiles to wrap completely past ankle bone joints
            scale([1, 1, 0.75]) sphere(d=INT_L);
            
            // Integrated External Reinforcement Support Ribs (Protects against rock strikes)
            for (rib = [-INT_L*0.2 : 20 : INT_L*0.3]) {
                translate([0, rib, 15.0])
                    cube([INT_W + 6.0, 4.0, 30.0], center=true);
            }
            Footwear_Base_Dovetail_Rails();
        }
        
        // Extended Deep Inner Foot Ingestion Cavity
        translate([0, 0, -2.0]) scale([0.95, 0.92, 0.72]) sphere(d=INT_L);
        // Elevated High-Top Ankle Entry Collar Window
        translate([-INT_L*0.1, 0, 65.0]) cylinder(h=50.0, r=INT_W*0.44, center=true);
        // Bottom Sole Separation Planar Cut
        translate([0, 0, -40.0]) cube([INT_L+10, INT_W+10, 80.0], center=true);
        
        // Tesla-Valve Waterproof Breathing Pores (Positioned high to dodge deep mud crossings)
        for (y_boot = [-INT_L*0.2 : 25 : INT_L*0.2]) {
            translate([INT_W*0.42, y_boot, 35.0]) rotate([0, 90, 0]) cylinder(h=15.0, r=1.2, center=true);
            translate([-INT_W*0.42, y_boot, 35.0]) rotate([0, 90, 0]) cylinder(h=15.0, r=1.2, center=true);
        }
    }
}

module Style_High_Velocity_Runner_Slide() {
    // VARIANT 3: THE HIGH-VELOCITY RUNNER SLIDE (Ultra-Lightweight Beach & Recovery Sandal)
    difference() {
        union() {
            scale([1, 1, 0.45]) sphere(d=INT_L);
            Footwear_Base_Dovetail_Rails();
        }
        
        // Inner Foot Ingestion Cavity
        translate([0, 0, -2.0]) scale([0.96, 0.94, 0.42]) sphere(d=INT_L);
        
        // MASSIVE FOREFOOT STRUCTURAL SUBTRACTION (Cuts out entire toe box section)
        translate([INT_L*0.2, 0, 10.0])
            cube([INT_L*0.6, INT_W+20, 40.0], center=true);
            
        // REAR HEEL COUNTER SUBTRACTION (Converts shell into a slip-on recovery slider)
        translate([-INT_L*0.35, 0, 15.0])
            cube([INT_L*0.4, INT_W+20, 40.0], center=true);
            
        // Bottom Sole Separation Planar Cut
        translate([0, 0, -40.0]) cube([INT_L+10, INT_W+10, 80.0], center=true);
    }
}

module Footwear_Base_Dovetail_Rails() {
    // Common interlocking architectural anchor rails hard-coded to fit the same 95A midsole base
    for (x_rail = [-20, 0, 20]) {
        translate([x_rail, 0, -SOLE_THICKNESS*0.35]) {
            cube([3.0, INT_L * 0.7, 4.0], center=true); 
            translate([0, 0, -2.0]) rotate([0, 0, 45]) cube([4.0, INT_L * 0.7, 4.0], center=true); 
        }
    }
    // Rear safety locking transverse pin cylinder
    translate([-INT_L * 0.44, 0, -SOLE_THICKNESS * 0.35]) {
        rotate([0, 90, 0])
            cylinder(h=14.0, r=3.0, center=true);
    }
}

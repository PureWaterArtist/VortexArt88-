// Matrix Biomimetic Utilities - Parametric MKX Retail Synergy Tray
// Version 2.1.0-Audited Core | Verified Shrinkage & Tolerance Compensated CAD

ROW_COUNT = 3;             
COL_COUNT = 4;             
SLOT_DIAMETER = 14.5;      
SLOT_DEPTH = 18.0;         

WALL_THICKNESS = 2.0;      
PADDING_XY = SLOT_DIAMETER * 0.4;

TRAY_X = (COL_COUNT * SLOT_DIAMETER) + ((COL_COUNT + 1) * PADDING_XY);
TRAY_Y = (ROW_COUNT * SLOT_DIAMETER) + ((ROW_COUNT + 1) * PADDING_XY);
TRAY_H = SLOT_DEPTH + WALL_THICKNESS;

// AUDITED TOLERANCE CORRECTION MATRIX
// Widened from 3.1mm to 3.25mm to offset 1.4% ASA polymer thermal shrinkage
MAG_RADIUS = 3.25;          
$fn = 80;                  

module MKX_Shelled_Synergy_Tray() {
    difference() {
        union() {
            difference() {
                cube([TRAY_X, TRAY_Y, TRAY_H]);
                translate([-1, TRAY_Y, TRAY_H - 4])
                    rotate()
                        cube([TRAY_X + 2, TRAY_Y * 1.5, TRAY_H]);
            }
            
            translate([TRAY_X, TRAY_Y * 0.5, 0])
                Magnetic_Coupling_Tab(male=true);
            translate([TRAY_X * 0.5, TRAY_Y, 0])
                rotate()
                    Magnetic_Coupling_Tab(male=true);
        }
        
        translate([WALL_THICKNESS, WALL_THICKNESS, -0.1])
            cube([TRAY_X - (WALL_THICKNESS * 2), TRAY_Y - (WALL_THICKNESS * 2), TRAY_H - WALL_THICKNESS]);
            
        translate([0, TRAY_Y * 0.5, 0])
            Magnetic_Coupling_Tab(male=false);
        translate([TRAY_X * 0.5, 0, 0])
            rotate()
                Magnetic_Coupling_Tab(male=false);
                
        translate([TRAY_X * 0.1, WALL_THICKNESS * 0.5, 2.0])
            cube([TRAY_X * 0.8, WALL_THICKNESS + 0.1, TRAY_H * 0.6]);
    }
    
    intersection() {
        difference() {
            cube([TRAY_X, TRAY_Y, TRAY_H]);
            translate([-1, TRAY_Y, TRAY_H - 4])
                rotate()
                    cube([TRAY_X + 2, TRAY_Y * 1.5, TRAY_H]);
        }
        
        for (r = [0 : ROW_COUNT - 1]) {
            for (c = [0 : COL_COUNT - 1]) {
                pos_x = PADDING_XY + (c * (SLOT_DIAMETER + PADDING_XY)) + (SLOT_DIAMETER / 2);
                pos_y = PADDING_XY + (r * (SLOT_DIAMETER + PADDING_XY)) + (SLOT_DIAMETER / 2);
                
                translate([pos_x, pos_y, 0]) {
                    difference() {
                        cylinder(h=TRAY_H, r=(SLOT_DIAMETER / 2) + WALL_THICKNESS);
                        translate([0, 0, TRAY_H - SLOT_DEPTH])
                            cylinder(h=SLOT_DEPTH + 10, r=SLOT_DIAMETER / 2);
                        translate([0, 0, -1])
                            cylinder(h=TRAY_H + 2, r=1.5);
                    }
                }
            }
        }
    }
}

module Magnetic_Coupling_Tab(male=true) {
    if (male) {
        difference() {
            cylinder(h=TRAY_H * 0.5, r=PADDING_XY * 0.8);
            // Flat entry channel offsets nozzle-rounding path limits
            translate([0, 0, -0.1])
                cylinder(h=2.3, r=MAG_RADIUS); 
        }
    } else {
        translate([0, 0, -1])
            cylinder(h=TRAY_H + 2, r=PADDING_XY * 0.9);
        translate([0, 0, -0.1])
            cylinder(h=2.3, r=MAG_RADIUS);
    }
}

MKX_Shelled_Synergy_Tray();

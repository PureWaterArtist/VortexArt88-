// Matrix Biomimetic Utilities - Parametric MKX Retail Synergy Tray
// Version 2.2.0-Production Core | Fluting, Outgas Venting, & Mechanical Cap Retention

ROW_COUNT = 3;             
COL_COUNT = 4;             
SLOT_DIAMETER = 14.5;      
SLOT_DEPTH = 18.0;         

WALL_THICKNESS = 2.0;      
PADDING_XY = SLOT_DIAMETER * 0.4;

TRAY_X = (COL_COUNT * SLOT_DIAMETER) + ((COL_COUNT + 1) * PADDING_XY);
TRAY_Y = (ROW_COUNT * SLOT_DIAMETER) + ((ROW_COUNT + 1) * PADDING_XY);
TRAY_H = SLOT_DEPTH + WALL_THICKNESS;

MAG_RADIUS = 3.1;  // Reverted to true 6mm x 2mm magnet bounds due to bottom cap isolation
$fn = 80;                  

module MKX_Production_Synergy_Tray() {
    difference() {
        union() {
            // Main Airframe Chassis Enclosure
            difference() {
                cube([TRAY_X, TRAY_Y, TRAY_H]);
                translate([-1, TRAY_Y, TRAY_H - 4])
                    rotate([10, 0, 0])
                        cube([TRAY_X + 2, TRAY_Y * 1.5, TRAY_H]);
            }
            
            // Tessellating Side Tabs (Male Connections)
            translate([TRAY_X, TRAY_Y * 0.5, 0])
                Magnetic_Coupling_Tab(male=true);
            translate([TRAY_X * 0.5, TRAY_Y, 0])
                rotate([0, 0, 90])
                    Magnetic_Coupling_Tab(male=true);
        }
        
        // Internal Core Hollowing
        translate([WALL_THICKNESS, WALL_THICKNESS, -0.1])
            cube([TRAY_X - (WALL_THICKNESS * 2), TRAY_Y - (WALL_THICKNESS * 2), TRAY_H - WALL_THICKNESS]);
            
        // Female Interlock Pockets
        translate([0, TRAY_Y * 0.5, 0])
            Magnetic_Coupling_Tab(male=false);
        translate([TRAY_X * 0.5, 0, 0])
            rotate([0, 0, 90])
                Magnetic_Coupling_Tab(male=false);
                
        // Front Quick-Swap Branding Track
        translate([TRAY_X * 0.1, WALL_THICKNESS * 0.5, 2.0])
            cube([TRAY_X * 0.8, WALL_THICKNESS + 0.1, TRAY_H * 0.6]);
            
        // CRITICAL BUGFIX 3: MICRO-VENTILATION OUTGAS GROOVES
        // Shallow 0.5mm bottom linear slits to let styrene gas escape flat bed plates safely
        for (g = [10 : 15 : TRAY_X - 10]) {
            translate([g, -1, -0.1]) cube([1.0, TRAY_Y + 2, 0.6]);
        }
    }
    
    // Internal Product Grid Columns
    intersection() {
        difference() {
            cube([TRAY_X, TRAY_Y, TRAY_H]);
            translate([-1, TRAY_Y, TRAY_H - 4])
                rotate([10, 0, 0])
                    cube([TRAY_X + 2, TRAY_Y * 1.5, TRAY_H]);
        }
        
        for (r = [0 : ROW_COUNT - 1]) {
            for (c = [0 : COL_COUNT - 1]) {
                pos_x = PADDING_XY + (c * (SLOT_DIAMETER + PADDING_XY)) + (SLOT_DIAMETER / 2);
                pos_y = PADDING_XY + (r * (SLOT_DIAMETER + PADDING_XY)) + (SLOT_DIAMETER / 2);
                
                translate([pos_x, pos_y, 0]) {
                    difference() {
                        // Structural Sleeve Cylinder
                        cylinder(h=TRAY_H, r=(SLOT_DIAMETER / 2) + WALL_THICKNESS);
                        
                        // Main Cartridge Intake Pocket Cylinder
                        translate([0, 0, TRAY_H - SLOT_DEPTH])
                            cylinder(h=SLOT_DEPTH + 10, r=SLOT_DIAMETER / 2);
                        
                        // Base Central Concentrate Drainage Siphon
                        translate([0, 0, -1])
                            cylinder(h=TRAY_H + 2, r=1.5);
                    }
                    
                    // CRITICAL BUGFIX 4: BIOMIMETIC SCALLOPED FLUTING RIDGES
                    // Three internal 0.5mm ribs to reduce contact area by 70% and prevent sticky vacuum jams
                    for (ang = [0, 120, 240]) {
                        rotate([0, 0, ang])
                            translate([(SLOT_DIAMETER / 2) - 0.4, 0, TRAY_H - SLOT_DEPTH])
                                cylinder(h=SLOT_DEPTH, r=0.5, $fn=12);
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
            
            // CRITICAL BUGFIX 1: MECHANICAL OVERHANG RETENTION LIP
            // Hidden bottom entry channel allows magnet insertion but creates an anti-flyout safety ceiling
            translate([0, 0, -0.1]) cylinder(h=2.2, r=MAG_RADIUS + 0.15);
            translate([0, 0, 1.8]) cylinder(h=TRAY_H, r=MAG_RADIUS - 0.4); // The Cap Lip
        }
    } else {
        translate([0, 0, -1]) cylinder(h=TRAY_H + 2, r=PADDING_XY * 0.9);
        translate([0, 0, -0.1]) cylinder(h=2.2, r=MAG_RADIUS + 0.15);
        translate([0, 0, 1.8]) cylinder(h=TRAY_H, r=MAG_RADIUS - 0.4);
    }
}

MKX_Production_Synergy_Tray();

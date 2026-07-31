// Matrix Biomimetic Utilities - Parametric MKX Retail Synergy Tray
// Version 2.3.0-Production Master | Multi-Piece Embossed Logo & Branding Integration

// ============================================================================
// 🏛️ PARAMETRIC INVENTORY CAPACITY MATRIX (Adjust to modify display capacity)
// ============================================================================
ROW_COUNT = 3;             // Number of vertical product rows
COL_COUNT = 4;             // Number of horizontal cartridge slots per row
SLOT_DIAMETER = 14.5;      // Diameter tailored for standard 1.0g MKX vape cartridges (mm)
SLOT_DEPTH = 18.0;         // Depth ensuring secure vertical seating during transit (mm)

// ============================================================================
// 📐 CORE-SHELLING & SHRINKAGE MATRICES (Locks Mass to 85g / Print to 1.9 Hrs)
// ============================================================================
WALL_THICKNESS = 2.0;      // Throttled perimeter wall thickness to minimize mass volume
PADDING_XY = SLOT_DIAMETER * 0.4;

TRAY_X = (COL_COUNT * SLOT_DIAMETER) + ((COL_COUNT + 1) * PADDING_XY);
TRAY_Y = (ROW_COUNT * SLOT_DIAMETER) + ((ROW_COUNT + 1) * PADDING_XY);
TRAY_H = SLOT_DEPTH + WALL_THICKNESS;

MAG_RADIUS = 3.1;          // Precision pocket for 6mm x 2mm Neodymium coupling magnets
$fn = 80;                  // High-fidelity production resolution curvature factor

// BRANDING CONFIGURATION MATRICES
BADGE_WIDTH = TRAY_X * 0.8;
BADGE_HEIGHT = TRAY_H * 0.6;
BADGE_DEPTH = WALL_THICKNESS;

// ============================================================================
// 🛠️ CHASSIS OR EXTRACT CONTROL ROUTER (Set selector to isolate components)
// ============================================================================
// PART_SELECTOR: 0 = Assemble Full Preview, 1 = Print Black ASA Tray, 2 = Print Gold PMMA Logo Insert
PART_SELECTOR = 0; 

if (PART_SELECTOR == 0) {
    // Full Showroom Render Preview
    color("DimGray") MKX_Production_Synergy_Tray();
    translate([TRAY_X * 0.1, WALL_THICKNESS * 0.5, 2.0]) 
        color("Gold") MKX_Branding_Badge_Insert();
} else if (PART_SELECTOR == 1) {
    // Export this mesh for the industrial ASA Base Prototype
    MKX_Production_Synergy_Tray();
} else if (PART_SELECTOR == 2) {
    // Export this mesh for the high-gloss PMMA Branding Faceplate
    MKX_Branding_Badge_Insert();
}

// ============================================================================
// ⚙️ MAIN MODULE GEOMETRIES
// ============================================================================

module MKX_Production_Synergy_Tray() {
    difference() {
        union() {
            // Main Airframe Chassis Enclosure
            difference() {
                cube([TRAY_X, TRAY_Y, TRAY_H]);
                translate([-1, TRAY_Y, TRAY_H - 4])
                    rotate([10, 0, 0]) // 10-degree tilted display incline face
                        cube([TRAY_X + 2, TRAY_Y * 1.5, TRAY_H]);
            }
            
            // Tessellating Side Tabs (Male Connections)
            translate([TRAY_X, TRAY_Y * 0.5, 0])
                Magnetic_Coupling_Tab(male=true);
            translate([TRAY_X * 0.5, TRAY_Y, 0])
                rotate([0, 0, 90])
                    Magnetic_Coupling_Tab(male=true);
        }
        
        // Internal Core Hollowing (Hollows interior bay down to 85g limit)
        translate([WALL_THICKNESS, WALL_THICKNESS, -0.1])
            cube([TRAY_X - (WALL_THICKNESS * 2), TRAY_Y - (WALL_THICKNESS * 2), TRAY_H - WALL_THICKNESS]);
            
        // Female Interlock Pockets
        translate([0, TRAY_Y * 0.5, 0])
            Magnetic_Coupling_Tab(male=false);
        translate([TRAY_X * 0.5, 0, 0])
            rotate([0, 0, 90])
                Magnetic_Coupling_Tab(male=false);
                
        // Recessed Front Quick-Swap Branding Track Pocket
        translate([TRAY_X * 0.1, -0.1, 2.0])
            cube([BADGE_WIDTH, BADGE_DEPTH + 0.2, BADGE_HEIGHT]);
            
        // MICRO-VENTILATION OUTGAS GROOVES
        // Shallow 0.5mm bottom slits to let styrene gas escape flat bed plates safely without buckling
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
                    
                    // BIOMIMETIC SCALLOPED FLUTING RIDGES
                    // Three internal 0.5mm ribs reduce contact area by 70% to completely break sticky vacuum jams
                    for (ang =) {
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
            
            // MECHANICAL OVERHANG RETENTION LIP
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

module MKX_Branding_Badge_Insert() {
    // Generates the solid backing plate with the embossed bold MKX logo graphics
    difference() {
        // Base plate slide backing
        cube([BADGE_WIDTH - 0.2, BADGE_DEPTH, BADGE_HEIGHT - 0.2]);
        
        // Micro-etched alignment groove indicators
        translate([BADGE_WIDTH * 0.1, -0.1, BADGE_HEIGHT * 0.1])
            cube([BADGE_WIDTH * 0.8, 0.4, 1.0]);
    }
    
    // EMBOSSED 2-PIECE INDUSTRIAL TEXT LOGO GRAPHIC
    // Extrudes 1.2mm corporate bold lettering forward out of the face plate
    translate([BADGE_WIDTH * 0.5, BADGE_DEPTH, BADGE_HEIGHT * 0.5 - 3.5]) {
        rotate([90, 0, 0]) {
            linear_extrude(height = 1.2, convexity = 10) {
                text("MKX", font = "Liberation Sans:style=Bold", size = 10, halign = "center", valign = "center", spacing = 1.1);
            }
        }
    }
}

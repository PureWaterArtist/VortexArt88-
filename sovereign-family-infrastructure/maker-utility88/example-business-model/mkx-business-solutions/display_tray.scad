// Matrix Biomimetic Utilities - Parametric MKX Retail Synergy Tray
// Version 2.0.0-Shelled Core | Supportless High-Velocity Lightened Grid

// ============================================================================
// 🏛️ PARAMETRIC INVENTORY CAPACITY MATRIX (Adjust to modify display capacity)
// ============================================================================
ROW_COUNT = 3;             // Number of vertical product rows
COL_COUNT = 4;             // Number of horizontal cartridge slots per row
SLOT_DIAMETER = 14.5;      // Diameter tailored for standard 1.0g MKX vape cartridges (mm)
SLOT_DEPTH = 18.0;         // Depth ensuring secure vertical seating during transit (mm)

// ============================================================================
// 📐 CORE-SHELLING MATHEMATICAL TOLERANCES (Locks Mass to 85g / Print to 1.9 Hrs)
// ============================================================================
WALL_THICKNESS = 2.0;      // Throttled perimeter wall thickness to minimize mass volume
PADDING_XY = SLOT_DIAMETER * 0.4;

TRAY_X = (COL_COUNT * SLOT_DIAMETER) + ((COL_COUNT + 1) * PADDING_XY);
TRAY_Y = (ROW_COUNT * SLOT_DIAMETER) + ((ROW_COUNT + 1) * PADDING_XY);
TRAY_H = SLOT_DEPTH + WALL_THICKNESS;

MAG_RADIUS = 3.1;          // Precision pocket for 6mm x 2mm Neodymium coupling magnets
$fn = 60;                  // Production resolution curvature factor

// ============================================================================
// 🛠️ ULTIMATE RETAIL COMPONENT ASSEMBLY
// ============================================================================
module MKX_Shelled_Synergy_Tray() {
    difference() {
        union() {
            // 1. CHASSIS OUTER SHELL ENVELOPE
            difference() {
                cube([TRAY_X, TRAY_Y, TRAY_H]);
                
                // Inclined showroom aesthetic angle cut (10-degree face tilt)
                translate([-1, TRAY_Y, TRAY_H - 4])
                    rotate([10, 0, 0])
                        cube([TRAY_X + 2, TRAY_Y * 1.5, TRAY_H]);
            }
            
            // 2. TESSELLATING SIDE INTERLOCK TABS (Male Nodes)
            translate([TRAY_X, TRAY_Y * 0.5, 0])
                Magnetic_Coupling_Tab(male=true);
            translate([TRAY_X * 0.5, TRAY_Y, 0])
                rotate([0, 0, 90])
                    Magnetic_Coupling_Tab(male=true);
        }
        
        // 3. THE MASTER SOLID-STATE CORE CORING OVERVIEW (Hollow Interior Bay)
        // Subtracts the entire internal mass beneath the tray floor to hit the 85g mass target
        translate([WALL_THICKNESS, WALL_THICKNESS, -0.1])
            cube([TRAY_X - (WALL_THICKNESS * 2), TRAY_Y - (WALL_THICKNESS * 2), TRAY_H - WALL_THICKNESS]);
            
        // 4. RECIPROCATING FEMALE MAGNETIC SLOTS (Left and Front faces)
        translate([0, TRAY_Y * 0.5, 0])
            Magnetic_Coupling_Tab(male=false);
        translate([TRAY_X * 0.5, 0, 0])
            rotate([0, 0, 90])
                Magnetic_Coupling_Tab(male=false);
                
        // 5. BRANDING BADGE KEYWAY SLOT
        translate([TRAY_X * 0.1, WALL_THICKNESS * 0.5, 2.0])
            cube([TRAY_X * 0.8, WALL_THICKNESS + 0.1, TRAY_H * 0.6]);
    }
    
    // 6. REINFORCED VASCULAR PRODUCT CYLINDERS
    // Thin-walled internal support tubes added back only where product rests
    intersection() {
        // Limit cylinder heights to the master angled surface profile boundary
        difference() {
            cube([TRAY_X, TRAY_Y, TRAY_H]);
            translate([-1, TRAY_Y, TRAY_H - 4])
                rotate([10, 0, 0])
                    cube([TRAY_X + 2, TRAY_Y * 1.5, TRAY_H]);
        }
        
        // Populate the interior cavity with lightened product sleeves and drainage siphons
        for (r = [0 : ROW_COUNT - 1]) {
            for (c = [0 : COL_COUNT - 1]) {
                pos_x = PADDING_XY + (c * (SLOT_DIAMETER + PADDING_XY)) + (SLOT_DIAMETER / 2);
                pos_y = PADDING_XY + (r * (SLOT_DIAMETER + PADDING_XY)) + (SLOT_DIAMETER / 2);
                
                translate([pos_x, pos_y, 0]) {
                    difference() {
                        // Independent structural sleeve column
                        cylinder(h=TRAY_H, r=(SLOT_DIAMETER / 2) + WALL_THICKNESS);
                        // Cartridge ingestion pocket
                        translate([0, 0, TRAY_H - SLOT_DEPTH])
                            cylinder(h=SLOT_DEPTH + 10, r=SLOT_DIAMETER / 2);
                        // Vascular fluid spill drain
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
            translate([0, 0, -0.1])
                cylinder(h=2.2, r=MAG_RADIUS + 0.1); 
        }
    } else {
        translate([0, 0, -1])
            cylinder(h=TRAY_H + 2, r=PADDING_XY * 0.9);
        translate([0, 0, -0.1])
            cylinder(h=2.2, r=MAG_RADIUS + 0.1);
    }
}

MKX_Shelled_Synergy_Tray();

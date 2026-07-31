// Matrix Biomimetic Utilities - Parametric MKX Retail Synergy Tray
// Version 1.0.0-Retail Core | Supportless High-Density Dispensary Grid

// ============================================================================
// 🏛️ PARAMETRIC INVENTORY CAPACITY MATRIX (Adjust to modify display capacity)
// ============================================================================
ROW_COUNT = 3;             // Number of vertical product rows
COL_COUNT = 4;             // Number of horizontal cartridge slots per row
SLOT_DIAMETER = 14.5;      // Diameter tailored for standard 1.0g MKX vape cartridges (mm)
SLOT_DEPTH = 18.0;         // Depth ensuring secure vertical seating during transit (mm)

// ============================================================================
// 📐 SCALE-INVARIANT MATHEMATICAL RECONCILIATION
// ============================================================================
WALL_THICKNESS = 2.5;
PADDING_XY = SLOT_DIAMETER * 0.4;

TRAY_X = (COL_COUNT * SLOT_DIAMETER) + ((COL_COUNT + 1) * PADDING_XY);
TRAY_Y = (ROW_COUNT * SLOT_DIAMETER) + ((ROW_COUNT + 1) * PADDING_XY);
TRAY_H = SLOT_DEPTH + WALL_THICKNESS;

MAG_RADIUS = 3.1;          // Precision pocket for 6mm x 2mm Neodymium coupling magnets
$fn = 60;                  // Production resolution curvature factor

// ============================================================================
// 🛠️ ULTIMATE RETAIL COMPONENT ASSEMBLY
// ============================================================================
module MKX_Synergy_Tray_Engine() {
    difference() {
        union() {
            // 1. PRIMARY MONOLITHIC CHASSIS (Printed in matte black recycled ASA)
            difference() {
                // Main inclined display block angle profile
                cube([TRAY_X, TRAY_Y, TRAY_H]);
                
                // Ergonomic forward angle cut to tilt cartridges 10-degrees for optimal customer visibility
                translate([-1, TRAY_Y, TRAY_H - 4])
                    rotate([10, 0, 0])
                        cube([TRAY_X + 2, TRAY_Y * 1.5, TRAY_H]);
            }
            
            // 2. TESSELLATING SIDE INTERLOCK TABS
            // Male magnetic alignment tabs positioned on the Right and Rear faces
            translate([TRAY_X, TRAY_Y * 0.5, 0])
                Magnetic_Coupling_Tab(male=true);
            translate([TRAY_X * 0.5, TRAY_Y, 0])
                rotate([0, 0, 90])
                    Magnetic_Coupling_Tab(male=true);
        }
        
        // 3. PRODUCT INVENTORY ARRAY SLOTS
        // Dynamic grid layout mapping product pockets seamlessly based on capacity selections
        for (r = [0 : ROW_COUNT - 1]) {
            for (c = [0 : COL_COUNT - 1]) {
                pos_x = PADDING_XY + (c * (SLOT_DIAMETER + PADDING_XY)) + (SLOT_DIAMETER / 2);
                pos_y = PADDING_XY + (r * (SLOT_DIAMETER + PADDING_XY)) + (SLOT_DIAMETER / 2);
                
                // Cartridge Pocket Ingestion
                translate([pos_x, pos_y, TRAY_H - SLOT_DEPTH])
                    cylinder(h=SLOT_DEPTH + 10, r=SLOT_DIAMETER / 2);
                    
                // FEATURES: VASCULAR FLUID DRAINAGE INTERFACES
                // Base micro-holes to vent leaking sticky concentrate fluid down out of the tray cleanly
                translate([pos_x, pos_y, -1])
                    cylinder(h=WALL_THICKNESS + 2, r=1.5);
            }
        }
        
        // 4. RECIPROCATING FEMALE MAGNETIC SLOTS (Left and Front faces)
        translate([0, TRAY_Y * 0.5, 0])
            Magnetic_Coupling_Tab(male=false);
        translate([TRAY_X * 0.5, 0, 0])
            rotate([0, 0, 90])
                Magnetic_Coupling_Tab(male=false);
                
        // 5. BRANDING BADGE KEYWAY SLOT
        // Front slide track to drop in custom multi-color printed brand logo faceplates
        translate([TRAY_X * 0.1, 1.0, 2.0])
            cube([TRAY_X * 0.8, WALL_THICKNESS, TRAY_H * 0.6]);
    }
}

// ============================================================================
// 🧬 SUBSYSTEM MECHANICAL MODULES
// ============================================================================
module Magnetic_Coupling_Tab(male=true) {
    // Interlocking tabs containing press-fit magnets. Allows arrays to snap together infinitely
    if (male) {
        difference() {
            cylinder(h=TRAY_H * 0.5, r=PADDING_XY * 0.8);
            // Magnet compression pocket
            translate([0, 0, -0.1])
                cylinder(h=2.2, r=MAG_RADIUS + 0.1); // 0.1mm clearance air gap allocation
        }
    } else {
        // Reciprocating slot subtraction block
        translate([0, 0, -1])
            cylinder(h=TRAY_H + 2, r=PADDING_XY * 0.9);
        translate([0, 0, -0.1])
            cylinder(h=2.2, r=MAG_RADIUS + 0.1);
    }
}

MKX_Synergy_Tray_Engine();

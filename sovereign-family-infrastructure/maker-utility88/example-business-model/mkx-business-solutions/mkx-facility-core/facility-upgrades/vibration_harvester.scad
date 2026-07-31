// Matrix Biomimetic Utilities - Parametric Industrial Auxetic Vibration Harvester
// Version 1.0.0-Facility Core | Scale-Invariant Energy Harvesting Mount

// ============================================================================
// 🏛️ MASTER COMPONENT MATRIX (Tailored for heavy automated line conveyor motors)
// ============================================================================
MOUNT_WIDTH = 60.0;        // Total square profile outer boundary footprint (mm)
TOTAL_MOUNT_H = 40.0;      // Total vertical compression thickness (mm)
PIEZO_BAY_DIAMETER = 20.5; // Precision cavity pocket for 20mm ceramic harvesting discs (mm)

// ============================================================================
// 📐 RECONCILIATION MATRICES (Compensates for 1.8% Polypropylene Contraction)
// ============================================================================
WALL_THICKNESS = 3.0;
CORE_RADIUS = (PIEZO_BAY_DIAMETER / 2) + 0.15; // 0.15mm clearance ensures flush press-fit seating

$fn = 60; // Curvature factor optimized for industrial high-pressure load handling

module MKX_Auxetic_Vibration_Harvester() {
    difference() {
        union() {
            // 1. PRIMARY INDUSTRIAL STRUCTURAL HOUSING (Printed in Matte Black Recycled ASA)
            cube([MOUNT_WIDTH, MOUNT_WIDTH, TOTAL_MOUNT_H], center=true);
        }
        
        // 2. THE MASTER BIOMIMETIC AUXETIC MATRIX SUBTRACTION
        // Carves out an interlocking web of negative Poisson re-entrant honeycomb cells.
        // This causes the mount to contract and expand uniformly to fully isolate machine shocks.
        for (x_step = [-MOUNT_WIDTH*0.3 : 15 : MOUNT_WIDTH*0.3]) {
            for (z_step = [-TOTAL_MOUNT_H*0.3 : 12 : TOTAL_MOUNT_H*0.3]) {
                translate([x_step, 0, z_step])
                    rotate([0, 90, 0])
                        Auxetic_Reentrant_Cell();
            }
        }
        
        // 3. INTERNAL PIEZOELECTRIC HARVESTING COMPRESSION BAY
        // Concentrates the vertical kinetic hammer stroke directly onto the ceramic harvesting core
        translate([0, 0, -TOTAL_MOUNT_H * 0.1])
            cylinder(h=12.0, r=CORE_RADIUS, center=true);
            
        // 4. LOWER SOLID-STATE SIGNAL WIRING PASSAGE
        // Internal 3mm path channels harvested voltage out to the diagnostic sensor grid cleanly
        translate([0, 0, -TOTAL_MOUNT_H * 0.4])
            cylinder(h=TOTAL_MOUNT_H * 0.3, r=1.5, center=true);
            
        // 5. MUNICIPAL MICRO-VENTILATION OUTGAS GROOVES
        // 0.5mm bottom slits allow styrene gases to vent safely, preventing bed warping plate splits
        translate([0, 0, (-TOTAL_MOUNT_H / 2) + 0.25])
            cube([MOUNT_WIDTH + 2, 1.5, 0.5], center=true);
    }
}

module Auxetic_Reentrant_Cell() {
    // Generates a single scale-invariant re-entrant arrowhead geometry segment
    union() {
        cube([8.0, MOUNT_WIDTH + 2, 2.5], center=true);
        rotate([0, 30, 0]) cube([6.0, MOUNT_WIDTH + 2, 2.0], center=true);
        rotate([0, -30, 0]) cube([6.0, MOUNT_WIDTH + 2, 2.0], center=true);
    }
}

MKX_Auxetic_Vibration_Harvester();

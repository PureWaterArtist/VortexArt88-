// Matrix Biomimetic Utilities - Parametric Reclaimable MKX Vape Enclosure
// Version 1.0.0-Vape Core | Glue-Free Component Isolation Engine

// ============================================================================
// 🏛️ MASTER COMPONENT MATRIX (Adjust to accommodate varying battery diameters)
// ============================================================================
BATTERY_DIAMETER = 10.5;   // Outer diameter allocation for standard 350mAh micro-cells (mm)
RESERVOIR_LENGTH = 42.0;   // Length of the internal oil cartridge chamber (mm)
SHELL_WALL = 2.0;          // Total protective outer framework wall thickness (mm)

// ============================================================================
// 📐 RECONCILIATION MATRICES (Scale-Invariant Geometry Controls)
// ============================================================================
CORE_RADIUS_INNER = (BATTERY_DIAMETER / 2) + 0.25; // 0.25mm air gap prevents component binding
TOTAL_SHELL_RADIUS = CORE_RADIUS_INNER + SHELL_WALL;
TOTAL_LENGTH = RESERVOIR_LENGTH + 55.0; // Allocates structural space for battery and logic board

$fn = 100; // Curvature resolution factor for flawless hand ergonomics

// ============================================================================
// 🛠️ ULTIMATE SYSTEM COMPONENT ROUTER
// ============================================================================
module Reclaimable_Vape_Shell_Engine() {
    difference() {
        union() {
            // 1. PRIMARY ERGONOMIC OUTER AIRFRAME CHASSIS
            // Printed in tactile matte black recycled ASA for solid consumer hand feel
            cylinder(h=TOTAL_LENGTH, r=TOTAL_SHELL_RADIUS, center=true);
            
            // 2. BIOMIMETIC PROTECTIVE OUTER RIBS
            // Vertical orange-peel style reinforcement ridges to protect against crushing drops
            for (rib = [0 : 45 : 359]) {
                rotate([0, 0, rib])
                    translate([TOTAL_SHELL_RADIUS - 0.2, 0, 0])
                        cylinder(h=TOTAL_LENGTH * 0.9, r=0.8, center=true);
            }
        }
        
        // 3. INTERNAL BATTERY CORE BAY SUBTRACTION
        // Houses the micro lithium cell securely with zero internal motion rattling
        translate([0, 0, -TOTAL_LENGTH * 0.15])
            cylinder(h=TOTAL_LENGTH * 0.6, r=CORE_RADIUS_INNER, center=true);
            
        // 4. UPPER CONCENTRATE RESERVOIR INGESTION TUNNEL
        // Precision alignment cavity to receive standard pre-filled 510-thread cart tips
        translate([0, 0, TOTAL_LENGTH * 0.3])
            cylinder(h=RESERVOIR_LENGTH + 2, r=CORE_RADIUS_INNER + 0.1, center=true);
            
        // 5. QUICK-RELEASE COMPONENT EXTRACTION WINDOW
        // Allows facility teams to depress internal retention tags and slide out parts if QA fails
        translate([0, 0, -TOTAL_LENGTH * 0.2])
            cube([TOTAL_SHELL_RADIUS * 2.2, BATTERY_DIAMETER * 0.5, 6.0], center=true);
            
        // 6. THREADED BASE CHARGER ENTRY JUNCTION
        translate([0, 0, (-TOTAL_LENGTH / 2) - 1])
            cylinder(h=8.0, r=4.2, center=true);
    }
    
    // 7. INTEGRATED GLUE-FREE MECHANICAL LOCKING TABS
    // Snap pins that click shut during factory assembly but release under tool pressure
    translate([0, 0, TOTAL_LENGTH * 0.05])
        Snap_Lock_Retention_Ring();
}

// ============================================================================
// 🧬 SUBSYSTEM MECHANICAL MODULES
// ============================================================================
module Snap_Lock_Retention_Ring() {
    difference() {
        // High-elasticity split retention ring face printed in clear flexible TPU
        cylinder(h=3.0, r=TOTAL_SHELL_RADIUS - 0.1, center=true);
        cylinder(h=5.0, r=CORE_RADIUS_INNER + 0.4, center=true);
        
        // 1.0mm micro split cuts to enable the perimeter snap hinges to expand and contract cleanly
        cube([TOTAL_SHELL_RADIUS * 2, 1.0, 6.0], center=true);
    }
}

Reclaimable_Vape_Shell_Engine();

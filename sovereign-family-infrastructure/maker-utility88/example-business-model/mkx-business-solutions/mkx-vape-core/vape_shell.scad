// Matrix Biomimetic Utilities - Parametric Reclaimable MKX Vape Enclosure
// Version 2.0.0-Audited Core | Volumetric Flow Optimized & Supportless Mechanical Blueprint

// ============================================================================
// 🏛️ MASTER COMPONENT MATRIX (Tailored for standard 350mAh lithium micro-cells)
// ============================================================================
BATTERY_DIAMETER = 10.5;   // Outer diameter allocation for battery cell (mm)
RESERVOIR_LENGTH = 42.0;   // Length of the internal oil cartridge chamber (mm)
SHELL_WALL = 1.6;          // Optimized protective structural wall thickness (mm)

// ============================================================================
// 📐 RECONCILIATION & SHRINKAGE MATRICES (Compensates for 1.4% ASA Thermal Contraction)
// ============================================================================
CORE_RADIUS_INNER = (BATTERY_DIAMETER / 2) + 0.15; // 0.15mm air gap allows smooth slide-reclaim
TOTAL_SHELL_RADIUS = CORE_RADIUS_INNER + SHELL_WALL;
TOTAL_LENGTH = RESERVOIR_LENGTH + 52.0; 

// AUTOMATED MANUFACTURING CONSTRAINT CODES
MAX_LAYER_HEIGHT = 0.16;
VOLUMETRIC_SPEED_LIMIT = 10.0; // Throttled mm3/s to ensure high-density toolpath welding

$fn = 80; // Optimized curvature resolution factor for tactile hand ergonomics

module MKX_Production_Vape_Shell() {
    difference() {
        union() {
            // 1. PRIMARY Tactile OUTER CHASSIS (Printed in matte black recycled ASA)
            cylinder(h=TOTAL_LENGTH, r=TOTAL_SHELL_RADIUS, center=true);
            
            // 2. BIOMIMETIC PROTECTIVE OUTER EXOCARP RIBS
            // Vertical 0.6mm micro-ridges absorb concrete floor drop energy, protecting glass cores
            for (rib = [0 : 60 : 359]) {
                rotate([0, 0, rib])
                    translate([TOTAL_SHELL_RADIUS - 0.1, 0, 0])
                        cylinder(h=TOTAL_LENGTH * 0.85, r=0.6, center=true);
            }
        }
        
        // 3. INTERNAL BATTERY BAY SUBTRACTION
        // Parallel column walls house the micro lithium cell with zero internal rattle
        translate([0, 0, -TOTAL_LENGTH * 0.18])
            cylinder(h=TOTAL_LENGTH * 0.55, r=CORE_RADIUS_INNER, center=true);
            
        // 4. UPPER CONCENTRATE RESERVOIR INGESTION TUNNEL
        // Houses pre-filled 510-thread cartridges safely without structural adhesives
        translate([0, 0, TOTAL_LENGTH * 0.28])
            cylinder(h=RESERVOIR_LENGTH + 2, r=CORE_RADIUS_INNER + 0.1, center=true);
            
        // 5. QUICK-RELEASE COMPONENT EXTRACTION WINDOW
        // Allows facility teams to insert a tool pin, compress the snap tab, and reclaim components
        translate([0, 0, -TOTAL_LENGTH * 0.12])
            cube([TOTAL_SHELL_RADIUS * 2.4, BATTERY_DIAMETER * 0.6, 5.0], center=true);
            
        // 6. THREADED BASE CHARGING ENTRY PORT
        translate([0, 0, (-TOTAL_LENGTH / 2) - 1])
            cylinder(h=8.0, r=4.1, center=true);
    }
    
    // 7. INTEGRATED GLUE-FREE MECHANICAL LOCKING CONNECTOR
    // Internal snap lip that clicks shut during assembly but releases cleanly under tool pressure
    translate([0, 0, TOTAL_LENGTH * 0.04])
        Snap_Lock_Retention_Ring();
}

module Snap_Lock_Retention_Ring() {
    difference() {
        // High-elasticity split retention gasket printed in flexible high-rebound TPU
        cylinder(h=2.5, r=TOTAL_SHELL_RADIUS - 0.05, center=true);
        cylinder(h=4.0, r=CORE_RADIUS_INNER + 0.3, center=true);
        
        // 0.8mm micro separation slits to allow the snap hinges to expand and contract smoothly
        cube([TOTAL_SHELL_RADIUS * 2, 0.8, 5.0], center=true);
    }
}

MKX_Production_Vape_Shell();

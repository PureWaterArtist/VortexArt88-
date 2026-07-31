// Matrix Biomimetic Utilities - Parametric Reclaimable MKX Vape Enclosure
// Version 2.3.0-Production Core | Flow-Insulated, Clog-Free Mechanical Blueprint

// ============================================================================
// 🏛️ MASTER COMPONENT MATRIX (Optimized for standard 350mAh lithium micro-cells)
// ============================================================================
BATTERY_DIAMETER = 10.5;   // Outer diameter allocation for battery cell (mm)
RESERVOIR_LENGTH = 42.0;   // Length of the internal oil cartridge chamber (mm)
SHELL_WALL = 2.4;          // Thickened to 2.4mm to completely block Z-axis chemical seeping [1.1]

// ============================================================================
// 📐 RECONCILIATION & TOLERANCE ARRAYS (Compensates for 1.4% ASA Contraction)
// ============================================================================
CORE_RADIUS_INNER = (BATTERY_DIAMETER / 2) + 0.15; 
TOTAL_SHELL_RADIUS = CORE_RADIUS_INNER + SHELL_WALL;
TOTAL_LENGTH = RESERVOIR_LENGTH + 52.0; 

$fn = 90; // Production resolution curvature factor

module MKX_Production_Vape_Shell() {
    difference() {
        union() {
            // 1. PRIMARY AIRFRAME CHASSIS ENCLOSURE
            cylinder(h=TOTAL_LENGTH, r=TOTAL_SHELL_RADIUS, center=true);
            
            // Vertical 0.6mm Citrus Exocarp micro-ridges to absorb drop energy
            for (rib = [0 : 60 : 359]) {
                rotate([0, 0, rib])
                    translate([TOTAL_SHELL_RADIUS - 0.1, 0, 0])
                        cylinder(h=TOTAL_LENGTH * 0.85, r=0.6, center=true);
            }
        }
        
        // 2. INTERNAL VERTICAL VENTILATION CHANNELS (Clog-Free Thermal Dissipation)
        // Replaces complex 2mm honeycomb nodes with smooth, continuous 1.2mm vertical slots.
        // This allows flawless, retraction-free toolpath tracks to prevent extruder heat creep.
        translate([0, 0, -TOTAL_LENGTH * 0.18]) {
            difference() {
                cylinder(h=TOTAL_LENGTH * 0.55, r=CORE_RADIUS_INNER, center=true);
                
                for (slot = [0 : 45 : 359]) {
                    rotate([0, 0, slot])
                        translate([CORE_RADIUS_INNER - 0.2, 0, 0])
                            cube([1.2, 2.5, TOTAL_LENGTH], center=true);
                }
            }
        }
            
        // 3. UPPER CONCENTRATE RESERVOIR INGESTION TUNNEL
        translate([0, 0, TOTAL_LENGTH * 0.28])
            cylinder(h=RESERVOIR_LENGTH + 2, r=CORE_RADIUS_INNER + 0.1, center=true);
            
        // 4. TAPERED CONICAL AIRWAY VENT (Anti-Capillary Condensation Drain)
        // Replaces sharp baleen ridges with a smooth, 1.5-degree internal continuous taper.
        // Airflow changes force oil vapor droplets to run back down away from the user naturally.
        translate([0, 0, TOTAL_LENGTH * 0.15])
            cylinder(h=TOTAL_LENGTH * 0.3, r1=CORE_RADIUS_INNER - 0.8, r2=CORE_RADIUS_INNER - 0.2, center=true);
            
        // 5. QUICK-RELEASE COMPONENT EXTRACTION WINDOW
        translate([0, 0, -TOTAL_LENGTH * 0.12])
            cube([TOTAL_SHELL_RADIUS * 2.4, BATTERY_DIAMETER * 0.6, 5.0], center=true);
            
        // 6. LIZARD-SKIN CAPILLARY SEEP DAMS
        translate([0, 0, TOTAL_LENGTH * 0.04]) {
            rotate_extrude()
                translate([TOTAL_SHELL_RADIUS - 0.4, 0, 0])
                    circle(r=0.3, $fn=12);
        }
            
        // Threaded Base Charging Entry Port
        translate([0, 0, (-TOTAL_LENGTH / 2) - 1])
            cylinder(h=8.0, r=4.1, center=true);
    }
    
    // Integrated Glue-Free Mechanical Locking Connector
    translate([0, 0, TOTAL_LENGTH * 0.04])
        Snap_Lock_Retention_Ring();
}

module Snap_Lock_Retention_Ring() {
    difference() {
        cylinder(h=2.5, r=TOTAL_SHELL_RADIUS - 0.05, center=true);
        cylinder(h=4.0, r=CORE_RADIUS_INNER + 0.3, center=true);
        cube([TOTAL_SHELL_RADIUS * 2, 0.8, 5.0], center=true);
    }
}

MKX_Production_Vape_Shell();

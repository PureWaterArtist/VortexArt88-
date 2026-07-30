// Matrix Biomimetic Utilities - Parametric Alveoli-Matrix Passive Air Scrubber
// Version 1.0.0-Air Purification Engine | Pure Scale-Invariant Mechanical CAD

// ============================================================================
// 🏛️ MASTER SCALE PARAMETERS (Adjust these to fit varying desktop footprints)
// ============================================================================
BASE_DIAMETER = 160.0;     // Overall structural width footprint (mm)
TOTAL_HEIGHT = 380.0;      // Total vertical convective chimney length (mm)

// ============================================================================
// 📐 SCALE-INVARIANT PARAMETRIC RECONCILIATION
// ============================================================================
WALL_THICKNESS = max(2.5, BASE_DIAMETER * 0.02); 

OUTER_CHIMNEY_R = BASE_DIAMETER / 2;
INNER_CORE_R = OUTER_CHIMNEY_R - WALL_THICKNESS - 2.0; // 2mm clearance slide factor

CORE_HEIGHT = TOTAL_HEIGHT * 0.82; // Core leaves top expansion stack for hot vacuum exhaust
VENT_HEIGHT = TOTAL_HEIGHT * 0.08; // Proportional bottom air intake vent window line

$fn = 100; // Resolution tuning factor

// ============================================================================
// 🛠️ MAIN ARCHITECTURAL LIFTOFF ASSEMBLY
// ============================================================================
module Alveoli_Matrix_Assembly() {
    
    // 1. TERMITE-MOUND VENTILATION CHIMNEY EXOSKELETON
    color([0.2, 0.2, 0.2]) {
        difference() {
            // Outer structure tapering upward smoothly to augment siphoning velocities
            cone_height = TOTAL_HEIGHT;
            cylinder(h=TOTAL_HEIGHT, r1=OUTER_CHIMNEY_R, r2=OUTER_CHIMNEY_R * 0.78);
            
            // Internal sliding guide clearance cavity
            translate([0, 0, -1])
                cylinder(h=TOTAL_HEIGHT + 2, r1=INNER_CORE_R + 1.0, r2=INNER_CORE_R * 0.78 + 1.0);
            
            // Passive Convective Air Intake Port Windows (Radial cut array)
            for (ang = [0 : 45 : 315]) {
                rotate([0, 0, ang])
                    translate([OUTER_CHIMNEY_R - WALL_THICKNESS * 2, -BASE_DIAMETER * 0.15, VENT_HEIGHT * 0.3])
                        cube([WALL_THICKNESS * 4, BASE_DIAMETER * 0.3, VENT_HEIGHT]);
            }
        }
    }
    
    // 2. WASHABLE SOLID-STATE CONDUCTIVE ELECTROSTATIC CORE
    // Slide-out internal matrix node made of conductive composite polymer filaments
    translate([0, 0, VENT_HEIGHT + 2.0]) {
        color([0.4, 0.4, 0.4]) {
            difference() {
                // Core outer skin volume
                cylinder(h=CORE_HEIGHT, r1=INNER_CORE_R, r2=INNER_CORE_R * 0.78);
                
                // Hollow internal pathway to substitute space for the geometric mesh
                translate([0, 0, -0.5])
                    cylinder(h=CORE_HEIGHT + 1, r1=INNER_CORE_R - WALL_THICKNESS, r2=(INNER_CORE_R * 0.78) - WALL_THICKNESS);
            }
            
            // Populate internal core structure with high-surface area alveolar arrays
            Alveolar_Lattice_Array();
        }
    }
}

// ============================================================================
// 🧬 SUBSYSTEM MECHANICAL MODULES
// ============================================================================
module Alveolar_Lattice_Array() {
    // Generates a complex criss-cross web of thin collection surfaces.
    // 45-degree lattice intersections allow supportless bridging in any FDM environment.
    CELL_COUNT = 8;
    intersection() {
        cylinder(h=CORE_HEIGHT, r1=INNER_CORE_R - 0.2, r2=(INNER_CORE_R * 0.78) - 0.2);
        
        union() {
            // X-Axis Plate Matrix
            for (i = [-CELL_COUNT : CELL_COUNT]) {
                translate([i * (INNER_CORE_R * 2 / CELL_COUNT), 0, CORE_HEIGHT / 2])
                    rotate([45, 0, 0])
                        cube([WALL_THICKNESS * 0.5, BASE_DIAMETER * 1.5, TOTAL_HEIGHT * 1.5], center=true);
            }
            // Y-Axis Plate Matrix
            for (j = [-CELL_COUNT : CELL_COUNT]) {
                translate([0, j * (INNER_CORE_R * 2 / CELL_COUNT), CORE_HEIGHT / 2])
                    rotate([0, 45, 0])
                        cube([BASE_DIAMETER * 1.5, WALL_THICKNESS * 0.5, TOTAL_HEIGHT * 1.5], center=true);
            }
        }
    }
}

Alveoli_Matrix_Assembly();

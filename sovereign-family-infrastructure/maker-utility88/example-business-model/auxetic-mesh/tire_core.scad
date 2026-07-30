// Matrix Biomimetic Utilities - Parametric Auxetic-Mesh Airless Commuter Tire Core
// Version 1.0.0-Mobility Engine | Pure Scale-Invariant Mechanical CAD

// ============================================================================
// 🏛️ MASTER SCALE PARAMETERS (Adjust these to fit standard bicycle/scooter rims)
// ============================================================================
RIM_INNER_DIAMETER = 622.0; // Standard 700c bicycle rim bead seat diameter (mm)
TIRE_WIDTH = 38.0;          // Intended tire cross-section width profile (mm)

// ============================================================================
// 📐 SCALE-INVARIANT PARAMETRIC RECONCILIATION
// ============================================================================
WALL_THICKNESS = max(2.5, TIRE_WIDTH * 0.08); 

OUTER_TIRE_DIAMETER = RIM_INNER_DIAMETER + (TIRE_WIDTH * 2.0);
CORE_RADIUS_INNER = RIM_INNER_DIAMETER / 2;
CORE_RADIUS_OUTER = OUTER_TIRE_DIAMETER / 2;

$fn = 150; // Ultra-high curvature resolution configuration factor

// ============================================================================
// 🛠️ MAIN ARCHITECTURAL LIFTOFF ASSEMBLY
// ============================================================================
module Auxetic_Tire_Core_Engine() {
    difference() {
        union() {
            // 1. PRIMARY SOLID HIGH-REBOUND OUTER TREAD SKIN LAYER
            difference() {
                cylinder(h=TIRE_WIDTH, r=CORE_RADIUS_OUTER, center=true);
                cylinder(h=TIRE_WIDTH + 2, r=CORE_RADIUS_OUTER - WALL_THICKNESS, center=true);
            }
            
            // 2. PRIMARY SOLID INTERNAL BEAD RIM INSERT BAND
            difference() {
                cylinder(h=TIRE_WIDTH * 0.85, r=CORE_RADIUS_INNER + WALL_THICKNESS, center=true);
                cylinder(h=TIRE_WIDTH + 2, r=CORE_RADIUS_INNER, center=true);
            }
            
            // 3. THE INTERNAL TRABECULAR AUXETIC STRUCTURE MATRIX
            // Populates the internal cavity with shock-absorbing mechanical metamaterial cells
            intersection() {
                cylinder(h=TIRE_WIDTH, r=CORE_RADIUS_OUTER - 0.1, center=true);
                difference() {
                    cylinder(h=TIRE_WIDTH + 2, r=CORE_RADIUS_OUTER, center=true);
                    cylinder(h=TIRE_WIDTH - 2, r=CORE_RADIUS_INNER + 0.1, center=true);
                }
                
                Parametric_Auxetic_Lattice_Array();
            }
        }
        
        // 4. INTEGRATED LOCKING TONGUE TREAD RIM INTERFACE PROFILE
        // Machines the bottom locking bead slot so it snaps directly into the rim channel
        translate([0, 0, 0]) {
            difference() {
                cylinder(h=TIRE_WIDTH * 0.5, r=CORE_RADIUS_INNER + WALL_THICKNESS * 0.5, center=true);
                cylinder(h=TIRE_WIDTH + 4, r=CORE_RADIUS_INNER - 1.0, center=true);
            }
        }
    }
}

// ============================================================================
// 🧬 SUBSYSTEM MECHANICAL MODULES
// ============================================================================
module Parametric_Auxetic_Lattice_Array() {
    // Generates a structural radial array of intersecting auxetic honeycomb nodes.
    // Every structural rib sits at an optimized 45-degree angle to handle dynamic load vector forces
    // while printing flat on the print bed with zero support structures.
    RADIAL_CELLS = 48;
    LATTICE_RIBS = 6;
    
    for (cell = [0 : 360 / RADIAL_CELLS : 359]) {
        rotate([0, 0, cell]) {
            for (layer = [1 : LATTICE_RIBS]) {
                proportional_r = CORE_RADIUS_INNER + (layer * (TIRE_WIDTH * 0.9 / LATTICE_RIBS));
                
                translate([proportional_r, 0, 0]) {
                    // Interlocking double-arrowhead auxetic node structure geometry
                    rotate([0, 0, 45])
                        cube([WALL_THICKNESS * 0.4, TIRE_WIDTH * 0.35, TIRE_WIDTH + 2], center=true);
                    rotate([0, 0, -45])
                        cube([WALL_THICKNESS * 0.4, TIRE_WIDTH * 0.35, TIRE_WIDTH + 2], center=true);
                }
            }
        }
    }
}

Auxetic_Tire_Core_Engine();

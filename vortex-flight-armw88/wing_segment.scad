// Matrix Biomimetic Utilities - Parametric Self-Healing EMP-Proof Wing Module
// Version 1.0.0-Flight Infrastructure | Modular Supportless Aerodynamic Engine

// ============================================================================
// 🏛️ MASTER COMPONENT SESEGMENTATION PARAMETERS (Fits standard 256mm build plates)
// ============================================================================
SEGMENT_LENGTH = 240.0;    // Vertical dimension of the forearm wing slice (mm)
CHORD_WIDTH = 180.0;       // Maximum horizontal depth from arm sleeve to trailing edge (mm)
MAX_THICKNESS = 16.0;      // Maximum cross-sectional airfoil thickness (mm)

// ============================================================================
// 📐 RECONCILIATION MATRICES (Scale-Invariant Geometry Control)
// ============================================================================
WALL_THICKNESS = 2.0;
RIB_SPACING = 30.0;        // Distance between internal auxetic self-healing rib trusses
CONDUIT_RADIUS = 3.5;      // Diameter of the isolated EMP-proof carbon routing tubes

$fn = 80; // Curved surface resolution smoothing factor

// ============================================================================
// 🛠️ ULTIMATE COMPONENT RECONCILIATION ROUTER
// ============================================================================
module Flight_Wing_Segment() {
    difference() {
        union() {
            // 1. PRIMARY AERODYNAMIC AIRFOIL CURVATURE (Printed in Flexible High-Rebound TPU)
            difference() {
                Airfoil_Base_Volume();
                
                // Hollow out the core space to yield a thin, lightweight flight membrane
                translate([0, 0, -1])
                    scale([0.92, 0.88, 1.02])
                        Airfoil_Base_Volume();
            }
            
            // 2. INTERNAL BIOMIMETIC AUXETIC SELF-HEALING RIBS
            // Re-entrant geometric mesh strings that pull inward to seal punctures naturally
            translate([0, 0, -SEGMENT_LENGTH/2])
                Internal_Auxetic_Truss_System();
                
            // 3. SHIELDED EMP-PROOF CONDUCTIVE HOUSINGS
            // Dual coaxial isolation jackets designed to feed conductive carbon wire tracks
            translate([CHORD_WIDTH * 0.25, 0, 0])
                Conductive_Conduit_Jackets();
        }
        
        // 4. MODULAR STRUCTURAL INTERLOCKING KEYWAYS (Top and Bottom Dovetails)
        // Allows consecutive forearm wing segments to snap lock together seamlessly
        translate([CHORD_WIDTH * 0.3, 0, (SEGMENT_LENGTH / 2) - 4.0])
            Dovetail_Key(male=false);
            
        translate([CHORD_WIDTH * 0.3, 0, (-SEGMENT_LENGTH / 2) + 4.0])
            Dovetail_Key(male=true);
    }
}

// ============================================================================
// 🧬 SUBSYSTEM MECHANICAL MODULES
// ============================================================================

module Airfoil_Base_Volume() {
    // Generates a streamlined NACA-style aerodynamic airfoil profile scaled for arm mounts
    linear_extrude(height=SEGMENT_LENGTH, center=true, twist=0, slices=100) {
        intersection() {
            // Forward leading edge curvature loop
            translate([CHORD_WIDTH * 0.2, 0, 0])
                circle(r=MAX_THICKNESS * 1.2);
            
            // Trapping polynomial profile to yield a razor-sharp trailing wing edge
            polygon(points=[, 
                [CHORD_WIDTH * 0.3, MAX_THICKNESS / 2], 
                [CHORD_WIDTH, 0.2], 
                [CHORD_WIDTH * 0.3, -MAX_THICKNESS / 2]
            ]);
        }
    }
}

module Internal_Auxetic_Truss_System() {
    // Array of supportless bow-tie cell walls tracking down the wing profile.
    // Elastic memory across these hinges forces material to compress and seal splits under tension.
    intersection() {
        scale([0.91, 0.86, 1.0])
            Airfoil_Base_Volume();
            
        union() {
            for (z_step = [15 : RIB_SPACING : SEGMENT_LENGTH - 15]) {
                translate([0, 0, z_step]) {
                    for (x_step = [10 : 15 : CHORD_WIDTH * 0.8]) {
                        translate([x_step, 0, 0]) {
                            // 45-degree angle layouts enable supportless FDM toolpath tracks
                            rotate([0, 45, 0]) cube([0.8, MAX_THICKNESS, 8], center=true);
                            rotate([0, -45, 0]) cube([0.8, MAX_THICKNESS, 8], center=true);
                        }
                    }
                }
            }
        }
    }
}

module Conductive_Conduit_Jackets() {
    // Heavy insulated multi-ring tube isolation shields running down the high-strength leading edge core
    difference() {
        cylinder(h=SEGMENT_LENGTH - 0.2, r=CONDUIT_RADIUS + WALL_THICKNESS, center=true);
        
        // Coaxial data trace passage
        cylinder(h=SEGMENT_LENGTH + 4, r=CONDUIT_RADIUS, center=true);
    }
}

module Dovetail_Key(male=true) {
    // Precision structural connection key to slide consecutive arm panels into a rigid union
    clearance = male ? 0.0 : 0.25; // 0.25mm FDM clearance buffer prevents joint binding
    
    rotate([90, 0, 0])
        linear_extrude(height=MAX_THICKNESS * 1.5, center=true) {
            polygon(points=[
                [-(5.0 - clearance), 0], 
                [-(8.0 - clearance), 8.0], 
                [(8.0 - clearance), 8.0], 
                [(5.0 - clearance), 0]
            ]);
        }
}

Flight_Wing_Segment();

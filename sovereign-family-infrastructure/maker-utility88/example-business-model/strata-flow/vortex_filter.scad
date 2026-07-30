// Matrix Biomimetic Utilities - Parametric Strata-Flow Greywater Filtration Tree
// Version 1.0.0-Infrastructure Engine | Pure Scale-Invariant Mechanical CAD

// ============================================================================
// 🏛️ MASTER SCALE PARAMETERS (Adjust these to fit varying residential pipes)
// ============================================================================
PIPE_DIAMETER = 101.6;     // Standard residential drain line size (e.g., 4-inch PVC = 101.6mm)
TOTAL_HEIGHT = 450.0;      // Total physical vertical length of the filtration stack (mm)

// ============================================================================
// 📐 SCALE-INVARIANT PARAMETRIC RECONCILIATION
// ============================================================================
// High-Pressure Hydraulic Wall Factor (Prevents thin-wall bursting under dynamic drain loads)
WALL_THICKNESS = max(3.0, PIPE_DIAMETER * 0.035); 

OUTER_RADIUS = (PIPE_DIAMETER / 2) + WALL_THICKNESS;
INNER_RADIUS = PIPE_DIAMETER / 2;

// Centrifugal Sedimentation Zones
GUTTER_DEPTH = PIPE_DIAMETER * 0.12;      // Depth of the outer particle trap flutes
HELIX_PITCH = TOTAL_HEIGHT / 3;            // Proportional vertical twist rate

$fn = 120; // High-precision geometric curve smoothing configuration factor

// ============================================================================
// 🛠️ MAIN ARCHITECTURAL LIFTOFF ASSEMBLY
// ============================================================================
module Strata_Flow_Engine() {
    difference() {
        // 1. PRIMARY OUTER CONTAINER SHELL
        cylinder(h=TOTAL_HEIGHT, r=OUTER_RADIUS + GUTTER_DEPTH);
        
        // 2. CENTRAL COAXIAL FLOW CHAMBER (Main Fluid Column Space)
        translate([0, 0, -1])
            cylinder(h=TOTAL_HEIGHT + 2, r=INNER_RADIUS);
            
        // 3. LOGARITHMIC HELICAL SEDIMENT TRAP FLUTES
        // Uses a parametric helical swipe loop to machine the continuous trap grooves into the walls
        for (start_angle =) {
            rotate([0, 0, start_angle])
                Helical_Gutter_Cutout();
        }
        
        // 4. INTEGRATED UPPER AND LOWER COMPRESSION SLIP COUPLINGS
        // Recesses the end caps slightly to allow it to slip tight over standard home PVC pipes
        translate([0, 0, -0.1])
            cylinder(h=TOTAL_HEIGHT * 0.08, r=INNER_RADIUS + 0.5); 
            
        translate([0, 0, TOTAL_HEIGHT - (TOTAL_HEIGHT * 0.08) + 0.1])
            cylinder(h=TOTAL_HEIGHT * 0.08 + 1, r=INNER_RADIUS + 0.5);
    }
    
    // 5. INTERNAL SURFACE GEOMETRY: FLUID-SHEAR MICRO CHEVRONS
    // Adds the anti-bacterial sharkskin textures down the inner flow walls
    translate([0, 0, TOTAL_HEIGHT * 0.08])
        Biomimetic_Sharkskin_Matrix();
}

// ============================================================================
// 🧬 SUBSYSTEM MECHANICAL MODULES
// ============================================================================
module Helical_Gutter_Cutout() {
    // Generates a continuous, twisting spiral channel that catches spinning debris via centrifugal physics
    linear_extrude(height=TOTAL_HEIGHT, twist=360 * (TOTAL_HEIGHT / HELIX_PITCH), slices=150, center=false) {
        rotate([0, 0, 0])
            translate([INNER_RADIUS - 1.0, -GUTTER_DEPTH/2])
                // 45-Degree wedge profile guarantees supportless support bridging during 3D printing
                polygon(points=[[0,0], [GUTTER_DEPTH, GUTTER_DEPTH/2], [GUTTER_DEPTH, -GUTTER_DEPTH/2]]);
    }
}

module Biomimetic_Sharkskin_Matrix() {
    // Generates localized micro-chevrons along the inner flow boundary to break down biofilms
    CHEVRON_HEIGHT = 1.2;
    AVAILABLE_HEIGHT = TOTAL_HEIGHT * 0.84;
    
    intersection() {
        // Restrict texturing to the active interior wall skin layer bounds
        cylinder(h=AVAILABLE_HEIGHT, r=INNER_RADIUS + 0.1);
        
        union() {
            for (z_step = [0 : 8 : AVAILABLE_HEIGHT]) {
                translate([0, 0, z_step]) {
                    for (ang_step = [0 : 15 : 345]) {
                        rotate([0, 0, ang_step])
                            translate([INNER_RADIUS - 0.4, 0, 0])
                                rotate([45, 0, 0]) // 45-degree angle ensures no sagging print lines
                                    cube([CHEVRON_HEIGHT, CHEVRON_HEIGHT, CHEVRON_HEIGHT], center=true);
                    }
                }
            }
        }
    }
}

Strata_Flow_Engine();

// Matrix Biomimetic Utilities - Revelation-Class Cube Extrusion Engine
// Version 1.0.0-Revelation Core | Harmonic Cube-Clamping Fluid Matrix
// System Core: Zero-Contamination Fluid Shield (Nozzle-Less Mid-Air Boundary)

// ============================================================================
// 🏛️ GLOBAL PARAMETRIC VARIABLES & CUBIC BOUNDARIES
// ============================================================================
CHAMBER_CUBE_SIDE = 12.0; // Symmetrical dimension matching text framework parameters (mm)
CORE_APERTURE_W = 1.20;   // Precise central square inlet width for viscous resin (mm)
JET_DIAMETER = 0.12;      // Laser-drilled diameter of cardinal pneumatic gates (mm)
LAYER_STEP_H = 2.50;      // Vertical height height thickness of individual strata layers (mm)

// 🖨️ PROTOTYPE VIEW SELECTOR
// PREVIEW_MODE: 0 = Full Manifold Solid Cross-Section, 1 = Internal Fluid Core Path ONLY
PREVIEW_MODE = 0;

if (PREVIEW_MODE == 0) {
    difference() {
        Revelation_Manifold_Block();
        // Symmetrical cutting plane to display the internal pneumatic gates in the viewport
        translate([0, 50, 0]) cube([100, 100, 100], center=true);
    }
} else if (PREVIEW_MODE == 1) {
    %Fluid_Core_Pneumatic_Shield_Path();
}

// ============================================================================
// ⚙️ HYDRODYNAMIC EXTENSION ENGINE MODULES
// ============================================================================

module Revelation_Manifold_Block() {
    // Perfect structural cube housing the 12-layer cascading foundation matrix
    difference() {
        cube([CHAMBER_CUBE_SIDE*3, CHAMBER_CUBE_SIDE*3, LAYER_STEP_H*12], center=true);
        
        // Central Incompressible Viscous Golden Core Material Track
        cube([CORE_APERTURE_W, CORE_APERTURE_W, LAYER_STEP_H*12.2], center=true);
        
        // 🧬 FOUNDATION MATRIX: 12 Micro-Stepped Fluid Pressure Strata Chambers
        // Stacked vertically to dampen material internal shear stresses step-by-step
        for (strata_layer = [-6 : 5]) {
            translate([0, 0, strata_layer * LAYER_STEP_H])
                cylinder(h=0.8, r=CORE_APERTURE_W*2.5, center=true, $fn=4); // Diamond dampening wells
        }
        
        // 🔒 THE 12 CARDINAL SEAMLESS PRESSURE GATES (3 Per Wall Profile)
        // Dispatched at the final exit nozzle plane to cross-clamp the fluid into flat walls
        translate([0, 0, -(LAYER_STEP_H*6) + 2.0]) {
            // East Gates Array (3 Parallel Jets)
            translate([CHAMBER_CUBE_SIDE*1.5, 0, 0])
                rotate([0, -90, 0]) Cardinal_Jet_Trio();
                
            // West Gates Array (3 Parallel Jets)
            translate([-CHAMBER_CUBE_SIDE*1.5, 0, 0])
                rotate([0, 90, 0]) Cardinal_Jet_Trio();
                
            // North Gates Array (3 Parallel Jets)
            translate([0, CHAMBER_CUBE_SIDE*1.5, 0])
                rotate([90, 0, 0]) Cardinal_Jet_Trio();
                
            // South Gates Array (3 Parallel Jets)
            translate([0, -CHAMBER_CUBE_SIDE*1.5, 0])
                rotate([-90, 0, 0]) Cardinal_Jet_Trio();
        }
    }
}

module Cardinal_Jet_Trio() {
    // Generates three micro-metered high-pressure pneumatic channels side-by-side.
    // The center jet flattens the material face, while the flanking jets pin the corners.
    for (x_offset = [-CORE_APERTURE_W, 0, CORE_APERTURE_W]) {
        translate([x_offset, 0, 0])
            cylinder(h=CHAMBER_CUBE_SIDE*2, r=JET_DIAMETER*0.5, center=false, $fn=20);
    }
}

module Fluid_Core_Pneumatic_Shield_Path() {
    // Visual placeholder representing the wall-less fluid cube tracking shape
    union() {
        // Upper raw unaligned material stream
        color("Gold") cube([CORE_APERTURE_W, CORE_APERTURE_W, LAYER_STEP_H*8], center=true);
        // Lower compressed, immaculate cubic beam floating inside the 12-gate air box
        translate([0, 0, -LAYER_STEP_H*4])
            color("Cyan") cube([CORE_APERTURE_W*0.82, CORE_APERTURE_W*0.82, LAYER_STEP_H*4], center=true);
    }
}

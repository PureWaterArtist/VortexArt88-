// =========================================================================
// PROJECT ARMW-88: MORPHING AERO-RESONATOR WING CORE ENGINE
// Schematics Module: Scale-Invariant Parametric Airfoil Layout v1.0.0
// Licensed under CERN-OHL-S-2.0 (Strongly Reciprocal Open Hardware)
// =========================================================================

$fn = 120; // High-resolution layout factor for cleanroom slicing metrics

// --- PARAMETRIC INPUT ATTRIBUTES (Keyed to hardware-bom.json) ---
max_span = 2400.0;        // Maximum extended wingspan target (mm)
root_chord = 650.0;       // Airfoil root chord length width (mm)
denticle_height = 0.28;   // Height of microscopic shark-denticle vortex traps (mm)
jet_induction_od = 95.0;  // Diameter of cardioid ram-air intakes (mm)
wing_thickness = 42.0;    // Maximum thickness profile of the airfoil ribs (mm)
spar_count = 5;          // Number of internal structural reinforcement spars

module RibSparMatrix() {
    // Internal hollow rib spars that distribute lift forces evenly across torso
    for (i = [0 : 1 : spar_count-1]) {
        translate([i * (root_chord / spar_count) - (root_chord/2), 0, 0])
            difference() {
                resize([root_chord / (spar_count + 1), wing_thickness, 180])
                    cylinder(h=1, r=10, center=true);
                resize([(root_chord / (spar_count + 1)) - 6, wing_thickness - 6, 190])
                    cylinder(h=1, r=10, center=true);
            }
    }
}

module ForearmSliderTracks() {
    // Sliding internal linear rail tracks to dynamically morph aspect ratio
    translate([0, 0, 0])
        rotate([90, 0, 0])
            cylinder(h=root_chord + 20, r=6.0, center=true);
}

module CardioidJetIntakePlenums() {
    // Curved ram-air induction intake passages that route into micro-Venturis
    translate([-120, -(root_chord/2) + 20, 0])
        rotate([0, 90, 0])
            difference() {
                cylinder(h=150, r=jet_induction_od/2, center=true);
                cylinder(h=160, r=(jet_induction_od/2) - 4.0, center=true);
            }
}

module MetamaterialDenticleSkin() {
    // Microscopic surface-bound asymmetric air scoops to trap micro-vortices
    for (x = [-root_chord/2 : 15 : root_chord/2]) {
        for (z = [-80 : 20 : 80]) {
            translate([x, (wing_thickness/2) - 0.5, z])
                rotate([0, 0, -15])
                    scale([2, 1, 1])
                        cylinder(h=denticle_height, r1=0.8, r2=0.1, center=true);
        }
    }
}

// --- MASTER AIRFOIL ASSEMBLY HOUSING ---
difference() {
    // Primary Solid Wing Airfoil Profile Base Block
    resize([root_chord, wing_thickness, 220])
        cylinder(h=1, r=10, center=true);
        
    // Core Mechanical Function Excavations
    ForearmSliderTracks();
    CardioidJetIntakePlenums();
}

// Materialize Internal Lightweight Rib Spar Framework
intersection() {
    resize([root_chord - 8, wing_thickness - 6, 218])
        cylinder(h=1, r=10, center=true);
    RibSparMatrix();
}

// Apply Metamaterial Boundary-Layer Control Skin to Leading Edge Area
intersection() {
    resize([root_chord, wing_thickness + 2, 222])
        cylinder(h=1, r=10, center=true);
    MetamaterialDenticleSkin();
}

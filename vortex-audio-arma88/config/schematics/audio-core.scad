// =========================================================================
// PROJECT ARMA-88: BIOMIMETIC IN-EAR ACOUSTIC RESONATOR CHASSIS
// Schematics Module: Scale-Invariant Parametric Solid Engine v1.0.0
// Licensed under CERN-OHL-S-2.0 (Strongly Reciprocal Open Hardware)
// =========================================================================

$fn = 120; // High-resolution layout factor for cleanroom slicing metrics

// --- PARAMETRIC INPUT ATTRIBUTES (Keyed to hardware-bom.json) ---
plenum_aperture = 6.5;     // Cardioid plenum main audio intake diameter (mm)
compression_ratio = 4.8;   // Logarithmic acoustic compression factor
venturi_pinch = 0.45;     // Internal width of sub-millimeter acoustic tracks (mm)
stf_valve_diam = 1.1;     // Diameter of Non-Newtonian fluid bypass loops (mm)
chassis_length = 22.0;     // Total front-to-back depth to fit securely in canal (mm)
chassis_radius = 7.5;      // Outermost radius of the flexible interface shell (mm)

module LogarithmicAcousticWaveguides() {
    // Spiral micro-channels that compress passing sound waves via centripetal acceleration
    render() {
        linear_extrude(height=chassis_length - 4, twist=compression_ratio * 45, center=true) {
            rotate_extrude(angle=90) {
                translate([plenum_aperture/2, 0, 0])
                    square([venturi_pinch, plenum_aperture/3], center=true);
            }
        }
    }
}

module NonNewtonianBypassValves() {
    // Micro-fluidic safety channels running parallel to the primary sound passage
    translate([chassis_radius - 2.0, 0, 0])
        cylinder(h=chassis_length + 2, r=stf_valve_diam/2, center=true);
    translate([-(chassis_radius - 2.0), 0, 0])
        cylinder(h=chassis_length + 2, r=stf_valve_diam/2, center=true);
}

module PiezoMeshSeatingSlots() {
    // Thin outer perimeter slots to guide and secure the 0.12mm PVDF strain mesh
    difference() {
        cylinder(h=chassis_length - 6, r=chassis_radius - 0.2, center=true);
        cylinder(h=chassis_length, r=chassis_radius - 0.8, center=true);
    }
}

module MainAcousticPlenumIntake() {
    // Funnel entry cone matching the outer ear canal transition zone
    translate([0, 0, (chassis_length/2) - 2])
        cylinder(h=4.1, r1=chassis_radius, r2=plenum_aperture/2, center=true);
}

// --- MASTER IN-EAR ASSEMBLY INTEGRATION ---
difference() {
    // Primary Outer Interface Solid Shell ( TPU / Silicone Boundary )
    cylinder(h=chassis_length, r=chassis_radius, center=true);
    
    // Internal Core Audio Components Excavation
    cylinder(h=chassis_length + 2, r=plenum_aperture/2, center=true);
    
    // Dynamic Functional Elements Cuts
    NonNewtonianBypassValves();
    
    // Front Side Exhaust Output toward Tympanic Membrane
    translate([0, 0, -(chassis_length/2) + 2])
        cylinder(h=4.1, r1=2.5, r2=chassis_radius - 1.5, center=true);
}

// Materialize Internal Logarithmic Spiral Core Structure
difference() {
    translate()
        cylinder(h=chassis_length - 4, r=plenum_aperture/2 + 0.5, center=true);
    LogarithmicAcousticWaveguides();
}

// Embed Outer Structural Guide Rings for the Kinetic Siphon Mesh
difference() {
    translate()
        cylinder(h=chassis_length - 6, r=chassis_radius, center=true);
    PiezoMeshSeatingSlots();
    NonNewtonianBypassValves();
}

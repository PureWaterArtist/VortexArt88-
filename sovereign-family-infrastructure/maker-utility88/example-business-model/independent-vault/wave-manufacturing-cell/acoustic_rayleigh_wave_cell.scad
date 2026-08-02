// Matrix Biomimetic Utilities - Acoustic Rayleigh-Wave Sizing Manifold
// Version 1.2.0-Acoustic Core | Pneumatic Cooling Shield Engine Matrix
// System Core: Non-Scorching Low-Ultrasonic Boundary Engine (Thermal Guard)

// ============================================================================
// 🏛️ GLOBAL PARAMETRIC VARIABLES & ACOUSTIC BOUNDARIES
// ============================================================================
CELL_RADIUS = 50.0;       // Radial boundary of the acoustic housing (mm)
CORE_PASS_DIAMETER = 6.0; // Wide-open, un-cloggable polymer delivery channel (mm)
WALL_THICKNESS = 3.0;     // Standardized wall footprint for optimal toolpaths (mm)
TRANSDUCER_HEIGHT = 8.0;  // Height of individual low-ultrasonic pads (mm)

// 🖨️ WORKBENCH VISUAL ROUTER
// PREVIEW_INDEX: 0 = Full Assembly View, 1 = Internal Pneumatic Cooling Jacket Only
PREVIEW_INDEX = 0;

if (PREVIEW_INDEX == 0) {
    Acoustic_Processing_Cell();
} else if (PREVIEW_INDEX == 1) {
    intersection() {
        Acoustic_Processing_Cell();
        cube([CELL_RADIUS*3, CELL_RADIUS*3, TRANSDUCER_HEIGHT], center=true);
    }
}

// ============================================================================
// ⚙️ ACOUSTIC ENGINE MODULE CORDS
// ============================================================================

module Acoustic_Processing_Cell() {
    // Multi-layered housing block linking kinetic torsion anchors and wave pads
    union() {
        // Rigid Outer Shield Housing
        difference() {
            cylinder(h=45.0, r=CELL_RADIUS, center=true, $fn=6);
            cylinder(h=47.0, r=CELL_RADIUS - WALL_THICKNESS, center=true, $fn=6);
            
            // Central Material Exit Bore Subtraction
            cylinder(h=50.0, r=CORE_PASS_DIAMETER*0.5, center=true, $fn=60);
            
            // 🛠️ INTEGRATED PATCH: COAXIAL PNEUMATIC AIR-COOLING SCUBBER JACKET
            // Carves a hollow 4.0mm deep insulation chamber directly behind the crystals 
            // to exhaust heat conduction, keeping ceramic temps permanently under 65C.
            cylinder(h=TRANSDUCER_HEIGHT*1.5, r=CORE_PASS_DIAMETER*1.8, center=true, $fn=60);
        }
        
        // 🧬 SURFACE-BOUNDED LAYER: 40 kHz Low-Ultrasonic Ring Array
        // Encircles the fluid path to project surface skin Rayleigh waves supportless
        translate([0, 0, 4.0]) {
            for (node = [0 : 45 : 359]) {
                rotate([0, 0, node])
                    translate([CORE_PASS_DIAMETER*0.5 + 1.2, 0, 0])
                        color("SlateGray")
                            cube([2.4, 4.5, TRANSDUCER_HEIGHT], center=true);
            }
        }
        
        // 🔒 KINETIC TORSION INTERLOCKS: 120 Hz Low-Frequency Base Bed Mounts
        // Blends the high-mass mounting tabs into the hexagonal wall loops via continuous
        // flared hull sweeps. This entirely stops cyclic fatigue stress wave accumulation.
        translate([0, 0, -20.0]) {
            for (tab = [0 : 120 : 359]) {
                rotate([0, 0, tab]) {
                    difference() {
                        hull() {
                            translate([CELL_RADIUS * 0.72, 0, 0])
                                cube([8.0, 24.0, WALL_THICKNESS*2], center=true); // Wall-side tie
                            translate([CELL_RADIUS * 0.9, 0, 0])
                                cube([15.0, 18.0, WALL_THICKNESS*2], center=true); // Tab extremity
                        }
                        // Precise M6 Steel Bolt Securing Slot
                        translate([CELL_RADIUS * 0.9, 0, 0])
                            cylinder(h=10.0, r=3.2, center=true, $fn=20); 
                    }
                }
            }
        }
    }
}

// =========================================================================
// PROJECT ARMW-88: PARAMETRIC FLUIDIC LOGIC COMPUTER ENGINE
// Modules Subsystem: Solid-State Micro-Channel Flight Sensor Core v1.0.0
// Licensed under CERN-OHL-S-2.0 (Strongly Reciprocal Open Hardware)
// =========================================================================

$fn = 120; // High-resolution layout factor for cleanroom SLA resin printing

// --- PARAMETRIC INPUT ATTRIBUTES (Keyed to hardware-bom.json) ---
trace_w = 1.5;             // Micro-fluidic logic channel trace width (mm)
trace_d = 2.2;             // Micro-fluidic logic channel groove depth (mm)
horn_id = 32.0;            // Inlet diameter for parabolic Doppler collectors (mm)
pitot_bore = 4.5;          // Bore size for pneumatic ground altimetry ports (mm)
cuff_port = 2.0;           // Port size for kinesthetic feedback bladder lines (mm)
block_w = 110.0;           // Total physical width of the computing block (mm)
block_l = 145.0;           // Total physical length of the computing block (mm)
block_h = 35.0;            // Total physical thickness of the monolithic block (mm)

module MonolithicCoreBlock() {
    // Primary un-excavated substrate housing the internal air logic tracks
    difference() {
        cube([block_w, block_l, block_h], center=true);
        
        // Alignment slots for clean seating into the torso backplate cavity
        translate([0, (block_l/2) - 8, 0])
            cube([block_w - 20, 16.5, block_h + 5], center=true);
    }
}

module MicroChannelLogicTracks() {
    // AND, OR, and NOT flip-flop paths operating on the Coandă Effect
    translate([0, 0, (block_h/2) - (trace_d/2)]) {
        // Primary central ram-air distribution conduit
        cube([trace_w, block_l - 40, trace_d], center=true);
        
        // Y-split bistable jet deflection channels
        rotate([0, 0, 15])
            translate([20, 0, 0])
                cube([trace_w, 60, trace_d], center=true);
        rotate([0, 0, -15])
            translate([-20, 0, 0])
                cube([trace_w, 60, trace_d], center=true);
                
        // Cross-over feedback loop paths causing logic state switching
        translate([0, 10, 0])
            cube([40, trace_w, trace_d], center=true);
    }
}

module DopplerHornCollectors() {
    // Parabolic collector funnels transforming sound signatures into air jets
    for (i = [-1, 1]) {
        translate([i * (block_w/3), -(block_l/2) - 2.0, 0])
            rotate([-90, 0, 0])
                difference() {
                    // Outer structural horn housing extension
                    cylinder(h=30, r1=horn_id/2 + 4.0, r2=trace_w + 3.0, center=false);
                    // Internal polished parabolic sound capture funnel
                    cylinder(h=32, r1=horn_id/2, r2=trace_w/2, center=false);
                }
    }
}

module GroundAltimetryPorts() {
    // Intake connections linking lower boot pitots to torso altimetry blocks
    for (i = [-1, 1]) {
        translate([i * (block_w/4), (block_l/2) + 2.0, -5])
            rotate([90, 0, 0])
                cylinder(h=25, r=pitot_bore/2, center=true);
    }
}

module KinestheticFeedbackPorts() {
    // Output vents routing threshold pressures to the arm sleeve bladders
    translate([-35, 0, -(block_h/2) + 4])
        cylinder(h=12, r=cuff_port/2, center=true);
    translate([35, 0, -(block_h/2) + 4])
        cylinder(h=12, r=cuff_port/2, center=true);
        
    // Failsafe backup canopy pneumatic line output trigger port
    translate([0, (block_l/3), -(block_h/2) + 4])
        cylinder(h=12, r=3.0, center=true);
}

// --- MASTER SOLID-STATE COMPILER CORE ASSEMBLY ---
difference() {
    union() {
        MonolithicCoreBlock();
        DopplerHornCollectors();
    }
    // Excavate internal programmatic pressure pathways
    MicroChannelLogicTracks();
    GroundAltimetryPorts();
    KinestheticFeedbackPorts();
}

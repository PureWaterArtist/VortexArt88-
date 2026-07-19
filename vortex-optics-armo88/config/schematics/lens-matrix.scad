// =========================================================================
// PROJECT ARMO-88: BIOMIMICRY OPTOELECTRONIC LENS MATRIX CHASSIS
// Schematics Module: Scale-Invariant Parametric Solid Engine v1.0.0
// Licensed under CERN-OHL-S-2.0 (Strongly Reciprocal Open Hardware)
// =========================================================================

$fn = 120; // High-resolution layout factor for cleanroom slicing metrics

// --- PARAMETRIC INPUT ATTRIBUTES (Keyed to hardware-bom.json) ---
lens_diameter = 52.0;       // Diameter of the dielectric metalens matrix (mm)
substrate_thick = 2.5;     // Thickness of the optics layer sandwich (mm)
capillary_width = 1.2;     // Width of the micro-fluidic focus loop channel (mm)
bridge_width = 18.0;       // Center nose bridge gap distance (mm)
frame_thickness = 6.0;     // Total front-to-back depth of the chassis frame (mm)
wall_thickness = 3.5;      // Protective structural containment loop width (mm)

module EyeWireRetentionWell() {
    // Primary circular cavity holding the multi-layer optics assembly
    cylinder(h=frame_thickness + 2, r=lens_diameter/2, center=true);
    
    // Step flange shelf to firmly seat the substrate plates
    translate([0, 0, -(frame_thickness/2) + (substrate_thick/2)])
        cylinder(h=substrate_thick + 0.1, r=(lens_diameter/2) - 1.5, center=true);
}

module MicroFluidicCapillaryChannel() {
    // Concentric capillary loop surrounding the lens for liquid gallium alloy routing
    difference() {
        cylinder(h=frame_thickness - 2, r=(lens_diameter/2) + capillary_width + 1.0, center=true);
        cylinder(h=frame_thickness, r=(lens_diameter/2) + 1.0, center=true);
    }
}

module PneumaticTriggerPorts() {
    // Horizontal guide ports entering from temple arms for focus compression lines
    translate([0, (lens_diameter/2) + wall_thickness, 0])
        rotate([0, 90, 0])
            cylinder(h=40, r=1.0, center=true);
}

module MainChassisSolid() {
    // Core structural mass block forming the front spectacles assembly
    hull() {
        // Left Eye Frame Section
        translate([-((lens_diameter/2) + (bridge_width/2)), 0, 0])
            cylinder(h=frame_thickness, r=(lens_diameter/2) + wall_thickness, center=true);
        
        // Right Eye Frame Section
        translate([((lens_diameter/2) + (bridge_width/2)), 0, 0])
            cylinder(h=frame_thickness, r=(lens_diameter/2) + wall_thickness, center=true);
    }
}

// --- MASTER CHASSIS COMPILATION ---
difference() {
    MainChassisSolid();
    
    // Left Eye Internal Cuts
    translate([-((lens_diameter/2) + (bridge_width/2)), 0, 0]) {
        EyeWireRetentionWell();
        MicroFluidicCapillaryChannel();
        PneumaticTriggerPorts();
    }
    
    // Right Eye Internal Cuts
    translate([((lens_diameter/2) + (bridge_width/2)), 0, 0]) {
        EyeWireRetentionWell();
        MicroFluidicCapillaryChannel();
        rotate([0, 0, 180]) PneumaticTriggerPorts(); // Mirror port entry for right side
    }
    
    // Center Ergonomic Nose Bridge Arch Relief
    translate([0, -((lens_diameter/2) + wall_thickness - 4), 0])
        cylinder(h=frame_thickness + 5, r=12.0, center=true);
}

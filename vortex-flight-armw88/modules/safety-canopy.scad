// =========================================================================
// PROJECT ARMW-88: PASSIVE BALLISTIC CANOPY SAFETY SUBSYSTEM
// Modules Subsystem: Fluidic-Triggered Ram-Air Deployment Chamber v1.0.0
// Licensed under CERN-OHL-S-2.0 (Strongly Reciprocal Open Hardware)
// =========================================================================

$fn = 120; // High-resolution definition for pressure containment walls

// --- PARAMETRIC INPUT ATTRIBUTES (Keyed to hardware-bom.json) ---
canopy_bore_diameter = 135.0;  // Internal diameter for tightly packed Kevlar canvas (mm)
pneumatic_valve_bore = 22.0;   // Bore diameter for the passive air release piston (mm)
canopy_housing_length = 290.0; // Total length of the ballistic spine cylinder (mm)
pressure_inlet_width = 1.5;   // Trace width of tracking fluidic logic nozzle ports (mm)
housing_wall_thickness = 5.5; // Structural wall thickness to handle deployment forces (mm)

module BallisticCanopyCanister() {
    // Main structural storage vault holding the emergency canopy array
    difference() {
        cylinder(h=canopy_housing_length, r=(canopy_bore_diameter/2) + housing_wall_thickness, center=true);
        cylinder(h=canopy_housing_length - 12, r=canopy_bore_diameter/2, center=true);
        
        // Front exit fracture window for ballistic deployment escape
        translate([0, 0, (canopy_housing_length/2) - 4])
            cylinder(h=10, r=(canopy_bore_diameter/2) - 4, center=true);
    }
}

module FluidicPneumaticTriggerValve() {
    // High-pressure mechanical piston sleeve that opens via fluidic computer lines
    translate([0, (canopy_bore_diameter/2) + housing_wall_thickness, -40])
        rotate([90, 0, 0])
            difference() {
                cylinder(h=45, r=pneumatic_valve_bore/2 + 5.0, center=true);
                cylinder(h=55, r=pneumatic_valve_bore/2, center=true);
                
                // Sub-millimeter tracking port inlets feeding from logic tracks
                translate([0, 0, 10])
                    rotate([0, 90, 0])
                        cylinder(h=40, r=pressure_inlet_width/2, center=true);
            }
}

module RamAirEjectionPassages() {
    // Dynamic air tubes that fill with ambient ram-pressure to launch the canopy
    translate([0, 0, -(canopy_housing_length/2) + 6])
        for (i = [0 : 90 : 270]) {
            rotate([0, 0, i])
                translate([canopy_bore_diameter/3, 0, 0])
                    cylinder(h=20, r=8.0, center=true);
        }
}

// --- MASTER EMERGENCY CANOPY DEPLOYMENT MATRIX ---
difference() {
    union() {
        BallisticCanopyCanister();
        FluidicPneumaticTriggerValve();
    }
    // Bore out base internal ram-air channels to complete pressure links
    RamAirEjectionPassages();
}

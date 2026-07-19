// =========================================================================
// PROJECT AWHC-88: ATMOSPHERIC WATER HARVESTER CONDENSER CORE
// Schematics Module: Scale-Invariant Parametric Fluid Engine v1.0.0
// Licensed under CERN-OHL-S-2.0 (Strongly Reciprocal Open Hardware)
// =========================================================================

$fn = 120; // High-resolution layout factor for cleanroom slicing metrics

// --- PARAMETRIC INPUT ATTRIBUTES (Keyed to hardware-bom.json) ---
plenum_od = 120.0;       // Outermost diameter of the cardioid suction intake (mm)
pitch_angle = 38.2;      // Parametric cardioid spiral pitch angle (deg)
venturi_throat = 3.5;    // Internal width of the micro-Venturi compression slots (mm)
core_radius = 45.0;      // Radius of the main condensation matrix cylinder (mm)
drain_bore = 15.0;       // Inner diameter of the bottom collection manifold port (mm)
housing_height = 90.0;   // Total vertical volume block height (mm)
wall_thickness = 5.0;   // Minimum structural wall thickness for pressure differential

module CardioidPlenumIntake() {
    // Outer vortex induction shell guide
    difference() {
        cylinder(h=housing_height/3, r1=plenum_od/2, r2=core_radius+wall_thickness, center=true);
        // Parametric spiral sweep cutout core using twisted pitch parameters
        linear_extrude(height=housing_height/3 + 2, twist=-pitch_angle, center=true)
            circle(r=plenum_od/2 - wall_thickness);
    }
}

module InternalVenturiCores() {
    // Generates an array of high-velocity pinching slots around the inner radius
    for (i = [0 : 45 : 360]) {
        rotate([0, 0, i])
            translate([core_radius - (venturi_throat/2), 0, 0])
                cube([venturi_throat, core_radius/2, housing_height + 10], center=true);
    }
}

module CondenserMeshGuides() {
    // Slotted guide rails to firmly seat pure oxygen-free copper mesh screens
    for (i = [22.5 : 45 : 360]) {
        rotate([0, 0, i])
            translate([core_radius - 10, 0, 0])
                cube([15.0, 2.0, housing_height - 10], center=true);
    }
}

module MainDrainageManifold() {
    // Central condensation collection basin and base exit passage
    translate([0, 0, -housing_height/2])
        cylinder(h=30, r=drain_bore/2, center=true);
}

// --- MASTER HOUSING INTEGRATION ---
difference() {
    // Main Solid Protection Block Outer Shell
    cylinder(h=housing_height, r=core_radius + wall_thickness, center=true);
    
    // Internal Core Condensation Chamber Hollow
    cylinder(h=housing_height - 10, r=core_radius, center=true);
    
    // Core Manifold Intersections
    InternalVenturiCores();
    MainDrainageManifold();
}

// Attach the upper Cardioid Plenum Induction Unit to the housing matrix top flange
translate([0, 0, (housing_height/2) + (housing_height/6)])
    CardioidPlenumIntake();
    
// Materialize internal mechanical guide mounts inside the core block
difference() {
    translate([0, 0, 0])
        cylinder(h=housing_height - 15, r=core_radius, center=true);
    cylinder(h=housing_height - 10, r=core_radius - 2.5, center=true);
    CondenserMeshGuides();
    InternalVenturiCores();
}

// =========================================================================
// PROJECT LCN-88: MANIFOLD CASCADE COUPLER (MODULES SUBSYSTEM)
// Component Module: Vertical Chaining Flange v1.0.0
// Licensed under CERN-OHL-S-2.0 (Strongly Reciprocal Open Hardware)
// =========================================================================

$fn = 120; // High-resolution layout factor for cleanroom workflows

port_diameter = 12.0;    // Matches the induction/drainage bore of LCN-88 core
wall_thickness = 4.0;    // High-pressure containment thickness
coupling_length = 30.0;  // Total spacing gap between chained nodes

difference() {
    // External solid coupling cylinder
    cylinder(h=coupling_length, r=(port_diameter/2) + wall_thickness, center=true);
    
    // Internal fluid path conduit passage
    cylinder(h=coupling_length + 2, r=port_diameter/2, center=true);
    
    // Dual O-Ring retention channels for watertight face seals
    translate([0, 0, (coupling_length/2) - 4])
        torus_cut(r_major=(port_diameter/2)+1.5, r_minor=1.2);
    translate([0, 0, -(coupling_length/2) + 4])
        torus_cut(r_major=(port_diameter/2)+1.5, r_minor=1.2);
}

module torus_cut(r_major, r_minor) {
    rotate_extrude() translate([r_major, 0, 0]) circle(r=r_minor);
}

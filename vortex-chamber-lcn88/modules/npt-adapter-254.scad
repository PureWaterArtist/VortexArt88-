// =========================================================================
// PROJECT LCN-88: COMMERCIAL NPT PIPE INTERFACE ADAPTER
// Component Module: 25.4mm Slip to 1" NPT Thread Sleeve v1.0.0
// Licensed under CERN-OHL-S-2.0 (Strongly Reciprocal Open Hardware)
// =========================================================================

$fn = 120; // High-resolution layout factor for cleanroom workflows

sleeve_id = 25.76;         // Inside diameter to slip tightly over LCN-88 nozzles
adapter_length = 35.0;     // Mechanical engagement length
npt_outer_diameter = 33.4; // Approximated major diameter for 1" pipe fittings

difference() {
    // Outer tapered protective adapter casing
    cylinder(h=adapter_length, r1=npt_outer_diameter/2 + 3, r2=sleeve_id/2 + 4, center=true);
    
    // Smooth lower half receiver pocket for LCN-88 nozzle attachment
    translate([0, 0, -adapter_length/4])
        cylinder(h=adapter_length/2 + 0.1, r=sleeve_id/2, center=true);
        
    // Upper core fluid flow conduit passage
    cylinder(h=adapter_length + 2, r=20.0/2, center=true);
}

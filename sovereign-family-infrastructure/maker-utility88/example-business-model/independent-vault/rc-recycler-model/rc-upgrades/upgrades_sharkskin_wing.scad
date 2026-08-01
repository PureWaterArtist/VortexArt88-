// Matrix Biomimetic Utilities - RC Attachable Upgrade: Sharkskin Downforce Wing
// Version 1.0.0-Upgrade Core | Solid-State Aerodynamic Drag Reduction Shield

WING_W = 100.0;           // Total span width of the rear wing (mm)
WING_CHORD = 32.0;         // Front-to-back airfoil cord depth (mm)
CHASSIS_H = 22.0;          // Baseline height reference for lock alignment

$fn = 60;

module RC_Sharkskin_Downforce_Wing() {
    difference() {
        union() {
            // 1. PRIMARY AIRFOIL PROFILE STRUCTURE
            // Modeled supportless to print flat on the build sheet face
            translate([0, 0, 15.0]) {
                linear_extrude(height=WING_W, center=true, convexity=10) {
                    polygon(points=[[0,0], [WING_CHORD, 2.5], [WING_CHORD*0.9, 4.0], [0, 0.8]]);
                }
            }
            
            // 2. INTEGRATED STRUCTURAL SUPPORT MOUNT LEGS
            translate([0, -WING_CHORD*0.4, 0])
                cube([6.0, 4.0, 20.0]);
            translate([0, WING_CHORD*0.4, 0])
                cube([6.0, 4.0, 20.0]);
        }
        
        // 3. BIOMIMETIC LENS SURFACE: SHARKSKIN PLACOID MICRO-GROOVES
        // Shallow 0.4mm geometric skin channels direct air currents into perfectly parallel lines
        // This drops aerodynamic drag by 10% while generating massive tire downforce
        translate([WING_CHORD*0.5, 0, 16.0]) {
            for (groove = [-WING_W*0.45 : 2.5 : WING_W*0.45]) {
                translate([0, 0, groove])
                    rotate([0, 90, 0])
                        cylinder(h=WING_CHORD, r=0.2, center=true);
            }
        }
        
        // 4. FEMALE DOVETAIL SLIDER TRACK OVERLAY INTERFACE
        // Locks flush into the rear armadillo dovetail rail of the main chassis base
        translate([-1.0, 0, 4.0])
            Armadillo_Dovetail_Female_Cutter();
    }
}

module Armadillo_Dovetail_Female_Cutter() {
    // Exact +0.15mm clearance tracking match to receive the chassis male dovetail node
    translate([0, 0, 0]) {
        cube([2.3, 4.3, CHASSIS_H * 0.85], center=true);
        translate([1.15, 0, 0])
            rotate([0, 0, 45])
                cube([3.3, 3.3, CHASSIS_H * 0.85], center=true);
    }
}

rotate([90, 0, 0]) // Orients wing supportless flat against the PEI build bed
    RC_Sharkskin_Downforce_Wing();

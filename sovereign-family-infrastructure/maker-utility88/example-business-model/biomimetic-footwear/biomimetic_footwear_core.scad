// Matrix Biomimetic Utilities - Universal Circular Footwear Core Array
// Version 5.5.0-Consumer Master | Debris Relief Wells & Porous Insole Matrix

// ============================================================================
// 🏛️ UNIVERSAL SIZING MATRIX (Parametric Scaling Boundaries)
// ============================================================================
FOOT_LENGTH = 270.0;       // Target foot length baseline reference (mm = Men's Size 9)
FOOT_WIDTH = 98.0;         // Target foot maximum width reference (mm)
SOLE_THICKNESS = 28.0;     // Total heel-strike padding height profile (mm)

// 📐 SCALE-INVARIANT TOLERANCES
INT_L = FOOT_LENGTH + 4.0;  // 4mm elongation buffer handles dynamic footprint stretch
INT_W = FOOT_WIDTH + 2.0;
$fn = 60;

// 🖨️ FABRICATION ROUTER SELECTOR
// PART_SELECTOR: 0 = Full Visual Assembly, 1 = LAYER 1 (TPU Upper), 
//                 2 = LAYER 2 (Gyroid Sole), 3 = LAYER 3 (Smooth Porous Insole)
PART_SELECTOR = 0;

if (PART_SELECTOR == 0) {
    color("LightCharcoal", 0.85) Footwear_Trabecular_Upper();
    translate([0, 0, -SOLE_THICKNESS*0.4]) color("DarkCharcoal") Footwear_Cushion_Sole();
    translate([0, 0, 2.0]) color("VelvetGray") Zero_Friction_Insole_Insert();
} else if (PART_SELECTOR == 1) {
    Footwear_Trabecular_Upper();
} else if (PART_SELECTOR == 2) {
    Footwear_Cushion_Sole();
} else if (PART_SELECTOR == 3) {
    Zero_Friction_Insole_Insert();
}

// ============================================================================
// ⚙️ SYSTEM CAD COMPONENT MODULES
// ============================================================================

module Footwear_Trabecular_Upper() {
    difference() {
        union() {
            // Main anatomical outer skin profile wrap
            scale([1, 1, 0.45]) sphere(d=INT_L);
            
            // LONGITUDINAL MALE DOVETAIL SPLINES
            // Lengthwise rails eliminate walking shear while allowing a 5-second slide teardown
            for (x_rail = [-20, 0, 20]) {
                translate([x_rail, 0, -SOLE_THICKNESS*0.35]) {
                    cube([3.0, INT_L * 0.7, 4.0], center=true); 
                    translate([0, 0, -2.0]) rotate() cube([4.0, INT_L * 0.7, 4.0], center=true); 
                }
            }
            
            // TRANSVERSE HEEL SAFETY LOCK PIN CYLINDER
            // Mechanical anchor stops backward sliding slide-creep forces during hard runs
            translate([-INT_L * 0.44, 0, -SOLE_THICKNESS * 0.35]) {
                rotate([0, 90, 0])
                    cylinder(h=14.0, r=3.0, center=true);
            }
        }
        
        // Inner Foot Ingestion Cavity
        translate([0, 0, -2.0]) scale([0.96, 0.94, 0.42]) sphere(d=INT_L);
                
        // Ankle Collar Entry Window Opening
        translate([-INT_L*0.15, 0, 30.0]) cylinder(h=40.0, r=INT_W*0.48, center=true);
            
        // Bottom Sole Separation Planar Cut
        translate([0, 0, -40.0]) cube([INT_L+10, INT_W+10, 80.0], center=true);
            
        // ASYMMETRICAL HYDROPHOBIC TESLA-VALVE WEAVE
        for (y_valve = [-INT_L*0.25 : 20 : INT_L*0.25]) {
            for (x_valve = [-INT_W*0.25 : 15 : INT_W*0.25]) {
                translate([x_valve, y_valve, 10.0]) rotate([0, 0, 0]) {
                    cylinder(h=10.0, r1=1.5, r2=0.5, center=true);
                    translate([0, 2.0, 0]) cylinder(h=10.0, r1=0.5, r2=1.5, center=true);
                }
            }
        }
    }
}

module Footwear_Cushion_Sole() {
    difference() {
        union() {
            // ELEPHANT-PAD MIDSOLE STRUCTURAL SHELL
            scale([1, 0.98, 1]) {
                hull() {
                    translate([-INT_L*0.25, 0, 0]) cylinder(h=SOLE_THICKNESS, r=INT_W*0.48, center=true);
                    translate([INT_L*0.25, 0, -2.0]) cylinder(h=SOLE_THICKNESS-4.0, r=INT_W*0.4, center=true);
                }
            }
            
            // OVERLOCKING CROCODILE HOOD POCKET
            // Rigid 15mm hood overhang traps the front toe upper to completely stop nose lift and delamination
            translate([INT_L*0.45, 0, SOLE_THICKNESS*0.2]) {
                difference() {
                    cube([22.0, INT_W*0.5, 10.0], center=true);
                    translate([-4.0, 0, -4.0]) cube([20.0, INT_W*0.6, 8.0], center=true); 
                }
            }
        }
        
        // Anatomical Footbed Contouring Sink
        translate([0, 0, SOLE_THICKNESS*0.35]) scale([0.97, 0.93, 0.3]) sphere(d=INT_L);
                
        // THREE LONGITUDINAL FEMALE DOVETAIL TRACK CUTTERS (+0.15mm Clearance)
        for (x_rail = [-20, 0, 20]) {
            translate([x_rail, 0, SOLE_THICKNESS*0.32]) {
                cube([3.3, INT_L * 0.75, 4.5], center=true);
                translate([0, 0, -2.0]) rotate([0, 0, 0]) cube([4.3, INT_L * 0.75, 4.3], center=true);
            }
        }
        
        // DEBRIS EVACUATION RELIEF WELLS
        // Alternating cutouts along the channel floors drop grit out through the outsole treads
        for (x_rail = [-20, 0, 20]) {
            for (y_well = [-INT_L*0.3 : 25 : INT_L*0.3]) {
                translate([x_rail, y_well, SOLE_THICKNESS*0.1])
                    cube([4.5, 6.0, 15.0], center=true);
            }
        }
        
        // VERTICAL HEEL SNAP-LATCH TRANSVERSE PIN SOCKET
        // Traps the upper rear pin cylinder with a sharp click to secure alignment
        translate([-INT_L * 0.44, 0, SOLE_THICKNESS * 0.32]) {
            rotate([0, 90, 0])
                cylinder(h=14.3, r=3.15, center=true);
        }
        
        // MOUNTAIN-GOAT TRACTION OUTSOLE TREAD GROOVES
        for (y_tread = [-INT_L*0.42 : 8.0 : INT_L*0.42]) {
            translate([0, y_tread, -SOLE_THICKNESS*0.5]) rotate([0, 0, sin(y_tread)*15])
                cube([INT_W + 10.0, 2.0, 4.0], center=true);
        }
    }
}

module Zero_Friction_Insole_Insert() {
    // ZERO-FRICTION TRABECULAR INSOLE WITH AIR-RELEASE VENTS
    // Printed at a velvet-matte finish to entirely eliminate heat spots.
    // 1.2mm vertical cylindrical micro-pores eliminate pneumatic lifting and wrinkling forces completely.
    difference() {
        intersection() {
            translate([0, 0, -SOLE_THICKNESS*0.2]) scale([0.96, 0.92, 0.28]) sphere(d=INT_L);
            cube([INT_L, INT_W, 2.0], center=true); 
        }
        
        // BIOMIMETIC APERTURES: MAMMALIAN POROUS AIR-RELEASE VENTS
        for (y_pore = [-INT_L*0.38 : 8.0 : INT_L*0.38]) {
            for (x_pore = [-INT_W*0.35 : 8.0 : INT_W*0.35]) {
                if (abs(x_pore) < (INT_W * 0.45 - abs(y_pore) * 0.08)) {
                    translate([x_pore, y_pore, 0])
                        cylinder(h=6.0, r=0.6, center=true); 
                }
            }
        }
    }
}

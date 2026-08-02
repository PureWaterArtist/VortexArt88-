// Matrix Biomimetic Utilities - Resonant-Class Biomimetic Hard Hat
// Version 1.3.0-Helmet Core | Swept-Fillet Helicoid Mantis & Lotus Matrix
// System Core: Continuous Filleted Micro-Papillae + Sinusoidal Ridgeways

// ============================================================================
// 🏛️ GLOBAL PARAMETRIC VARIABLES & HELMET GEOMETRIES
// ============================================================================
HELMET_DIAMETER = 220.0;  // Total ear-to-ear internal diameter of the dome (mm)
TOTAL_DEPTH = 140.0;      // Vertical clearance height from rim to crown (mm)
SHELL_THICKNESS = 3.00;   // Weather-proof outer ASA structural wall (mm)
WEB_DEPTH = 6.00;         // Thick high-rebound internal auxetic crumple web (mm)

// 📐 PARAMENTRIC AUXETIC SHOCK MATRIX CONSTANTS
AUX_H = 6.0;              
AUX_W = 4.5;              
AUX_L = 8.0;              

// 📐 BIOMIMETIC TEXTURE SPECS
PAPILLAE_SIZE = 0.60;    // Footprint size of individual superhydrophobic lotus cones (mm)

// 🧲 STAGING METRICS (Sized for Standard 8mm x 2mm Discs)
MAG_DIAMETER = 8.0;
MAG_THICKNESS = 2.0;
FIT_TOLERANCE = 0.20;

Full_Biomimetic_Hard_Hat();

// ============================================================================
// ⚙️ BIOMIMETIC HARDWARE ENGINES & STRUCTURAL MODULES
// ============================================================================

module Full_Biomimetic_Hard_Hat() {
    union() {
        // LAYER 1: MANTIS HELICOID SHIELD & SUPERHYDROPHOBIC LOTUS SKIN
        // Printed in weather-proof matte ASA filament
        color([0.2, 0.2, 0.2]) {
            difference() {
                // Main Protective Dome Shell
                sphere(d=HELMET_DIAMETER + SHELL_THICKNESS*2, $fn=100);
                sphere(d=HELMET_DIAMETER, $fn=100);
                
                // Lower Neck Clearance Cutout Subtraction
                translate([0, 0, -TOTAL_DEPTH*0.5])
                    cube([HELMET_DIAMETER*2, HELMET_DIAMETER*2, TOTAL_DEPTH], center=true);
                    
                // Front Bill Brim Magnet Compartment Ports
                translate([0, HELMET_DIAMETER*0.48, -TOTAL_DEPTH*0.02])
                    cylinder(h=MAG_THICKNESS + 0.2, r=(MAG_DIAMETER - FIT_TOLERANCE)*0.5, center=true, $fn=40);
            }
            
            // MANTIS SHRIMP HELICOID SHOCK RIDGEWAY ARRAY
            for (rib_arc = [-60 : 30 : 60]) {
                rotate([rib_arc, 0, 0])
                    difference() {
                        scale([1, 1 + 0.08*sin(rib_arc*3), 1])
                            torus(r1=HELMET_DIAMETER*0.5 + SHELL_THICKNESS*0.5, r2=1.6);
                        translate([0, 0, -TOTAL_DEPTH*0.5]) cube([HELMET_DIAMETER*2, HELMET_DIAMETER*2, TOTAL_DEPTH], center=true);
                    }
            }
            
            // 🌿 🛠️ BUGFIX: LOTUS-EFFECT SWEPT-FILLET MICRO-PAPILLAE SKIN
            // Replaces standalone cones with continuous hull fillet blends.
            // Distributes high-velocity side-impact shear loads down the wide base curves,
            // preventing the papillae from cracking or shattering under tool strikes.
            intersection() {
                difference() {
                    sphere(d=HELMET_DIAMETER + SHELL_THICKNESS*2 + 0.6, $fn=100);
                    sphere(d=HELMET_DIAMETER + SHELL_THICKNESS*2 - 0.2, $fn=100);
                    translate([0, 0, -TOTAL_DEPTH*0.5]) cube([HELMET_DIAMETER*2, HELMET_DIAMETER*2, TOTAL_DEPTH], center=true);
                }
                union() {
                    for (phi = [15 : 12 : 85]) {
                        for (theta = [0 : 15 : 359]) {
                            rotate([0, phi, theta])
                                translate([0, 0, HELMET_DIAMETER*0.5 + SHELL_THICKNESS])
                                    // 🛠️ Continuous Flare-Base Cone Modification
                                    hull() {
                                        cylinder(h=PAPILLAE_SIZE*0.3, r1=PAPILLAE_SIZE*0.9, r2=PAPILLAE_SIZE*0.4, center=false, $fn=10);
                                        translate([0, 0, PAPILLAE_SIZE*0.3])
                                            cylinder(h=PAPILLAE_SIZE*0.7, r1=PAPILLAE_SIZE*0.4, r2=0.05, center=false, $fn=10);
                                    }
                        }
                    }
                }
            }
        }
        
        // LAYER 2: RE-ENTRANT AUXETIC SHOCK COMPACTION LATTICE
        color([0.4, 0.4, 0.4, 0.6]) {
            translate([0, 0, -0.2]) {
                intersection() {
                    difference() {
                        sphere(d=HELMET_DIAMETER, $fn=100);
                        sphere(d=HELMET_DIAMETER - WEB_DEPTH*2, $fn=100);
                    }
                    
                    // TESSELLATING AUXETIC STRUCTURAL CELL LOOPS
                    union() {
                        for (ax = [-HELMET_DIAMETER*0.55 : AUX_L*1.6 : HELMET_DIAMETER*0.55]) {
                            for (ay = [-HELMET_DIAMETER*0.55 : AUX_H*1.8 : HELMET_DIAMETER*0.55]) {
                                translate([ax + (mod(floor(ay/(AUX_H*1.8)), 2) * AUX_L*0.8), ay, 0])
                                    scale([1, 1, HELMET_DIAMETER/AUX_H])
                                        ReEntrant_Auxetic_BowTie_Cell();
                            }
                        }
                    }
                }
            }
        }
        
        // FRONT EXTENDED BRIM BILL
        translate([0, HELMET_DIAMETER*0.42, -TOTAL_DEPTH*0.05])
            color([0.15, 0.15, 0.15])
                scale([1.2, 0.5, 0.2])
                    cylinder(h=15.0, r=HELMET_DIAMETER*0.28, center=true, $fn=60);
    }
}

module ReEntrant_Auxetic_BowTie_Cell() {
    wall_w = 1.0;
    union() {
        translate([0, AUX_H*0.5, 0]) cube([AUX_L, wall_w, AUX_H], center=true);
        translate([0, -AUX_H*0.5, 0]) cube([AUX_L, wall_w, AUX_H], center=true);
        
        translate([AUX_L*0.25, 0, 0]) rotate() cube([wall_w, AUX_H*1.1, AUX_H], center=true);
        translate([-AUX_L*0.25, 0, 0]) rotate([0, 0, -30]) cube([wall_w, AUX_H*1.1, AUX_H], center=true);
        
        cube([AUX_W, wall_w, AUX_H], center=true);
    }
}

module torus(r1, r2) {
    rotate_extrude($fn=80) translate([r1, 0, 0]) circle(r=r2, $fn=30);
}

function mod(a, b) = a - floor(a/b)*b;

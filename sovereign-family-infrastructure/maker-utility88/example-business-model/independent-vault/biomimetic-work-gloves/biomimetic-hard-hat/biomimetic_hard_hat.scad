// Matrix Biomimetic Utilities - Resonant-Class Biomimetic Hard Hat
// Version 1.1.0-Helmet Core | 3D Rotational Auxetic Honeycomb Engine
// System Core: Woodpecker Hyoid Carapace + Re-Entrant Expansion Shock Lattice

// ============================================================================
// 🏛️ GLOBAL PARAMETRIC VARIABLES & HELMET GEOMETRIES
// ============================================================================
HELMET_DIAMETER = 220.0;  // Total ear-to-ear internal diameter of the dome (mm)
TOTAL_DEPTH = 140.0;      // Vertical clearance height from rim to crown (mm)
SHELL_THICKNESS = 3.00;   // Weather-proof outer ASA structural wall (mm)
WEB_DEPTH = 6.00;         // Thick high-rebound internal auxetic crumple web (mm)

// 📐 PARAMENTRIC AUXETIC SHOCK MATRIX CONSTANTS
AUX_H = 6.0;              // Height profile of individual re-entrant bow-tie cells (mm)
AUX_W = 4.5;              // Internal narrow waist width of the cell (mm)
AUX_L = 8.0;              // External length scale of the expansion cell (mm)

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
        // OUTER CHASSIS: WOODPECKER HYOID CARAPACE
        // Printed in high-impact, weather-proof matte ASA filament
        color([0.2, 0.2, 0.2]) {
            difference() {
                // Main Structural Protective Dome
                sphere(d=HELMET_DIAMETER + SHELL_THICKNESS*2, $fn=100);
                sphere(d=HELMET_DIAMETER, $fn=100);
                
                // Lower Neck Clearance Cutout Subtraction
                translate([0, 0, -TOTAL_DEPTH*0.5])
                    cube([HELMET_DIAMETER*2, HELMET_DIAMETER*2, TOTAL_DEPTH], center=true);
                    
                // Front Bill Brim Magnet Compartment Ports
                translate([0, HELMET_DIAMETER*0.48, -TOTAL_DEPTH*0.02])
                    cylinder(h=MAG_THICKNESS + 0.2, r=(MAG_DIAMETER - FIT_TOLERANCE)*0.5, center=true, $fn=40);
            }
            
            // Integrated Woodpecker Energy-Diverting Hyoid Ribs
            for (rib_arc = [-60 : 30 : 60]) {
                rotate([rib_arc, 0, 0])
                    difference() {
                        torus(r1=HELMET_DIAMETER*0.5 + SHELL_THICKNESS*0.5, r2=1.5);
                        translate([0, 0, -TOTAL_DEPTH*0.5]) cube([HELMET_DIAMETER*2, HELMET_DIAMETER*2, TOTAL_DEPTH], center=true);
                    }
            }
        }
        
        // 🧬 INTERNAL SHIELD: RE-ENTRANT AUXETIC SHOCK COMPACTION LATTICE
        // 🛠️ HARDWARE UPGRADE: Replaces plain grids with 3D re-entrant bow-tie cells.
        // Under localized crushing forces, the structure contracts inward laterally,
        // multiplying energy density directly beneath the blow while deadening head twist.
        color([0.4, 0.4, 0.4, 0.6]) {
            translate([0, 0, -0.2]) {
                intersection() {
                    difference() {
                        sphere(d=HELMET_DIAMETER, $fn=100);
                        sphere(d=HELMET_DIAMETER - WEB_DEPTH*2, $fn=100);
                    }
                    
                    // 📐 TESSELLATING AUXETIC STRUCTURAL CELL LOOPS
                    union() {
                        for (ax = [-HELMET_DIAMETER*0.55 : AUX_L*1.6 : HELMET_DIAMETER*0.55]) {
                            for (ay = [-HELMET_DIAMETER*0.55 : AUX_H*1.8 : HELMET_DIAMETER*0.55]) {
                                // Alternating honeycomb layout grid offset
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
    // Generates an individual negative Poisson's ratio expansion element
    // via continuous toolpath-optimized thin ribbon wall sweeps.
    wall_w = 1.0;
    union() {
        // Upper Arched Flange Web
        translate([0, AUX_H*0.5, 0]) cube([AUX_L, wall_w, AUX_H], center=true);
        // Lower Arched Flange Web
        translate([0, -AUX_H*0.5, 0]) cube([AUX_L, wall_w, AUX_H], center=true);
        
        // Angled Re-Entrant Inward-Leaning Struts (The Core Bow-Tie Knots)
        translate([AUX_L*0.25, 0, 0]) rotate([0, 0, 32]) cube([wall_w, AUX_H*1.1, AUX_H], center=true);
        translate([-AUX_L*0.25, 0, 0]) rotate([0, 0, -32]) cube([wall_w, AUX_H*1.1, AUX_H], center=true);
        
        // Narrow Internal Structural Hinge Core
        cube([AUX_W, wall_w, AUX_H], center=true);
    }
}

module torus(r1, r2) {
    rotate_extrude($fn=80) translate([r1, 0, 0]) circle(r=r2, $fn=30);
}

function mod(a, b) = a - floor(a/b)*b;

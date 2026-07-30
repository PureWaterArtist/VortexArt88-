// Matrix Biomimetic Utilities - Parametric Hourglass Dual-Vortex Hub Core
TOTAL_HEIGHT = 320.0;       
OUTER_DIAMETER = 140.0;   

WALL_THICKNESS = max(2.5, OUTER_DIAMETER * 0.025); 
GLASS_RADIUS = (OUTER_DIAMETER - (WALL_THICKNESS * 2)) / 2;
GLASS_HEIGHT = TOTAL_HEIGHT * 0.52;    
BASE_HEIGHT = TOTAL_HEIGHT * 0.26;     
TOP_CAP_HEIGHT = TOTAL_HEIGHT * 0.22;  
PILLAR_WIDTH = OUTER_DIAMETER * 0.13;  
CONDUIT_RADIUS = PILLAR_WIDTH * 0.45;   
IMPELLER_RADIUS = GLASS_RADIUS * 0.72;  
IMPELLER_HEIGHT = TOP_CAP_HEIGHT * 0.32;    
$fn = 120; 

module Ultimate_Sensory_Hub() {
    // 1. SMART INTERACTIVE POWER BASE (Dry Electronics and Aroma Matrix)
    color([0.12, 0.12, 0.12]) {
        difference() {
            cylinder(h=BASE_HEIGHT, r=OUTER_DIAMETER/2);
            translate([0, 0, -0.1])
                cylinder(h=BASE_HEIGHT - WALL_THICKNESS, r=(OUTER_DIAMETER/2) - WALL_THICKNESS);
            translate([0, 0, BASE_HEIGHT - (WALL_THICKNESS * 1.5)])
                cylinder(h=WALL_THICKNESS * 2, r=GLASS_RADIUS + 0.4);
            // Essential Oil Passive Thermal Venting Grilles
            for (ang = [0 : 30 : 330]) {
                rotate([0, 0, ang]) {
                    translate([GLASS_RADIUS + (WALL_THICKNESS * 0.5), -WALL_THICKNESS/2, BASE_HEIGHT - WALL_THICKNESS*1.2])
                        cube([WALL_THICKNESS * 1.5, WALL_THICKNESS, WALL_THICKNESS * 2]);
                }
            }
            // Ambient Nursery Sound Sensor Mic Port
            translate([0, -OUTER_DIAMETER/2 + WALL_THICKNESS, BASE_HEIGHT * 0.25])
                rotate([90, 0, 0]) cylinder(h=WALL_THICKNESS * 2, r=1.5, center=true);
            // Recessed Qi Wireless Charging Cradle
            translate([0, OUTER_DIAMETER/2 - WALL_THICKNESS*1.5, BASE_HEIGHT - WALL_THICKNESS*1.2])
                cube([OUTER_DIAMETER * 0.4, WALL_THICKNESS * 2, WALL_THICKNESS * 1.5], center=true);
        }
    }
    // 2. COUNTER-ROTATING WATER KINETIC ENGINE (Biomimetic Blades)
    translate([0, 0, BASE_HEIGHT + (WALL_THICKNESS * 1.1)])
        color([0.1, 0.6, 0.8, 0.85]) Biomimetic_Impeller(IMPELLER_RADIUS, IMPELLER_HEIGHT, 1);
    translate([0, 0, BASE_HEIGHT + GLASS_HEIGHT - IMPELLER_HEIGHT - (WALL_THICKNESS * 1.1)])
        color([0.95, 0.5, 0.1, 0.85]) Biomimetic_Impeller(IMPELLER_RADIUS, IMPELLER_HEIGHT, -1);
    // 3. CAPACITIVE TOUCH SUPPORT COLUMNS
    color([0.3, 0.3, 0.3]) {
        translate([-(OUTER_DIAMETER/2 - PILLAR_WIDTH), 0, 0]) Capacitive_Conduit_Pillar(TOTAL_HEIGHT);
        translate([(OUTER_DIAMETER/2 - PILLAR_WIDTH), 0, 0]) Capacitive_Conduit_Pillar(TOTAL_HEIGHT);
    }
    // 4. ACOUSTIC WATER CHIME REVERSE TOP CAP
    translate([0, 0, BASE_HEIGHT + GLASS_HEIGHT]) {
        color([0.12, 0.12, 0.12]) {
            difference() {
                cylinder(h=TOP_CAP_HEIGHT, r=OUTER_DIAMETER/2);
                translate([0, 0, WALL_THICKNESS]) cylinder(h=TOP_CAP_HEIGHT, r=(OUTER_DIAMETER/2) - WALL_THICKNESS);
                translate([0, 0, -0.5]) cylinder(h=WALL_THICKNESS * 1.5, r=GLASS_RADIUS + 0.4);
            }
            // Acoustic Biomimetic Chime Ring
            translate([0, 0, WALL_THICKNESS]) {
                difference() {
                    cylinder(h=WALL_THICKNESS * 1.2, r=GLASS_RADIUS - 1);
                    cylinder(h=WALL_THICKNESS * 2, r=GLASS_RADIUS - WALL_THICKNESS - 1);
                    for (chime_cut = [0 : 45 : 315]) {
                        rotate([0, 0, chime_cut]) translate([GLASS_RADIUS - WALL_THICKNESS, -1, -0.5]) cube([WALL_THICKNESS * 2, 2, WALL_THICKNESS * 3]);
                    }
                }
            }
        }
    }
}
module Capacitive_Conduit_Pillar(h_p) {
    difference() {
        cylinder(h=h_p, r=PILLAR_WIDTH);
        translate([0, 0, -1]) cylinder(h=h_p + 2, r=CONDUIT_RADIUS);
        translate([0, -PILLAR_WIDTH*0.5, -1]) cylinder(h=h_p + 2, r=CONDUIT_RADIUS * 0.4);
    }
}
module Biomimetic_Impeller(r, h, phase_dir) {
    cylinder(h=h*0.3, r=r*0.35);
    for (blade_angle = [0 : 60 : 300]) {
        rotate([0, 0, blade_angle * phase_dir]) {
            linear_extrude(height=h, twist=45 * phase_dir, slices=40) {
                translate([r*0.18, -WALL_THICKNESS/3, 0]) square([r * 0.82, WALL_THICKNESS/1.5]);
            }
        }
    }
}
Ultimate_Sensory_Hub();

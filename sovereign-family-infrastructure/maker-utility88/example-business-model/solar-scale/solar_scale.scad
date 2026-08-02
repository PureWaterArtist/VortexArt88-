// Matrix Biomimetic Utilities - Parametric Solar-Scale Harvesting Engine
// Version 2.3.0-Acrylic Core | Mechanical Anti-Creep Riveted Matrix Array

// ============================================================================
// 🏛️ MASTER SCALE PARAMETERS (Adjust to scale individual tile footprint)
// ============================================================================
TILE_WIDTH = 150.0;        // Flat-to-flat distance of individual hexagonal scale (mm)
TOTAL_STACK_H = 18.0;      // Complete multi-layer vertical thickness profile (mm)

// ============================================================================
// 📐 SCALE-INVARIANT PARAMETRIC RECONCILIATION
// ============================================================================
WALL_THICKNESS = max(2.0, TILE_WIDTH * 0.015);

// Tessellating Mechanical Constraints
SNAP_RADIUS = TILE_WIDTH * 0.04; 
SNAP_DEPTH = TOTAL_STACK_H * 0.4;

// PMMA Optical Refractive Trapping Vector Calculations (Index n = 1.49)
PRISM_ANGLE = 42.3; 
PRISM_SIZE = 1.5;  // Base footprint size of individual micro-lenses

$fn = 60; // Production resolution factor for interlocking nodes

// ============================================================================
// 🛠️ ULTIMATE SYSTEM ASSEMBLY INGESTION
// ============================================================================
module Full_Solar_Scale_Matrix() {
    difference() {
        union() {
            // LAYER 9 & LAYER 8: VASCULAR ENVELOPE BASE CHASSIS (Matte Weather-Proof ASA)
            color([0.15, 0.15, 0.15]) 
                Vascular_Base_Envelope();
            
            // LAYER 7 & LAYER 6: THERMOELECTRIC MATRIX & SILICON PV CORE
            translate([0, 0, TOTAL_STACK_H * 0.35])
                color([0.1, 0.2, 0.4]) 
                    cylinder(h=1.2, r=TILE_WIDTH * 0.42, $fn=6);
            
            // LAYER 5 & LAYER 4: TYMPANAL FREQUENCY HARVESTER (High-Crystallinity Piezo PVDF)
            translate([0, 0, TOTAL_STACK_H * 0.45])
                color([0.6, 0.5, 0.7, 0.8]) 
                    Tympanal_Piezo_Lattice(TOTAL_STACK_H * 0.15);
            
            // LAYER 3: AUXETIC METAMATERIAL ARMOR SHIELD LAYER (High-Rebound Clear TPU)
            translate([0, 0, TOTAL_STACK_H * 0.60])
                color([0.2, 0.7, 0.9, 0.5]) 
                    Auxetic_Armor_Web(TOTAL_STACK_H * 0.20);
            
            // LAYER 2 & LAYER 1: ANGLE-INVARIANT PRISMS & HYDROPHOBIC SKIN (Optical PMMA)
            translate([0, 0, TOTAL_STACK_H * 0.80])
                color([0.9, 0.9, 0.9, 0.35]) 
                    Optical_Acrylic_Prism_Skin(TOTAL_STACK_H * 0.20);
                    
            // TESSELLATING INTERLOCKING SNAP CONNECTORS (Male Contacts)
            for (face = [0 : 120 : 359]) {
                rotate([0, 0, face])
                    translate([TILE_WIDTH * 0.505, 0, 0])
                        Male_Interlock_Pin();
            }
        }
        
        // TESSELLATING RECIPROCATING SNAP SLOTS (Female Keyways)
        for (face = [60 : 120 : 359]) {
            rotate([0, 0, face])
                translate([TILE_WIDTH * 0.505, 0, 0])
                    Female_Keyway_Slot();
        }
        
        // 🛠️ INTEGRATED INDUSTRIAL PATCH: Z-AXIS RIVET ANCHOR HOLE ARRAY
        // Subtracts matching anchor paths down through the upper sheets into the ASA base
        // to receive solid mechanical PMMA lock-pins during multi-material extrusion
        for (rivet_node = [0 : 60 : 359]) {
            rotate([0, 0, rivet_node])
                translate([TILE_WIDTH * 0.35, 0, TOTAL_STACK_H * 0.1])
                    cylinder(h=TOTAL_STACK_H * 0.8, r=3.0, center=false);
        }
    }
}

// ============================================================================
// 🧬 SUBSYSTEM MECHANICAL MODULES
// ============================================================================

module Vascular_Base_Envelope() {
    difference() {
        cylinder(h=TOTAL_STACK_H * 0.35, r=TILE_WIDTH * 0.57, $fn=6);
        translate([0, 0, WALL_THICKNESS])
            cylinder(h=TOTAL_STACK_H, r=TILE_WIDTH * 0.45, $fn=6);
            
        // Elephant-Ear passive convective siphons
        for (vent = [-TILE_WIDTH*0.4 : WALL_THICKNESS*3 : TILE_WIDTH*0.4]) {
            translate([vent, -TILE_WIDTH*0.5, WALL_THICKNESS/2])
                rotate([-90, 0, 0])
                    cylinder(h=TILE_WIDTH, r=WALL_THICKNESS * 0.6);
        }
    }
}

module Auxetic_Armor_Web(h_armor) {
    difference() {
        intersection() {
            cylinder(h=h_armor, r=TILE_WIDTH * 0.54, $fn=6);
            union() {
                for (x = [-TILE_WIDTH : 12 : TILE_WIDTH]) {
                    for (y = [-TILE_WIDTH : 12 : TILE_WIDTH]) {
                        translate([x, y, h_armor/2]) {
                            rotate([0,0,45]) cube([1.2, 8, h_armor + 0.1], center=true);
                            rotate([0, 0, -45]) cube([1.2, 8, h_armor + 0.1], center=true);
                            cube([6, 1.2, h_armor + 0.1], center=true);
                        }
                    }
                }
            }
        }
        // Clearance loops for mechanical structural lock-rivets
        for (rivet_node = [0 : 60 : 359]) {
            rotate([0, 0, rivet_node])
                translate([TILE_WIDTH * 0.35, 0, -0.1])
                    cylinder(h=h_armor + 0.2, r=3.1, $fn=20);
        }
    }
}

module Tympanal_Piezo_Lattice(h_piezo) {
    intersection() {
        cylinder(h=h_piezo, r=TILE_WIDTH * 0.54, $fn=6);
        for (r_ring = [5 : 8 : TILE_WIDTH * 0.5]) {
            difference() {
                cylinder(h=h_piezo, r=r_ring + 0.6);
                translate([0, 0, -0.1])
                    cylinder(h=h_piezo + 0.2, r=r_ring - 0.6);
            }
        }
    }
}

module Optical_Acrylic_Prism_Skin(h_skin) {
    union() {
        // Main micro-prism array face
        intersection() {
            cylinder(h=h_skin, r=TILE_WIDTH * 0.57, $fn=6);
            union() {
                for (x = [-TILE_WIDTH : PRISM_SIZE : TILE_WIDTH]) {
                    for (y = [-TILE_WIDTH : PRISM_SIZE : TILE_WIDTH]) {
                        translate([x, y, 0])
                            polyhedron(
                                points=[[0,0,PRISM_SIZE*tan(PRISM_ANGLE)], [PRISM_SIZE/2,PRISM_SIZE/2,0], [PRISM_SIZE/2,-PRISM_SIZE/2,0], [-PRISM_SIZE/2,-PRISM_SIZE/2,0], [-PRISM_SIZE/2,PRISM_SIZE/2,0]],
                                faces=[[0,1,2], [0,2,3], [0,3,4], [0,4,1], [1,4,3,2]]
                            );
                    }
                }
            }
        }
        
        // 🛠️ ANTI-CREEP MECHANICAL RIVET STUDS
        // Extrudes solid PMMA structural anchor posts downward straight into the core shell
        for (rivet_node = [0 : 60 : 359]) {
            rotate([0, 0, rivet_node])
                translate([TILE_WIDTH * 0.35, 0, -TOTAL_STACK_H * 0.45])
                    cylinder(h=TOTAL_STACK_H * 0.46, r=2.9, $fn=20);
        }
    }
}

module Male_Interlock_Pin() {
    translate([0, 0, 0]) {
        cylinder(h=SNAP_DEPTH, r=SNAP_RADIUS, center=false);
        translate([0, 0, SNAP_DEPTH*0.7])
            torus(SNAP_RADIUS, 0.8);
    }
}

module Female_Keyway_Slot() {
    translate([0, 0, -0.1]) {
        cylinder(h=SNAP_DEPTH + 0.4, r=SNAP_RADIUS + 0.15, center=false);
        translate([0, 0, SNAP_DEPTH*0.7])
            torus(SNAP_RADIUS + 0.15, 1.0);
    }
}

module torus(r1, r2) {
    rotate_extrude() translate([r1, 0, 0]) circle(r=r2);
}

Full_Solar_Scale_Matrix();

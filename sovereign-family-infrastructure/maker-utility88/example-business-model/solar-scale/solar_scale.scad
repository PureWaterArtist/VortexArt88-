// Matrix Biomimetic Utilities - Parametric Solar-Scale Harvesting Engine
// Version 2.1.0-Acrylic Core | Pure Scale-Invariant Mechanical CAD (PMMA Optimized)

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
SNAP_RADIUS = TILE_WIDTH * 0.08;
SNAP_DEPTH = TOTAL_STACK_H * 0.4;

// PMMA Optical Refractive Trapping Vector Calculations (Index n = 1.49)
// 42.3-degree facet slopes maximize total internal reflection (TIR) for acrylic
PRISM_ANGLE = 42.3; 
PRISM_SIZE = 1.5;  // Base footprint size of individual micro-lenses

$fn = 60; // Production resolution factor for interlocking nodes

// ============================================================================
// 🛠️ ULTIMATE SYSTEM ASSEMBLY INGESTION
// ============================================================================
module Full_Solar_Scale_Matrix() {
    difference() {
        union() {
            // LAYER 9 & LAYER 8 SUB-ASSEMBLY: VASCULAR ENVELOPE BASE CHASSIS
            // Printed in weather-proof matte ASA filament
            color([0.15, 0.15, 0.15]) 
                Vascular_Base_Envelope();
            
            // LAYER 7 & LAYER 6: THERMOELECTRIC MATRIX & SILICON PV CORE
            // Embedded solid-state hardware integration steps
            translate([0, 0, TOTAL_STACK_H * 0.35])
                color([0.1, 0.2, 0.4]) 
                    cylinder(h=1.2, r=TILE_WIDTH * 0.42, $fn=6);
            
            // LAYER 5 & LAYER 4: MOTH-EYE MESH & TYMPANAL FREQUENCY HARVESTER
            // Printed via high-crystallinity piezoelectric PVDF homopolymer
            translate([0, 0, TOTAL_STACK_H * 0.45])
                color([0.6, 0.5, 0.7, 0.8]) 
                    Tympanal_Piezo_Lattice(TOTAL_STACK_H * 0.15);
            
            // LAYER 3: AUXETIC METAMATERIAL ARMOR SHIELD LAYER
            // Printed via impact-resistant high-rebound transparent TPU
            translate([0, 0, TOTAL_STACK_H * 0.60])
                color([0.2, 0.7, 0.9, 0.5]) 
                    Auxetic_Armor_Web(TOTAL_STACK_H * 0.20);
            
            // LAYER 2 & LAYER 1: ANGLE-INVARIANT PRISMS & HYDROPHOBIC SKIN
            // Co-extruded via sustainable, high-clarity optical-grade PMMA Acrylic
            translate([0, 0, TOTAL_STACK_H * 0.80])
                color([0.9, 0.9, 0.9, 0.35]) 
                    Optical_Acrylic_Prism_Skin(TOTAL_STACK_H * 0.20);
                    
            // TESSELLATING INTERLOCKING SNAP CONNECTORS (Male Contacts)
            for (face =) {
                rotate([0, 0, face])
                    translate([TILE_WIDTH * 0.5, 0, 0])
                        Male_Interlock_Pin();
            }
        }
        
        // TESSELLATING RECIPROCATING SNAP SLOTS (Female Keyways)
        for (face =) {
            rotate([0, 0, face])
                translate([TILE_WIDTH * 0.5, 0, 0])
                    Female_Keyway_Slot();
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
    intersection() {
        cylinder(h=h_armor, r=TILE_WIDTH * 0.54, $fn=6);
        union() {
            for (x = [-TILE_WIDTH : 12 : TILE_WIDTH]) {
                for (y = [-TILE_WIDTH : 12 : TILE_WIDTH]) {
                    translate([x, y, h_armor/2]) {
                        rotate([0, 0, 45]) cube([1.2, 8, h_armor + 0.1], center=true);
                        rotate([0, 0, -45]) cube([1.2, 8, h_armor + 0.1], center=true);
                        cube([6, 1.2, h_armor + 0.1], center=true);
                    }
                }
            }
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
    // PMMA Optimized Micro-Prisms
    intersection() {
        cylinder(h=h_skin, r=TILE_WIDTH * 0.57, $fn=6);
        union() {
            for (x = [-TILE_WIDTH : PRISM_SIZE : TILE_WIDTH]) {
                for (y = [-TILE_WIDTH : PRISM_SIZE : TILE_WIDTH]) {
                    translate([x, y, 0])
                        // Parametric pyramids optimized to a 42.3-degree refraction angle mask
                        polyhedron(
                            points=[[0,0,PRISM_SIZE*tan(PRISM_ANGLE)], [PRISM_SIZE/2,PRISM_SIZE/2,0], [PRION_SIZE/2,-PRISM_SIZE/2,0], [-PRISM_SIZE/2,-PRISM_SIZE/2,0], [-PRISM_SIZE/2,PRISM_SIZE/2,0]],
                            faces=[[0,1,2], [0,2,3], [0,3,4], [0,4,1], [1,4,3,2]]
                        );
                }
            }
        }
    }
}

module Male_Interlock_Pin() {
    translate([0, 0, SNAP_DEPTH/2]) {
        cylinder(h=SNAP_DEPTH, r=SNAP_RADIUS, center=true);
        translate([0, 0, SNAP_DEPTH*0.2])
            torus(SNAP_RADIUS, 1.0);
    }
}

module Female_Keyway_Slot() {
    translate([0, 0, SNAP_DEPTH/2 - 0.1]) {
        cylinder(h=SNAP_DEPTH + 0.4, r=SNAP_RADIUS + 0.15, center=true);
        translate([0, 0, SNAP_DEPTH*0.2])
            torus(SNAP_RADIUS + 0.15, 1.2);
    }
}

module torus(r1, r2) {
    rotate_extrude() translate([r1, 0, 0]) circle(r=r2);
}

Full_Solar_Scale_Matrix();

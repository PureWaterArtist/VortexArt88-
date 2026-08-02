// Matrix Biomimetic Utilities - Turnkey Compliant Hair Claw Clip Engine
// Version 1.4.0-Claw Core | Non-Fusing Hinge & Asymmetrical Herringbone Matrix

// ============================================================================
// 🏛️ GLOBAL PARAMETRIC VARIABLES & DIMENSIONAL BOUNDARIES
// ============================================================================
CLIP_LENGTH = 85.0;       // Total lengthwise footprint of claw backbone (mm)
CLIP_WIDTH = 42.0;        // Max width of closed double-jaw assembly (mm)
WALL_THICKNESS = 2.4;     // Optimized toolpath wall trace (mm)
CLEARANCE_OFFSET = 0.40;  // Expanded shield to completely stop hinge fusing

// 🎨 STYLE SELECTION MATRIX
// STYLE_SELECTOR: 1 = Base Minimalist Chassis, 2 = The Blooming Dahlia (Floral), 
//                 3 = The Monarch Wing (Butterfly), 4 = The Interlocking Chevron (Heart)
STYLE_SELECTOR = 1;

// Slicing Compilation Logic Router
if (STYLE_SELECTOR == 1) {
    Base_Claw_Chassis();
} else if (STYLE_SELECTOR == 2) {
    Style_Blooming_Dahlia();
} else if (STYLE_SELECTOR == 3) {
    Style_Monarch_Wing();
} else if (STYLE_SELECTOR == 4) {
    Style_Interlocking_Chevron_Heart();
}

// ============================================================================
// ⚙️ MECHANICAL ENGINE CORE MODULES
// ============================================================================

module Base_Claw_Chassis() {
    // Master print-in-place compliant drivetrain mesh assembly
    union() {
        // Left Claw & Handle Subsystem
        Left_Claw_Wing();
        
        // Right Claw & Handle Subsystem
        Right_Claw_Wing();
        
        // Central Resilient Chevron Living Spring
        Central_Chevron_Spring();
    }
}

module Left_Claw_Wing() {
    difference() {
        union() {
            // Main backbone armature strut
            translate([0, -CLIP_WIDTH*0.35, 0])
                cube([CLIP_LENGTH, WALL_THICKNESS, 22.0], center=true);
            
            // Lever handle leaf flange
            translate([0, -CLIP_WIDTH*0.5, 30.0])
                rotate()
                    cube([CLIP_LENGTH*0.7, WALL_THICKNESS, 20.0], center=true);
                    
            // Multi-Directional Logarithmic "Cat's Claw" Teeth
            for (tooth = [-CLIP_LENGTH*0.4 : 12.0 : CLIP_LENGTH*0.4]) {
                translate([tooth, -CLIP_WIDTH*0.35, -5.0])
                    rotate()
                        difference() {
                            // Primary Solid Tooth Foundation Core
                            hull() {
                                cube([3.5, 2.0, 16.0], center=true);
                                translate([0, 8.0, -10.0]) sphere(r=0.6); 
                            }
                            
                            // 🛠️ INTEGRATED PATCH: ASYMMETRICAL HERRINGBONE SURFACE GRIP RIBS
                            // V-grooves rotated to 120 degrees to cut straight across the 45-degree print paths.
                            // Wipes out toolpath bleeding while providing lateral expansion under load.
                            for (z_rib = [-6 : 3 : 6]) {
                                translate([0, 0.4, z_rib])
                                    rotate([0, 0, 30]) // 120-degree inclusive angle alignment
                                        cube([4.0, 0.6, 0.8], center=true);
                                translate([0, 0.4, z_rib])
                                    rotate([0, 0, -30])
                                        cube([4.0, 0.6, 0.8], center=true);
                            }
                        }
            }
        }
        // Material weight reduction and hair clearance windows
        cube([CLIP_LENGTH*0.8, CLIP_WIDTH*2, 12.0], center=true);
        
        // LEFT HINGE CHAMFERED V-GROOVE SEPARATION TRACK
        translate([0, -WALL_THICKNESS*0.5 - CLEARANCE_OFFSET*0.5, 12.0])
            rotate()
                cube([CLIP_LENGTH*1.1, CLEARANCE_OFFSET, 18.0], center=true);
    }
}

module Right_Claw_Wing() {
    // Exact symmetrical inversion mirror of the primary mechanical jaw layout
    mirror() {
        difference() {
            union() {
                translate([0, -CLIP_WIDTH*0.35, 0])
                    cube([CLIP_LENGTH, WALL_THICKNESS, 22.0], center=true);
                translate([0, -CLIP_WIDTH*0.5, 30.0])
                    rotate()
                        cube([CLIP_LENGTH*0.7, WALL_THICKNESS, 20.0], center=true);
                for (tooth = [-CLIP_LENGTH*0.4 : 12.0 : CLIP_LENGTH*0.4]) {
                    translate([tooth, -CLIP_WIDTH*0.35, -5.0])
                        rotate()
                            difference() {
                                hull() {
                                    cube([3.5, 2.0, 16.0], center=true);
                                    translate([0, 8.0, -10.0]) sphere(r=0.6);
                                }
                                // RIGHT SIDE ASYMMETRICAL HERRINGBONE SURFACE GRIP RIBS
                                for (z_rib = [-6 : 3 : 6]) {
                                    translate([0, 0.4, z_rib])
                                        rotate([0, 0, 30])
                                            cube([4.0, 0.6, 0.8], center=true);
                                    translate([0, 0.4, z_rib])
                                        rotate([0, 0, -30])
                                            cube([4.0, 0.6, 0.8], center=true);
                                }
                            }
                }
            }
            cube([CLIP_LENGTH*0.8, CLIP_WIDTH*2, 12.0], center=true);
            
            // RIGHT HINGE CHAMFERED V-GROOVE SEPARATION TRACK
            translate([0, -WALL_THICKNESS*0.5 - CLEARANCE_OFFSET*0.5, 12.0])
                rotate()
                    cube([CLIP_LENGTH*1.1, CLEARANCE_OFFSET, 18.0], center=true);
        }
    }
}

module Central_Chevron_Spring() {
    // Continuous zigzag living spring link. Slices supportless at a 45-degree bed hatch
    for (segment = [-CLIP_LENGTH*0.35 : 10.0 : CLIP_LENGTH*0.35]) {
        translate([segment, 0, 12.0]) {
            rotate() cube([WALL_THICKNESS - CLEARANCE_OFFSET*0.5, 7.0, 11.5], center=true);
            rotate([0, -45, 0]) cube([WALL_THICKNESS - CLEARANCE_OFFSET*0.5, 7.0, 11.5], center=true);
        }
    }
}

// ============================================================================
// 🎨 ELEVATED AESTHETIC VISUAL STYLE VARIANT EXTENSIONS
// ============================================================================

module Style_Blooming_Dahlia() {
    difference() {
        Base_Claw_Chassis();
        for (petal_angle = [-30 : 15 : 30]) {
            translate([sin(petal_angle)*30, -CLIP_WIDTH*0.5, 30.0])
                rotate([25, 0, petal_angle])
                    cube([2.0, 12.0, 25.0], center=true);
            translate([sin(petal_angle)*30, CLIP_WIDTH*0.5, 30.0])
                rotate([-25, 0, -petal_angle])
                    cube([2.0, 12.0, 25.0], center=true);
        }
    }
}

module Style_Monarch_Wing() {
    difference() {
        Base_Claw_Chassis();
        for (vein = [-CLIP_LENGTH*0.25 : 14.0 : CLIP_LENGTH*0.25]) {
            translate([vein, -CLIP_WIDTH*0.52, 30.0])
                rotate() cube([6.0, 10.0, 12.0], center=true);
            translate([vein, CLIP_WIDTH*0.52, 30.0])
                rotate([-25, -45, 0]) cube([6.0, 10.0, 12.0], center=true);
        }
    }
}

module Style_Interlocking_Chevron_Heart() {
    difference() {
        union() {
            Base_Claw_Chassis();
            translate([0, -CLIP_WIDTH*0.45, 28.0])
                rotate() cube([20.0, 4.0, 20.0], center=true);
            translate([0, CLIP_WIDTH*0.45, 28.0])
                rotate([-25, 0, -45]) cube([20.0, 4.0, 20.0], center=true);
        }
        translate([0, 0, 38.0])
            cube([4.0, CLIP_WIDTH*2, 8.0], center=true);
    }
}

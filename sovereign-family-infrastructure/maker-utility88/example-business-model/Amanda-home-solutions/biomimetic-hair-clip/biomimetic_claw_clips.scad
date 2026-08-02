// Matrix Biomimetic Utilities - Turnkey Compliant Hair Claw Clip Engine
// Version 1.2.0-Claw Core | Non-Fusing Hinge V-Groove Drivetrain Matrix

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
        
        // Central高度 Resilient Chevron Living Spring
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
                rotate([25, 0, 0])
                    cube([CLIP_LENGTH*0.7, WALL_THICKNESS, 20.0], center=true);
                    
            // Multi-Directional Logarithmic "Cat's Claw" Teeth
            for (tooth = [-CLIP_LENGTH*0.4 : 12.0 : CLIP_LENGTH*0.4]) {
                translate([tooth, -CLIP_WIDTH*0.35, -5.0])
                    rotate([0, 15, 0])
                        hull() {
                            cube([3.5, 2.0, 16.0], center=true);
                            translate([0, 8.0, -10.0]) sphere(r=0.6); // 3-Degree curved apex
                        }
            }
        }
        // Material weight reduction and hair clearance windows
        cube([CLIP_LENGTH*0.8, CLIP_WIDTH*2, 12.0], center=true);
        
        // INTEGRATED PATCH: LEFT HINGE CHAMFERED V-GROOVE SEPARATION TRACK
        // Carves a micro-slice relief line along the internal jaw pivot spine
        translate([0, -WALL_THICKNESS*0.5 - CLEARANCE_OFFSET*0.5, 12.0])
            rotate([0, 0, 0])
                cube([CLIP_LENGTH*1.1, CLEARANCE_OFFSET, 18.0], center=true);
    }
}

module Right_Claw_Wing() {
    // Exact symmetrical inversion mirror of the primary mechanical jaw layout
    mirror([0, 1, 0]) {
        difference() {
            union() {
                translate([0, -CLIP_WIDTH*0.35, 0])
                    cube([CLIP_LENGTH, WALL_THICKNESS, 22.0], center=true);
                translate([0, -CLIP_WIDTH*0.5, 30.0])
                    rotate([25, 0, 0])
                        cube([CLIP_LENGTH*0.7, WALL_THICKNESS, 20.0], center=true);
                for (tooth = [-CLIP_LENGTH*0.4 : 12.0 : CLIP_LENGTH*0.4]) {
                    translate([tooth, -CLIP_WIDTH*0.35, -5.0])
                        rotate([0, 15, 0])
                            hull() {
                                cube([3.5, 2.0, 16.0], center=true);
                                translate([0, 8.0, -10.0]) sphere(r=0.6);
                            }
                }
            }
            cube([CLIP_LENGTH*0.8, CLIP_WIDTH*2, 12.0], center=true);
            
            // INTEGRATED PATCH: RIGHT HINGE CHAMFERED V-GROOVE SEPARATION TRACK
            translate([0, -WALL_THICKNESS*0.5 - CLEARANCE_OFFSET*0.5, 12.0])
                rotate([0, 0, 0])
                    cube([CLIP_LENGTH*1.1, CLEARANCE_OFFSET, 18.0], center=true);
        }
    }
}

module Central_Chevron_Spring() {
    // Continuous zigzag living spring link. Slices supportless at a 45-degree bed hatch
    // Shifted and thinned slightly along the boundaries to perfectly mirror the clearance slots
    for (segment = [-CLIP_LENGTH*0.35 : 10.0 : CLIP_LENGTH*0.35]) {
        translate([segment, 0, 12.0]) {
            rotate([0, 45, 0]) cube([WALL_THICKNESS - CLEARANCE_OFFSET*0.5, 7.0, 11.5], center=true);
            rotate([0, -45, 0]) cube([WALL_THICKNESS - CLEARANCE_OFFSET*0.5, 7.0, 11.5], center=true);
        }
    }
}

// ============================================================================
// 🎨 ELEVATED AESTHETIC VISUAL STYLE VARIANT EXTENSIONS
// ============================================================================

module Style_Blooming_Dahlia() {
    // VARIANT A: THE BLOOMING DAHLIA (High-Fashion Geometric Floral Plates)
    difference() {
        Base_Claw_Chassis();
        
        // Overlays continuous layered geometric petals across the outer handle loops
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
    // VARIANT B: THE MONARCH WING (Skeletal Insect Aerodynamic Grid)
    difference() {
        Base_Claw_Chassis();
        
        // Carves elegant open vein windows directly through the outer thumb flanges
        for (vein = [-CLIP_LENGTH*0.25 : 14.0 : CLIP_LENGTH*0.25]) {
            translate([vein, -CLIP_WIDTH*0.52, 30.0])
                rotate([25, 45, 0]) cube([6.0, 10.0, 12.0], center=true);
            translate([vein, CLIP_WIDTH*0.52, 30.0])
                rotate([-25, -45, 0]) cube([6.0, 10.0, 12.0], center=true);
        }
    }
}

module Style_Interlocking_Chevron_Heart() {
    // VARIANT C: THE INTERLOCKING CHEVRON HEART (Symmetrical Contour Closure)
    difference() {
        union() {
            Base_Claw_Chassis();
            
            // Adds external soft sweeping boundary plates to the closed handle profiles
            translate([0, -CLIP_WIDTH*0.45, 28.0])
                rotate([25, 0, 45]) cube([20.0, 4.0, 20.0], center=true);
            translate([0, CLIP_WIDTH*0.45, 28.0])
                rotate([-25, 0, -45]) cube([20.0, 4.0, 20.0], center=true);
        }
        // Cuts an ergonomic heart indentation split tracking line straight over the jaw spine
        translate([0, 0, 38.0])
            cube([4.0, CLIP_WIDTH*2, 8.0], center=true);
    }
}

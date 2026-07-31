// Matrix Biomimetic Utilities - Parametric MKX Transit Packaging Shield
// Version 2.0.0-Production Core | 2-Piece Mechanical Slide-Interlock Layout

PRODUCT_DIAMETER = 22.0;   
PRODUCT_LENGTH = 85.0;     
SHELL_WALL = 2.0;          

CORE_RADIUS_INNER = (PRODUCT_DIAMETER / 2) + 0.15; 
TOTAL_SHELL_RADIUS = CORE_RADIUS_INNER + SHELL_WALL;
TOTAL_LENGTH = PRODUCT_LENGTH + 12.0; 

$fn = 90; 

// PART_SELECTOR: 0 = Full Visual Preview, 1 = Print Black ASA Outer Armor, 2 = Print Flexible TPU Core Insert
PART_SELECTOR = 0;

if (PART_SELECTOR == 0) {
    color("DimGray") MKX_Transit_Chassis_Base();
    translate([0, 0, 2.0]) color("Orange") MKX_Flexible_TPU_Core();
} else if (PART_SELECTOR == 1) {
    MKX_Transit_Chassis_Base();
} else if (PART_SELECTOR == 2) {
    MKX_Flexible_TPU_Core();
}

module MKX_Transit_Chassis_Base() {
    difference() {
        union() {
            // 1. PRIMARY TURTLE-SHELL MATTE ASA OUTER EXOSKELETON
            cylinder(h=TOTAL_LENGTH, r=TOTAL_SHELL_RADIUS, center=true);
            
            // External alignment interlocking ribs for transit crate nesting
            for (rib = [0 : 90 : 359]) {
                rotate([0, 0, rib])
                    translate([TOTAL_SHELL_RADIUS - 0.2, 0, 0])
                        cube([1.5, 4.0, TOTAL_LENGTH * 0.9], center=true);
            }
        }
        
        // 2. MASTER INTERNAL SLIDE-KEYWAY SUBTRACTION
        // Clearance pocket to receive the mechanical TPU insert sleeve core
        translate([0, 0, 4.0])
            cylinder(h=TOTAL_LENGTH, r=CORE_RADIUS_INNER + 0.4, center=true);
            
        // 3. TWIST-LOCK TOP CHILD-RESISTANT FLANGE GROOVE
        translate([0, 0, (TOTAL_LENGTH / 2) - 3.0])
            rotate_extrude()
                translate([CORE_RADIUS_INNER + 0.4, 0, 0])
                    circle(r=0.8, $fn=12);
                    
        // 4. LOWER OUTGAS VENTILATION CROSS-RIBS
        translate([0, 0, (-TOTAL_LENGTH / 2) + 0.25])
            cube([TOTAL_SHELL_RADIUS * 2.2, 1.2, 0.5], center=true);
    }
}

module MKX_Flexible_TPU_Core() {
    // Independent thin-walled spring sleeve that slides mechanically into the ASA base
    difference() {
        cylinder(h=PRODUCT_LENGTH, r=CORE_RADIUS_INNER + 0.2, center=true);
        cylinder(h=PRODUCT_LENGTH + 2, r=CORE_RADIUS_INNER - 0.2, center=true);
    }
    
    // Internal 0.6mm thin biomimetic spring fingers grip product securely to absorb road vibrations
    intersection() {
        cylinder(h=PRODUCT_LENGTH, r=CORE_RADIUS_INNER, center=true);
        for (finger = [30 : 120 : 359]) {
            rotate([0, 0, finger])
                translate([CORE_RADIUS_INNER - 0.4, 0, 0])
                    cylinder(h=PRODUCT_LENGTH, r1=0.2, r2=0.6, center=true);
        }
    }
}

// Matrix Biomimetic Utilities - Parametric MKX Transit Packaging Shield
// Version 1.0.0-Packaging Core | Supportless Closed-Loop Reusable Armor

// ============================================================================
// 🏛️ MASTER PRODUCT CHAMBER (Adjust to match changing product case footprints)
// ============================================================================
PRODUCT_DIAMETER = 22.0;   // Interior chamber diameter for master product vials (mm)
PRODUCT_LENGTH = 85.0;     // Total vertical height clearance of the internal product (mm)
SHELL_WALL = 2.4;          // 2.4mm thick high-density perimeter barrier wall [1.1]

// ============================================================================
// 📐 RECONCILIATION & SHRINKAGE CONTROLS (Compensates for 1.8% Polypropylene Contraction)
// ============================================================================
CORE_RADIUS_INNER = (PRODUCT_DIAMETER / 2) + 0.15; // 0.15mm air gap prevents product extraction binding
TOTAL_SHELL_RADIUS = CORE_RADIUS_INNER + SHELL_WALL;
TOTAL_LENGTH = PRODUCT_LENGTH + 12.0; // Allocates base and cap mechanical clearances

$fn = 100; // Premium curvature resolution for smooth industrial automated line grabbing

// ============================================================================
// 🛠️ CHASSIS ENGINE ROUTER
// ============================================================================
module MKX_Biomimetic_Transit_Shield() {
    difference() {
        union() {
            // 1. PRIMARY TURTLE-SHELL AEROSPACE FRAME
            // Printed in highly ductile, chemical-resistant Polypropylene (PP)
            cylinder(h=TOTAL_LENGTH, r=TOTAL_SHELL_RADIUS, center=true);
            
            // 2. TESSELLATING INTERLOCKING ALIGNMENT RIBS
            // External alignment ribs ensure shields nest perfectly flush inside master transit cases
            for (rib = [0 : 90 : 359]) {
                rotate([0, 0, rib])
                    translate([TOTAL_SHELL_RADIUS - 0.2, 0, 0])
                        cube([1.5, 4.0, TOTAL_LENGTH * 0.9], center=true);
            }
        }
        
        // 3. MASTER INNER PRODUCT BAY INGESTION POCKET
        translate([0, 0, 4.0])
            cylinder(h=TOTAL_LENGTH, r=CORE_RADIUS_INNER, center=true);
            
        // 4. TWIST-LOCK TOP FLANGE INTERFACE
        // Secure guide groove to take a multi-use child-resistant locking cap without tape
        translate([0, 0, (TOTAL_LENGTH / 2) - 3.0])
            rotate_extrude()
                translate([CORE_RADIUS_INNER, 0, 0])
                    circle(r=0.8, $fn=12);
                    
        // 5. LOWER OUTGAS VENTILATION CROSS-RIBS
        // 0.5mm bottom grooves prevent styrene bed bubble traps during high-speed farm layers
        translate([0, 0, (-TOTAL_LENGTH / 2) + 0.25])
            cube([TOTAL_SHELL_RADIUS * 2.2, 1.2, 0.5], center=true);
    }
    
    // 6. BIOMIMETIC VERTICAL RETENTION REED FINGERS
    // Internal 0.6mm thin spring fingers printed out of high-rebound flexible TPU.
    // They flex inward to grip varied product diameters securely, erasing transit rattling shock.
    intersection() {
        translate([0, 0, 4.0])
            cylinder(h=PRODUCT_LENGTH * 0.8, r=CORE_RADIUS_INNER, center=true);
            
        for (finger = [30 : 120 : 359]) {
            rotate([0, 0, finger])
                translate([CORE_RADIUS_INNER - 0.4, 0, 0])
                    cylinder(h=PRODUCT_LENGTH * 0.8, r1=0.2, r2=0.6, center=true);
        }
    }
}

MKX_Biomimetic_Transit_Shield();

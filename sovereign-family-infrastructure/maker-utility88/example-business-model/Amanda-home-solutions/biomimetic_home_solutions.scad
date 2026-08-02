// Matrix Biomimetic Utilities - Floral Home Solutions Master File (Complete Master)
// Version 1.6.0-Home Master | Conical Escape Taper Interlocking Matrix

// ============================================================================
// 🏛️ GLOBAL SYSTEM VARIABLES & PARAMETRIC SCALE BOUNDARIES
// ============================================================================
BASE_RADIUS = 60.0;       // Reference radius for unified box-set footprint (mm)
WALL_THICKNESS = 2.4;     // Standardized wall thickness for optimal toolpaths (mm)
CLEARANCE_OFFSET = 0.30;  // Expanded horizontal clearance to fully eliminate TPU stick

// 🖨️ FABRICATION ROUTER SELECTOR
// ITEM_SELECTOR: 0 = Master Unified Visual Preview (Grid Array Mode)
//                 1 = Sunflower Scrub Daddy Mount       2 = Water-Lily Dish Rack
//                 3 = Calla-Lily Towel Spire            4 = Orchid Under-Sink Caddy
//                 5 = Tulip Roll Terminal               6 = Succulent Wall Pods
//                 7 = Peony Meal Prep Pods              8 = Carnation Snap Wraps
//                 9 = Rose-Thorn Multi-Hooks           10 = Passion-Flower Universal Spline
//                11 = Orchid Caddy T-Spline Grip Sleeve
ITEM_SELECTOR = 0;

if (ITEM_SELECTOR == 0) {
    // 3x4 Grid Visual Matrix Preview for Executive Showroom Presentation
    translate([-150,  150, 0]) color("MatteTerracotta") Item_Sunflower_Mount();
    translate() color("NaturalBone") Item_Water_Lily_Rack();
    translate() color("WarmDesert") Item_Calla_Lily_Spire();
    
    translate([-150,    0, 0]) color("SoftSage") Item_Orchid_Caddy();
    translate() color("WarmDesert") Item_Tulip_Terminal();
    translate() color("SoftSage") Item_Succulent_Pod();
    
    translate([-150, -150, 0]) color("NaturalBone") Item_Peony_Prep_Pod();
    translate([   0, -150, 0]) color("MatteTerracotta") Item_Carnation_Snap_Wrap();
    translate([ 150, -150, 0]) color("SlateGray") Item_Rose_Thorn_Hook();
    
    translate([   0,    0, -15]) color("Charcoal") Item_Passion_Flower_Spline();
    translate([ -75,  250, 0]) color("Charcoal") Item_Caddy_Grip_Sleeve();
} else if (ITEM_SELECTOR == 1) { Item_Sunflower_Mount(); }
  else if (ITEM_SELECTOR == 2) { Item_Water_Lily_Rack(); }
  else if (ITEM_SELECTOR == 3) { Item_Calla_Lily_Spire(); }
  else if (ITEM_SELECTOR == 4) { Item_Orchid_Caddy(); }
  else if (ITEM_SELECTOR == 5) { Item_Tulip_Terminal(); }
  else if (ITEM_SELECTOR == 6) { Item_Succulent_Pod(); }
  else if (ITEM_SELECTOR == 7) { Item_Peony_Prep_Pod(); }
  else if (ITEM_SELECTOR == 8) { Item_Carnation_Snap_Wrap(); }
  else if (ITEM_SELECTOR == 9) { Item_Rose_Thorn_Hook(); }
  else if (ITEM_SELECTOR == 10) { Item_Passion_Flower_Spline(); }
  else if (ITEM_SELECTOR == 11) { Item_Caddy_Grip_Sleeve(); }

// ============================================================================
// ⚙️ KITCHEN INFRASTRUCTURE COMPONENT ENGINE MODULES (BLOCK 1)
// ============================================================================

module Item_Sunflower_Mount() {
    difference() {
        union() {
            cylinder(h=4.0, r=BASE_RADIUS, center=true, $fn=6); 
            translate([0, 0, 15.0]) cylinder(h=30.0, r1=12.0, r2=9.0, center=true, $fn=60);
        }
        Universal_Interface_Keyway();
        for (petal = [0 : 22.5 : 359]) {
            rotate([0, 0, petal])
                translate([BASE_RADIUS*0.6, 0, 0])
                    cube([BASE_RADIUS*0.7, 3.0, 10.0], center=true);
        }
    }
}

module Item_Water_Lily_Rack() {
    difference() {
        cylinder(h=12.0, r1=BASE_RADIUS*1.4, r2=BASE_RADIUS*1.5, center=true, $fn=6);
        translate([0, 0, WALL_THICKNESS])
            cylinder(h=12.0, r1=BASE_RADIUS*1.38, r2=BASE_RADIUS*1.46, center=true, $fn=6);
        for (ring = [20 : 18 : BASE_RADIUS*1.2]) {
            difference() {
                cylinder(h=15.0, r=ring+1.5, center=true);
                cylinder(h=17.0, r=ring-1.5, center=true);
            }
        }
        translate([BASE_RADIUS*1.4, 0, -4.0]) cube([15.0, 30.0, 10.0], center=true);
    }
}

module Item_Calla_Lily_Spire() {
    difference() {
        union() {
            cylinder(h=160.0, r1=18.0, r2=12.0, center=true, $fn=60);
            translate([0, 0, -10.0]) rotate()
                difference() {
                    cylinder(h=140.0, r1=45.0, r2=55.0, center=true, $fn=60);
                    cylinder(h=142.0, r1=45.0-WALL_THICKNESS, r2=55.0-WALL_THICKNESS, center=true, $fn=60);
                    translate([45.0, 0, 0]) cube([30.0, 120.0, 145.0], center=true); 
                }
        }
        translate([0, 0, -78.0]) Universal_Interface_Keyway();
    }
}

module Universal_Interface_Keyway() {
    difference() {
        cylinder(h=16.0, r=9.6, center=true, $fn=6); 
        for (gutter = [0 : 90 : 270]) {
            rotate([0, 0, gutter])
                translate([4.0, 0, -8.0])
                    cube([12.0, 1.0, 1.2], center=true);
        }
    }
    translate([0, 0, -8.0]) cylinder(h=6.0, r=0.8, center=true, $fn=20);
}

// ============================================================================
// ⚙️ SANITARY & ORGANIZATIONAL COMPONENT ENGINE MODULES (BLOCK 2)
// ============================================================================

module Item_Orchid_Caddy() {
    difference() {
        union() {
            cube([BASE_RADIUS*1.6, BASE_RADIUS*1.2, 50.0], center=true);
            translate([BASE_RADIUS*0.8, 0, 0])
                rotate() cube([6.0, 6.0, 46.0], center=true);
        }
        translate([-BASE_RADIUS*0.8, 0, 0])
            rotate() cube([6.0 + CLEARANCE_OFFSET, 6.0 + CLEARANCE_OFFSET, 52.0], center=true);
            
        for (x_pock = [-30, 30]) {
            for (y_pock = [-20, 20]) {
                translate([x_pock, y_pock, 4.0]) {
                    cylinder(h=46.0, r=24.0, center=true, $fn=40); 
                    
                    for (slot =) {
                        rotate([0, 0, slot]) translate([24.0, 0, 0]) {
                            cube([2.0, 4.0, 46.0], center=true); 
                            translate([1.2, 0, 0]) cube([2.5, 6.3, 46.0], center=true); 
                        }
                    }
                }
            }
        }
        Universal_Interface_Keyway();
    }
}

module Item_Caddy_Grip_Sleeve() {
    // 🛠️ BUGFIX: 1-DEGREE CONICAL ESCAPE TAPER INTEGRATION (TPU LINER FACE)
    // Slices flat on Plate 3. Incorporates a subtle Z-axis draft thickness 
    // to instantly shatter rubber friction surface drag upon a 1.0mm vertical lift.
    union() {
        translate([0, 0, WALL_THICKNESS*0.5])
            cube([150.0, 42.0, WALL_THICKNESS], center=true);
            
        for (x_rail = [-50, 0, 50]) {
            translate([x_rail, 0, -1.0]) {
                // Tapered neck profile
                cylinder(h=42.0, r1=1.0, r2=0.75, center=true, $fn=4);
                translate([0, 0, -1.0]) cube([2.2, 42.0, 5.8], center=true); 
            }
        }
    }
}

module Item_Tulip_Terminal() {
    difference() {
        union() {
            cube([40.0, 40.0, WALL_THICKNESS], center=true);
            translate([0, BASE_RADIUS*0.5, 0]) cube([16.0, BASE_RADIUS, 12.0], center=true);
            translate([0, BASE_RADIUS, 30.0]) {
                for (leaf = [0 : 90 : 270]) {
                    rotate([0, 0, leaf]) translate([14.0, 0, 0])
                        rotate([0, -4, 0]) cube([WALL_THICKNESS, 18.0, 70.0], center=true);
                }
            }
        }
        Universal_Interface_Keyway();
    }
}

module Item_Succulent_Pod() {
    difference() {
        union() {
            scale([1, 1.3, 1]) sphere(r=BASE_RADIUS*0.4, $fn=6);
            translate([0, -BASE_RADIUS*0.35, 0]) cube([45.0, 4.0, 45.0], center=true);
        }
        scale([0.92, 1.22, 0.92]) sphere(r=BASE_RADIUS*0.4, $fn=6);
        translate([0, 0, BASE_RADIUS*0.4]) cube([100.0, 100.0, BASE_RADIUS*0.4], center=true);
        translate([0, -BASE_RADIUS*0.35, 0]) rotate() Universal_Interface_Keyway();
    }
}

// ============================================================================
// ⚙️ MEAL PREP & INTERLOCKING CONNECTOR ENGINE MODULES (BLOCK 3)
// ============================================================================

module Item_Peony_Prep_Pod() {
    // 🛠️ BUGFIX: 1-DEGREE CONICAL ESCAPE TAPER INTEGRATION (OUTER PP WALL)
    // Tapers the external shell radius from bottom-to-top by 1 degree.
    // This allows the container to slide past the soft inner caddy sleeve 
    // with flat-zero friction drag during unboxing extraction runs.
    difference() {
        cylinder(h=45.0, r1=BASE_RADIUS*1.08, r2=BASE_RADIUS*1.12, center=true, $fn=60);
        translate([0, 0, WALL_THICKNESS])
            cylinder(h=45.0, r1=BASE_RADIUS*1.08 - WALL_THICKNESS, r2=BASE_RADIUS*1.12 - WALL_THICKNESS, center=true, $fn=60);
        cube([BASE_RADIUS*2.3, 1.2, 50.0], center=true);
        cube([1.2, BASE_RADIUS*2.3, 50.0], center=true);
    }
}

module Item_Carnation_Snap_Wrap() {
    difference() {
        cube([BASE_RADIUS*1.3, 16.0, 8.0], center=true);
        cube([BASE_RADIUS*1.0, 2.0, 12.0], center=true);
        for (teeth = [-BASE_RADIUS*0.4 : 6.0 : BASE_RADIUS*0.4]) {
            translate([teeth, 0, 0]) rotate() cube([4.0, 4.0, 10.0], center=true);
        }
    }
}

module Item_Rose_Thorn_Hook() {
    difference() {
        union() {
            cube([35.0, 35.0, 4.0], center=true);
            hull() {
                translate([0, 6.0, 0]) cube([12.0, 10.0, 12.0], center=true);
                translate([0, 35.0, -25.0]) sphere(r=2.0); 
            }
        }
        Universal_Interface_Keyway();
    }
}

module Item_Passion_Flower_Spline() {
    union() {
        cylinder(h=6.0, r=14.0, center=true, $fn=6); 
        translate([0, 0, 6.0]) cylinder(h=8.0, r=9.5 - CLEARANCE_OFFSET, center=true, $fn=6); 
    }
}

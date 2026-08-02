// Matrix Biomimetic Utilities - Floral Home Solutions Master File (Block 1)
// Version 1.6.0-Home Master | Supportless Parametric Floral Geometry Matrix

// ============================================================================
// 🏛️ GLOBAL SYSTEM VARIABLES & PARAMETRIC SCALE BOUNDARIES
// ============================================================================
BASE_RADIUS = 60.0;       // Reference radius for unified box-set footprint (mm)
WALL_THICKNESS = 2.4;     // Standardized wall thickness for optimal toolpaths (mm)
CLEARANCE_OFFSET = 0.30;  // Expanded horizontal clearance to fully eliminate TPU stick

// 🖨️ FABRICATION ROUTER SELECTOR
// ITEM_SELECTOR: 0 = Master Unified Visual Preview (Grid Array Mode)
//                 1 = Sunflower Scrub Daddy Mount       2 = Water-Lily Dish Rack
//                 3 = Calla-Lily Towel Spire            
ITEM_SELECTOR = 0;

if (ITEM_SELECTOR == 0) {
    // Row 1: Kitchen Infrastructure Cores Display Preview
    translate([-150,  150, 0]) color("MatteTerracotta") Item_Sunflower_Mount();
    translate([   0,  150, 0]) color("NaturalBone") Item_Water_Lily_Rack();
    translate([ 150,  150, 0]) color("WarmDesert") Item_Calla_Lily_Spire();
} else if (ITEM_SELECTOR == 1) { Item_Sunflower_Mount(); }
  else if (ITEM_SELECTOR == 2) { Item_Water_Lily_Rack(); }
  else if (ITEM_SELECTOR == 3) { Item_Calla_Lily_Spire(); }

// ============================================================================
// ⚙️ KITCHEN INFRASTRUCTURE COMPONENT ENGINE MODULES
// ============================================================================

module Item_Sunflower_Mount() {
    // ITEM 1: THE SUNFLOWER SCRUB DADDY AERATION MOUNT (Suction Sink Basin Node)
    difference() {
        union() {
            cylinder(h=4.0, r=BASE_RADIUS, center=true, $fn=6); // Hexagonal mounting wall flange
            // Raised Central Flower Stalk (Drives straight through original sponge eye loops)
            translate([0, 0, 15.0]) cylinder(h=30.0, r1=12.0, r2=9.0, center=true, $fn=60);
        }
        // Hollow Core Channel for the Universal Passion-Flower Interface Spline Keyway
        Universal_Interface_Keyway();
        
        // 16 Radiating Air-Filtration Petal Slots (Channels gravity moisture drop directly out)
        for (petal = [0 : 22.5 : 359]) {
            rotate([0, 0, petal])
                translate([BASE_RADIUS*0.6, 0, 0])
                    cube([BASE_RADIUS*0.7, 3.0, 10.0], center=true);
        }
    }
}

module Item_Water_Lily_Rack() {
    // ITEM 2: THE WATER-LILY DYNAMIC SELF-DRAINING DISH RACK (Hydrophobic Tiers)
    difference() {
        // Base overlapping lily-pad platter curvature profile
        cylinder(h=12.0, r1=BASE_RADIUS*1.4, r2=BASE_RADIUS*1.5, center=true, $fn=6);
        translate([0, 0, WALL_THICKNESS])
            cylinder(h=12.0, r1=BASE_RADIUS*1.38, r2=BASE_RADIUS*1.46, center=true, $fn=6);
            
        // Concentric Dish-Holding Ridge Slots
        for (ring = [20 : 18 : BASE_RADIUS*1.2]) {
            difference() {
                cylinder(h=15.0, r=ring+1.5, center=true);
                cylinder(h=17.0, r=ring-1.5, center=true);
            }
        }
        // Front Pivoting Stem Spout Drainage Cutout Hole
        translate([BASE_RADIUS*1.4, 0, -4.0]) cube([15.0, 30.0, 10.0], center=true);
    }
}

module Item_Calla_Lily_Spire() {
    // ITEM 3: THE CALLA-LILY VERTICAL PAPER TOWEL SPIRE (Living Friction Shroud)
    difference() {
        union() {
            // Heavy wide-bottomed vertical core stem
            cylinder(h=160.0, r1=18.0, r2=12.0, center=true, $fn=60);
            // Sweeping Calla Lily wrap envelope acting as an organic living tension brake
            translate([0, 0, -10.0]) rotate([0, 5, 0])
                difference() {
                    cylinder(h=140.0, r1=45.0, r2=55.0, center=true, $fn=60);
                    cylinder(h=142.0, r1=45.0-WALL_THICKNESS, r2=55.0-WALL_THICKNESS, center=true, $fn=60);
                    translate([45.0, 0, 0]) cube([30.0, 120.0, 145.0], center=true); // Splitting loop gap
                }
        }
        // Base counter-bore for Universal Spline anchoring matrix
        translate([0, 0, -78.0]) Universal_Interface_Keyway();
    }
}

module Universal_Interface_Keyway() {
    // Centralized Hexagonal Female Connector Socket with Asymmetrical Fluid-Drainage Gutters
    // Cut directly into every standalone asset to receive the Passion-Flower spline key cleanly
    difference() {
        cylinder(h=16.0, r=9.6, center=true, $fn=6); // Primary male spline channel
        
        // 4x Cross-hatched fluid-drainage gutter channels to completely stop hydrostatic lock
        for (gutter = [0 : 90 : 270]) {
            rotate([0, 0, gutter])
                translate([4.0, 0, -8.0])
                    cube([12.0, 1.0, 1.2], center=true);
        }
    }
    // Deep center anti-pneumatic core relief vent
    translate([0, 0, -8.0]) cylinder(h=6.0, r=0.8, center=true, $fn=20);
}
// Matrix Biomimetic Utilities - Floral Home Solutions Master File (Block 2)
// ============================================================================
// ⚙️ SANITARY & ORGANIZATIONAL COMPONENT ENGINE MODULES
// ============================================================================

// Append this routing selector segment to the master preview logic loop:
// else if (ITEM_SELECTOR == 4) { Item_Orchid_Caddy(); }
// else if (ITEM_SELECTOR == 5) { Item_Tulip_Terminal(); }
// else if (ITEM_SELECTOR == 6) { Item_Succulent_Pod(); }
// else if (ITEM_SELECTOR == 11) { Item_Caddy_Grip_Sleeve(); }

if (ITEM_SELECTOR == 0) {
    // Row 2: Sanitary & Organizational Cores Display Preview
    translate([-150,    0, 0]) color("SoftSage") Item_Orchid_Caddy();
    translate([   0,    0, 0]) color("WarmDesert") Item_Tulip_Terminal();
    translate([ 150,    0, 0]) color("SoftSage") Item_Succulent_Pod();
}

module Item_Orchid_Caddy() {
    // ITEM 4: THE ORCHID UNDER-SINK CLEANER CADDY (Mechanical T-Slot Integration)
    difference() {
        union() {
            // Primary chemical bottle container block
            cube([BASE_RADIUS*1.6, BASE_RADIUS*1.2, 50.0], center=true);
            // Right Wall Male Interlocking Dovetail Spline
            translate([BASE_RADIUS*0.8, 0, 0])
                rotate([0, 0, 45]) cube([6.0, 6.0, 46.0], center=true);
        }
        translate([-BASE_RADIUS*0.8, 0, 0])
            rotate([0, 0, 45]) cube([6.0 + CLEARANCE_OFFSET, 6.0 + CLEARANCE_OFFSET, 52.0], center=true);
            
        // 4x Spray Bottle Wells with Hard-Coded Mechanical Interlock Channels
        for (x_pock = [-30, 30]) {
            for (y_pock = [-20, 20]) {
                translate([x_pock, y_pock, 4.0]) {
                    cylinder(h=46.0, r=24.0, center=true, $fn=40); // Primary pocket cavity
                    
                    // 3x Vertical Female T-Slot Keyways (+0.15mm Slicer Offset) to entirely bypass overmold peel failures
                    for (slot =) {
                        rotate([0, 0, slot]) translate([24.0, 0, 0]) {
                            cube([2.0, 4.0, 46.0], center=true); // Slot neck
                            translate([1.2, 0, 0]) cube([2.5, 6.3, 46.0], center=true); // Lock head
                        }
                    }
                }
            }
        }
        Universal_Interface_Keyway();
    }
}

module Item_Caddy_Grip_Sleeve() {
    // ITEM 11: INDEPENDENT FLAT-PRINT MALE T-SPLINE GRIP SLEEVE (Soft 85A TPU Liner)
    // Sliced completely flat on Plate 3. Rolled up and slid by hand down the PP slots for a zero-glue lifetime lock.
    union() {
        // Flat flexible wrap sleeve array panel
        translate([0, 0, WALL_THICKNESS*0.5])
            cube([150.0, 42.0, WALL_THICKNESS], center=true);
            
        // 3x Corresponding Male T-Spline Anchors
        for (x_rail = [-50, 0, 50]) {
            translate([x_rail, 0, -1.0]) {
                cube([1.7, 42.0, 2.0], center=true); // Neck spline
                translate([0, 0, -1.0]) cube([2.2, 42.0, 5.8], center=true); // Anchor block head
            }
        }
    }
}

module Item_Tulip_Terminal() {
    // ITEM 5: THE TULIP TOILET PAPER ROLL TERMINAL (Springless Leaf Splines)
    difference() {
        union() {
            // Rear wall base flange mount
            cube([40.0, 40.0, WALL_THICKNESS], center=true);
            // Outward cantilever arm structure
            translate([0, BASE_RADIUS*0.5, 0]) cube([16.0, BASE_RADIUS, 12.0], center=true);
            // 4 Flexible leaf splines forming the self-expanding toilet paper expansion core
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
    // ITEM 6: THE SUCCULENT WALL-MOUNTED STORAGE PODS (Cascading Hex-Cluster Cups)
    difference() {
        union() {
            // Deep hollow succulent leaf cup geometry profile
            scale([1, 1.3, 1]) sphere(r=BASE_RADIUS*0.4, $fn=6);
            // Flat back planar wall interface
            translate([0, -BASE_RADIUS*0.35, 0]) cube([45.0, 4.0, 45.0], center=true);
        }
        scale([0.92, 1.22, 0.92]) sphere(r=BASE_RADIUS*0.4, $fn=6);
        translate([0, 0, BASE_RADIUS*0.4]) cube([100.0, 100.0, BASE_RADIUS*0.4], center=true);
        translate([0, -BASE_RADIUS*0.35, 0]) rotate([0, 0, 30]) Universal_Interface_Keyway();
    }
}
// Matrix Biomimetic Utilities - Floral Home Solutions Master File (Block 3)
// ============================================================================
// ⚙️ MEAL PREP & INTERLOCKING CONNECTOR ENGINE MODULES
// ============================================================================

// Append this routing selector segment to the master preview logic loop:
// else if (ITEM_SELECTOR == 7) { Item_Peony_Prep_Pod(); }
// else if (ITEM_SELECTOR == 8) { Item_Carnation_Snap_Wrap(); }
// else if (ITEM_SELECTOR == 9) { Item_Rose_Thorn_Hook(); }
// else if (ITEM_SELECTOR == 10) { Item_Passion_Flower_Spline(); }

if (ITEM_SELECTOR == 0) {
    // Row 3: Meal Prep Cores & Master Connector Preview
    translate([-150, -150, 0]) color("NaturalBone") Item_Peony_Prep_Pod();
    translate([   0, -150, 0]) color("MatteTerracotta") Item_Carnation_Snap_Wrap();
    translate([ 150, -150, 0]) color("SlateGray") Item_Rose_Thorn_Hook();
    
    translate([   0,    0, -15]) color("Charcoal") Item_Passion_Flower_Spline();
}

module Item_Peony_Prep_Pod() {
    // ITEM 7: THE PEONY MULTI-TIER SCHOOL LUNCH PREP PODS (Nesting Sector Bins)
    difference() {
        // Main external concentric container shell structure
        cylinder(h=45.0, r=BASE_RADIUS*1.1, center=true, $fn=60);
        translate([0, 0, WALL_THICKNESS])
            cylinder(h=45.0, r=BASE_RADIUS*1.1 - WALL_THICKNESS, center=true, $fn=60);
            
        // Cross-Wall Segment Splitters to accept individual closing petal inserts supportless
        cube([BASE_RADIUS*2.3, 1.2, 50.0], center=true);
        cube([1.2, BASE_RADIUS*2.3, 50.0], center=true);
    }
}

module Item_Carnation_Snap_Wrap() {
    // ITEM 8: THE CARNATION DYNAMIC BAG-SEALING SNAP WRAPS (Interlocking Wave Jaws)
    difference() {
        // External solid-state band arm loop structure
        cube([BASE_RADIUS*1.3, 16.0, 8.0], center=true);
        // Integrated central split entry track
        cube([BASE_RADIUS*1.0, 2.0, 12.0], center=true);
        
        // Interlocking Carnation Zig-Zag Wave Teeth cutters
        for (teeth = [-BASE_RADIUS*0.4 : 6.0 : BASE_RADIUS*0.4]) {
            translate([teeth, 0, 0]) rotate([0, 0, 45]) cube([4.0, 4.0, 10.0], center=true);
        }
    }
}

module Item_Rose_Thorn_Hook() {
    // ITEM 9: THE ROSE-THORN MULTI-SURFACE UTILITY HOOKS (High-Load PP-CF Spire)
    difference() {
        union() {
            // Flat back face flange plate
            cube([35.0, 35.0, 4.0], center=true);
            // High-tensile steep downward-angled structural rose thorn hook profile
            hull() {
                translate([0, 6.0, 0]) cube([12.0, 10.0, 12.0], center=true);
                translate([0, 35.0, -25.0]) sphere(r=2.0); // Concentrated hook tip anchor point
            }
        }
        // Back slot cutter to snap lock straight over the global hexagon wall nodes
        Universal_Interface_Keyway();
    }
}

module Item_Passion_Flower_Spline() {
    // ITEM 10: THE PASSION-FLOWER UNIVERSAL INTERFACE NODE (The Symmetrical Master Lock Key)
    // Slipped straight into the back profiles of the entire collection to enable interchangeable alignment
    union() {
        cylinder(h=6.0, r=14.0, center=true, $fn=6); // Center locking turn dial head
        translate([0, 0, 6.0]) cylinder(h=8.0, r=9.5 - CLEARANCE_OFFSET, center=true, $fn=6); // Male anchor spline
    }
}

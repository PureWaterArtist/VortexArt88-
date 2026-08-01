// Matrix Biomimetic Utilities - RC Attachable Upgrade: Polar Bear Sled Ski
// Version 1.0.0-Upgrade Core | All-Terrain Mud & Snow Glide Matrix

SKI_L = 110.0;            // Total front-to-back glide length (mm)
SKI_W = 28.0;             // Total footprint width for weight distribution (mm)
AXLE_DIAMETER = 4.1;      // Precision slip clearance hole for standard 1:16 axle pins (mm)

$fn = 80;

module RC_Polar_Bear_Sled_Ski() {
    difference() {
        union() {
            // 1. MAIN GLIDE PLANK HULL STRUCTURE
            // Features an upward curved front radius tip to slide over deep snow drifts cleanly
            difference() {
                cube([SKI_W, SKI_L, 2.5], center=true);
                
                // Generates the curved front ski tip shovel profile via geometric intersection
                translate([0, SKI_L*0.5, 6.0])
                    rotate([0, 90, 0])
                        cylinder(h=SKI_W+2, r=6.0, center=true);
            }
            
            // Extended Curved Front Tip Shovel Overlay
            translate([0, SKI_L*0.5 - 2.0, 2.0])
                rotate([-35, 0, 0])
                    cube([SKI_W, 12.0, 2.5], center=true);
            
            // 2. CENTRAL HIGH-STIFFNESS MOUNTING HUB BLOCK
            translate([0, 0, 8.0])
                cube([14.0, 16.0, 14.0], center=true);
        }
        
        // 3. STANDARD AXLE HUB CONNECTION SOCKET HOLE
        // Allows the ski to pivot smoothly over bumps while remaining locked onto the suspension hub
        translate([0, 0, 8.0])
            rotate([0, 90, 0])
                cylinder(h=20.0, r=AXLE_DIAMETER/2, center=true);
                
        // 4. BIOMIMETIC UNDERCARRIAGE MESH: PAPILLAE TRACTION BUMPS
        // Alternating micro-dimple clusters mimic polar bear paws to break surface tension and hold line steering
        for (x_bump = [-SKI_W*0.35 : 4.0 : SKI_W*0.35]) {
            for (y_bump = [-SKI_L*0.4 : 6.0 : SKI_L*0.4]) {
                translate([x_bump, y_bump, -1.3])
                    sphere(r=0.6);
            }
        }
    }
}

RC_Polar_Bear_Sled_Ski();

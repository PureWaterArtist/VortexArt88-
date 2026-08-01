// Matrix Biomimetic Utilities - RC Attachable Upgrade: Firefly LED Bumper
// Version 1.0.0-Upgrade Core | Integrated Night Vision Protection Shield

BUMPER_SPAN = 90.0;       // Total frontal wrap-around crash protection width (mm)
LED_SOCKET_R = 2.55;      // Precision clearance pocket for standard 5mm hobby LED bulbs (mm)
CHASSIS_W = 85.0;          // Main vehicle scale footprint match reference

$fn = 60;

module RC_Firefly_LED_Bumper() {
    difference() {
        union() {
            // 1. REINFORCED FRONT EXOSKELETON WING BUMPER (Printed in High-Impact TPU)
            cube([BUMPER_SPAN, 8.0, 16.0], center=true);
            
            // Rearward Mounting Arms (Slid and friction lock flat over the nose)
            for (x_arm = [-CHASSIS_W*0.3, CHASSIS_W*0.3]) {
                translate([x_arm, -12.0, 0])
                    cube([8.0, 16.0, 16.0], center=true);
            }
        }
        
        // 2. BIOMIMETIC LENS APERTURES: FIREFLY LUMINESCENT LIGHT SOCKETS
        // Forward-facing push-fit chambers accept 5mm bulbs tightly with zero screws required
        for (x_led = [-22.0, 22.0]) {
            translate([x_led, 5.0, 0])
                rotate([90, 0, 0]) {
                    cylinder(h=15.0, r=LED_SOCKET_R, center=true); // Main bulb bay
                    translate([0, 0, -6.0])
                        cylinder(h=10.0, r=1.0, center=true); // Wire lead passthrough exit
                }
        }
        
        // 3. INTEGRATED 1MM CONCENTRIC WIRE-ROUTING GUTTER TRACKS
        // Completely isolates and shields incoming electrical lines from debris and tyre strikes
        translate([0, -4.0, -8.1])
            cube([BUMPER_SPAN - 10.0, 1.2, 1.2], center=true);
        for (x_gutter = [-CHASSIS_W*0.3, CHASSIS_W*0.3]) {
            translate([x_gutter, -12.0, -8.1])
                cube([1.2, 16.0, 1.2], center=true);
        }
        
        // Front Face Core Hollowing (Reduces frontal mass overload parameters)
        translate([0, 4.1, 0])
            cube([BUMPER_SPAN - 16.0, 2.0, 12.0], center=true);
    }
}

RC_Firefly_LED_Bumper();

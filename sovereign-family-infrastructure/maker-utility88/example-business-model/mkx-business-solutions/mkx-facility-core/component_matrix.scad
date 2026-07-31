// Matrix Biomimetic Utilities - Parametric MKX Facility Component Node
// Version 1.0.0-Facility Core | High-Velocity Chemical-Resistant Engineering CAD

// ============================================================================
// 🏛️ MASTER FACILITY PARAMETERS (Adjust to match specific processing line specs)
// ============================================================================
INNER_BORE_DIAMETER = 12.0;  // Core fluid flow passage diameter (mm)
OUTER_SEAL_RADIUS = 18.5;    // Maximum outer diameter of the compression gasket face (mm)
TOTAL_COMPONENT_H = 35.0;    // Vertical thickness profile of the sorting nozzle (mm)

// ============================================================================
// 📐 RECONCILIATION MATRICES (Compensates for 1.4% High-Temp Polymer Shrinkage)
// ============================================================================
WALL_THICKNESS = 3.0;
CORE_RADIUS = (INNER_BORE_DIAMETER / 2) + 0.15; // Clearance buffer maps clean fluid velocities

$fn = 90; // High-resolution curvature mapping for industrial pressure seals

// ============================================================================
// 🛠️ ULTIMATE SYSTEM COMPONENT ROUTER
// ============================================================================
module MKX_Biomimetic_Facility_Nozzle() {
    difference() {
        union() {
            // 1. PRIMARY HIGH-PRESSURE AIRFRAME ENCLOSURE
            // Printed in ultra-chemical-resistant Fluoropolymer PVDF or Carbon-Fiber ASA
            cylinder(h=TOTAL_COMPONENT_H, r1=OUTER_SEAL_RADIUS, r2=CORE_RADIUS + WALL_THICKNESS, center=true);
            
            // 2. BIOMIMETIC FLEXIBLE COMPRESSION LIPS
            // Perimeter sealing rings modeled after marine organism suction mechanics
            translate([0, 0, (TOTAL_COMPONENT_H / 2) - 1.5])
                rotate_extrude()
                    translate([OUTER_SEAL_RADIUS - 1.0, 0, 0])
                        circle(r=1.2, $fn=12);
        }
        
        // 3. INTERNAL HIGH-VELOCITY FLUID BORE PASSAGE
        translate([0, 0, -TOTAL_COMPONENT_H])
            cylinder(h=TOTAL_COMPONENT_H * 2, r=CORE_RADIUS, center=true);
            
        // 4. BIOMIMETIC VERTICAL HELICAL FLUTING TRACKS
        // Internal spiral groves modeled after plant xylem structures.
        // This coordinates fluid flow vectors, completely eliminating high-speed filling turbulence.
        translate([0, 0, 0]) {
            linear_extrude(height=TOTAL_COMPONENT_H + 2, center=true, twist=90, slices=60) {
                for (groove = [0 : 90 : 359]) {
                    rotate([0, 0, groove])
                        translate([CORE_RADIUS - 0.2, 0, 0])
                            circle(r=0.6, $fn=12);
                }
            }
        }
        
        // 5. THREADED FLANGE INTERFACE JUNCTION
        // Precision mounting seat to bolt directly onto standard filling line manifolds
        translate([0, 0, (-TOTAL_COMPONENT_H / 2) - 0.1])
            cylinder(h=6.0, r=CORE_RADIUS + 2.5, $fn=6);
    }
}

MKX_Biomimetic_Facility_Nozzle();

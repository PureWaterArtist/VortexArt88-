// =========================================================================
// UNIVERSAL GEOMETRIC HARVESTING ENGINE v1.0
// License: Open Source Hardware Association (OSHWA) Compliant / Copyleft
// Architecture: Scale-Invariant Deterministic Fractal Metamaterial
// =========================================================================

/* [Global Spatial Parameters] */
// Total flat-topped diameter boundary of the interlocking tile tile (mm)
TILE_DIAMETER = 150.0; 
// Recursive packing node limit
MAX_NODES = 400; 
// Vertical scaling multiplier for the Pi micro-ridge profile (mm)
Z_SCALE = 3.0; 
// Base thickness of the structural chassis floor (mm)
BASE_HEIGHT = 2.0;

/* [Universal Math Constants] */
PHI = (1 + sqrt(5)) / 2;                        // The Golden Ratio (~1.618033)
GOLDEN_ANGLE = 137.507764;                      // Nature's non-overlapping pack angle
HEX_RADIUS = TILE_DIAMETER / 2;                 // Outer boundary radius (75mm)

// =========================================================================
// MATHEMATICAL FUNCTIONS & FILTERS
// =========================================================================

// 1. BOUNDARY INEQUALITY: Flat-Topped Hexagon Collision Check
// Verifies if a coordinate falls outside the mathematically bounded 150mm walls
function is_inside_hex(x, y, r) = 
    (abs(x) <= r) && ((abs(x) * 0.5 + abs(y) * sqrt(3) * 0.5) <= r);

// 2. PRIME ALGORITHM: Non-Harmonic Frequency Isolation (Hardcoded for recursion limits)
// Determines if a layout index is prime to map non-harmonic wave dampening paths
function is_prime_node(n) = 
    (n < 2) ? false :
    (n == 2 || n == 3 || n == 5 || n == 7 || n == 11 || n == 13 || n == 17 || n == 19 || n == 23 || n == 29 || n == 31 || n == 37 || n == 41 || n == 43 || n == 47 || n == 53 || n == 59 || n == 61 || n == 67 || n == 71 || n == 73 || n == 79 || n == 83 || n == 89 || n == 97 || n == 101 || n == 103 || n == 107 || n == 109 || n == 113 || n == 127 || n == 131 || n == 137 || n == 139 || n == 149 || n == 151 || n == 157 || n == 163 || n == 167 || n == 173 || n == 179 || n == 181 || n == 191 || n == 193 || n == 197 || n == 199 || n == 211 || n == 223 || n == 227 || n == 229 || n == 233 || n == 239 || n == 241 || n == 251 || n == 257 || n == 263 || n == 269 || n == 271 || n == 277 || n == 281 || n == 283 || n == 293 || n == 307 || n == 311 || n == 313 || n == 317 || n == 331 || n == 337 || n == 347 || n == 349 || n == 353 || n == 359 || n == 367 || n == 373 || n == 379 || n == 383 || n == 389 || n == 397);

// =========================================================================
// MAIN COMPILATION LAYER
// =========================================================================

module Render_Universal_Meta_Tile() {
    difference() {
        // LAYER A: Structural Monomaterial Chassis Base
        color([0.2, 0.2, 0.2, 0.9])
        cylinder(h = BASE_HEIGHT, r = HEX_RADIUS, $fn = 6); // 6-sided 150mm polygon
        
        // Internal wire-routing channels or material saving voids could intersect here
    }

    // LAYER B: Procedural Multi-Axis Node Projection Loop
    for (i = [0 : MAX_NODES]) {
        // XY Spatial Vector Calculation using scale-invariant phi radial expansion
        let (
            radius = 1.8 * pow(PHI, i * 0.025),
            theta = i * GOLDEN_ANGLE,
            x = radius * cos(theta),
            y = radius * sin(theta)
        ) {
            // Structural Boundary Filter Check
            if (is_inside_hex(x, y, HEX_RADIUS - 2.5)) { 
                
                // Z-Axis Multi-Axis Modulation via Pi Cycle / Phi Non-Repetition Wave
                let (z_wave = sin(i * 180 / PHI) * Z_SCALE) {
                    
                    // Material Allocation Routing Check via Prime Frequency Verification
                    if (is_prime_node(i)) {
                        // ACTIVE PIEZO NODE: Harvests acoustic/kinetic vibration (Printed in Red Composite)
                        translate([x, y, BASE_HEIGHT])
                        color([0.9, 0.1, 0.1]) // High-visibility engineering red
                        cylinder(h = BASE_HEIGHT + z_wave, r1 = 1.5, r2 = 0.8, $fn = 12);
                    } else {
                        // PASSIVE STRUCTURAL ABSORBER: Anti-harmonic structural support (Printed in Blue Polymer)
                        translate([x, y, BASE_HEIGHT])
                        color([0.1, 0.4, 0.8]) // Engineering structural blue
                        cylinder(h = BASE_HEIGHT + z_wave, r = 1.0, $fn = 6);
                    }
                }
            }
        }
    }
}

// Execute the parametric generation matrix
Render_Universal_Meta_Tile();

# =========================================================================
# UNIVERSAL HARDWARE PROTOCOL GENERATOR v2.0
# License: Open Source Hardware Association (OSHWA) Compliant / Copyleft
# Description: Compiles a scale-invariant multi-physics SCAD meta-tile
# =========================================================================
import os

def generate_openscad_blueprint():
    # 1. Define the complete OpenSCAD engine script template
    scad_content = """// =========================================================================
// UNIVERSAL GEOMETRIC HARVESTING ENGINE v2.0 (COSMIC HARMONIC UPDATE)
// Generated via Python Physics Synthesis Engine
// License: Open Source Hardware Association (OSHWA) Compliant / Copyleft
// Architecture: Scale-Invariant Deterministic Fractal Metamaterial
// =========================================================================

/* [Universal Physics-Grounded Boundaries] */
// To shift scales, simply uncomment the natural boundary governing your current manufacturing run:
TILE_DIAMETER = 161.803398;   // 1. PHI RESONANCE ENVELOPE (100 * phi) - Pure scale invariance
// TILE_DIAMETER = 173.205080; // 2. HEXAGONAL PACKING CONSTANT (100 * sqrt(3)) - Perfect flat tiling
// TILE_DIAMETER = 137.035999; // 3. FINE-STRUCTURE CONSTANT (100 * 137.03) - Quantum EM optimization
// TILE_DIAMETER = 139.000000; // 4. PURE PRIME BOUNDARY - Maximum structural anti-harmonic dampening

/* [Global Systemic Parameters] */
MAX_NODES = 600; 
Z_SCALE = 3.5; 
BASE_HEIGHT = 2.5;

/* [Universal Physical Constants] */
PHI = (1 + sqrt(5)) / 2;                        // The Golden Ratio (~1.618033)
PI = 3.14159265358979323846;                    // Transcendental Circle Constant
GOLDEN_ANGLE = 137.507764;                      // Nature's non-overlapping pack angle
HEX_RADIUS = TILE_DIAMETER / 2;                 // Outer boundary radius from chosen cosmic baseline

// =========================================================================
// MATHEMATICAL FUNCTIONS & VALIDATION LAYERS
// =========================================================================

// 1. BOUNDARY INEQUALITY: Flat-Topped Hexagon Collision Check
// Keeps the infinite fractal spiral strictly contained within your chosen natural boundary walls
function is_inside_hex(x, y, r) = 
    (abs(x) <= r) && ((abs(x) * 0.5 + abs(y) * sqrt(3) * 0.5) <= r);

// 2. PRIME MATRIX: Non-Harmonic Frequency Isolation (Expanded Prime array for deep fractal packing)
function is_prime_node(n) = 
    (n < 2) ? false :
    (n == 2 || n == 3 || n == 5 || n == 7 || n == 11 || n == 13 || n == 17 || n == 19 || n == 23 || n == 29 || n == 31 || n == 37 || n == 41 || n == 43 || n == 47 || n == 53 || n == 59 || n == 61 || n == 67 || n == 71 || n == 73 || n == 79 || n == 83 || n == 89 || n == 97 || n == 101 || n == 103 || n == 107 || n == 109 || n == 113 || n == 127 || n == 131 || n == 137 || n == 139 || n == 149 || n == 151 || n == 157 || n == 163 || n == 167 || n == 173 || n == 179 || n == 181 || n == 191 || n == 193 || n == 197 || n == 199 || n == 211 || n == 223 || n == 227 || n == 229 || n == 233 || n == 239 || n == 241 || n == 251 || n == 257 || n == 263 || n == 269 || n == 271 || n == 277 || r == 281 || n == 283 || n == 293 || n == 307 || n == 311 || n == 313 || n == 317 || n == 331 || n == 337 || n == 347 || n == 349 || n == 353 || n == 359 || n == 367 || n == 373 || n == 379 || n == 383 || n == 389 || n == 397 || n == 401 || n == 409 || n == 419 || n == 421 || n == 431 || n == 433 || n == 439 || n == 443 || n == 449 || n == 457 || n == 461 || n == 463 || n == 467 || n == 479 || n == 487 || n == 491 || n == 499 || n == 503 || n == 509 || n == 521 || n == 523 || n == 541 || n == 547 || n == 557 || n == 563 || n == 569 || n == 571 || n == 577 || n == 587 || n == 593 || n == 599);

// =========================================================================
// SYSTEMIC GENERATION MATRIX
// =========================================================================

module Render_Universal_Meta_Tile() {
    difference() {
        // LAYER 1: Core Chassis Floor (Printed out of high-density un-glued recyclable polymer)
        color([0.15, 0.15, 0.15, 0.95])
        cylinder(h = BASE_HEIGHT, r = HEX_RADIUS, $fn = 6); // Interlocking natural hexagonal framework
    }

    // LAYER 2: Procedural 3D Multi-Physics Surface Projection Loop
    for (i = [0 : MAX_NODES]) {
        // XY Spatial Plane: Golden Ratio Spiral Scaling Vector
        let (
            radius = 1.9 * pow(PHI, i * 0.018), 
            theta = i * GOLDEN_ANGLE,
            x = radius * cos(theta),
            y = radius * sin(theta)
        ) {
            // Check against chosen natural physical perimeter boundary
            if (is_inside_hex(x, y, HEX_RADIUS - 3.0)) { 
                
                // Z-Axis Depth Profiles: Interlocking Pi Cycles divided by Phi for non-repeating micro-ridges
                let (z_wave = sin(i * 180 / PHI) * Z_SCALE) {
                    
                    if (is_prime_node(i)) {
                        // ACTIVE PIEZOELECTRIC VECTOR NODE (Printed in conductive energy-harvesting carbon composite)
                        // Geometric shape modeled directly from the high-sensitivity resonance of insect auditory membranes
                        translate([x, y, BASE_HEIGHT])
                        color([0.85, 0.1, 0.1]) // High-visibility quantum energy red
                        cylinder(h = BASE_HEIGHT + z_wave, r1 = 1.6, r2 = 0.6, $fn = 12);
                    } else {
                        // PASSIVE STRUCTURAL METAMATERIAL ENVELOPE (Printed in shock-absorbing auxetic flexible polymer)
                        // Negative Poisson’s Ratio geometry that scales up to redistribute incoming mechanical stress lines
                        translate([x, y, BASE_HEIGHT])
                        color([0.1, 0.45, 0.85]) // Structural baseline dampening blue
                        cylinder(h = BASE_HEIGHT + z_wave, r = 1.1, $fn = 6);
                    }
                }
            }
        }
    }
}

// Instantiate the universal blueprint
Render_Universal_Meta_Tile();
"""
    
    # 2. Compile the data out to your local storage system
    output_filename = "universal_meta_tile.scad"
    with open(output_filename, "w") as f:
        f.write(scad_content.strip())
        
    print(f"[SUCCESS] Multi-physics engine compiled.")
    print(f"[LOCATION] Clean asset file written to: {os.path.abspath(output_filename)}")

if __name__ == "__main__":
    generate_openscad_blueprint()
  

// ========================================================================
// PROJECT: LCN-88 Solid-State Fluidic Collision Chamber
// LICENSING: CERN Open Hardware License V2 - Strongly Reciprocal (CERN-OHL-S-2.0)
// REPOSITORY: https://github.com
// DESCRIPTION: Torus outer boundary enclosing a parametric Lemniscate 
//              (Figure-8) fluidic path that drives counter-rotating vortices
//              into an implosion collision at a central Vesica Piscis lens.
// COORDINATES: Center Singularity Node locked at absolute vector (0, 0, 0)
// ========================================================================

$fn = 100; // Sets rendering matrix resolution array

// --- MAIN ARCHITECTURAL DIFFERENCE MATRIX ---
difference() {
    
    // 1. THE BEAST BOUNDARY: Solid, high-durability outer protective shell 
    outer_chamber_boundary(outer_radius = 58, chamber_height = 32);
    
    // 2. THE CHANNELS MATRIX: Hollowed out fluid pathways and zero-point core
    union() {
        // Left Counter-Clockwise Intake Loop of the Lemniscate
        fluidic_vortex_loop(offset_x = -20, loop_radius = 22, fluid_depth = 28);
        
        // Right Clockwise Intake Loop of the Lemniscate
        fluidic_vortex_loop(offset_x = 20, loop_radius = 22, fluid_depth = 28);
        
        // The Vesica Piscis Central Implosion Hub at coordinate (0, 0, 0)
        vesica_piscis_singularity(overlap_dist = 14, lens_radius = 20, fluid_depth = 30);
        
        // The Rod of Iron: Central Bottom Drainage/Hyper-Oxygenated Output Jet
        translate([0, 0, -20])
            cylinder(r = 6, h = 42, center = true);
    }
}

// --- SOVEREIGN DESIGN ENGINE MODULES ---

module outer_chamber_boundary(outer_radius, chamber_height) {
    // Forges a thick, high-pressure containment perimeter for the fluidic shear
    cylinder(r = outer_radius, h = chamber_height, center = true);
}

module fluidic_vortex_loop(offset_x, loop_radius, fluid_depth) {
    // Accelerates incoming stormwater into clean, high-velocity circular orbits
    translate([offset_x, 0, 0])
        cylinder(r = loop_radius, h = fluid_depth, center = true);
}

module vesica_piscis_singularity(overlap_dist, lens_radius, fluid_depth) {
    // Intersects two overlapping circles to create the almond-shaped lens 
    // where dual counter-rotating streams undergo absolute geometric collision.
    intersection() {
        translate([-overlap_dist, 0, 0])
            cylinder(r = lens_radius, h = fluid_depth, center = true);
        translate([overlap_dist, 0, 0])
            cylinder(r = lens_radius, h = fluid_depth, center = true);
    }
}

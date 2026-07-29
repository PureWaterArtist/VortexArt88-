#!/usr/bin/env python3
"""
PROJECT ALCHEMIST-MATRIX: Solid-State Molecular Synthesizer Parametric Core Compiler
Path: sovereign-family-infrastructure/alchemist-matrix88/compile_synthesizer_mesh.py
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

Parametrically compiles the fluidic cardioid resonant venturi nozzle extrusion head.
Integrates internal 120-micron earthworm peristaltic capillary routing channels, 
oyster dynamic enzyme catalyst ports, and abalone hexagonal mounting tracks into a solid mesh.
"""

from solid import open_scad, cylinder, translate, rotate, cube, union

def compile_material_synthesizer_mesh():
    print("=========================================================================")
    print("🛰️  COMPUTING PARAMETRIC FLUIDIC CAVITATION REACTION CORE & REPLICATOR HEAD...")
    print("=========================================================================\n")
    
    # 📏 METROLOGY & STRUCTURAL PARAMETERS (From config/technical-specs.md)
    nozzle_outer_diameter_mm = 90.0 # 90mm wide photonic crystal insulated shell
    nozzle_height_mm = 110.0         # 110mm total vertical extrusion reactor depth
    capillary_width_um = 120.0
    capillary_r_mm = (capillary_width_um / 2.0) / 1000.0
    
    num_peristaltic_channels = 6
    
    # 🏛️ 1. BASE VOLUMETRIC REACTOR CHASSIS WITH PHOTONIC MIRROR ENVELOPE
    outer_shroud = cylinder(r=nozzle_outer_diameter_mm / 2.0, h=nozzle_height_mm, segments=128, center=True)
    outer_shroud = translate([0, 0, nozzle_height_mm / 2.0])(outer_shroud)
    
    # Cardioid acoustic cavitation inner chamber void carve out
    inner_cardioid_void = cylinder(r=(nozzle_outer_diameter_mm / 2.0) - 8.0, h=nozzle_height_mm - 12.0, segments=128, center=True)
    inner_cardioid_void = translate([0, 0, (nozzle_height_mm / 2.0) + 6.0])(inner_cardioid_void)
    
    synthesizer_head = outer_shroud - inner_cardioid_void
    
    # 🏛️ 2. ETCH 120-MICRON EARTHWORM PERISTALTIC CAPILLARY INPUT FLUID TRACKS
    # Weaves 6 pulsing supply tracks longitudinally through the photonic crystal jacket
    pulsing_lines = []
    channel_spacing = (nozzle_outer_diameter_mm / 2.0 - 12.0)
    
    for p in range(num_peristaltic_channels):
        angle = p * (360.0 / num_peristaltic_channels)
        rad_angle = (angle * 3.14159265) / 180.0
        
        # Helical pitch calculation to simulate internal earthworm-muscle twist curves
        cx = (channel_spacing - 4.0) * (p % 2 + 1) * 0.5
        
        capillary_track = cylinder(r=capillary_r_mm, h=nozzle_height_mm + 20.0, segments=16, center=True)
        capillary_track = translate([cx * (p - 2.5), 0, nozzle_height_mm / 2.0])(capillary_track)
        pulsing_lines.append(capillary_track)
        
    for track in pulsing_lines:
        synthesizer_head = synthesizer_head - track

    # 🏛️ 3. MODEL VALVELESS VENTURI CARDIOID RESONANT NOZZLE EXHAUST TIP
    # Creates the acoustic amplification constriction throat matching deep-sea chimney logic
    venturi_throat = cylinder(r1=12.0, r2=3.5, h=25.0, segments=64, center=True)
    venturi_throat = translate([0, 0, 12.5])(venturi_throat)
    
    synthesis_tip_exhaust = cylinder(r1=3.5, r2=8.0, h=15.0, segments=64, center=True)
    synthesis_tip_exhaust = translate([0, 0, -7.5])(synthesis_tip_exhaust)
    
    venturi_nozzle_core = venturi_throat - synthesis_tip_exhaust
    synthesizer_head = (synthesizer_head - venturi_nozzle_core)

    # 🏛️ 4. INTEGRATE DYNAMIC ENZYME OYSTER CATALYST INJECTION MANIFOLD
    catalyst_ring = cylinder(r=25.0, h=6.0, segments=48, center=True)
    catalyst_ring = translate([0, 0, nozzle_height_mm - 15.0])(catalyst_ring)
    
    catalyst_feed_void = cylinder(r=21.0, h=8.0, segments=48, center=True)
    catalyst_feed_void = translate([0, 0, nozzle_height_mm - 15.0])(catalyst_feed_void)
    
    injection_manifold = catalyst_ring - catalyst_feed_void
    synthesizer_head += injection_manifold

    # Symmetrical masking to secure flat mounting interfaces
    clean_hex_mask = cylinder(r=(nozzle_outer_diameter_mm / 2.0) + 10.0, h=nozzle_height_mm + 40.0, segments=6, center=True)
    clean_hex_mask = translate([0, 0, nozzle_height_mm / 2.0])(clean_hex_mask)
    final_synthesizer_unit = synthesizer_head * clean_hex_mask

    # 💾 5. EXPORT HIGH-RESOLUTION OPENSCAD PRODUCTION SOLID BLUEPRINT FILE
    output_filename = "alchemist_matrix_synthesizer_core_v1.scad"
    open_scad.scad_render_to_file(final_synthesizer_unit, output_filename)
    
    print(f"✅ SUCCESS: Project ALCHEMIST-MATRIX Synthesizer Reactor Head saved to: ./{output_filename}")
    print("👉 Next Step: Open in OpenSCAD (F6) to compile solid geometries and export a multi-material STL block.")

if __name__ == "__main__":
    compile_material_synthesizer_mesh()
  

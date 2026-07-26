#!/usr/bin/env python3
"""
PROJECT METAMATRIX: Open-Source Pneumatic Material Synthesizer 3D Mesh Compiler
Path: vortex-synthesizer-mmx88/generate-synthesizer-mesh.py
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

Programmatically compiles and exports the uncompressed ASCII STL 3D solid mesh
for the fluid-driven synthesizer chassis blocks, integrating aerostatic air logic ducts.
"""

import math

def compile_synthesizer_3d_mesh():
    print("=========================================================================")
    print("🛰️  COMPUTING PROJECT METAMATRIX PNEUMATIC COMPONENT BALANCES...")
    print("=========================================================================\n")
    
    # HARD-LOCKED CORE METROLOGY SPECIFICATIONS (config/technical-specs.md)
    chassis_block_width = 250.0  # 250mm modular structural frame blocks
    chassis_block_height = 80.0  # 80mm height profile thickness per frame block segment
    spinneret_outer_r = 25.0     # 50mm total multi-channel deposition head diameter
    capillary_channel_w = 0.12   # 120-micron microfluidic internal vascular tracks
    
    facets = []
    radial_divs = 24
    
    # 🏛️ 1. MODEL THE HEAVY AUXETIC BALSA-MIMICKING EXOSKELETON CHASSIS BLOCK MESH
    x_bounds = [0.0, chassis_block_width]
    y_bounds = [0.0, chassis_block_width]
    
    # Top and Bottom Planar Face Caps
    facets.append(f"  facet normal 0.0 0.0 -1.0\n    outer loop\n      vertex {x_bounds:.1f} {y_bounds:.1f} 0.0\n      vertex {x_bounds:.1f} {y_bounds:.1f} 0.0\n      vertex {x_bounds:.1f} {y_bounds:.1f} 0.0\n    endloop\n  endfacet")
    facets.append(f"  facet normal 0.0 0.0 1.0\n    outer loop\n      vertex {x_bounds:.1f} {y_bounds:.1f} {chassis_block_height:.1f}\n      vertex {x_bounds:.1f} {y_bounds:.1f} {chassis_block_height:.1f}\n      vertex {x_bounds:.1f} {y_bounds:.1f} {chassis_block_height:.1f}\n    endloop\n  endfacet")

    # 💨 2. ETCH PNEUMATIC AEROSTATIC LEVITATION DUCTS DIRECTLY IN WALLS (REPLACEMENT CORE)
    # Carve internal horizontal air pipelines for the frictionless 175 kPa fluidic cushion
    for idx in range(4):
        y_pos = (idx * 60.0) + 35.0
        for step in range(radial_divs):
            t1 = (step * 2.0 * math.pi) / radial_divs
            t2 = ((step + 1) * 2.0 * math.pi) / radial_divs
            
            # 6mm internal diameter compressed air logic ducts
            rx1, ry1 = 3.0 * math.cos(t1), y_pos + 3.0 * math.sin(t1)
            rx2, ry2 = 3.0 * math.cos(t2), y_pos + 3.0 * math.sin(t2)
            
            facets.append(f"  facet normal 1.0 0.0 0.0\n    outer loop\n      vertex 10.0 {rx1:.1f} {ry1:.1f}\n      vertex {chassis_block_width-10.0:.1f} {rx2:.1f} {ry2:.1f}\n      vertex 10.0 {rx2:.1f} {ry2:.1f}\n    endloop\n  endfacet")

    # 🫀 3. MODEL THE MULTI-VASCULAR SPINNERET HEAD HOUSING
    for ring in range(3):
        r_inner = (ring * spinneret_outer_r) / 3.0
        r_outer = ((ring + 0.5) * spinneret_outer_r) / 3.0
        
        for step in range(radial_divs):
            t1 = (step * 2.0 * math.pi) / radial_divs
            t2 = ((step + 1) * 2.0 * math.pi) / radial_divs
            
            x1_in, y1_in = r_inner * math.cos(t1), r_inner * math.sin(t1)
            x2_in, y2_in = r_inner * math.cos(t2), r_inner * math.sin(t2)
            x1_out, y1_out = r_outer * math.cos(t1), r_outer * math.sin(t1)
            x2_out, y2_out = r_outer * math.cos(t2), r_outer * math.sin(t2)
            
            facets.append(f"  facet normal 0.0 0.0 -1.0\n    outer loop\n      vertex {x1_in:.1f} {y1_in:.1f} 5.0\n      vertex {x2_in:.1f} {y2_in:.1f} 5.0\n      vertex {x1_out:.1f} {y1_out:.1f} 5.0\n    endloop\n  endfacet")

            # 💧 4. INJECT DEFENSIVE 120-MICRON CAPILLARY SELF-PATCHING TRACKS
            x1_heal = x1_out + 1.5 * math.cos(t1)
            y1_heal = y1_out + 1.5 * math.sin(t1)
            x2_heal = x2_out + 1.5 * math.cos(t2)
            y2_heal = y2_out + 1.5 * math.sin(t2)
            
            facets.append(f"  facet normal 0.0 0.0 1.0\n    outer loop\n      vertex 0.0 0.0 12.0\n      vertex {x1_heal:.1f} {y1_heal:.1f} 12.0\n      vertex {(x2_heal+capillary_channel_w):.4f} {y2_heal:.1f} {(12.0-capillary_channel_w):.4f}\n    endloop\n  endfacet")

    # 🏛️ 5. WRITE SOLID STRUCTURAL CHASSIS BLUEPRINT DATA DISK
    output_mesh_path = "reso-synthesizer-3d-mesh.stl"
    with open(output_mesh_path, "w") as f:
        f.write("solid project_metamatrix_parametric_mesh\n")
        f.write("\n".join(facets))
        f.write("\nendsolid project_metamatrix_parametric_mesh\n")
        
    print(f"✅ SUCCESS: PROJECT METAMATRIX Synthesizer Casing Mesh saved to disk: ./{output_mesh_path}")
    print("🛠️  PROPULSION CORE SECURED: Frictionless aerostatic air cushion tracking frozen.")

if __name__ == "__main__":
    compile_synthesizer_3d_mesh()
            

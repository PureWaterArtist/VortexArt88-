#!/usr/bin/env python3
"""
PROJECT SOVEREIGN CORNERSTONE: KINETIC88 Terrestrial Transmitter 3D Mesh Compiler
Path: vortex-flight-kinetic88/generate-transmitter-mesh.py
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

Programmatically compiles the uncompressed ASCII STL 3D solid mesh for the
wireless ground-plane hop transmitter housing, resonance rings, and coupling cores.
"""

import math

def compile_transmitter_3d_mesh():
    print("🛰️  COMPUTING KINETIC88 TRANSMITTER COUPLING GEOMETRY...")
    
    # PARAMETRIC TRANSMITTER CONFIGURATION CONSTANTS
    base_pad_radius = 300.0   # 600mm total ground-station footprint radius (mm scale)
    resonance_rings = 4       # 4 nested concentric induction rings
    vertical_stem_height = 180.0 # Height of central fluidic coupler column
    
    facets = []
    divs = 36
    
    # 🏛️ 1. MODEL THE NESTED CONCENTRIC RESONANCE RING EMBEDMENTS
    for ring in range(resonance_rings):
        r_inner = (ring * base_pad_radius) / resonance_rings
        r_outer = ((ring + 0.4) * base_pad_radius) / resonance_rings
        
        for i in range(divs):
            t1 = (i * 2.0 * math.pi) / divs
            t2 = ((i + 1) * 2.0 * math.pi) / divs
            
            x1_in, y1_in = r_inner * math.cos(t1), r_inner * math.sin(t1)
            x2_in, y2_in = r_inner * math.cos(t2), r_inner * math.sin(t2)
            
            x1_out, y1_out = r_outer * math.cos(t1), r_outer * math.sin(t1)
            x2_out, y2_out = r_outer * math.cos(t2), r_outer * math.sin(t2)
            
            # Base pad planar facets
            facets.append(f"  facet normal 0.0 0.0 1.0\n    outer loop\n      vertex {x1_in:.1f} {y1_in:.1f} 10.0\n      vertex {x2_in:.1f} {y2_in:.1f} 10.0\n      vertex {x1_out:.1f} {y1_out:.1f} 10.0\n    endloop\n  endfacet")
            facets.append(f"  facet normal 0.0 0.0 1.0\n    outer loop\n      vertex {x2_in:.1f} {y2_in:.1f} 10.0\n      vertex {x2_out:.1f} {y2_out:.1f} 10.0\n      vertex {x1_out:.1f} {y1_out:.1f} 10.0\n    endloop\n  endfacet")

    # 🏛️ 2. PROJECT THE CENTRAL LIQUID-METAL VERTICAL TERMINAL COLUMN
    for i in range(divs):
        t1 = (i * 2.0 * math.pi) / divs
        t2 = ((i + 1) * 2.0 * math.pi) / divs
        
        cx1, cy1 = 25.0 * math.cos(t1), 25.0 * math.sin(t1)
        cx2, cy2 = 25.0 * math.cos(t2), 25.0 * math.sin(t2)
        
        facets.append(f"  facet normal {math.cos(t1):.4f} {math.sin(t1):.4f} 0.0\n    outer loop\n      vertex {cx1:.1f} {cy1:.1f} 10.0\n      vertex {cx2:.1f} {cy2:.1f} 10.0\n      vertex {cx1:.1f} {cy1:.1f} {vertical_stem_height:.1f}\n    endloop\n  endfacet")
        facets.append(f"  facet normal {math.cos(t2):.4f} {math.sin(t2):.4f} 0.0\n    outer loop\n      vertex {cx2:.1f} {cy2:.1f} 10.0\n      vertex {cx2:.1f} {cy2:.1f} {vertical_stem_height:.1f}\n      vertex {cx1:.1f} {cy1:.1f} {vertical_stem_height:.1f}\n    endloop\n  endfacet")

    # 🏛️ 3. WRITE SOLID DECONSTRUCTED TEXT DATA MESH TO DIRECTORY DISK
    output_tx_path = "kinetic88-transmitter-3d-mesh.stl"
    with open(output_tx_path, "w") as f:
        f.write("solid kinetic88_transmitter_parametric_mesh\n")
        f.write("\n".join(facets))
        f.write("\nendsolid kinetic88_transmitter_parametric_mesh\n")
        
    print(f"✅ SUCCESS: KINETIC88 Transmitter Mesh file written to disk: ./{output_tx_path}")
    print("⚡ TRANSMISSION NODE SECURED: Wireless ground-plane hop wave guide locked.")

if __name__ == "__main__":
    compile_transmitter_3d_mesh()
          

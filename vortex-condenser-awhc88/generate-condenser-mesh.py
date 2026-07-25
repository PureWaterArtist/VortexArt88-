#!/usr/bin/env python3
"""
PROJECT SOVEREIGN CORNERSTONE: AWHC-88 Vortex Condenser 3D Mesh Compiler
Path: vortex-condenser-awhc88/generate-condenser-mesh.py
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

Programmatically compiles the uncompressed ASCII STL 3D solid mesh for the
solid-state atmospheric water condenser, cardioid gateways, and micro-venturi ports.
"""

import math

def compile_condenser_3d_mesh():
    print("🛰️  COMPUTING AWHC-88 VORTEX CONDENSER SOLID GEOMETRY...")
    
    # PARAMETRIC CONDENSER CORE DIMENSIONS
    housing_radius = 180.0    # 180mm outer manifold shell radius
    condenser_height = 450.0  # Overall vertical profile casing depth
    venturi_ratio = 4.0       # 4:1 cross-sectional pressure drop drop index
    
    facets = []
    divs = 36
    
    # 🏛️ 1. GENERATE THE EXTERIOR CARDIOID CONDENSATION CASING
    for i in range(divs):
        w1 = (i * 2.0 * math.pi) / divs
        w2 = ((i + 1) * 2.0 * math.pi) / divs
        
        # Calculate cardioid shell curve boundaries
        rc1 = housing_radius * (1.0 - math.sin(w1))
        rc2 = housing_radius * (1.0 - math.sin(w2))
        
        x1_b, y1_b = rc1 * math.cos(w1), rc1 * math.sin(w1)
        x2_b, y2_b = rc2 * math.cos(w2), rc2 * math.sin(w2)
        
        x1_t, y1_t = (rc1 / venturi_ratio) * math.cos(w1), (rc1 / venturi_ratio) * math.sin(w1)
        x2_t, y2_t = (rc2 / venturi_ratio) * math.cos(w2), (rc2 / venturi_ratio) * math.sin(w2)
        
        facets.append(f"  facet normal 1.0 0.0 0.0\n    outer loop\n      vertex {x1_b:.1f} {y1_b:.1f} 0.0\n      vertex {x2_b:.1f} {y2_b:.1f} 0.0\n      vertex {x1_t:.1f} {y1_t:.1f} {condenser_height:.1f}\n    endloop\n  endfacet")
        facets.append(f"  facet normal 1.0 0.0 0.0\n    outer loop\n      vertex {x2_b:.1f} {y2_b:.1f} 0.0\n      vertex {x2_t:.1f} {y2_t:.1f} {condenser_height:.1f}\n      vertex {x1_t:.1f} {y1_t:.1f} {condenser_height:.1f}\n    endloop\n  endfacet")

    # 💧 2. ETCH THE INTEGRATED LIQUID RECOVERY CHANNELS
    for step in range(15):
        z_lip = (step * 25.0) + 20.0
        for s in range(divs // 2):
            v1 = (s * 2.0 * math.pi) / (divs // 2)
            v2 = ((s + 1) * 2.0 * math.pi) / (divs // 2)
            lx1, ly1 = 15.0 * math.cos(v1), 15.0 * math.sin(v1)
            lx2, ly2 = 15.0 * math.cos(v2), 15.0 * math.sin(v2)
            
            facets.append(f"  facet normal 0.0 0.0 -1.0\n    outer loop\n      vertex 0.0 0.0 {z_lip:.1f}\n      vertex {lx1:.1f} {ly1:.1f} {z_lip:.1f}\n      vertex {lx2:.1f} {ly2:.1f} {(z_lip - 5.0):.1f}\n    endloop\n  endfacet")

    # 🏛️ 3. COMPILE ASSEMBLY AND WRITE FILE TO DISK
    output_condenser_path = "awhc88-condenser-3d-mesh.stl"
    with open(output_condenser_path, "w") as f:
        f.write("solid awhc88_condenser_parametric_mesh\n")
        f.write("\n".join(facets))
        f.write("\nendsolid awhc88_condenser_parametric_mesh\n")
        
    print(f"✅ SUCCESS: AWHC-88 Condenser Mesh generated at path: ./{output_condenser_path}")
    print("💧 MOISTURE EXTRACTION SECURED: Pure fluidic condense tracking lines frozen.")

if __name__ == "__main__":
    compile_condenser_3d_mesh()
  

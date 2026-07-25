#!/usr/bin/env python3
"""
PROJECT SOVEREIGN CORNERSTONE: ARMD-88 Vortex Recycler 3D Mesh Compiler
Path: vortex-recycler-armd88/generate-recycler-mesh.py
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

Programmatically compiles the uncompressed ASCII STL 3D solid mesh for the
solid-state material disintegrator, steam nozzle arrays, and classifier funnels.
"""

import math

def compile_recycler_3d_mesh():
    print("🛰️  COMPUTING ARMD-88 RECIPROCAL DISINTEGRATOR HOUSING GEOMETRY...")
    
    # PARMAMETRIC MATERIAL CLASSIFIER FIELDS
    chamber_max_radius = 320.0 # 320mm main vortex shearing barrel radius
    cyclone_height = 650.0     # Total vertical particle separation drop
    nozzle_ports_count = 6     # 6 supersonic steam injection slits
    
    facets = []
    divs = 48
    
    # 🏛️ 1. SOLVE THE INVERTED CONICAL SEPARATION BARREL MESH
    for i in range(divs):
        theta1 = (i * 2.0 * math.pi) / divs
        theta2 = ((i + 1) * 2.0 * math.pi) / divs
        
        # Top intake lip circumference
        x1_top, y1_top = chamber_max_radius * math.cos(theta1), chamber_max_radius * math.sin(theta1)
        x2_top, y2_top = chamber_max_radius * math.cos(theta2), chamber_max_radius * math.sin(theta2)
        
        # Bottom sorting exit aperture (Drastically narrowed to force cyclone separation)
        x1_bot, y1_bot = 40.0 * math.cos(theta1), 40.0 * math.sin(theta1)
        x2_bot, y2_bot = 40.0 * math.cos(theta2), 40.0 * math.sin(theta2)
        
        facets.append(f"  facet normal 1.0 0.0 0.0\n    outer loop\n      vertex {x1_bot:.1f} {y1_bot:.1f} 0.0\n      vertex {x2_bot:.1f} {y2_bot:.1f} 0.0\n      vertex {x1_top:.1f} {y1_top:.1f} {cyclone_height:.1f}\n    endloop\n  endfacet")
        facets.append(f"  facet normal 1.0 0.0 0.0\n    outer loop\n      vertex {x2_bot:.1f} {y2_bot:.1f} 0.0\n      vertex {x2_top:.1f} {y2_top:.1f} {cyclone_height:.1f}\n      vertex {x1_top:.1f} {y1_top:.1f} {cyclone_height:.1f}\n    endloop\n  endfacet")

    # 🏭 2. PROJECT THE 6 TANGENTIAL SUPERSONIC STEAM INJECTION PORTS
    for n in range(nozzle_ports_count):
        n_angle = (n * 2.0 * math.pi) / nozzle_ports_count
        nx = (chamber_max_radius - 20.0) * math.cos(n_angle)
        ny = (chamber_max_radius - 20.0) * math.sin(n_angle)
        
        for p in range(12):
            p1 = (p * 2.0 * math.pi) / 12
            p2 = ((p + 1) * 2.0 * math.pi) / 12
            px1, py1 = nx + 10.0 * math.cos(p1), ny + 10.0 * math.sin(p1)
            px2, py2 = nx + 10.0 * math.cos(p2), ny + 10.0 * math.sin(p2)
            
            facets.append(f"  facet normal 0.0 1.0 0.0\n    outer loop\n      vertex {nx:.1f} {by:.1f} {cyclone_height-50.0:.1f}\n      vertex {px1:.1f} {py1:.1f} {cyclone_height-10.0:.1f}\n      vertex {px2:.1f} {py2:.1f} {cyclone_height-10.0:.1f}\n    endloop\n  endfacet")

    # 🏛️ 3. WRITE SHREDDER ASSEMBLY CODE STRAIGHT TO WORKBENCH DISK
    output_recycler_path = "armd88-recycler-3d-mesh.stl"
    with open(output_recycler_path, "w") as f:
        f.write("solid armd88_recycler_parametric_mesh\n")
        f.write("\n".join(facets))
        f.write("\nendsolid armd88_recycler_parametric_mesh\n")
        
    print(f"✅ SUCCESS: ARMD-88 Recycling Classifier Mesh safely saved: ./{output_recycler_path}")
    print("♻️ MATERIAL DISINTEGRATOR SECURED: Bladeless sonic shredding geometry locked.")

if __name__ == "__main__":
    compile_recycler_3d_mesh()
  

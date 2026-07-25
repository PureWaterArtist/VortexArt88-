#!/usr/bin/env python3
"""
PROJECT RESO-ARMOR: 100mm Benchtop Self-Healing Test Coupon 3D Mesh Compiler
Path: vortex-armor-resilient88/modules/testing-coupon/generate-coupon-mesh.py
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

Programmatically compiles and exports the uncompressed ASCII STL 3D solid mesh
for the scaled-down 100mm x 100mm x 8.0mm benchtop armor test coupon tile.
"""

import math

def compile_coupon_3d_mesh():
    print("🛰️  COMPUTING RESO-ARMOR 100mm BENCHTOP TEST COUON CAD TOPOLOGY...")
    
    # HARD-LOCKED PARAMETRIC SPECS (modules/testing-coupon/config/coupon-bom.json)
    coupon_length_x = 100.0    # 100mm compact test block length
    coupon_width_y = 100.0     # 100mm compact test block width
    coupon_thickness_z = 8.0   # 8mm ultra-thin single layer depth
    interlock_height = 1.5    # 1.5mm sinusoidal lock-wave amplitude
    capillary_port_dia = 0.12 # 120-micron micro-capillary tracking lines
    
    facets = []
    cell_divs = 16
    cells_count = 2           # Scaled-down 2x2 auxetic experiment grid layout
    divisions_xy = 16         # Surface grid calculation resolution
    
    # 🏛️ 1. GENERATE THE TOP FACE SINUSOIDAL INTERLOCKING RIDGE WAVES
    for i in range(divisions_xy):
        x1 = (i * coupon_length_x) / divisions_xy
        x2 = ((i + 1) * coupon_length_x) / divisions_xy
        for j in range(divisions_xy):
            y1 = (j * coupon_width_y) / divisions_xy
            y2 = ((j + 1) * coupon_width_y) / divisions_xy
            
            # Symmetrical scale-invariant surface lock-wave functions
            z1_top = coupon_thickness_z + interlock_height * math.sin((x1 * math.pi) / 25.0) * math.cos((y1 * math.pi) / 25.0)
            z2_top = coupon_thickness_z + interlock_height * math.sin((x2 * math.pi) / 25.0) * math.cos((y2 * math.pi) / 25.0)
            z3_top = coupon_thickness_z + interlock_height * math.sin((x1 * math.pi) / 25.0) * math.cos((y2 * math.pi) / 25.0)
            
            facets.append(f"  facet normal 0.0 0.0 1.0\n    outer loop\n      vertex {x1:.1f} {y1:.1f} {z1_top:.4f}\n      vertex {x2:.1f} {y2:.1f} {z2_top:.4f}\n      vertex {x1:.1f} {y2:.1f} {z3_top:.4f}\n    endloop\n  endfacet")

    # 🏛️ 2. GENERATE THE BOTTOM FACE INVERTED GROOVE MATRICES
    for i in range(divisions_xy):
        x1 = (i * coupon_length_x) / divisions_xy
        x2 = ((i + 1) * coupon_length_x) / divisions_xy
        for j in range(divisions_xy):
            y1 = (j * coupon_width_y) / divisions_xy
            y2 = ((j + 1) * coupon_width_y) / divisions_xy
            
            z1_bot = 0.0 + interlock_height * math.sin((x1 * math.pi) / 25.0) * math.cos((y1 * math.pi) / 25.0)
            z2_bot = 0.0 + interlock_height * math.sin((x2 * math.pi) / 25.0) * math.cos((y2 * math.pi) / 25.0)
            z3_bot = 0.0 + interlock_height * math.sin((x1 * math.pi) / 25.0) * math.cos((y2 * math.pi) / 25.0)
            
            facets.append(f"  facet normal 0.0 0.0 -1.0\n    outer loop\n      vertex {x1:.1f} {y1:.1f} {z1_bot:.4f}\n      vertex {x2:.1f} {y2:.1f} {z2_bot:.4f}\n      vertex {x1:.1f} {y2:.1f} {z3_bot:.4f}\n    endloop\n  endfacet")

    # 🔄 3. ETCH THE COMPACT 2X2 AUXETIC STAR CORE & CENTRAL INJECTION VALVE
    for cx_idx in range(cells_count):
        cx_center = (cx_idx * (coupon_length_x / cells_count)) + (coupon_length_x / (cells_count * 2.0))
        for cy_idx in range(cells_count):
            cy_center = (cy_idx * (coupon_width_y / cells_count)) + (coupon_width_y / (cells_count * 2.0))
            
            for s in range(cell_divs):
                p1 = (s * 2.0 * math.pi) / cell_divs
                p2 = ((s + 1) * 2.0 * math.pi) / cell_divs
                
                # Outer perimeter auxetic lattice struts coordinates mapping
                r_aux = 12.0 * (1.0 - 0.25 * math.cos(p1 * 4))
                x1, y1 = cx_center + r_aux * math.cos(p1), cy_center + r_aux * math.sin(p1)
                x2, y2 = cx_center + r_aux * math.cos(p2), cy_center + r_aux * math.sin(p2)
                
                facets.append(f"  facet normal 1.0 0.0 0.0\n    outer loop\n      vertex {x1:.1f} {y1:.1f} 1.0\n      vertex {x2:.1f} {y2:.1f} 1.0\n      vertex {x1:.1f} {y1:.1f} {coupon_thickness_z-1.0:.1f}\n    endloop\n  endfacet")

    # 📥 4. EMBED CENTER TRACK LUER-LOCK SYRINGE INTERFACE VALVE NODE
    # Generates a solid 3D funnel cavity at the absolute origin center (50.0, 50.0)
    for s in range(cell_divs):
        v1 = (s * 2.0 * math.pi) / cell_divs
        v2 = ((s + 1) * 2.0 * math.pi) / cell_divs
        vx1, vy1 = 50.0 + 3.0 * math.cos(v1), 50.0 + 3.0 * math.sin(v1)
        vx2, vy2 = 50.0 + 3.0 * math.cos(v2), 50.0 + 3.0 * math.sin(v2)
        
        facets.append(f"  facet normal 0.0 0.0 -1.0\n    outer loop\n      vertex 50.0 50.0 1.0\n      vertex {vx1:.1f} {vy1:.1f} {coupon_thickness_z-1.0:.1f}\n      vertex {vx2:.1f} {vy2:.1f} {coupon_thickness_z-1.0:.1f}\n    endloop\n  endfacet")

    # 🏛 =====================================================================
    output_coupon_path = "modules/testing-coupon/reso-armor-coupon-mesh.stl"
    # Fallback to local save layer if folder routing is run outside the workspace root
    if not os.path.exists("modules/testing-coupon/"):
        output_coupon_path = "reso-armor-coupon-mesh.stl"
        
    with open(output_coupon_path, "w") as f:
        f.write("solid reso_armor_coupon_mesh\n")
        f.write("\n".join(facets))
        f.write("\nendsolid reso_armor_coupon_mesh\n")
        
    print(f"✅ SUCCESS: Machine-readable 100mm Test Coupon 3D STL file safely compiled: ./{output_coupon_path}")

if __name__ == "__main__":
    compile_coupon_3d_mesh()
          

# Comprehensive Guide: Compiling and Preparing the Solid Vox-Vortex Funnel for 3D Printing

This document contains all the necessary code, dependencies, and software instructions required to convert the parametric script into a solid, watertight STL model ready for any 3D printer slicer.

---

## Part 1: Prerequisites & Environment Setup

The corrected design utilizes the open-source **SolidPython** library to construct solid, manifold geometries via OpenSCAD instead of raw 2D triangle facets. 

Before running the compiler script, install the required library using your terminal or command prompt:

```bash
pip install solidpython
```

You will also need to download and install the free geometry rendering engine:
* **OpenSCAD:** Download from [openscad.org](https://openscad.org)

---

## Part 2: The Solid Geometry Python Script

Save the following complete Python code exactly as `generate_solid_vortex.py`. 

```python
#!/usr/bin/env python3
"""
PROJECT VOX-VORTEX: Solid Parametric Atmospheric Condenser Compiler
Path: vortex-condenser-vox88/generate_solid_vortex.py
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

Programmatically compiles and exports a solid, watertight OpenSCAD geometry 
for the 320mm vortex core funnel, enforcing a structural 3mm print wall thickness.
"""

from solid import open_scad, cone, cylinder, translate
import os

def compile_solid_condenser():
    print("=========================================================================")
    print("🛰️  COMPUTING SOLID VOX-VORTEX ATMOSPHERIC SYNTHESIZER...")
    print("=========================================================================\n")
    
    # HARD-LOCKED METROLOGY CONSTANTS
    cone_length_z = 320.0       # 320mm primary vortex expansion cylinder length
    max_radius_r = 22.5         # 45mm maximum base diameter intake entry
    cold_orifice_r = 3.25       # 6.5mm cold core axis drop line orifice
    wall_thickness = 3.0        # 3mm physical solid wall thickness for physical printing
    
    # 🏛️ 1. GENERATE THE SOLID OUTER HULL
    # Constructs an external solid cone offset by the structural print wall thickness
    outer_cone = cone(
        r1=max_radius_r + wall_thickness, 
        r2=cold_orifice_r + wall_thickness, 
        h=cone_length_z,
        segments=72  # High radial coordinate resolution for smooth fluid dynamics
    )
    
    # 🏛️ 2. GENERATE THE INNER VOID (THE FLOW CORRIDOR)
    # Establishes the exact interior air pathway parameters
    inner_void = cone(
        r1=max_radius_r, 
        r2=cold_orifice_r, 
        h=cone_length_z + 0.2,  # Over-extended slightly to ensure a perfectly clean manifold cut
        segments=72
    )
    
    # Shift void downward slightly along Z-axis to cleanly pass through hull limits
    inner_void = translate([0, 0, -0.1])(inner_void)
    
    # 🏛️ 3. CONSTRUCT THE WATERTIGHT MANIFOLD (BOOLEAN DIFFERENCE)
    # Subtracts the inner volume from the outer volume to create an airtight shell
    solid_vortex_funnel = outer_cone - inner_void
    
    # 💾 4. EXPORT AIRTIGHT PARAMETRIC GEOMETRY
    output_scad_name = "solid_vortex_condenser.scad"
    open_scad.scad_render_to_file(solid_vortex_funnel, output_scad_name)
    
    print(f"✅ SUCCESS: Solid OpenSCAD script saved to: ./{output_scad_name}")
    print("👉 Next Step: Open this file in OpenSCAD, render (F6), and export to STL (F7).")

if __name__ == "__main__":
    compile_solid_condenser()
```

---

## Part 3: Step-by-Step Production Workflow

Follow these steps in sequence to generate, process, and print the resulting design:

### Step 1: Run the Script
1. Open your terminal or command prompt.
2. Navigate to the folder where you saved the script (e.g., `cd Downloads`).
3. Execute the compiler:
   ```bash
   python generate_solid_vortex.py
   ```
4. Confirm that a file named `solid_vortex_condenser.scad` has been generated in that directory.

### Step 2: Compile to STL via OpenSCAD
1. Launch the **OpenSCAD** software interface.
2. Click **File -> Open** and select `solid_vortex_condenser.scad`.
3. Press **F6** on your keyboard (or click *Design -> Render*). Wait for the computational rendering to complete.
4. Press **F7** on your keyboard (or click *File -> Export as STL...*). Save the output file as `vox_vortex.stl`.

### Step 3: Slicing Configurations for Production
Import the `vox_vortex.stl` file into your preferred slicing program (e.g., PrusaSlicer, Bambu Studio, or Cura) and apply the following parameters to ensure structural resilience and water security:

* **Material Select:** Use **PETG** or **ASA**. Avoid standard PLA, which degrades when exposed to moisture and UV environments.
* **Wall Loops / Perimeters:** Increase this value to a minimum of **4 to 6 loops**. This forces the printer to build the shell out of solid concentric lines, rendering it completely watertight without relying on internal infill patterns.
* **Infill Density:** Set to **20% to 30%** using a strong structural pattern like **Gyroid** to support the 3mm wall separation.
* **Layer Height:** Use **0.2mm** for an optimal balance between smooth interior fluid flow curves and physical structural print time.
* **Orientation:** Position the model completely flat and upright on its widest base. This layout eliminates the need for complex, messy internal breakaway supports.
* 

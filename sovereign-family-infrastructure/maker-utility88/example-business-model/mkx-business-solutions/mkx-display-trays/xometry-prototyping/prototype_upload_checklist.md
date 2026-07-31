# 🗺️ Industrial Prototype Order & Mesh Export Guide
**System Posture:** Physical Manufacturing File Dispatch Protocol
**Target Platforms:** Xometry / Protolabs / Hubs On-Demand Portals
**Output Materials:** Matte Black ASA (Chassis) & Premium Color PMMA/PETG (Badge)

To secure absolute geometric perfection when ordering your physical sample display tray from a commercial manufacturing bureau, follow this exact step-by-step file generation and portal configuration routine. 

Commercial vendors cannot execute raw OpenSCAD (.scad) code. They require standard 3D mesh boundary files (.stl or .3mf) and will utilize their own proprietary, highly calibrated industrial slicing parameters based on the checkboxes you select on their website.

---

## 🖥️ STEP 1: EXPORT THE SEPARATE COMPONENT MESHES FROM OPENSCAD

Because your flagship prototype utilizes a multi-piece assembly to avoid mid-print material change bottlenecks, you must compile and export the chassis and the branding logo as two distinct mesh files.

### A. Exporting the Primary Chassis Base
1. Open `display_tray.scad` inside your OpenSCAD editing workspace.
2. Locate the control variable on line 22: `PART_SELECTOR = 0;`.
3. Change the variable parameter to: `PART_SELECTOR = 1;` to isolate the cored tray base.
4. Press **F6** on your keyboard to compile the 3D polygonal geometry.
5. Go to the top navigation header: **File ──► Export as STL** (or Export as 3MF).
6. Save the file inside your local directory under the exact filename: `mkx_chassis_base.stl`.

### B. Exporting the Branded Logo Faceplate
1. Return to line 22 of the script editor.
2. Change the variable parameter to: `PART_SELECTOR = 2;` to isolate the embossed corporate badge.
3. Press **F6** on your keyboard to compile the high-fidelity lettering paths.
4. Go to the top navigation header: **File ──► Export as STL** (or Export as 3MF).
5. Save this second file inside your local directory under the exact filename: `mkx_branding_badge.stl`.
6. Reset line 22 back to `PART_SELECTOR = 0;` to restore the master workspace preview assembly.

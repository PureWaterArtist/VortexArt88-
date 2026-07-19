# Project ARMW-Wings Parametric Schematics & Structural Lift Frame Index

This directory houses the foundational parametric three-dimensional solid engine code for the **Morphing Aero-Resonator Wing Structure (Module: suit-wings)**. It serves as the mathematical blueprint layer responsible for turning programmatic variable constraints into watertight, machine-sliceable CAD geometry.

---

## 📂 Internal Directory Manifest

*   **`README.md`:** This file (Schematics Directory Blueprint Index).
*   **`wing-joints.scad`:** Parametric OpenSCAD 3D solid model folding wing-joint script file mapping the central spine root block, morphing rib hinges, and slotted vortextips.

---

## 🛠 CAD Compilation & Rendering Directives

To compile and inspect the 3D morphing wing spars and multi-segmented folding joint assemblies without relying on restrictive, closed-source CAD packages, adhere to the following workflow:

*   **Compiler Medium:** Download and execute the open-source solid modeler **OpenSCAD** (Version 2021.01 or later).
*   **Asset Ingestion:** Load `wing-joints.scad` directly into the compiler dashboard workspace.
*   **Resolution Tuning:** The rendering variable `$fn` pre-set to `120` ensures ultra-smooth arc interpolation for the curved aerodynamic wing ribs and slotted tip segments. For quick rendering drafts, you may adjust this locally to `30`.
*   **Export Pipeline:** Execute a complete mathematical render (`F6`), followed by an STL export (`F7`) to generate the polygon mesh required by your slicer software.

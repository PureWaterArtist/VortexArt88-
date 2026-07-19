# Project ARMW-Arms Parametric Schematics & Limb Frame Index

This directory houses the foundational parametric three-dimensional solid engine code for the **Wearable Arm Flight Chassis (Module: suit-arms)**. It serves as the mathematical blueprint layer responsible for turning programmatic variable constraints into watertight, machine-sliceable CAD geometry.

---

## 📂 Internal Directory Manifest

*   **`README.md`:** This file (Schematics Directory Blueprint Index).
*   **`arm-sleeves.scad`:** Parametric OpenSCAD 3D solid model arm sleeve engine file mapping bicep cuffs, forearm slider rails, and flexible elbow wells.

---

## 🛠 CAD Compilation & Rendering Directives

To compile and inspect the 3D arm framework without relying on restrictive, closed-source CAD packages, adhere to the following workflow:

*   **Compiler Medium:** Download and execute the open-source solid modeler **OpenSCAD** (Version 2021.01 or later).
*   **Asset Ingestion:** Load `arm-sleeves.scad` directly into the compiler dashboard workspace.
*   **Resolution Tuning:** The rendering variable `$fn` pre-set to `120` ensures smooth arc interpolation for the circular sleeve cuffs. For quick rendering drafts, you may adjust this locally to `30`.
*   **Export Pipeline:** Execute a complete mathematical render (`F6`), followed by an STL export (`F7`) to generate the polygon mesh required by your slicer software.

# Project ARMW-Helmet Parametric Schematics & Head Shield Index

This directory houses the foundational parametric three-dimensional solid engine code for the **Wearable Head Flight Chassis (Module: suit-head)**. It serves as the mathematical blueprint layer responsible for turning programmatic variable constraints into watertight, machine-sliceable CAD geometry.

---

## 📂 Internal Directory Manifest

*   **`README.md`:** This file (Schematics Directory Blueprint Index).
*   **`head-chassis.scad`:** Parametric OpenSCAD 3D solid model engine file mapping the clamshell core, visor well, and camouflage skin.

---

## 🛠 CAD Compilation & Rendering Directives

To compile and inspect the 3D helmet framework without relying on restrictive, closed-source CAD packages, adhere to the following workflow:

*   **Compiler Medium:** Download and execute the open-source solid modeler **OpenSCAD** (Version 2021.01 or later).
*   **Asset Ingestion:** Load `head-chassis.scad` directly into the compiler dashboard workspace.
*   **Resolution Tuning:** The rendering variable `$fn` is pre-set to `120` to ensure ultra-smooth arc interpolation for the curved cranial surfaces. For quick rendering drafts, you may adjust this locally to `30`.
*   **Export Pipeline:** Execute a complete mathematical render (`F6`), followed by an STL export (`F7`) to generate the polygon mesh required by your slicer software.

# Project ARMW-Legs Parametric Schematics & Exoskeleton Frame Index

This directory houses the foundational parametric three-dimensional solid engine code for the **Wearable Leg & Landing Gear Chassis (Module: suit-legs)**. It serves as the mathematical blueprint layer responsible for turning programmatic variable constraints into watertight, machine-sliceable CAD geometry.

---

## 📂 Internal Directory Manifest

*   **`README.md`:** This file (Schematics Directory Blueprint Index).
*   **`leg-exoskeleton.scad`:** Parametric OpenSCAD 3D solid model leg chassis engine file mapping thigh guards, shin sleeves, ankle collars, and high-elasticity leaf springs.

---

## 🛠 CAD Compilation & Rendering Directives

To compile and inspect the 3D leg framework and kinetic landing loops without relying on restrictive, closed-source CAD packages, adhere to the following workflow:

*   **Compiler Medium:** Download and execute the open-source solid modeler **OpenSCAD** (Version 2021.01 or later).
*   **Asset Ingestion:** Load `leg-exoskeleton.scad` directly into the compiler dashboard workspace.
*   **Resolution Tuning:** The rendering variable `$fn` pre-set to `120` ensures ultra-smooth arc interpolation for the curved kangaroo-tendon leaf loops and limb collars. For quick rendering drafts, you may adjust this locally to `30`.
*   **Export Pipeline:** Execute a complete mathematical render (`F6`), followed by an STL export (`F7`) to generate the polygon mesh required by your slicer software.

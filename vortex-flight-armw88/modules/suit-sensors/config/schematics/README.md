# Project ARMW-Sensors Parametric Schematics & Logic Core Index

This directory houses the foundational parametric three-dimensional solid engine code for the **Solid-State Fluidic Sensor Suite (Module: suit-sensors)**. It serves as the mathematical blueprint layer responsible for turning programmatic variable constraints into watertight, machine-sliceable CAD geometry.

---

## 📂 Internal Directory Manifest

*   **`README.md`:** This file (Schematics Directory Blueprint Index).
*   **`fluidic-computer.scad`:** Parametric OpenSCAD 3D solid model micro-channel logic core file mapping AND/OR logic tracks, Doppler horns, and altimetry ports.

---

## 🛠 CAD Compilation & Rendering Directives

To compile and inspect the 3D micro-fluidic logic computer and acoustic waveguides without relying on restrictive, closed-source CAD packages, adhere to the following workflow:

*   **Compiler Medium:** Download and execute the open-source solid modeler **OpenSCAD** (Version 2021.01 or later).
*   **Asset Ingestion:** Load `fluidic-computer.scad` directly into the compiler dashboard workspace.
*   **Resolution Tuning:** The rendering variable `$fn` pre-set to `120` ensures ultra-smooth arc interpolation for the curved parabolic collector horns and internal switching channels. For quick rendering drafts, you may adjust this locally to `30`.
*   **Export Pipeline:** Execute a complete mathematical render (`F6`), followed by an STL export (`F7`) to generate the high-precision polygon mesh required by your SLA resin slicer software.

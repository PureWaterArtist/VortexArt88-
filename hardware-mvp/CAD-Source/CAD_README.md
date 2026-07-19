# 📐 CAD Source Assets & Printing Rules

This directory houses the foundational solid-state geometries required to manufacture the physical framework for the `Hardware-MVP` testing loop. 

## 📦 Directory Contents
1. `Schauberger_Imploder_Funnel_Optimized.stl` — Binary mesh file for the golden-ratio Clockwise nozzle flow.
2. `Figure8_Chamber_Reference_Layout.step` — Parametric solid body layout mapping the exact geometric collision coordinates.

## 🖨️ Master Slicer Settings for Hydrodynamic Integrity
To prevent high water pressure from leaking through internal layer lines or causing structural delamination, use these parameters:

*   **Material:** PETG or Tough Resin (**Strictly Avoid PLA** for extended wet runs; it absorbs moisture and degrades).
*   **Perimeters / Wall Loops:** 5 Layers Minimum.
*   **Infill Density:** 45% to 50% Gyroid. (Provides isotropic rigidity against back-pressure).
*   **Layer Height:** 0.16mm - 0.20mm (Finer layers ensure smooth rendering of the internal $\Phi$ spiral).

## 🪞 The Mirror Maneuver (Generating the Twin)
*   **Nozzle A (Clockwise):** Import the `.stl` file and slice directly.
*   **Nozzle B (Counter-Clockwise):** Import a second copy of the `.stl` file into your slicer, right-click, select the **Mirror** tool, and flip the model strictly along the **X-Axis**. Print this mirrored file.
*   

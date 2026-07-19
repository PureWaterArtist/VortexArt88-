# Project ARMW-Legs Configuration Matrix & Metrology Schema Index

This directory serves as the centralized configuration registry and hardware parameter repository for the **Wearable Leg & Landing Gear Chassis (Module: suit-legs)**. It acts as the digital data vault bridging physical cleanroom part procurement, machine slicing metadata, and parametric 3D CAD engine generation.

---

## 📂 Internal Directory Manifest

*   **`README.md`:** This file (Configuration Directory Blueprint Index).
*   **`hardware-bom.json`:** Machine-readable metrology properties, spring-rate limits, and lander constants.
*   **`HARDWARE_BOM.md`:** Human-readable workbench procurement ledger manual for raw composite stocks and high-elasticity leaf structures.
*   **`CLEANROOM_OPS.md`:** Cleanroom post-processing, drop-tower verification, and kinetic loop calibration QA protocols.
*   **`schematics/`:** Subdirectory housing the 3D parametric CAD solid rendering engine.

---

## 📊 Structural Schema Architecture & Interlink Map

To maintain strict scale-invariant data parity across the lander chassis matrix, the files within this block are bound by a rigid, cross-referenced validation chain:

    [ hardware-bom.json ]  ──► (Feeds Attributes) ──►  [ schematics/leg-exoskeleton.scad ]
             │                                                  │
     (Enforces Schema)                                  (Generates Geometry)
             ▼                                                  ▼
     [ HARDWARE_BOM.md ]   ──► (Governs Testing)  ──►  [ CLEANROOM_OPS.md ]
     

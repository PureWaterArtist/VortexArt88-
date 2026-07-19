# Project ARMW-Sensors Configuration Matrix & Metrology Schema Index

This directory serves as the centralized configuration registry and hardware parameter repository for the **Solid-State Fluidic Sensor Suite (Module: suit-sensors)**. It acts as the digital data vault bridging physical cleanroom part procurement, machine slicing metadata, and parametric 3D CAD engine generation.

---

## 📂 Internal Directory Manifest

*   **`README.md`:** This file (Configuration Directory Blueprint Index).
*   **`hardware-bom.json`:** Machine-readable metrology properties, threat detection acoustic tolerances, and ground altimetry metrics.
*   **`HARDWARE_BOM.md`:** Human-readable workbench procurement ledger manual for raw photopolymers and acoustic waveguide horns.
*   **`CLEANROOM_OPS.md`:** Cleanroom post-processing, micro-channel vacuum testing, and tactical threat gate calibration QA protocols.
*   **`schematics/`:** Subdirectory housing the 3D parametric CAD solid rendering engine.

---

## 📊 Structural Schema Architecture & Interlink Map

To maintain strict scale-invariant data parity across the fluid logic matrix, the files within this block are bound by a rigid, cross-referenced validation chain:

    [ hardware-bom.json ]  ──► (Feeds Attributes) ──►  [ schematics/fluidic-computer.scad ]
             │                                                  │
     (Enforces Schema)                                  (Generates Geometry)
             ▼                                                  ▼
     [ HARDWARE_BOM.md ]   ──► (Governs Testing)  ──►  [ CLEANROOM_OPS.md ]
     

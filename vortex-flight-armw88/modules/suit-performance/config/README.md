# Project ARMW-Performance Configuration Matrix & Metrology Schema Index

This directory serves as the centralized configuration registry and hardware parameter repository for the **Aerodynamic Performance Vectors Module (Module: suit-performance)**. It acts as the digital data vault bridging fluid-dynamic calculations, wind-tunnel validation, and automated machine telemetry parameters.

---

## 📂 Internal Directory Manifest

*   **`README.md`:** This file (Configuration Directory Blueprint Index).
*   **`hardware-bom.json`:** Machine-readable metrology properties, aerodynamic lift slopes, and velocity constants.
*   **`CLEANROOM_OPS.md`:** Cleanroom post-processing, wind-tunnel validation protocols, and pitot-tube velocity calibration QA logs.

---

## 📊 Structural Schema Architecture & Interlink Map

To maintain strict scale-invariant data parity across the aerodynamic flight matrix, the files within this block are bound by a rigid, cross-referenced validation chain:

    [ hardware-bom.json ]  ──► (Feeds Attributes) ──►  [ armw88-flight-twin.py ]
             │                                                  │
     (Enforces Schema)                                  (Validates Curves)
             ▼                                                  ▼
     [ FLIGHT_ENVELOPE.md ]──► (Governs Testing)  ──►  [ CLEANROOM_OPS.md ]
     

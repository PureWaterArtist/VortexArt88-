# Project ARMW-Master Configuration Matrix & Full-Armor Schema Index

This directory serves as the centralized configuration registry and hardware parameter repository for the **Master Suit Integration & Full Armor Architecture (Module: suit-master)**. It acts as the digital data vault bridging physical cleanroom multi-module assembly, global parameter scaling, and structural system-wide validation.

---

## 📂 Internal Directory Manifest

*   **`README.md`:** This file (Configuration Directory Blueprint Index).
*   **`hardware-bom.json`:** Machine-readable global control properties card, system-wide G-damping limits, and full armor node maps.
*   **`HARDWARE_BOM.md`:** Human-readable master procurement ledger manual covering raw stocks, hydrogels, and full-suite COTS hardware parts.
*   **`CLEANROOM_OPS.md`:** Full-suit post-processing, system-wide Faraday cage grounding continuity loops, and multi-module pressure calibration QA protocols.
*   **`resodynamic-patches.md`:** [ADDED] Engineering parameters governing Coandă thrust multipliers, pulsed shield oscillators, and wing boundary-layer vacuum suction loops.

---

## 📊 Structural Schema Architecture & Interlink Map

To maintain strict scale-invariant data parity across the entire integrated flight suit, the files within this block enforce a global cross-referenced validation chain:

                     [ config/hardware-bom.json ] (Global Parameter Control)
                                   │
              ┌────────────────────┴────────────────────┐
              ▼                                         ▼
 [ config/HARDWARE_BOM.md ] (Sourcing)     [ config/CLEANROOM_OPS.md ] (Verification)
              │                                         │
              └────────────────────┬────────────────────┘
                                   ▼
                   [ modules/suit-X/config/hardware-bom.json ]
                    (Enforces Sub-Module Parameter Symmetry)
                    

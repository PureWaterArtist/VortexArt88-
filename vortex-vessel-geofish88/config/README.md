# Project GEO-FISH-v88: Global Configuration Registry & Master Schema Index

This directory serves as the centralized root configuration registry and master parameter vault for the **Project GEO-FISH-v88 Ultra-Compact Origami Vessel Platform**. It establishes the cross-referenced schema validations bridging your human-readable markdown guides, CNC machine-readable tool paths, and the automated calculations running inside the python digital twin.

---

## 📂 Internal Directory Manifest

*   **`README.md`:** This file (Global Configuration Directory Blueprint Index Manual).
*   **`global-vessel-card.json`:** Machine-readable global parameter card detailing hull dimensions, material densities, and maximum buoyant capacity limits.

---

## 📊 Structural Schema Architecture & Interlink Map

To prevent parameter drift and guarantee absolute data parity across all localized sub-modules, the data schemas within this directory are bound by a rigid, cross-referenced validation chain:

    [ global-vessel-card.json ]  ──► (Feeds Constants) ──►  [ geofish88-geometry-twin.py ]
               │                                                      │
       (Enforces Schema)                                      (Validates Draft)
               ▼                                                      ▼
       [ Root README.md ]        ──► (Governs Testing)  ──►  [ Module Checklists ]
       

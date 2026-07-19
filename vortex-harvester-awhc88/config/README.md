# Project AWHC-88 Configuration Matrix & Metrology Schema Index

This directory serves as the centralized configuration registry and hardware parameter repository for the **Atmospheric Water Harvester Condenser (Project AWHC-88)**. It acts as the digital data vault bridging physical cleanroom part procurement, machine slicing metadata, and parametric 3D CAD engine generation.

---

## 📂 Internal Directory Manifest

```
vortex-harvester-awhc88/config/
├── README.md                 # This file (Configuration Directory Blueprint Index)
├── hardware-bom.json         # Machine-readable metrology properties and print variables
├── HARDWARE_BOM.md           # Human-readable workbench procurement ledger manual
├── CLEANROOM_OPS.md          # Cleanroom post-processing and moisture validation protocols
└── schematics/
    └── harvest-core.scad     # Parametric OpenSCAD 3D solid fluid engine file
```

## 📊 Structural Schema Architecture & Interlink Map

To maintain strict scale-invariant data parity across the entire ecosystem, the files within this matrix are bound by a rigid, cross-referenced validation chain:

    [ hardware-bom.json ]  ──► (Feeds Attributes) ──►  [ harvest-core.scad ]
             │                                                  │
     (Enforces Schema)                                  (Generates Geometry)
             ▼                                                  ▼
     [ HARDWARE_BOM.md ]   ──► (Governs Testing)  ──►  [ CLEANROOM_OPS.md ]

1.  **Metrology Control Center (`hardware-bom.json`):** Holds the raw numerical variables (such as tolerances, cardioid angles, and infill parameters). This JSON structure can be fed directly into custom Python testing environments or distributed ledgers to automate quality audits.

2.  **Physical Acquisition Ledger (`HARDWARE_BOM.md`):** Translates the raw numeric keys from the JSON card into standard commercial terms and dimensions for field mechanics sourcing raw polymer mass or copper-mesh cores.

3.  **Parametric 3D Solid Engine (`schematics/harvest-core.scad`):** Dynamically scales the 3D water extraction housing geometry based on the data variables declared in the JSON hardware card, preventing human layout errors during file conversions.

4.  **Verification Protocol Manual (`CLEANROOM_OPS.md`):** Outlines the strict hydrostatic validation procedures to confirm the printed condenser matches the target metrology bounds under continuous intake pressures.
5.  

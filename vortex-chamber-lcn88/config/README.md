# Project LCN-88 Configuration Matrix & Metrology Schema Index

This directory serves as the centralized configuration registry and hardware parameter repository for the **Lemniscate Collision Node (Project LCN-88)**. 
It acts as the digital data vault bridging physical cleanroom part procurement, machine slicing metadata, and parametric 3D CAD engine generation.

---

## 📂 Internal Directory Manifest

vortex-chamber-lcn88/config/
├── README.md                 # This file (Configuration Directory Blueprint Index)
├── hardware-bom.json         # Machine-readable metrology properties and print variables
├── HARDWARE_BOM.md           # Human-readable workbench procurement ledger manual
├── CLEANROOM_OPS.md          # Cleanroom post-processing and bench validation protocols
└── schematics/
    └── chamber-profile.scad  # Parametric OpenSCAD 3D solid fluid engine file

## 📊 Structural Schema Architecture & Interlink Map

To maintain strict scale-invariant data parity across the entire ecosystem, the files within this matrix are bound by a rigid, cross-referenced validation chain:

    [ hardware-bom.json ]  ──► (Feeds Attributes) ──►  [ chamber-profile.scad ]
             │                                                  │
     (Enforces Schema)                                  (Generates Geometry)
             ▼                                                  ▼
     [ HARDWARE_BOM.md ]   ──► (Governs Testing)  ──►  [ CLEANROOM_OPS.md ]
     

1.  **Metrology Control Center (`hardware-bom.json`):** Holds the raw numerical variables (such as tolerances, radiuses, and infill parameters). This JSON structure can be fed directly into custom Python testing environments or distributed ledgers to automate quality audits.
2.  2.  **Physical Acquisition Ledger (`HARDWARE_BOM.md`):** Translates the raw numeric keys from the JSON card into standard commercial terms and dimensions for field mechanics sourcing raw polymer mass or clamping fittings.

3.  **Parametric 3D Solid Engine (`schematics/chamber-profile.scad`):** Dynamically scales the 3D fluidic chamber geometry based on the data variables declared in the JSON hardware card, preventing human layout errors during file conversions.

4.  **Verification Protocol Manual (`CLEANROOM_OPS.md`):** Outlines the strict hydrostatic validation procedures to confirm the printed object matches the target metrology bounds under continuous pump pressures.

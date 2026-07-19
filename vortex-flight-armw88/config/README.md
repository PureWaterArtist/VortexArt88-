# Project ARMW-88 Configuration Matrix & Metrology Schema Index

This directory serves as the centralized configuration registry and hardware parameter repository for the **Morphing Aero-Resonator Wing Matrix (Project ARMW-88)**. It acts as the digital data vault bridging physical cleanroom part procurement, machine slicing metadata, and parametric 3D CAD engine generation.

---

## 📂 Internal Directory Manifest

```
vortex-flight-armw88/config/
├── README.md                 # This file (Configuration Directory Blueprint Index)
├── hardware-bom.json         # Machine-readable metrology properties and print variables
├── HARDWARE_BOM.md           # Human-readable workbench procurement ledger manual
├── CLEANROOM_OPS.md          # Life-critical post-processing and impact validation protocols
└── schematics/
    └── wing-core.scad        # Parametric OpenSCAD 3D solid airfoil framework file
```

## 📊 Structural Schema Architecture & Interlink Map

To maintain strict scale-invariant data parity across the entire ecosystem, the files within this matrix are bound by a rigid, cross-referenced validation chain:

    [ hardware-bom.json ]  ──► (Feeds Attributes) ──►  [ schematics/wing-core.scad ]
             │                                                  │
     (Enforces Schema)                                  (Generates Geometry)
             ▼                                                  ▼
     [ HARDWARE_BOM.md ]   ──► (Governs Testing)  ──►  [ CLEANROOM_OPS.md ]

1.  **Metrology Control Center (`hardware-bom.json`):** Holds the life-critical raw numerical variables (such as wingspan targets, chord lengths, denticle heights, and fluidic trace widths). This JSON structure can be fed directly into custom Python testing environments or distributed ledgers to automate quality audits.

2.  **Physical Acquisition Ledger (`HARDWARE_BOM.md`):** Translates the raw numeric keys from the JSON card into standard commercial terms and elements for field mechanics sourcing aerospace-grade polycarbonate composites or raw Kevlar canvases.

3.  **Parametric 3D Solid Engine (`schematics/wing-core.scad`):** Dynamically scales the 3D morphing airfoil skeleton, sliding forearm rails, and outer skin boundaries based on the data variables declared in the JSON hardware card, preventing human layout errors during file conversions.

4.  **Verification Protocol Manual (`CLEANROOM_OPS.md`):** Outlines the strict life-critical validation procedures to confirm the printed frame and flexible skin assemblies match target metrology bounds under continuous structural flight loads and vertical impact testing loops.

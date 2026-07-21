# Project GEO-FISH-v88: Hydrodynamic Analytics & Displacement Curves (Module: hull-hydro)

## 🌊 System Manifest & Hydrostatic Equilibrium Philosophy

The **Hydrodynamic Analytics & Displacement Curves Module (Project GEO-FISH-Hydro)** houses the fluid-dynamic coefficients, volumetric buoyancy curves, and skin friction drag parameters for the fully extended watercraft hull. Because this origami chassis uses a rigid flat-panel configuration, it avoids the fluid plowing or flexing typical of inflatable rafts. Instead, it maintains a precision **V-Chassis Surface Profile** [v1].

When the hull transitions to its 100% open state, the integrated valley folds lock at exact angles to form continuous under-hull water channels. These channels act as **Shallow Tracking Chines** [v1] that trap and direct the water column beneath the boat, ensuring tracking stability in crosswinds and minimizing parasitic wetted surface drag ($C_d$). This database certifies that under a full combined cargo load of $115.0\text{ kg}$, the hull displaces water predictably, preserving a safe gunwale freeboard clearance line well above hazardous swamping boundaries.

---

## 🗂 Sub-Module Symmetrical Directory Map

vortex-vessel-geofish88/modules/hull-hydro/
├── README.md                 # This file (Hydrodynamics Module Index Manual)
├── media/                    # Local folder holding fluid vector layouts
│   ├── README.md             # Local media directory reference index manual
│   └── geofish88-hydro-stability.svg # Native vector blueprint drawing of waterline fluid planes
└── config/
    ├── README.md             # Symmetrical configuration directory reference index
    ├── hardware-bom.json     # Machine-readable drag coefficients, block factors, and trim limits
    └── DISPLACEMENT_LOGS.md  # Human-readable buoyancy curves and waterline draft metrics
    

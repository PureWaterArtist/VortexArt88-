# Project ARMA-88 Parametric Schematics & Acoustic Framework Index

This directory houses the foundational parametric three-dimensional solid engine code for the **Biomimetic Acoustic Resonator Array (Project ARMA-88)** chassis and inner logic core. It serves as the mathematical blueprint layer responsible for turning programmatic variable constraints into watertight, machine-sliceable CAD geometry.

---

## 📂 Internal Directory Manifest

```
vortex-audio-arma88/config/schematics/
├── README.md               # This file (Schematics Directory Blueprint Index)
└── audio-core.scad         # Parametric OpenSCAD 3D solid in-ear chassis file
```

## 🧬 Spatial Geometry & Acoustic Fluid Wave Propagation

![ARMA-88 Flexible TPU and SLA Resin Core Material Cutaway Profile](../../media/arma88-material-profile.png)

The solid geometry rendered by this module is meticulously mapped to secure and support the multi-layer in-ear array assembly. It integrates sub-millimeter log-spiral waveguides alongside micro-fluidic bypass dampening tracks:

    [ Ambient Sound Waves ] ──► [ Log-Cardioid Plenum Intake ] ──► [ Spiral Micro-Channels ]
                                                                             │
                                                                  (Passive dB Amplification)
                                                                             ▼
    [ Tympanic Membrane ] ◄── [ Piezo Bone Conduction ] ◄── [ Non-Newtonian Blast Shield ]

1.  **Logarithmic Cardioid Waveguide Matrix:** The inner core channels use a specialized $4.8$ geometric taper ratio. This design naturally forces sound waves into a tight centripetal spiral, accelerating wave velocity to generate clear acoustic pressure gains without digital speakers.

2.  **Micro-Fluidic Protection Channels:** Dual bypass paths house the non-Newtonian shear-thickening fluid loop. This subsystem acts as a physical circuit breaker, reacting instantly to high-decibel shockwaves to protect the ear drum from percussive pressure hazards.

## 🛠 CAD Compilation & Rendering Directives

To compile and inspect the 3D in-ear chassis without relying on restrictive, closed-source CAD packages, adhere to the following workflow:

*   **Compiler Medium:** Download and execute the open-source solid modeler **OpenSCAD** (Version 2021.01 or later).
*   **Asset Ingestion:** Load `audio-core.scad` directly into the compiler dashboard workspace.
*   **Resolution Tuning:** The rendering variable `$fn` is pre-set to `120` to ensure ultra-smooth arc interpolation for the curved logarithmic acoustic channels. For quick rendering drafts, you may adjust this locally to `30`.
*   **Export Pipeline:** Execute a complete mathematical render (`F6`), followed by an STL export (`F7`) to generate the polygon mesh required by your slicer software.

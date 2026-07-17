# ARVT-01: Intake Header Cardioid Siphon Splitter

## 📐 Functional Mechanism
The **ARVT-01 Intake Header** acts as the foundational atmospheric interface for Project ARVT-88. Standard pipe splitters employ hard right-angle intersections or flat walls that disrupt the fluid column, building severe internal back-pressure spikes and kinetic scattering. 

This component bypasses classical bottlenecks by shaping the input volume using an asymmetric cardioid funnel mapping. As water enters from the open atmospheric tank, the curved outer perimeter folds the downward mass into a coherent, tightly wound helical vortex sheet. This rotation forms a natural hollow air-core down the exact center, acting as a passive siphon that accelerates the fluid column downward. 

Right at the exit throat, the stream encounters an integrated, solid-state asymmetric Tesla manifold splitter. The channels branch out following an exact geometric reduction area profile (\(1:\sqrt{2}\) cross-sectional shift), dividing the incoming stream into dual independent output channels with **absolute zero back-pressure resistance**.

## 🗂 Module Map
```text
modules/ARVT-01-intake-header/
├── README.md          # This file (Sub-module Specifications)
├── header-config.json # Machine-readable cardioid parameters
└── header_engine.py   # Parametric vector calculation script
```

## 🚀 Execution & Verification
To independently calculate and audit the 3D cardioid vector coordinates for this module, execute the script inside this directory:

```bash
cd vortex-tower-arvt88/modules/ARVT-01-intake-header
python header_engine.py
```

## 🛠 Bench Manufacturing Specifications
To prevent internal delamination under continuous volumetric flow loops, adhere to these explicit printing guidelines:
* **Recommended Filament:** PETG, ABS, or High-Tough Composite Resin.
* **Perimeter Wall Shells:** 6 Loops (Mandatory to ensure water tightness along the thin cardioid splitter edge).
* **Infill Strategy:** 40% Density utilizing a self-supporting Gyroid path layout to handle twisting shear loads.
* 

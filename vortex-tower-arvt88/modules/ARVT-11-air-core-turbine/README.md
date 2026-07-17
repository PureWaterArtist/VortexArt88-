# ARVT-11: Air-Core Kinetic Turbine Array

## 📐 Functional Mechanism
The **ARVT-11 Air-Core Kinetic Turbine Array** introduces a completely non-invasive mechanical energy harvesting layer to Project ARVT-88. When water cascades down the `ARVT-02` Hyperbolic Shaft and is wrapped into a tightly wound vortex sheet, a low-pressure singular void forms down the exact geometric centerline of the tower. 

Because the spinning water sheets possess high rotational and downward velocity, they create extreme surface friction against the internal air column. This structural boundary friction drags the central air down with immense force, spinning it into a localized vertical tornado that rushes downward through the hollow core of the pipe.

Rather than placing a standard turbine directly across the channel—which would impact the water, choke the flow, and destroy the water-vortex configuration—this module hangs an ultra-lightweight string of **Twisted Savonius Impellers** directly down the hollow air core singularity. 

As the rushing air current spins these 12.5mm radius aerodynamic spools, a top-mounted magnetic levitation micro-generator harvests clean, three-phase alternating current (AC). This current is routed out to your power combiner board box, transforming ambient vortex draft friction into active electricity while keeping the water path 100% open and uninhibited.

## 🗂 Module Map
```text
modules/ARVT-11-air-core-turbine/
├── README.md           # This file (Sub-module Specifications)
├── turbine-config.json # Machine-readable diameter limits & specs
└── turbine_engine.py   # S-shape aerodynamic helix vector engine
```

## 🚀 Execution & Verification
To independently calculate and audit the 3D twisted Savonius mesh coordinates for this suspended array, execute the script inside this directory:

```bash
cd vortex-tower-arvt88/modules/ARVT-11-air-core-turbine
python turbine_engine.py
```

## 🛠 Bench Manufacturing Specifications
Because this turbine must spin effortlessly under light air-drag currents, the blades must remain exceptionally thin, balanced, and lightweight:
* **Recommended Filament:** Ultra-Lightweight Carbon Fiber PLA or low-density foaming filaments.
* **Perimeter Wall Shells:** 3 Loops (Keeps the outer shell light while ensuring structural integrity along the thin S-curve scoops).
* **Infill Strategy:** 15% Density utilizing a highly spaced **Gyroid path layout** to maintain structural rigidity along the internal spin axis with the lowest possible weight footprint.
* 

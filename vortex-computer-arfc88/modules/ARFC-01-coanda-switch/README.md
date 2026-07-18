# ARFC-01: Bi-Stable Flip-Flop Fluidic Logic Registers

## 📐 Computational Mechanism
The **ARFC-01 Coanda Switch** acts as the primary solid-state memory register and logic flip-flop switch of the fluidic computer framework. Traditional digital electronics rely on silicon-based field-effect transistors (FETs) that open and close electronic channels to store binary data bits (0 and 1). These micro-components remain deeply vulnerable to tactical or solar High-Altitude Electromagnetic Pulse (EMP) surges, which introduce high-voltage electrical overloads that permanently short-circuit the processing junctions.

This module completely bypasses silicon vulnerabilities by executing binary switching through **Fixed-Geometry Coanda-Effect Streamline Latching**. The internal micro-channels feature a central 0.5mm "Power Jet" nozzle flanked symmetrically by two perpendicular 0.15mm "Control Inlets" (Input A and Input B), expanding into a dual-branch output track set at a precise 12.5° curved wall profile.

### 💨 Boundary Layer State Latching
When a continuous gas or liquid stream is pumped into the module at 45 PSI, the fluid accelerates to a minimum threshold velocity of **32.5 m/s**. According to the physical principles of the *Coanda Effect*, as the high-velocity jet shoots past the curved entry walls, a local vacuum drop is established along the boundary layer. The fluid stream naturally tracks, bends, and firmly adheres to one of the curved surfaces. It remains tightly latched and locked within that branch track indefinitely (representing State 1 / Logic High) without consuming a single micro-amp of electricity.

To flip the binary bit, a micro-pulse of control fluid is injected through the active side **Control Inlet**. This pulse breaks the boundary layer vacuum and pushes the power jet past a central golden ratio splitter island (Φ ≈ 1.618). The main stream instantly snaps and locks to the opposite wall surface (representing State 0 / Logic Low). This achieves solid-state data registration with **absolute zero mechanical moving flaps or transistor micro-traces**, completely securing the memory array.

## 🗂 Module Map
```text
modules/ARFC-01-coanda-switch/
├── README.md         # This file (Sub-module Specifications)
├── switch-config.json# Machine-readable switching parameters card
└── switch_engine.py  # Coanda parametric streamline vector calculator script
```

## 🚀 Execution & Verification
To independently calculate and verify the 3D parametric wall-attachment streamline vectors for this logic register block, execute the script inside this directory:

```bash
cd vortex-computer-arfc88/modules/ARFC-01-coanda-switch
python switch_engine.py
```

## 🛠️ Micro-Etching Substrate Tolerances
Because fluid behavior at sub-millimeter widths is deeply sensitive to minor edge defects, strict cleanroom fabrication limits must be maintained:
*   **Mandatory Material:** Wafer substrates must be cut from optical-grade **Monocrystalline Quartz** or high-performance, non-conductive **PEEK polymers**.
*   **Surface Finishing:** Internal channel trenches must be cleanroom etched to a precise depth of **250 microns** with a laser or chemical surface finish target roughness of **Ra 0.02 microns**, ensuring zero surface ripples that could trigger random boundary layer separation.
*   **Sealing Protocol:** Wafers must be hermetically capped using **Laser Diffusion Bonding** to form a solid-state block rated to handle up to $2,500\text{ PSI}$ of internal burst pressure.
*   

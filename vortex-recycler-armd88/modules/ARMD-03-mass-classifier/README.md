# ARMD-03: Cyclonic Magnetohydrodynamic Sorting Sleeve

## 📐 Industrial Mechanism
The **ARMD-03 Mass Classifier Sleeve** serves as the definitive mechanical sorting house of the resodynamic maelstrom disintegrator platform. Traditional recycling facilities utilize primitive mechanical sorting systems—such as vibrating trommel screens, optic sorting lasers, and magnetic eddy current separators—to categorize shredded materials. These large networks consume heavy amounts of facility grid energy, wear down continuously under abrasive loads, and experience massive contamination rates when erratic plastics stick to metals, dragging sorting efficiency down to an industrial bottleneck.

This module entirely replaces mechanical sorting with **Solid-State Centrifugal Magnetohydrodynamic (MHD) Classification** coupled with an integrated **PVDF Acoustic Noise Energy Recovery Ring**. The horizontal chamber contains a 600mm concentric stack of high-intensity **0.65 Tesla Coaxial N52 Magnet Arrays**.

### 🧲 Real-Time Lorentz Force Trajectory Splitting
Flush-mounted **Glassy Carbon Electrode Traces** are engraved directly into the non-conductive Silicon Nitride (Si₃N₄) bore walls following a continuous 45° double-helix tracking pitch. As the completely atomized, highly conductive fluid waste slurry passes from the cavitation core into this sleeve, low-voltage electrical micro-pulses are driven across the traces, cutting perpendicular to the stable magnetic flux fields (\(\mathbf{B}\)). 

According to the fundamental *Lorentz Force Law*, this interaction generates an intense, continuous volumetric cross-field force vector (\(\mathbf{F} = \mathbf{J} \times \mathbf{B}\)) directly inside the flowing stream, driving the fluid into a blinding cyclonic spin tracking up to **120 Gs of centrifugal force**. 

Because different materials inside the waste slurry possess entirely unique physical mass densities and electrical conductivities, they are forced onto completely separate spatial trajectories:
1.  **High-Density Metals:** Highly conductive copper and aluminum are thrown outward at wide, aggressive angles into the outer collection channel tracking.
2.  **Clean Polymers:** Purified chemical monomer liquids split down a stable midplane track.
3.  **Organic Cellulose Fibers:** Paper and organic wood pulp are focused tightly down the low-pressure central axis.

This architecture effectively classifies the entire unsorted waste stream into pure material categories in real-time with **absolute zero moving mechanical wheels or sorting bins**.

### 🔊 Acoustic-to-Electrical Vibration Capture
To shield the outer Inconel housing from long-term material vibration fatigue caused by the intense cyclonic fluid flow, a secondary **PVDF Piezoelectric Ring** sits directly behind the internal ceramic liner. This ring intercepts the loud acoustic sorting noise and mechanical structural vibrations (delivering up to 42 dB of noise dampening), transforming the destructive vibration noise into extra high-frequency electrical current to trickle-charge the main battery bus.

## 🗂 Module Map
```text
modules/ARMD-03-mass-classifier/
├── README.md              # This file (Sub-module Specifications)
├── classifier-config.json # Machine-readable electromagnetic parameters
└── classifier_engine.py   # Double-helical Lorentz force vector engine
```

## 🚀 Execution & Verification
To independently calculate and verify the 3D helical sorting electrode traces and check the field centerline nodes, execute the script inside this directory:

```bash
cd vortex-recycler-armd88/modules/ARMD-03-mass-classifier
python classifier_engine.py
```

## 🛠️ Industrial Slicing & Ceramic Insulation Standards
Because this module handles direct electrical current pathways within an abrasive, high-velocity multi-phase slurry environment, absolute dielectric isolation boundaries are required:
*   **Internal Wall Liner:** Must be machined from non-conductive, wear-resistant **Silicon Nitride Ceramic ($\text{Si}_3\text{N}_4$)** to act as a permanent insulation barrier, diamond-honed to a mirror finish of **Ra 0.05 microns**.
*   **Perimeter Wall Loops:** Set slicing profiles to a minimum of **12 structural wall loops** inside your Inconel 718 DMLS sintering system to guarantee deep material mass thickness.
*   **Infill Strategy:** **100% Solid Infusion** deploying a concentric print track profile to eliminate any internal air gaps, ensuring absolute structural integrity under peak load.

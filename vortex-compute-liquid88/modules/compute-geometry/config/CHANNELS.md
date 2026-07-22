# Module compute-geometry: Non-Equilibrium Micro-Fluidic Channel Matrices

This document maps out the exact flat-plane node intersection offsets ($X, Y$) and track width limits required to execute fluidic logic gate decisions with zero signal drift.

---

## 📐 Logic Block Cartesian Node Intersections

The micro-fluidic compute block utilizes a high-density, multi-layered layout. Primary decision-gate junctions are measured in millimeters from the absolute bottom-left corner of the logic core ($0, 0$):

*   **Row 1 (Primary Input Buffers):**
    *   `Gate_In_A` = ($12.50\text{ mm}$, $8.25\text{ mm}$) ──► EGaIn Fluid Reservoir Input A
    *   `Gate_In_Clock` = ($25.00\text{ mm}$, $8.25\text{ mm}$) ──► Master Acoustic Sync Rail Input
    *   `Gate_In_B` = ($37.50\text{ mm}$, $8.25\text{ mm}$) ──► EGaIn Fluid Reservoir Input B
*   **Row 2 & 3 (Interaction Cavities & AND/OR Decision Rings):**
    *   `Junction_Y1` = ($18.75\text{ mm}$, $24.50\text{ mm}$) ──► Bistable Coandă Splitter Junction
    *   `Choke_Vortex1` = ($25.00\text{ mm}$, $36.75\text{ mm}$) ──► 0.8 mm Overclock Micro-Vortex Ring
    *   `Junction_Y2` = ($31.25\text{ mm}$, $24.50\text{ mm}$) ──► Bistable Coandă Splitter Junction
*   **Row 4 (Primary Output Siphons):**
    *   `Gate_Out_AND` = ($18.75\text{ mm}$, $52.00\text{ mm}$) ──► High-State Conductor Output Channel
    *   `Gate_Out_XOR` = ($31.25\text{ mm}$, $52.00\text{ mm}$) ──► High-State Conductor Output Channel

---

## 📐 Channel Boundary & Hydrodynamic Constraints

To guarantee that moving droplets of liquid metal smoothly split at the Y-junctions without fragmenting into dead-end residues, track carving must follow these exact angular constraints:

$$\theta_{\text{splitter_angle}} = 30.0^\circ \pm 0.02^\circ$$
$$\text{Nominal Channel Depth} = 2.20\text{ mm} \pm 0.01\text{ mm}$$

*   **Interaction Loops:** Designed to force a physical collision between fluid lines. If only Input A is high, the fluid moves cleanly to the XOR output line via surface wetting forces. If both are high, the fluid collision pushes the metal into the central AND track.

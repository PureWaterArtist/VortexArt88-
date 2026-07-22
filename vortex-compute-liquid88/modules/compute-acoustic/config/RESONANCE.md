# Module compute-acoustic: Acoustic Calibration Logs & Standing Wave Nodes

This document tracks the analytical acoustic frequencies, wave node layout dimensions, and fluidic drag metrics needed to lift the liquid metal conductor stream.

---

## 🎵 1. Harmonic Standing Wave Calibration

To completely negate the heavy viscous drag of the EGaIn alloy inside the micro-channels, the acoustic excitation network must establish permanent, symmetrical standing wave node configurations. The system matches the physical channel width to the half-wavelength ($\lambda/2$) of the acoustic signal:

$$\lambda = \frac{c_{\text{poly}}}{f_{\text{target}}}$$

*   **Target Excitation Pinpoint ($f = 2400.0\text{ Hz}$):**
    *   `Acoustic Wave Match Index` = $100.0\%$ ──► Perfect Resonant Peak Alignment
    *   `Viscosity Fluid Drag Drop` = $95.0\%$ ──► Frictionless Levitation Mode Locked
    *   `Liquid State Behavior` = Metal stream hovers cleanly in track center channel
*   **Transitional Drift Zone ($f = 1200.0\text{ Hz}$ Half-Harmonic):**
    *   `Acoustic Wave Match Index` = $49.8\%$ ──► Secondary Wave Coupling
    *   `Viscosity Fluid Drag Drop` = $47.3\%$ ──► Partial Wall Friction Mitigation
*   **Un-Excited Brute-Force Baseline ($f = 0.0\text{ Hz}$ Static System):**
    *   `Acoustic Wave Match Index` = $0.0\%$ ──► Total Viscous Contact Friction
    *   `Dynamic Fluid Viscosity` = $0.0024\text{ Pa\cdot s}$ (Heavy internal drag choking)

---

## 🔬 Transducer Boundary & Node Alignment Limits

To maintain absolute phase-locked stability across the 0.8 mm overclock tracks without causing cavitation bubbles or material fracturing, the acoustic grid must enforce these boundaries:

*   **Acoustic Node Tolerance Margin:** $2400.0\text{ Hz} \pm 0.1\text{ Hz}$. Slicing and layout anomalies must be held under this threshold to avoid wave cancellation.
*   **Acoustic Shock Siphoning:** Wave reflections reaching the logic track dead-ends must be captured cleanly via micro-Venturi apertures and re-routed to the kinetic energy recycling loop, preventing echo distortion from destabilizing the logic gates.

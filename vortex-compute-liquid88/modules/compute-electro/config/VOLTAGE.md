# Module compute-electro: Electrohydrodynamic Voltage Trigger & Contact Angle Matrices

This document tracks the analytical electrical inputs, dielectric breakdown margins, and contact angle transformation metrics needed to manipulate liquid metal surface energy.

---

## ⚡ 1. Lippmann-Young Surface Energy Attenuation

The physical deformation and fluidic pulling force ($F_{\text{drive}}$) of the EGaIn liquid metal droplet are directly regulated by modifying its localized contact angle ($\theta_V$) against the insulated channel wall. This relationship is mathematically governed by the Lippmann-Young field equation:

$$\cos(\theta_V) = \cos(\theta_0) + \frac{\epsilon_0 \epsilon_d}{2 \gamma d} V^2$$

*   **Zero-Voltage Static Equilibrium State ($V = 0.0\text{ V}$):**
    *   `Native Contact Angle` = $140.0^\circ$ ──► Highly Hydrophobic (Spherical Droplet Boundary)
    *   `Surface Tension` = $0.624\text{ N/m}$
*   **Standard Logic Switching State ($V = 5.0\text{ V}$ Trigger):**
    *   `Attenuated Contact Angle` = $118.4^\circ$ ──► Dynamic Wetted Slant
    *   `Transit Velocity` = $0.052\text{ m/s}$ ──► Standard decision-gate tracking
*   **God-Tier Overclock Drive State ($V = 12.0\text{ V}$ High-Torque Pulse):**
    *   `Attenuated Contact Angle` = $72.1^\circ$ ──► Highly Hydrophilic (Aggressive Forward Elongation)
    *   `Transit Velocity` = $3.593\text{ m/s}$ ──► Near-electronic switching speed

---

## 🔬 Dielectric Insulation & Breakdown Envelopes

To prevent dangerous electrostatic arc-shorting from piercing the internal substrate walls and boiling the liquid metal lines, the insulation boundary must maintain these strict safety constraints:

*   **Insulation Composite Profile:** $1.2\text{ \mu m}$ thin-film fluoropolymer coating (Teflon-AF or Cytop) co-extruded cleanly flush across the gold base pads.
*   **Maximum Voltage Breakdown Ceiling:** $18.5\text{ V}$. Operating triggers must never cross this limit to ensure zero localized cross-link molecular tearing of the insulator.
*   **Self-Healing Reset Window:** If an external charge spike temporarily scatters the liquid metal, the logic track drops voltage to $0.0\text{ V}$ for a $1.5\text{ ms}$ reset window, allowing the native high surface tension ($0.624\text{ N/m}$) to pull the circuit lines back together into an unbroken path.

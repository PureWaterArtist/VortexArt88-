# Module compute-thermal: Thermo-Electric Energy Harvesting & Seebeck Calibration Logs

This document tracks the analytical thermal dissipation profiles, Seebeck coefficient calibrations, and active recycling efficiency checkpoints for the closed-loop computer core.

---

## 📈 1. Joule Heating & Seebeck Voltage Generation

When high-frequency control voltages trigger the EGaIn liquid metal logic tracks, internal electrical resistance causes localized Joule heating ($I^2R$). The solid-state conversion loop utilizes thin-film Bismuth-Telluride ($Bi_2Te_3$) thermopiles to harvest this temperature gradient ($\Delta T$) between the core channel and the cool outer block wall:

$$V_{\text{seebeck}} = \alpha \cdot \Delta T$$

*   **Idle Ambient Condition ($\Delta T = 0.0^\circ\text{C}$):**
    *   `Core Internal Temperature` = $22.0^\circ\text{C}$ ──► Equilibrium baseline
    *   `Seebeck Voltage Output` = $0.0\text{ mV}$
*   **Standard Switching Load ($\Delta T = 20.0^\circ\text{C}$ Gradient):**
    *   `Core Internal Temperature` = $42.0^\circ\text{C}$
    *   `Seebeck Voltage Generated` = $160.0\text{ mV}$ ──► Auxiliary logic rail assistance active
*   **God-Tier Overclock Drive State ($\Delta T = 43.0^\circ\text{C}$ Peak Gradient):**
    *   `Core Internal Temperature` = $65.0^\circ\text{C}$ ──► Maximum allowable safe operating roof
    *   `Seebeck Voltage Generated` = $344.0\text{ mV}$ ──► Maximum thermal energy recycling load

---

## 🔬 Thermal Dissipation & Core Material Constraints

To prevent structural melting, layer cross-link degradation, or liquid metal vaporization, the thermopile grid must enforce these absolute physical boundaries:

*   **Maximum Allowable Core Heat:** $65.0^\circ\text{C}$. Continuous voltage overclock drives must drop back to lower power states if the channel temperature breaches this safety line.
*   **Seebeck Thin-Film Integration:** $250.0\text{ \mu m}$ thick vapor-deposited $Bi_2Te_3$ p-n thermocouple arrays layered flush behind the gold control pads.
*   **Energy Recovery Parity:** Combined with the kinetic siphons, the thermal harvesting sub-module must clear an independent energy conversion efficiency floor of $\eta_{\text{thermal}} \geq 6.5\%$ under maximum operational cycles.

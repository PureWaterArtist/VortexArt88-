# Module suction-shroud: Aerodynamic Mass Airflow & Coaxial Fan Metrics
**Configuration:** Version 2.0.0 // Shroud Intake Alignment // 2-Passenger Compact Proto

This document tracks the analytical volumetric airflow compression limits, intake velocities, and starter motor pre-charge efficiency matrices for the active dorsal dome.

---

## 🔬 1. Volumetric Air Compression & Intake Plenum Velocities

As the aircraft establishes vertical velocity or forward transit, the tapering 5:1 ratio dorsal shroud forces passing atmospheric mass through an active centripetal compression profile:

*   **Volumetric Compression Ratio:** Hard-locked at a strict 5.0 : 1.0 convergence index.
*   **Passive Air Velocity Acceleration Formula:**
    $$V_{\text{plenum}} = V_{\text{airspeed}} \cdot 5.0$$
*   **Nominal Air Intake Mass Flow Rate:** Captures up to $14.2\text{ kg/s}$ of continuous atmospheric air mass during standard high-altitude cruise maneuvers.
*   **Boundary Layer Friction Factor:** Reduced down to $\mu_{\text{friction}} = 0.005$ across the entire shroud throat area due to atomic layer CVD Graphene linings.
*   **Laminar Flow Maintenance Window:** Maintains 100% laminar flow integrity with zero localized stall vectors up to forward velocities of $300.0\text{ km/h}$.

---

## 🎛️ 2. Coaxial Fan Geometries & Pre-Charge Power Limits

To bring the machine past its static inertia threshold on the launch pad, a lightweight, non-metallic coaxial fan draws the initial air volume inward to spool the spin-discs:

*   **Primary Fan Hub Radius:** Exactly $85.0\text{ mm}$ center concentric diameter profile.
*   **Blade Twist Profile:** Logarithmic curve pitch matching a fixed $22.5\text{-degree}$ entry tracking line.
*   **Pre-Charge Starter Burst Potential:** Consumes a high-voltage, low-amperage starting pulse ($5,000\text{ V}$ at $\leq 0.005\text{ A}$) from the graphene floor ultracapacitors.
*   **Automated Power Cutoff Threshold:** The starter fan disengages entirely within $\leq 15\text{ seconds}$ once internal spin-disc velocities cross the **12,500 RPM critical vortex ignition point**, switching propulsion entirely over to passive atmospheric siphoning.

# Manifold Distribution Plenum

The **Manifold Distribution Plenum** is a high-volume intake and pressure-stabilization component. Positioned at the primary inlet of the system layout, this module functions as an anti-cavitation distribution chamber—taking a single high-velocity fluid source from the main pump line and dividing it evenly across three sub-ports without inducing back-pressure, structural resistance, or dead-zone turbulence.

## 📐 Geometric Split & Anti-Cavitation Logic

Traditional T-junction pipe manifolds split fluid mass at harsh 90-degree angles, creating significant fluid drag, pressure drop, and localized kinetic dead-zones. This plenum mitigates those mechanical inefficiencies through specialized geometric expansion:

* **Smooth 30-Degree Bifurcation Curve:** The intake chamber expands gradually at a 30° angle along the vertical Z-axis, allowing incoming fluid to maintain its linear momentum as it stretches outward.
* **Unified-to-Triple Transition Profile:** The internal geometry curves smoothly from a unified 50mm intake ring into three discrete 25mm branching ports, maintaining a uniform volume distribution across all parallel lines.
* **Hydrodynamic Equilibrium:** By distributing the input mass symmetrically, the component prevents internal back-pressure spikes and limits structural cavitation fatigue.

## 🗂 Folder Structure

```text
manifold-distribution-plenum/
├── README.md            # This file (Component Documentation)
├── plenum-config.json   # Machine-readable dimensional bounds & print specs
└── plenum_vectors.py    # Bifurcation expansion calculation engine
```

## 🚀 Execution & Verification

To verify the expansion boundaries and calculate the coordinate matrix for this component independently, navigate to this directory and run the execution script:

```bash
cd components/manifold-distribution-plenum
python plenum_vectors.py
```

### Expected Output Structure
The calculation engine pulls variables directly from `plenum-config.json` and updates the coordinate matrix across 180 vector layers:

```text
============================================================
INITIALIZING: MANIFOLD DISTRIBUTION PLENUM MATRIX
============================================================
[+] Configuration metadata safely loaded into memory map.
[*] Simulating anti-cavitation fluid split lines...
[*] Mapping expansion boundaries at angle: 30.0°

[+] SUCCESS: Distribution plenum vector grid successfully built.
[-] Total structural path layers logged: 180
[-] Transition Boundary Audit:
    ↳ Active Structural Phase: Bifurcation_Transition_Zone
    ↳ Cartesian Mesh Node (X,Y,Z): (44.6063, -19.8587, 27.7778)
============================================================
```

## 🛠 Manufacturing Parameters

Because this component receives the raw, un-throttled kinetic impact directly from the primary pump source, it must be fabricated using specialized, structural print constraints:
* **Recommended Material:** ASA (for weather and chemical resistance) or solid Glass Fiber PETG.
* **Perimeter Wall Loops:** 6 (To eliminate structural layer stress during pressure cycles).
* **Infill Density Profile:** 60% Gyroid internal path structure (maximizing spatial strength-to-weight ratio).

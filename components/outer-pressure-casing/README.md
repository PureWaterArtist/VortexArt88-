# Outer Pressure Casing Jacket

The **Outer Pressure Casing Jacket** is the primary structural containment vessel for the entire system assembly. Functioning as the ultimate mechanical boundary layer (the structural horizon), this heavy-duty cylindrical sleeve encapsulates all internal filtration and dynamic vector modules—ensuring the entire multi-stage infrastructure remains locked in perfect geometric alignment under intense hydraulic pressures.

## 📐 Structural Engineering & Pressure Dynamics

Internal fluid streams moving at high velocities generate significant outward radial forces known as **hoop stress**. Without an unyielding external chassis, modular 3D-printed inner components risk layer separation and localized structural failure. This casing is engineered with specific safeguards to neutralize those loads:

* **Heavy-Wall Cylindrical Sleeve:** Plotted across a rigid 450mm assembly length, the housing maintains a uniform 10mm material wall thickness (110mm internal diameter to 130mm outer diameter) to distribute mechanical expansion stress symmetrically.
* **Integrated O-Ring Gasket Grooves:** Precision-etched 2.5mm deep seating channels are built directly into the top and bottom entry thresholds. These tracks house physical rubber seals, establishing a hermetic, pressurized seal at the structural boundaries without the need for messy chemical adhesives.
* **Threaded End-Cap Coupling:** The design is optimized for matching heavy-duty threaded cap collars, locking the internal components tightly together along the central vertical Z-axis.

## 🗂 Folder Structure

```text
outer-pressure-casing/
├── README.md             # This file (Component Documentation)
├── casing-config.json    # Machine-readable dimensional bounds & pressure specs
└── casing_vectors.py     # Structural boundary calculation engine
```

## 🚀 Execution & Verification

To verify the structural boundaries and calculate the coordinate matrix for this outer jacket independently, navigate to this directory and execute the script:

```bash
cd components/outer-pressure-casing
python casing_vectors.py
```

### Expected Output Structure
The calculation engine pulls variables directly from `casing-config.json` and tracks the structural integrity check across 180 coordinate layers:

```text
============================================================
INITIALIZING: OUTER PRESSURE CASING BOUNDARY ENGINE
============================================================
[+] Physical casing constraints parsed cleanly from configuration dataset.
[*] Simulating structural hoop stress envelopes...
[*] Mapping sleeve boundaries: Total Length = 450.0mm

[+] SUCCESS: Casing sleeve geometry fully compiled.
[-] Total structural perimeters mapped: 180
[-] Gasket Track Interface Audit:
    ↳ Geometric Layer Status: O_Ring_Gasket_Groove
    ↳ Inner Groove Vector (X,Y,Z): (57.478, -2.1587, 27.0)
============================================================
```

## 🛠 Manufacturing & Hardening Standards

Because this casing acts as the primary defense against system leaks and catastrophic over-pressurization, builders must adhere to strict production constraints:
* **Recommended Material:** Carbon Fiber Nylon, Polycarbonate, or structural composite tough resin.
* **Perimeter Wall Loops:** 10 (Mandatory to maximize lateral layer bond strength and resist hoop splitting).
* **Infill Density Profile:** 80% Gyroid internal path structure (Providing maximum torsional rigidity and impact resistance).
* 

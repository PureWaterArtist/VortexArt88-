# 🏛️ Micro-Foundry Technical Guide: Thermal Polymer Chain Preservation
**System Core:** Preventing Polymer Degradation, Volumetric Flow Calibration, and Outgas Mitigation  
**Material Footprint:** Recycled Matte ASA, High-Rebound TPU, Carbon-Fiber Nylon, and Polypropylene  

When engineering thermoplastic polymers through a closed-loop recycling stream, a mechanical workshop faces a hard chemical reality: Hydrolytic Cleavage and Thermal Oxidation. Every single time a plastic component is heated to its melting point and extruded through a nozzle, the long-term polymer chain lengths are subjected to thermal stress, which can cause the molecular bonds to snap. If this molecular degradation is not managed through pure processing discipline, the plastic will lose its tensile modulus, turn brittle, and fail during high-velocity field impacts. This document codifies the exact chemical controls and processing thresholds required to maintain 100% factory-spec material integrity across infinite recycling loops.

---

## 📈 1. THERMAL PROCESSING THRESHOLDS & MELT VELOCITIES

To prevent chemical chain degradation, the print farm cell must enforce strict volumetric flow caps and precise nozzle temperature limits. Forcing a plastic through a nozzle too fast or too hot tears the molecular strands apart.

| Material Matrix | Optimum Melt Temperature | Safe Volumetric Flow Cap | Primary Degradation Failure Vector | The Local Micro-Foundry Fix |
| :--- | :--- | :--- | :--- | :--- |
| **Recycled Matte ASA** | 245°C to 265°C | 12.0 mm³/s | Styrene Volatilization / Layer Warping | Enforce 0% print fan cooling to allow polymer chains to self-weld slowly. |
| **High-Rebound TPU** | 235°C to 238°C | 3.5 mm³/s | Viscoelastic Stringing / Shear Thinning | Throttle print head travel velocity to maximize layer-line boundary density. |
| **Carbon-Fiber Nylon**| 285°C to 288°C | 5.5 mm³/s | Hydrolytic Cleavage (Moisture Foaming) | Pre-bake raw pellets at 80°C for 6 hours to completely remove ambient H2O. |
| **Polypropylene (PP)** | 238°C to 240°C | 7.0 mm³/s | Crystalline Shrinkage / Delamination | Maintain a constant 85°C bed plate environment to lock the molecular lattice. |

---

## 🔬 2. THE THREE LAWS OF POLYMER CHAIN PRESERVATION

To guarantee your re-compounded, shredded workshop filament performs exactly like virgin commercial lots, your lab operations must strictly enforce these three solid-state processing laws:

### Law 1: Absolute De-Humidification (Preventing Hydrolytic Cleavage)
Nylon and ASA are highly hygroscopic polymers, meaning they actively suck moisture straight out of the ambient Michigan air. If you attempt to melt down engineering pellets that contain even a fraction of a percent of trapped water, the superheated moisture will instantly expand into steam bubbles inside the printer's hotend. This steam triggers a chemical reaction called hydrolytic cleavage, permanently severing the long polymer chains and reducing your part's impact strength by up to 60%. All shredded granulates must be cooked inside your material drying oven until internal moisture indexes register flatly below 0.05% prior to extrusion.

### Law 2: Sacrificial Thermal Stabilizer Blending
To fully offset the minor oxidative stress that occurs during motorized re-granulation, our compounding line utilizes a 1% batch weight addition of a commercial **Primary Antioxidant Stabilizer (such as Irganox 1010)**. These micronized organic compounds act as sacrificial free-radical scavengers. During the thermal extrusion loop, the heat waves consume the stabilizer molecules first, leaving the parent polymer chains completely un-impacted and perfectly intact across infinite recycling runs.

### Law 3: Concentric Toolpath Orientation
Because 3D-printed parts possess an anisotropic strength profile (meaning they are inherently stronger along the continuous printed strand than they are across the stacked layers), your slicing profiles must enforce concentric perimeter wall loops on high-torque components like our square telescoping drive axles. This forces the printer to lay down continuous, unbroken molecular loops parallel to the mechanical rotational torque vectors, entirely preventing layer-line separation under full battery acceleration bursts.

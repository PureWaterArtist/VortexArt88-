# Manufacturing Blueprint: Slicer Profiles & Optimization Matrices for Vox-Vortex V2

This document establishes the hard-locked slicing configurations, material selections, and physical print parameters required to produce a watertight, structurally sound, and high-yield biomimetic atmospheric condenser core using standard Fused Deposition Modeling (FDM) 3D printers.

---

## Section 1: Material Selection Matrix

Standard PLA **must be avoided** for this deployment, as it undergoes active hydrolytic degradation when subjected to constant moisture and exhibits poor ultraviolet (UV) stability in outdoor environments.

| Material Property | Polyethylene Terephthalate Glycol (PETG) | Acrylonitrile Styrene Acrylate (ASA) |
| :--- | :--- | :--- |
| **UV Resistance** | Moderate (Requires shade or paint) | High (Excellent for direct desert sun) |
| **Hydrophobic Stability**| High (Excellent moisture resistance) | High (Impervious to water degradation) |
| **Thermal Deflection** | ~75°C (Stable for most climates) | ~90°C - 100°C (Stable for extreme heat) |
| **Print Difficulty** | Low (Low warping, highly accessible) | Moderate (Requires enclosed print chamber) |
| **Primary Use Case** | Baseline functional prototyping | Long-term rugged field deployment |

---

## Section 2: Core Slicer Configuration Profiles

To ensure the final part is completely watertight and structurally stable under its own geometric weight without requiring secondary chemical post-processing or epoxy coatings, input the following exact parameters into your slicing software (PrusaSlicer, Bambu Studio, or Cura):

### 1. Shell & Perimeter Settings (Watertight Integrity)
*   **Wall Loops / Perimeters:** `6` (Minimum ceiling. This forces the internal lizard tracks and external beetle ridges to be built out of solid concentric loops, completely preventing internal leaks between layer seams.)
*   **Top Surface Layers:** `5`
*   **Bottom Surface Layers:** `5`
*   **Seam Position:** `Aligned` or `Rear` (Do not use "Random," as random seam placement creates microscopic pitting across the surface, disrupting the hyper-laminar airflow tracking.)

### 2. Infill Settings (Structural Stability)
*   **Infill Density:** `15%` to `20%` (The natural conical shape of the model provides massive geometric rigidity, allowing a lower infill percentage to save filament material.)
*   **Infill Pattern:** `Gyroid` (Crucial. Gyroid infill provides equal structural strength in all three dimensions and prevents internal moisture traps by allowing open internal airflow within the structural walls.)

### 3. Layer Heights & Speed Dynamics
*   **Layer Height:** `0.28mm` or `0.30mm` (Coarse/Draft Profile). 
    *   *Biomimetic Rationale:* Thicker layer steps act as micro-grooves that actively disrupt the boundary layer airflow, helping tiny airborne water vapor droplets catch and coalesce onto the macro-scale ridges.
*   **First Layer Height:** `0.20mm` (Ensures a highly crushed, uniform seal across the build plate.)
*   **Outer Wall Speed:** `60 mm/s` (Slowing down the outer wall ensures high layer adhesion and pristine physical translation of the internal lizard channels.)

### 4. Cooling & Environmental Settings
*   **Part Cooling Fan:** `30%` to `50%` for PETG; `10%` to `20%` for ASA. 
    *   *Rationale:* Minimizing fan speeds drastically maximizes cross-layer molecular bonding, ensuring the printed cylinder behaves like a single solid piece of plastic that won't crack under internal fluid pressures.

---

## Section 3: Physical Bed Orientation & Build Strategy

### 1. Orientation
*   Orient the model completely flat on the build plate with the **widest 260mm bucket lip facing down**. 
*   The conic geometry tapers upward naturally at a safe printable angle. This orientation creates an entirely self-supporting architecture, requiring **0% support material**. Do not turn on support generation.

### 2. Adherence & Warp Prevention
*   Because a 260mm base covers a large percentage of a standard 256x256mm or 300x300mm build plate, thermal contraction at the corners can cause lifting (warping).
*   **Brim Type:** `Outer Brim Only`
*   **Brim Width:** `8.0mm` to `10.0mm`
*   **Bed Temperature:** `80°C` (for PETG) or `100°C - 110°C` (for ASA). 

---

## Section 4: Post-Print Verification Checklist

Once the printing operation completes, perform the following validation protocol before field deployment:

1.  **Visual Inspect:** Ensure the 36 internal vertical lizard drainage tracks are smooth and completely free of plastic stringing or wisps.
2.  **Seat Alignment:** Test-fit the lower 260mm rim onto a standard 5-gallon container. It should slide tightly over the upper lip with a 1mm clearance allowance to prevent shifting under windy conditions.
3.  **Hydro-Test:** Pour a small volume of water around the outer beetle-stepped ridges. Verify that all fluid tracks directly down the outer slope and that zero weeping or condensation sweating occurs through the physical 3D print layer lines.

# Module config: Sub-Module 12 - Technical Specifications & 30-Product Slicing Overrides
**Document Class:** System Production Authority Card (PROJECT MAKER-UTILITY)
**Version:** 2.0.0 // Restructured Manufacturing Blueprint // From File to Print Settings

This specifications ledger locks in the precise physical dimensions, material selectors, layer boundaries, and infill strategies required to reliably manufacture all 30 catalog designs across your three retail tiers.

---

## 📐 1. General Print-in-Place Assembly Tolerances (Global Slicer Rules)
To guarantee that single-piece designs (hinges, sliders, and clips) separate cleanly on the print bed with zero sticking, all meshes enforce these parameters:
*   **Mechanical Moving Part Air Clearance:** Fixed at exactly $\geq 0.35\text{ mm}$ wall-to-wall separation.
*   **Primary Slicing Nozzle Diameter:** Standard $0.40\text{ mm}$ tool-steel or hardened nozzle profile.
*   **Baseline Layer Height Resolution:** Locked at $0.20\text{ mm}$ for optimal balance between speed and shear strength.
*   **First Layer Line Width Multiplier:** Fixed at $120.0\%$ to establish high plate adhesion without unheated bed detachment failures.

---

## 🤱 2. Section 1 Slicing Matrix: The Mom & Toddler Suite (UTL-01 to UTL-10)
*   **Target Material Feedstock:** Food-Contact Safe, High-Impact Polyethylene or Toughened Bio-PLA Co-Polymer.
*   **Wall Perimeter Count Ceiling:** Minimum floor of $\geq 4\text{ Wall Shells}$ to handle continuous drops.
*   **Infill Density Layout Configuration:** Locked at $\geq 35.0\%$ using a continuous **Auxetic Gyroid** pattern to disperse kinetic impact loads from drops onto hard kitchen tiles.
*   **Solid Skin Shell Profiles:** Minimum of $\geq 5\text{ Top and Bottom Layers}$ to ensure fluidic components (Bath Rinser, Pacifier Shield) remain 100% airtight and waterproof.

---

## 🔨 3. Section 2 Slicing Matrix: The Working Dad Suite (UTL-11 to UTL-20)
*   **Target Material Feedstock:** Industrial Carbon-Fiber Reinforced Nylon (PA-CF) or High-Tensile Polycarbonate (PC).
*   **Wall Perimeter Count Ceiling:** Hard-locked to a minimum floor of $\geq 6\text{ Wall Shells}$ to resist heavy tool vise torque and toolbelt strain.
*   **Infill Density Layout Configuration:** Escalated to $\geq 55.0\%$ density using a dense **3D Honeycomb or Gyroid** pattern to prevent structural crushing and mechanical fracture under heavy hammer shocks.
*   **Nozzle Temperature Threshold Range:** $285^{\circ}\text{C}$ to $300^{\circ}\text{C}$ depending on carbon-fiber fill density, running on a high-adhesion polyetherimide (PEI) sheet bed.

---

## 🏡 4. Section 3 Slicing Matrix: The Whole Household Suite (UTL-21 to UTL-30)
*   **Target Material Feedstock:** Tough PETG Glycol-Modified Composite or UV-Stabilized ASA Polymer.
*   **Wall Perimeter Count Ceiling:** Minimum floor of $\geq 4\text{ Wall Shells}$ for balanced flexibility and toughness.
*   **Infill Density Layout Configuration:** Locked at $\geq 40.0\%$ using an **Auxetic Gyroid** pattern to handle continuous day-to-day push-pull mechanical friction loops.
*   **Chemical and Water Insulation Pass:** Requires zero-cooling fan profiles for the first 3 layers to maximize chemical interlayer cross-linking, completely eliminating water logging or mold pockets inside the soap decks or sink guard lines.
  

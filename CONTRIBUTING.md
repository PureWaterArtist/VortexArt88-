# Contributing to VortexArt88: CAD & Engineering Standards

Thank you for helping scale the Twin-Vortex Singularity project! To ensure our open-source hardware models remain precise, scalable, and easy to manufacture across all three target tiers (Backyard, Neighborhood, and Regional Town Park), please adhere to the following design and contribution protocols.

---

## 🛠️ Preferred Software & File Formats

To ensure cross-compatibility among open-source developers, all submissions to the `/CAD/` folder must include both parametric and universal formats:

1. **Universal Formats (Mandatory for merge):**
   * `.STEP` / `.STP` (For high-fidelity parametric geometry sharing)
   * `.STL` (Optimized for 3D printing slicing software)
2. **Native Engineering Formats (Highly Encouraged):**
   * Autodesk Fusion 360 (`.f3d`)
   * SolidWorks (`.sldprt`, `.sldasm`)
   * FreeCAD (`.FCStd`)
   * Blender (`.blend` - For architectural landscaping visualizations only)

---

## 📐 Design & Modeling Guidelines

*   **Scale Invariance:** Keep your nozzle geometries clean and parametric so they can be seamlessly scaled up or down based on incoming fluid pipe pipe dimensions.
*   **The Golden Ratio (Φ):** All internal acceleration spirals must strictly map to the golden spiral equation ($r = a e^{b \theta}$ where $b$ corresponds to the golden ratio geometry). 
*   **Printability:** Minimize severe overhangs. Design nozzles to be printable using PETG, Nylon, or Tough Resin without requiring excessive structural support material that alters the internal micro-surface texture.
*   **Thread Standards:** Standardize input plumbing junctions to match universal NPT (National Pipe Tapered) thread specifications (e.g., 1/2" for micro rigs, 1.5" or 2" for mid-scale neighborhood setups).

---

## 📂 File Naming & Organization Standard

When submitting a file to the `/CAD/` folder, use clear, structured naming conventions so developers know exactly what scale and software they are looking at:

`[Scale]_[PartType]_[NPT-Size]_[Software].[Extension]`

**Examples:**
*   `Backyard_Nozzle_Clockwise_0.50in_Fusion360.step`
*   `Neighborhood_Nozzle_CounterClockwise_2.00in_SolidWorks.stl`
*   `TownPark_FlumeSplitter_10.00in_FreeCAD.step`

---

## 🚀 How to Submit Your Modifications

1. **Fork the Repository:** Create your own local copy of `VortexArt88` to test your adjustments.
2. **Run Print Tests:** If you are modifying a nozzle, print a benchmark prototype on your own workbench to verify it spins water cleanly without leaking or creating turbulent wall stalls.
3. **Submit a Pull Request (PR):** Open a Pull Request back to our main repository. In your PR notes, explicitly include:
   * A short summary of your adjustments (e.g., "Increased nozzle wall thickness by 1.5mm to handle higher pump head pressure").
   * Your software settings and filament testing notes.
   * Verification that your file matches our open-source CERN-OHL-S licensing framework.

Thank you for contributing to the democratization of nature-based, decentralized civil infrastructure!

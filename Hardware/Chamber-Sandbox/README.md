# 🧩 The Figure-8 Chamber Sandbox

Welcome to the collaborative hardware core of the **VortexArt88** infrastructure. This directory is a decentralized workspace where global designers, engineers, and makers submit variations of the Figure-8 Collision Chamber housing.

By providing our strict geometric vectors while leaving the external form-factor open, we enable a diverse ecosystem of adaptable, bio-integrated hardware variations tailored for different manufacturing methods and localized deployment needs.

---

## 📐 The Unalterable Spatial Constraints

To maintain the precise physical properties required to anchor the steady-state fluid singularity plane, your CAD model **MUST** rigidly lock in these exact internal coordinate constraints:

| Reference Attribute | Spatial Coordinate / Vector | Functional Purpose |
| :--- | :--- | :--- |
| **The Singularity Node** | `(0.00, 0.00, 0.00)` | The exact mathematical center of the collision zone. |
| **Inlet A Center-line** | Vector `(1, 0, 0)` | Holds Nozzle A (Counter-Clockwise vortex) facing the origin. |
| **Inlet B Center-line** | Vector `(-1, 0, 0)` | Holds Nozzle B (Clockwise vortex) facing the origin. |
| **Angular Parity** | Exactly **180.00°** | Direct, head-on fluid collision axis along the X-axis. |
| **Induction Port** | Vector `(0, 0, 1)` | Feeds atmospheric air down the Z-axis into the vacuum core. |
| **Discharge Port** | Vector `(0, 0, -1)` | Routes the micro-bubble/fluid matrix down the negative Z-axis. |

### 🛠️ Hardware Tolerance Notice:
* **Slip-Fit Clearance:** When modeling the internal sleeves that receive Nozzle A and Nozzle B, design a uniform radial air gap of **0.15mm to 0.20mm**. This ensures standard desktop FDM and SLA printers can slide the parts together cleanly without loose wobbling or tight binding.

<a id="safety-matrix-section"></a>
## 🛡️ The Material & Water Safety Matrix

Because standard 3D prints possess microscopic layer lines, they naturally create porous voids where bacteria can colonize and anaerobic pathogens can hide. To ensure that **nothing unclean enters** your fluid loop, all desktop-printed prototypes intended for water contact must strictly adhere to these two defense protocols.

---

### 🧬 Protocol A: Sovereign Material Selection
Never use toxic, industrial plastics or uncured standard resins for fluid testing loops. 
* **Approved Filaments:** Use uncolored, natural **PETG** or **PLA**. These materials are inherently stable and do not leach heavy metal colorants into the water matrix.
* **Approved Resins:** If utilizing SLA/DLP printing, you *must* use certified biocompatible or dental-grade resins, followed by a complete UV post-cure cycle.

---

### 🧪 Protocol B: The Impermeable Food-Grade Seal (Mandatory)
Raw FDM prints will micro-weep, leak, and trap pathogens under pump pressure. To seal the geometry completely, you must apply an internal food-safe barrier coat:

1. **Procure a Certified Coating:** Acquire an FDA-compliant, food-contact-safe epoxy resin (such as *Max CLR* or *Smooth-On Task 16*).
2. **Execute the Internal Wash:** Mix a small batch of the epoxy and pour it directly into the inlet ports of your printed Figure-8 chamber.
3. **Centripetal Rotation:** Slowly rotate the part by hand in all directions, ensuring the liquid epoxy flows smoothly over every internal layer line and nozzle interface.
4. **Drain and Cure:** Pour out the excess epoxy completely so it does not alter your internal nozzle dimensions, then let it fully cure for 24 to 48 hours.

**The Result:** A perfectly smooth, glass-like internal boundary layer. This permanently eliminates structural micro-weeping under heavy pump pressure, prevents bacterial growth, and keeps your fluid dynamics pristine.

---

## 🎨 Where You Can Innovate

As long as the internal nozzle positioning and vector alignments above remain perfect, the rest of the canvas is yours. We welcome variations optimized for:
* **Aesthetics:** Biomimetic forms, sacred geometry contours, or industrial minimalist blocks.
* **Plumbing Interfaces:** Standard NPT/G-threads, quick-connect barb fittings, or custom flanges.
* **Structural Integration:** Desktop tripod frames, zip-tie utility channels, or heavy bolt-down tabs.
* **Manufacturing Pathways:** Single-piece FDM prints (optimized to reduce supports), SLA resin chambers, or CNC aluminum milling paths.

---

## 📥 Submission Protocol

When your variant is ready to share with the human family, submit a Pull Request to this directory using the following folder organization and naming standards:

1. **Create a sub-folder** named after your variant: `housing-[your-username]-[brief-style-tag]/`
2. **Include your project files** inside that folder using open, cross-compatible file standards:
   * `.step` (Mandatory for parametric CAD modifications)
   * `.stl` or `.3mf` (For immediate slicing and 3D printing)
3. **Add a quick markdown log** (`README.md`) inside your sub-folder highlighting your design choices, print recommendations, and plumbing connections used.

Thank you for contributing your time and intelligence to the open-source commons. Let's manifest this geometry together!

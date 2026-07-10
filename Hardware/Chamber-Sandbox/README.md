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

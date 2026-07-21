# Module hull-origami: Non-Euclidean Miura-Ori Crease Coordinate Matrix

This document maps out the exact flat-sheet node coordinate offsets ($X, Y$) and localized fold sector angles ($\alpha, \beta$) required to execute the self-locking rigid origami transformation loop.

---

## 📐 Flat Sheet Cartesian Node Offsets

The continuous topological sheet utilizes a symmetrical $6 \times 4$ tessellation layout matrix. The primary node intersections are measured in millimeters from the absolute bottom-left corner of the flat production sheet ($0, 0$):

*   **Row 1 (Bow Entry Chines):**
    *   `Node_A1` = ($475.0\text{ mm}$, $312.5\text{ mm}$) ──► Valley Fold (Tracking Chine Entry)
    *   `Node_A2` = ($475.0\text{ mm}$, $625.0\text{ mm}$) ──► Mountain Fold (Center Keel Line)
    *   `Node_A3` = ($475.0\text{ mm}$, $937.5\text{ mm}$) ──► Valley Fold (Tracking Chine Entry)
*   **Row 2 & 3 (Main Midship Cockpit Core):**
    *   `Node_B1` = ($950.0\text{ mm}$, $312.5\text{ mm}$) ──► Mountain Fold (Chine Extension)
    *   `Node_B2` = ($1425.0\text{ mm}$, $625.0\text{ mm}$) ──► Mountain Fold (Center Keel Line)
    *   `Node_B3` = ($1900.0\text{ mm}$, $312.5\text{ mm}$) ──► Mountain Fold (Chine Extension)
*   **Row 4 (Stern Exit Transom):**
    *   `Node_C1` = ($2375.0\text{ mm}$, $312.5\text{ mm}$) ──► Valley Fold (Tracking Chine Exit)
    *   `Node_C2` = ($2375.0\text{ mm}$, $625.0\text{ mm}$) ──► Mountain Fold (Center Keel Line)

---

## 📐 Fold Sector Angle Constraints

To guarantee that the 3D expanded structure achieves a stable, flat waterline floor plane while keeping the hull side walls angled outward at an optimal $112.0^\circ$ flare, the live-hinge creases must follow these angular constraints:

$$\alpha_{\text{sector}} = 45.0^\circ \pm 0.05^\circ$$
$$\beta_{\text{sector}} = 67.5^\circ \pm 0.05^\circ$$

*   **Mountain Folds:** Executed via an external V-groove channel tool path. Allows panels to swing completely face-to-face outward during stowed trunk storage.
*   **Valley Folds:** Executed via an internal V-groove channel tool path. Forms the self-tracking hydrodynamic water channels on the underside of the vessel.

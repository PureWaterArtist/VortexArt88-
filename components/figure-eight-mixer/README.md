# Figure-Eight Mixing Chamber

The **Figure-Eight Mixing Chamber** is a high-performance fluid-dynamics component designed to manage and balance intersecting counter-rotational flows. By utilizing a dual-loop geometry, this module channels incoming fluid streams through a structured path that guides them into a controlled, zero-shear kinetic collision at the absolute center of the basin.

## 📐 Mathematical Framework: The Lemniscate of Bernoulli

To achieve a seamless dual-loop flow without sharp angles that cause fluid friction, the interior geometry of this chamber is plotted using the parametric equations for the **Lemniscate of Bernoulli**:

\[x = \frac{a \cos(t)}{1 + \sin^2(t)}\]
\[y = \frac{a \cos(t)\sin(t)}{1 + \sin^2(t)}\]

* **Focal Length (a):** Governs the overall physical scale and width of the twin mixing loops.
* **The Vortex Loops:** Fluid enters the left and right loops at symmetrical high velocities, creating two counter-balancing vortex matrices.
* **Collision Center (x=0, y=0):** The precise spatial junction where the counter-balanced forces cross paths, neutralizing macro-turbulence and maximizing kinetic aeration.

## 🗂 Folder Structure

```text
figure-eight-mixer/
├── README.md           # This file (Component Documentation)
├── mixer-config.json   # Machine-readable dimensional bounds & print profiles
└── mixer_vectors.py    # Trigonometric parametric calculation engine
```

## 🚀 Execution & Diagnostics

While this module can be executed independently, it is fully integrated into the master repository pipeline. To run the vector generator manually, navigate to this folder and execute the script:

```bash
cd components/figure-eight-mixer
python mixer_vectors.py
```

### Expected Output Structure
The engine will pull dimensional properties directly from `mixer-config.json` and output the coordinate alignment check for the central collision zone:

```text
============================================================
INITIALIZING: FIGURE-EIGHT MIXING CHAMBER GENERATOR
============================================================
[+] Configuration profiles extracted successfully.
[*] Compiling geometry map using the Lemniscate of Bernoulli...
[*] Processing boundaries at scale: Focal Length = 50.0mm

[+] SUCCESS: Figure-Eight vector matrix compiled cleanly.
[-] Total structural nodes mapped: 360
[-] Collision Zone Intersection Check (Midpoint):
    ↳ Vector Node Zone: Collision_Center
    ↳ Spatial Vectors (X, Y, Z): (0.0, 0.0, 37.5)
============================================================
```

## 🛠 Manufacturing Parameters

To handle the structural shear stress generated at the center collision point, the housing profile must be manufactured using high-strength, isotropic print settings:
* **Recommended Material:** Tough Resin, Polycarbonate, or solid-filled PETG.
* **Minimum Wall Loops:** 6 (To prevent anisotropic micro-fracturing along layer lines under cyclic loads).
* **Infill Density:** 100% Solid Infusion.
* 

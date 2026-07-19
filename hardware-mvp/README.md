# 🛠️ Hardware Minimum Viable Product (MVP) Implementation Guide

Welcome to the physical execution layer of VortexArt88. This document strips away the macro-architectural philosophy to provide independent makers with a direct, safe, and standardized pathway to prototype the Twin-Vortex Singularity on a standard home workbench.

---

## 📂 Folder Directory Structure
To maintain a clean repository structure, organize your local assets as follows:

```
VortexArt88/
├── Hardware-MVP/
│   ├── README.md               <-- This Guide
│   ├── bill_of_materials.csv   <-- Parts & procurement sheet
│   └── /CAD-Source/            <-- Low-poly, optimized STL/STEP files
```

# 🧩 Hardware-MVP: The Figure-8 Collision Chamber Layout

To manifest the twin-vortex singularity, Nozzle A (Clockwise) and Nozzle B (Counter-Clockwise) must be locked into a rigid, fluidic housing. This specification outlines a basic, functional layout that handles high-pressure fluid vectors while remaining simple enough for any community member to model.

---

## 📐 Absolute Spatial & Geometric Layout

Any parametric model submitted to the Sandbox must align precisely with the following vector network. All dimensions are calculated relative to the absolute spatial origin $(0.00, 0.00, 0.00)$, which serves as the physical point of vector cancellation.

```
                  [ +Z Air Induction Port ]
                             │
                             ▼
   [ Nozzle B Inflow ] ───> (0,0,0) <─── [ Nozzle A Inflow ]
  (-X Vector, Clockwise)     │      (+X Vector, Counter-Clockwise)
                             ▼
                 [ -Z Central Discharge ]
```

### 1. The Collision Chamber Housing (The Housing Core)
*   **The Profile:** The internal geometry must be a true geometric **Lemniscate (Figure-8)** profile consisting of two overlapping, tangent circles.
*   **Internal Diameter:** Each circle must possess an internal diameter of exactly **$50.00\text{ mm}$**.
*   **Center-to-Center Distance:** The focal centers of the two overlapping circles must be spaced exactly **$38.20\text{ mm}$** apart (derived from the Golden Ratio scale factor relative to the outer boundary).
*   **The Intersection Node:** The tangent overlap creates a central bottleneck aperture measuring exactly **$11.80\text{ mm}$** wide at the coordinate origin $(0.00, 0.00, 0.00)$.

### 2. The Fluid Inflow Channels (X-Axis Vectors)
*   **Nozzle A Receiver (Counter-Clockwise Flow):** Centerline entry aligned along the $+X$ vector $(1, 0, 0)$, feeding fluid tangentially into the upper rim of the right chamber loop.
*   **Nozzle B Receiver (Clockwise Flow):** Centerline entry aligned along the $-X$ vector $(-1, 0, 0)$, feeding fluid tangentially into the lower rim of the left chamber loop.
*   **The Phase Opposition:** This layout forces both streams to sprint along the perimeter walls of the Figure-8 until they smash head-on at exactly **$180.00^\circ$ of phase opposition** right at the central intersection node.

### 3. The Induction & Discharge Ports (Z-Axis Vectors)
*   **Atmospheric Induction Port ($+Z$ Axis):** A cylindrical channel with an internal diameter of **$6.00\text{ mm}$** located at vector $(0, 0, 1)$. This port drills straight down into the ceiling of the intersection node to feed the vacuum core with ambient air.
*   **Central Discharge Port ($-Z$ Axis):** A funneling drainage exit located at vector $(0, 0, -1)$ directly beneath the intersection node. The opening must taper smoothly from an internal diameter of **$20.00\text{ mm}$** down to a standard **$1/2\text{-inch BSP/NPT}$** threaded pipe connection for easy workbench plumbing.

---

## 🛠️ Physical Interface & Slip-Fit Tolerances

To ensure 3D-printed parts slide together easily without binding or leaking, your CAD models must utilize these exact boundaries:

*   **Sleeve Clearance:** Apply a uniform **$0.20\text{ mm}$ radial air-gap tolerance** between the outside diameter (OD) of your printed nozzles and the inside diameter (ID) of the housing receiver sleeves.
*   **O-Ring Grooves:** Model two concentric O-ring seats (width: **$2.5\text{ mm}$**, depth: **$1.8\text{ mm}$**) inside both receiver sleeves to allow for standard Nitrile rubber seals, preventing high-pressure weeping.
*   **Fastener Pattern:** The housing must be split horizontally into an upper and lower shell. Model a 4-bolt symmetrical flange pattern utilizing **$M4 \times 0.7\text{ mm}$** hex-head machine screw channels to securely clamp the halves together.
                 

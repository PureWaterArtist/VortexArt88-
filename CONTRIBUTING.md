# Contributing to VortexArt88

This is a completely open-source project. If you know how to make these golden ratio nozzles spin faster, scale easier, or print cleaner, your changes are welcome here!

## 🚀 How to Contribute
1. **Fork this repository** to your own account.
2. Make your adjustments to the CAD models, documentation, or layouts.
3. Open a **Pull Request** back to this main repository.

## 📐 Rough File Preferences
*   Universal formats like `.STEP` or `.STL` are highly preferred so anyone with a basic 3D printer can use them.
*   If you adapt the nozzle to match a specific country's local pipe dimensions (metric, imperial, garden hose adapters), please name the file clearly with the size included.

## 🛠 CFD & Open Hardware Collaboration Request

We are actively seeking Computational Fluid Dynamics (CFD) engineers, parametric designers, and open-source fluid dynamicists to optimize, validate, and scale the **VortexArt88 Twin-Vortex Singularity Engine**. 

The current baseline files (`/CAD-Models/Schauberger_Imploder_Funnel.stl`) require rigorous hydrodynamic simulation to map the velocity profiles, shear stress distributions, and pressure drops across the intersecting geometry.

### 📊 Baseline Operating Parameters (Garage Prototype V1)
To ensure simulations reflect reproducible, low-cost physical deployment, we are grounding our initial boundaries in standard off-the-shelf hardware metrics:
*   **Volumetric Flow Rate ($Q$):** $3.15 \times 10^{-4} \text{ m}^3/\text{s}$ to $6.31 \times 10^{-4} \text{ m}^3/\text{s}$ (~5 to 10 Gallons Per Minute / GPM).
*   **Operating Pump Pressure ($\Delta P$):** $1.38 \times 10^5 \text{ Pa}$ to $2.76 \times 10^5 \text{ Pa}$ (~20 to 40 PSI).
*   **Working Fluid:** Water ($\rho = 998 \text{ kg/m}^3$, $\mu = 1.002 \times 10^{-3} \text{ Pa}\cdot\text{s}$ at 20°C).
*   **Inlet/Outlet Geometry:** Standard $1.905 \text{ cm}$ (~3/4-inch) NPT threaded attachments.
*   **Manufacturing Method:** Fused Deposition Modeling (FDM) 3D printing utilizing PETG (assumed absolute wall roughness $\varepsilon \approx 0.05 \text{ mm}$).

### 🔬 Core Simulation & Optimization Directives

We need contributors to run steady-state and transient multiphase simulations (e.g., using ANSYS Fluent, OpenFOAM, or SimScale) focusing on three critical phases of the fluidic pathway:

#### 1. Centrifugal Boundary Layer Dynamics & De-Gritting
*   **Objective:** Optimize the internal logarithmic/golden-ratio ($\Phi$) spiral curvature of the nozzle to maximize tangential velocity while minimizing parasitic head loss.
*   **Analysis:** Map the wall shear stress and centripetal particle trajectory tracking to validate the self-cleaning perimeter extraction loop for heavy sediment and microplastics.

#### 2. The Intersecting Figure-8 Singularity Plane
*   **Objective:** Model the exact geometric intersection where the Clockwise (Nozzle A) and Counter-Clockwise (Nozzle B) fluid streams collide.
*   **Analysis:** Verify the complete neutralization of rotational kinetic energy along the central vertical plane. Quantify the localized pressure drop to confirm the induction of a steady-state passive vacuum core.

#### 3. Multiphase Cavitation & Kinetic Aeration
*   **Objective:** Analyze the atmospheric air-induction core under the generated vacuum.
*   **Analysis:** Map the phase interaction between the incoming air and the high-shear water columns. We need to optimize bubble size distribution (targeting micro-to-nano bubble saturation) to maximize Dissolved Oxygen (DO) transfer rates.

There are no strict corporate gates here. Tweak it, break it, fix it, and submit your ideas!

Free the Living Water.

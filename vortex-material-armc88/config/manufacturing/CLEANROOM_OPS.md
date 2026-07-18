# ARMC-88 Cleanroom Operations & Symmetrical Integration Manual
### Standard Operating Protocols for Molecular Synthesis Hardware Calibration

This manual documents the mandatory step-by-step cleaning, high-vacuum outgassing, and torque integration protocols required to assemble the **Project ARMC-88 Closed-Loop Vortex Crystallizer**. All procedures must be executed within a certified **ISO Class 5 (Class 100) Cleanroom Environment** to prevent microscopic organic dust or particulate contaminants from entering the fluid core, which would disrupt lattice growth symmetry and cause structural fracturing under peak load.

---

## 🧼 1. Multi-Stage Component Decontamination & Outgassing

Prior to mechanical assembly, all Direct Metal Laser Sintered (DMLS) housings, cubic Boron Nitride (cBN) liners, and semiconductor plates must undergo an intense ultra-purification sweep:

1.  **Acoustic Solvent Bath:** Submerge all metal and ceramic parts inside an ultrasonic tank filled with high-purity **Isopropyl Alcohol (IPA, 99.9% Electronic Grade)**. Run a continuous $40\text{ kHz}$ acoustic vibration sweep for 30 minutes to strip away trace manufacturing soot, machining oils, and particulate surface debris.
2.  **Ultra-Pure Water Rinse:** Transfer the parts immediately into an ultrasonic bath of **Type I Ultra-Pure Deionized Water** (resistivity $\ge 18.2\text{ M}\Omega\cdot\text{cm}$) for 15 minutes to fully neutralize and flush remaining solvent films.
3.  **High-Vacuum Thermal Outgassing:** Place the components inside a cleanroom vacuum oven. Draw the internal chamber pressure down to an ultra-high vacuum ceiling of **$10^{-6}\text{ Torr}$** while raising the temperature to a steady **$200^\circ\text{C}$**. Maintain these conditions for a continuous 4-hour cycle. This forces any trapped atomic hydrogen, moisture, or microscopic volatile gasses trapped within the sintered metal pores to outgas, preventing micro-bubble outgassing from contaminating the supercritical $\text{sCO}_2$ fluid stream.

---

## 🔩 2. Sequential Inter-Chamber Mechanical Integration

Once outgassing is complete and parts have stabilized to room temperature ($20^\circ\text{C}$), execute the cleanroom mechanical stack integration using non-marring, oil-free titanium hand tools:

### Phase A: Sealing the ARMC-01 Injector Header
1. Retrieve the DMLS printed Titanium **ARMC-01 Injector Header** from the outgassing tray. 
2. Seat a fresh, silver-plated **Inconel 718 Hollow-Core Metal O-Ring** directly into the concentric bottom mating flange groove. 
3. Carefully thread the high-pressure feedstock inlet adapter into the top bore, taping the NPT lines with high-density Teflon PTFE tape. Ensure the 6 internal **45-degree Swirl Brake Vanes** remain 100% free of handling contact or lint particles.

### Phase B: Aligning the ARMC-02 Acceleration Throat
1. Retrieve the pre-assembled, shrink-fitted **ARMC-02 Hyperbolic Accelerator Sleeve** (the Inconel 718 outer shell permanently pre-loaded around the cBN sawtooth liner).
2. Solder the dead-soft **High-Conductivity Copper Contact Strips** to the positive and negative terminals of the 32 **Bismuth Telluride ($\text{Bi}_2\text{Te}_3$) Seebeck Pellets** arrayed concentrically around the throat jacket. Insulate the traces using high-temperature polyimide tape.
3. Align the ARMC-02 inlet bore directly with the base exit throat of the ARMC-01 header module. Check your multi-axial alignment using a calibrated digital dial indicator—the internal flow path step lips must align within a tolerance window of **$<0.02\text{mm}$** to preserve fluid laminar continuity.

### Phase C: Locking the ARMC-03 Crystallization Core
1. Slide the **PVDF Piezoelectric High-Polymer Film Sheets** into the outer retention tracking slots of the **ARMC-03 Crystallization Core**, sealing the contact gaps with a thin bead of conductive nickel-graphite compound paste.
2. Position the diamond seed collection substrate plate squarely on the central anvil seat.
3. Siphon a single drop of NSF-61 food-safe silicone grease onto the primary high-purity **Fluorosilicone O-Rings** and compress them into the outer coaxial thermal-siphon pre-heater jacket sleeves. 
4. Bring the full 3-module stack together vertically. Pass your heavy-duty structural tie-rods through the alignment ears and thread on the nylon-insert locknuts.

---

## 🔧 3. Symmetrical Crosswise Clamping & Torque Calibration

To handle an explosive $5,000\text{ PSI}$ operational fluid load without catastrophic structural separation or seal failure, you must establish perfect, uniform gasket compression using a calibrated digital click-torque wrench:

1.  **Hand Tighten Baseline:** Thread all nuts down until they sit flush against the mudguard washers.
2.  **Stage I Pre-Torque Sweep:** Following a strict diagonal, crosswise star-pattern, tighten each nut to exactly **$2.5\text{ Nm}$**. 
3.  **Stage II Intermediate Torque Sweep:** Repeating the exact same diagonal crosswise star-pattern, raise the clamping threshold on all fasteners to **$5.0\text{ Nm}$**.
4.  **Stage III Ultimate Structural Torque Lock:** Execute the final calibration sweep along the star-pattern path, locking every nut down to an ultimate high-tensile compression ceiling of exactly **$8.5\text{ Nm}$**. 

This crosswise sequence forces the Inconel metal O-rings to crush down uniformly across the flange split-lines, establishing an unbreakable gas-tight hermetic metal-to-metal boundary layer seal rated to handle over **$12,500\text{ PSI}$ of ultimate burst safety margins**.

---

## 🚦 4. Post-Assembly System Readiness Checkout

Before introducing any supercritical carbon dioxide or sparking up the cavitation fields, verify system parameters from this standalone cleanroom control console panel:

*   **The Dielectric Continuity Audit:** Connect a high-voltage megohmmeter across the isolated copper Seebeck bus-bars and the outer aluminum combiner box casing. Execute a **1000V DC insulation test sweep**. The dielectric isolation barrier must register a continuous resistance value higher than **500 Megohms**, proving the conformal coating layer is entirely flawless.
*   **The Hydrostatic Hydro-Seal Validation:** Connect a high-pressure hydraulic hand pump filled with pure liquid $\text{CO}_2$ to the inlet gate. Slow-ramp internal pressure up to an extreme checkout ceiling of **$7,500\text{ PSI}$**. Lock the intake valves and monitor the gauge—the system must hold this peak structural load for 12 continuous hours with **absolute zero pressure drop or fluid micro-seeping**, verifying an airtight seal.

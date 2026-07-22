# Module compute-prototyping: 4-Day Rapid Fabrication Scheduling Ledger

This document details the exact 4-day cleanroom production steps, machine setups, and validation checkpoints required to materialize the physical hybrid liquid metal computer block from raw photopolymer substrates.

---

## 📅 Day 1: Micro-SLA Block Layer Slicing & Channel Post-Curing (Phase 1)

### A. Substrate Layer Deposition
*   **Execution Matrix:** Mount the high-stiffness, high-transparency photopolymer resin inside an industrial micro-SLA stereolithography engine. Set Z-axis layer resolution to an ultra-fine depth of $0.025\text{ mm}$ and calibrate the ultraviolet laser spot to a precise $25.0\text{ \mu m}$ diameter.
*   **Timeline Target:** Continuous machine runtime metrics to layer-slice the $50\text{ mm} \times 60\text{ mm} \times 12\text{ mm}$ substrate body requires **12 hours**.

### B. Evacuation Flush & Post-Curing
*   **Execution Matrix:** Place the printed block into an ultrasonic tank. Execute a high-purity isopropyl alcohol flush to completely evacuate uncured resin from the $1.5\text{ mm}$ standard and $0.8\text{ mm}$ overclock logic tracks. Transfer the block to a UV-thermal curing chamber stabilized at exactly $60^\circ\text{C}$ to lock structural dimensions.
*   **Timeline Target:** Ultrasonic clearing and cross-linking thermal stabilization requires **12 hours**.

---

## 📅 Day 2: Gold Pad Vapor Deposition & Insulation Coating (Phase 2)

### A. Control Pad Metallization
*   **Execution Matrix:** Mask the cured channel tracks and place the substrate inside a physical vapor deposition (PVD) vacuum chamber. Magnetron-sputter high-purity gold across the pre-mapped coordinate nodes to grow the 24 internal actuation points.
*   **Timeline Target:** Sputtering process to achieve a uniform film depth of $1500.0\text{ \AA}$ requires **12 hours**.

### B. Fluoropolymer Dielectric Application
*   **Execution Matrix:** Spin-coat a layer of amorphous fluoropolymer Cytop resin cleanly flush over the vapor-deposited gold pads. Transfer the housing to a vacuum baking deck to eliminate localized micro-fissure bubbles.
*   **Timeline Target:** Coating and thermal baking to lock in a flawless $1.2\text{ \mu m}$ insulating barrier with a $18.5\text{ V}$ dielectric breakdown threshold requires **12 hours**.

---

## 📅 Day 3: Thermopile Integration & Piezoelectric Venturi Siphoning (Phase 3)

### A. Seebeck Thermocouple Layering
*   **Execution Matrix:** Micro-align the 48 Bismuth-Telluride ($Bi_2Te_3$) thin-film thermocouple junction pairs directly behind the gold actuation pads. Execute a localized polyolefin mechanical fusion weld to lock the $250.0\text{ \mu m}$ recovery arrays in place.
*   **Timeline Target:** Thermopile embedding and alignment tracking requires **12 hours**.

### B. PVDF Ribbon Placement & Transducer Bond
*   **Execution Matrix:** Layer the 16 thin-film, $110.0\text{ \mu m}$ thick Polyvinylidene Fluoride ($PVDF$) flexible ribbons inside the carved micro-Venturi exit nozzle throats ($0.3\text{ mm}$ diameter). Mount the 12 sub-miniature Lead Zirconate Titanate ($PZT-5H$) acoustic transducers flanking the channels.
*   **Timeline Target:** Component positioning, curing conductive epoxy anchors, and running a $35.0\text{ dB}$ acoustic isolation check requires **12 hours**.

---

## 📅 Day 4: Vacuum Leak Decay Audit & Liquid Bus Charging (Phase 4)

### A. Hydrostatic Joint Verification (Gate 1 Check)
*   **Execution Matrix:** Clamp a specialized diagnostic manifold across the logic track joints. Apply an analog draw vacuum of $-20.0\text{ kPa}$ and seal the line. The total pressure decay loss must stay below a strict line of $\leq 0.05\text{ kPa}$ over a 5-minute hold. Requires **12 hours**.

### B. Liquid Metal Charging & Clock Lock Checkout (Gate 2 Check)
*   **Execution Matrix:** Vacuum-syringe $140\text{ mL}$ of Eutectic Gallium-Indium ($EGaIn$) into the primary logic bus loop. Apply a $2400.0\text{ Hz}$ acoustic tone to confirm perfect frictionless hovering. Ramp control pad triggers to $12.0\text{ V}$ to verify a $3.48\text{ ms}$ gate decision latency while certifying a $\eta \geq 18.5\%$ energy recycling rate.
*   **Timeline Target:** Fluid injection, clock lock profiling, and final data verification loop requires **12 hours**. Compute core cleared for live service.

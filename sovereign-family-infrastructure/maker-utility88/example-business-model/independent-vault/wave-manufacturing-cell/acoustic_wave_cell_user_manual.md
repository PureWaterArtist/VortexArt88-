# 🔧 Acoustic Rayleigh-Wave Cell — Prototype Operation SOP & Manual
**System Version:** 1.3.0-Acoustic Core Master  
**Operational Target:** Non-Contact Wave Boundary Material Processing (Biomimetic Matrix)  
**Zoning Authority:** OSHA Industrial Sound Attenuation Compliance Enforced  

---

## 🛠️ SECTION 1: THE CRITICAL PNEUMATIC COOLING PURGE TIMELINE

Because the PZT-4 piezoelectric ceramic crystals generate extreme internal friction heat at 40 kHz, the operator must strictly execute this three-step pneumatic sequence before, during, and after every manufacturing run to completely prevent thermal depolarization burnout:

### 1. The Pre-Flight Air Ignition Loop
*   **Action:** Before turning on the nozzle heaters or firing up the ultrasonic driver board, open the main shop air line. Adjust the SMC precision pressure regulator to exactly **2.0 Bar for TPU** or **2.2 Bar for Polypropylene**. Verify that air is flowing smoothly through the internal coaxial scrubber jacket and exhausting cleanly out the top vent ports. 

### 2. The Active Manufacturing Thermal Interlock
*   **Action:** Launch the print run file (`acoustic_rayleigh_wave_cell.scad`). The air cooling line must remain active at continuous pressure. The air stream strips away both internal vibration friction heat and external conduction heat, holding ceramic crystal temps permanently beneath 65°C. If air line pressure drops below 1.5 Bar at any point during extrusion, the thermal interlock safety switch will instantly cut all power to the nozzle heaters to protect the hardware.

### 3. The Post-Print Heat-Flush Standby
*   **Action:** The exact second the final top layer finishes, the nozzle heaters shut off flatly. The compressed air line **must remain open at full pressure for exactly 5.0 minutes of post-print cooling standby**. This flushes away all residual latent heat from the metal block core, allowing the ceramic elements to cool down uniformly to ambient room temperature before the air system is powered down.

---

## 🔬 SECTION 2: THE BIOMIMETIC MECHANICAL MANIFOLD CALIBRATION

Our advanced fluid delivery block incorporates optimized natural geometries modeled directly after the Chambered Nautilus and the Human Cochlea. Follow these steps to calibrate the manifold assembly right on the workbench:

### 1. The Logarithmic Nautilus Vortex Alignment
*   **The Physics Action:** The internal entry throat is machined with a smooth, expanding logarithmic spiral curvature. As molten polymer enters the cell under high intake pressure, this spiral forces the liquid to naturally rotate and curl into a self-stabilizing vortex. This entirely replaces sharp entry corners, dropping material boundary friction to absolute zero and expanding your stable volumetric flow rate limits without requiring higher pump torque.

### 2. The Cochlear Parabolic Acoustic Calibration
*   **The Physics Action:** The metal backing chambers behind the 40 kHz piezoelectric crystals are sculpted into micro-parabolic acoustic mirrors. When the crystals shake, these cochlear-shaped shrouds automatically catch the backward-radiating sound energy, focus it, and bounce it straight inward toward the moving material core. This acts as a physical acoustic lens, magnifying the power of the surface-bounded Rayleigh waves on the outer skin of the plastic while keeping the exterior housing walls completely cold, silent, and vibration-isolated from your electronic mainboards.

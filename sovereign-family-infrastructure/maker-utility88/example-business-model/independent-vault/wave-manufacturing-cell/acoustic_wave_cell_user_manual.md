# 🔧 Acoustic Rayleigh-Wave Cell — Prototype Operation SOP & Manual
**System Version:** 1.2.0-Acoustic Core Master  
**Operational Target:** Non-Contact Wave Boundary Material Processing  
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

## 🔬 SECTION 2: THE KINETIC TORSION BED INITIALIZATION CALIBRATION

The mechanical linear shaker exciter bolted underneath your PEI spring steel plates executes intense 120 Hz horizontal mechanical vibrations to settle polymer chains uniformly. Follow these steps to calibrate the bed assembly right on the workbench:

### 1. Anti-Fatigue Bolt Torque Lock
*   **Action:** Take three M6 high-tensile steel structural bolts. Thread them straight through the flared anti-fatigue mounting tabs into the heavy mass iron damping bed. Torque each bolt down uniformly using a hand wrench to exactly **6.8 Nm of torque**. The flared geometric fillet loops completely scatter cyclic fatigue stress waves, ensuring the plastic flanges can handle infinite vibration cycles without ever parking stress fractures.

### 2. The 120 Hz Resonant Frequency Sweep
*   **Action:** Turn on the digital ultrasonic driver board and trigger the low-frequency audio amplifier line. Run a baseline 10-second frequency sweep at a flat **120 Hz**. Place your hand flat against the center face of the PEI spring steel sheet. You should feel a completely uniform, intense, horizontal mechanical vibration buzz across the entire surface area of the plate, with zero rattling or clicking noises at the tab joints. The bed is now fully initialized, balanced, and ready for high-velocity zero-friction extrusion.

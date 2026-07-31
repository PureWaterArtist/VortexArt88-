# 📊 Laboratory Bench Testing & Calibration Protocol
**Operational Scope:** Validating Energy Extraction across Multi-Phase Vectors  

This standard testing procedure defines the exact laboratory bench setups required to measure and verify the current generation metrics of the first completed prototype tile.

### Test 1: Angle-Invariant Optical Trap Verification
*   **Setup:** Mount the prototype onto a manual angle-rotator jig. Position a calibrated solar simulator light source (1,000 W/m² baseline output) at a flat 90-degree perpendicular angle to the tile face. Record baseline wattage.
*   **The Dynamic Shift:** Slowly rotate the tile away from the light source down to an oblique **15-degree low-horizon angle** to simulate 6:00 AM sun.
*   **Pass/Fail Threshold:** A standard flat panel drops output by over 85% at this oblique angle. The Solar-Scale's 42.3-degree PMMA micro-prisms must refract light downward, retaining at least **40% of peak vertical current generation**. Any heavy light bouncing or glare tracking triggers an immediate design verification **FAILURE**.

### Test 2: Thermoelectric Midnight Voltage Extraction
*   **Setup:** Disconnect the light simulator. Place the prototype tile flat onto an industrial lab hot plate calibrated to hold a steady structural temperature of **25°C (77°F)** (Simulating warm earth/roof residual day heat radiation). 
*   **The Delta:** Place a flat dry-ice cooling block directly onto the top PMMA face to rapidly drop surface temperatures to **5°C (41°F)** (Simulating cold ambient night air). Connect an oscilloscope to the Seebeck ADC lines.
*   **Pass/Fail Threshold:** The resulting 20°C thermal differential across the internal Bismuth Telluride modules must generate a continuous, ripple-free solid-state DC baseline of at least **0.30 Watts** in absolute darkness.

### Test 3: Kinetic Wave Sound Transduction
*   **Setup:** Turn off the hot plate and cooling systems. Place the tile inside a soundproof audio diagnostic chamber. Position a calibrated high-output acoustic transducer horn directly over the tile face.
*   **The Stressor:** Blast a low-frequency pink-noise audio loop calibrated to exactly **80 dB** while simultaneously drop-testing water droplets at a rate of 60 drops/minute from a vertical height of 1 meter to simulate a heavy thunderstorm.
*   **Pass/Fail Threshold:** The internal tympanal PVDF piezoelectric layer must deform under the acoustic pressure waves, outputting a clear, measurable AC waveform registering at least **0.20 Watts** on your digital multimeter.

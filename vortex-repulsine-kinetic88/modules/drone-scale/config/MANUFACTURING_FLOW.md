# Module drone-scale: 48-Hour Prototyping Roadmap & Manufacturing Protocol
**Configuration:** Version 2.0.0 // 350mm RC Implosion Drone // Desktop Production Track

This protocol establishes the sequential, toolless assembly roadmaps and validation holds required to construct a functional 350mm prototype on a home workbench in less than two days.

---

## ⏳ Sequential Prototyping & Validation Timeline

```
[Hour 00 - 12]: SLA Laser Slicing Run ──►
[Hour 12 - 14]: IPA Channel Flush & UV Cure│
[Hour 18 - 24]: Motor Hub Alignment    ◄──
[Hour 14 - 18]: Hydrophobic Drag Spray│
[Hour 24 - 36]: Syringe Fluid Injection ──►
[Hour 36 - 48]: 6h Vacuum Hold & Launch
```

### 🖨️ Phase 1: 3D Printing & Post-Processing [Hours 00 – 14]
*   **Hour 00 – 12 (SLA Resin Print):** Wipe down the desktop SLA vat. Pour 1 Liter of Tough Clear Photopolymer Resin into the bed. Load the 350mm frame file, orienting the microfluidic logic channels vertically along the Z-axis. Initiate the print run at a 10-micron layer thickness depth. (Time: 12 Hours continuous).
*   **Hour 12 – 13 (Ultrasonic Channel Flush):** Remove the printed drone frame from the build plate. Submerge the component inside a bath of 99% pure isopropyl alcohol (IPA). Engage ultrasonic agitations to completely flush out uncured resin trapped inside the $250\text{ \mu m}$ logic channels. (Time: 1 Hour).
*   **Hour 13 – 14 (Photolytic UV Bake):** Transfer the flushed chassis card directly into a UV post-curing chamber. Bake at 45°C for 60 minutes to eliminate internal layer stresses and lock geometric structural boundaries. (Time: 1 Hour).

### 🌪️ Phase 2: Surface Sputter Coating & Component Assembly [Hours 14 – 24]
*   **Hour 14 – 18 (Hydrophobic Spray Inlay):** Shake the hydrophobic super-slip aerosol container for 2 minutes. Evenly coat the internal 1:1.618 golden spiral plate corrugations and the entry throat of the dorsal funnel. Leave the chassis to air-dry at room temperature until a matte non-wetting film forms. (Time: 4 Hours).
*   **Hour 18 – 22 (Mechanical Integration):** Press-fit the 2212 1400KV brushless motor axle spindle into the center coaxial adapter hub. Mount the 12 miniature 2,400 Hz piezo transducer discs flanking the fluid channels using thin layers of cyanoacrylate adhesive. (Time: 4 Hours).
*   **Hour 22 – 24 (Electronics Bus Interlock):** Solder the brushless motor phase leads directly to the 30A electronic speed controller (ESC). Map the auxiliary piezo transducer lines straight to a receiver PWM channel to enable radio-triggered pre-charge excitation hooks. (Time: 2 Hours).

### 🧪 Phase 3: Fluidic Charging & Launch Verification [Hours 24 – 48]
*   **Hour 24 – 30 (Syringe Charging):** Fill the 50mL Luer-Lock syringe with deionized distilled water. Connect the blunt-tip needle to the central logic entry port and inject exactly 350mL of fluid. Lightly tap the printed resin bulkheads to drive out trapped micro-bubbles. (Time: 6 Hours).
*   **Hour 30 – 36 (Vacuum Metrology Hold):** Seal the fluid entry valves. Connect a pressure gauge, apply a low vacuum of $-101.3\text{ kPa}$, and clamp the line. The pressure loss signature must remain flat ($\leq 0.10\text{ kPa}$ deviation) over a 6-hour hold to confirm a 100% sealed closed loop. (Time: 6 Hours).
*   **Hour 36 – 48 (Ignition & Staging Check):** Place the 1.93 kg prototype onto a clear 2-meter outdoor test pad. Bind the 2.4GHz radio transmitter. Trigger the transmitter toggle to engage the 2,400 Hz acoustic pre-charge hum. Push the throttle stick forward to drive the motor hub past the critical **12,500 RPM threshold** within 1.2 seconds, initiating centripetal vacuum flight. (Time: 12 Hours validation buffer window).

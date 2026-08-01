# 🏭 Matrix RC Platform — Complete End-to-End Manufacturing Protocol
**System Version:** 4.0.0-Hobby Master  
**Target Hardware Core:** 3x Enclosed Bambu Lab P1S Engines (0.4mm Hardened Steel Nozzles)  
**Quality Engineering Standard:** Six-Sigma Defect Isolation / IP67 Mechanical Seal  

This operational document codifies the exact, step-by-step procedures required to slice, execute, assemble, post-process, and validate the 1:16 scale indestructible multi-material vehicle chassis.

---

## 📈 STAGE 1: SOFTWARE SLICING & TOLERANCE CALIBRATION (TIME: 05 MIN)

1.  **Mesh Compiling:** Open `auxetic_rc_chassis.scad` in your OpenSCAD workspace editor.
2.  **Isolate Component Plates:**
    *   Set `PART_SELECTOR = 1;`. Compile (F6) and export as `rc_exoskeleton_tpu.3mf`.
    *   Set `PART_SELECTOR = 2;`. Compile (F6) and export as `rc_heatsink_spine_nacf.3mf`.
    *   Set `PART_SELECTOR = 3;`. Export the outer square cup as `female_cup_nacf.3mf`.
    *   Set `PART_SELECTOR = 4;`. Export the inner slider shaft as `male_shaft_pp.3mf`.
3.  **Bambu Studio Ingestion:** Load the mesh profiles into your Bambu Studio slicing dashboard. Arrange components onto separate building plates to segregate material profiles:
    *   **Plate 1 (Flexible TPU Bumper):** Houses `rc_exoskeleton_tpu`. Assign the `rc_beetle_exoskeleton_tpu` parameters (3 Wall Loops, 25% Gyroid infill).
    *   **Plate 2 (Rigid Nylon Structures):** Houses `rc_heatsink_spine_nacf` and `female_cup_nacf`. Assign the concentric 100% solid Carbon-Fiber Nylon profiles.
    *   **Plate 3 (Ductile Polypropylene Axles):** Houses `male_shaft_pp`. Assign the raw Polypropylene material profile.
4.  **CRITICAL HORIZONTAL TOLERANCE OVERRIDE BUGFIX:** To prevent the cranial puzzle-seams and square axle sliders from permanently welding together on your print bed due to plastic expansion flare, you must manually go to the **Quality ──► Precise Wall / XY Hole Compensation** field inside Bambu Studio and input a strict **-0.15mm horizontal tolerance offset compensation index** on all models. This guarantees a friction-locked, smooth-sliding keyway clearance right off the print sheet.
5.  **Farm Dispatch:** Slice the files and dispatch the compiled G-code tracking files to your active print engines via the local wireless workspace array network.

---

## 🖨️ STAGE 2: PHYSICAL MACHINE SETUPS & PRINTING LOOPS (TIME: 84 MIN)

1.  **Build Sheet Conditioning:** Spray your spring-steel textured PEI build plates with a light, uniform layer of liquid PVP adhesive glue stick to secure flat-bed adhesion under high-heat thermal loops.
2.  **Nozzle Pre-Heating:** Initiate automated print sequences. The machines will auto-level their beds, run active vibration frequency sweeps to calibrate CoreXY resonance offsets, and pre-heat hotends to their target processing limits:
    *   *Printer Alpha (TPU Bumper Hull):* Nozzle 238°C / Bed 55°C
    *   *Printer Beta (PA-CF Spine & Cups):* Nozzle 285°C / Bed 80°C
    *   *Printer Gamma (PP Axle Shafts):* Nozzle 240°C / Bed 85°C
3.  **Automated Execution Runway:** Allow the print engines to run completely undisturbed for exactly 1.4 hours. The machines will build the variable-density gyroid matrices, supportless upper air chimneys, and solid-state telescoping square slider paths flawlessly.

---

## 🛠️ STAGE 3: STRIPPING THE BEDS & BENCH ASSEMBLIES (TIME: 15 MIN)

1.  **Thermal Cooldown Lock:** Once print head executions drop to zero, allow the heated beds to naturally cool down below 35°C to prevent the flexible TPU components from warping or stretching during hot extraction.
2.  **Part Stripping:** Remove the spring-steel sheets from the magnetic beds. Give the plates a slight, uniform flex to naturally release the printed components from the PEI texture faces.
3.  **The Zero-Tool Ingestion Loop:** Open `rc_user_manual_operations.md`. Guide your kids through the drop-in snap-fit electronics insertion sequence:
    *   Drop the 17g micro servo into the front socket until the TPU spring tab clicks shut.
    *   Slide the 390 brushed motor into the rigid spine tunnel along the keyways and give it a 45-degree clockwise twist to lock the pinion gear mesh inline.
    *   Slide the wavy, puzzle-piece zig-zag cranial seams of the TPU outer exoskeleton body lengthwise over the matching tracks of the Carbon-Fiber Nylon core spine. The frames will friction lock together flat, sealing the electronics inside a dust-proof, impact-insulated structural vault.
    *   Slide the male Polypropylene square shafts straight inside the female Carbon-Fiber Nylon square cups. The parts will fit together perfectly inline with a 0.2mm air clearance buffer.
    *   Pop the hardcase 2S LiPo pack flat into its pre-tensioned battery cradle. Connect the Deans T-Plug. Secure the axle couplings over the differential pins.
4.  **Active Bench Operational Audit:** Turn on the 2.4GHz pistol grip transmitter. Pull the throttle trigger to confirm that the telescoping square slider axles expand and contract smoothly during full suspension strokes without binding, and verify that the steering links swing a full 45 degrees cleanly. The machine is officially certified, protected, fully collateralized, and ready to basher-test across backyard concrete tracks.

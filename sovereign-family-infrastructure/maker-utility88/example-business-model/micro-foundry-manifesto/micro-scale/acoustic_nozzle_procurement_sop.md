# 🔧 Custom Acoustic Nozzle Procurement — Step-by-Step SOP
**System Version:** 1.0.0-Procurement Master Core  
**Target Component:** Coaxial Biomimetic Rayleigh-Wave Nozzle Block Platform  
**CAD Source File:** `acoustic_rayleigh_wave_cell.scad`  
**Primary Manufacturing Method:** Precision 5-Axis CNC Milling / Lathe Turning  
**Target Cost Baseline:** $116.00 USD (POC Budget Lot)  

This Standard Operating Procedure (SOP) hardcodes the exact, low-friction technical steps required to prepare, upload, configure, and inspect your custom 360 brass alloy nozzle prototype using quick-turn digital manufacturing networks.

---

## 🛠️ STEP 1: DIGITAL GEOMETRIC COMPILATION & FILE EXPORT

Because professional commercial machine shops cannot read raw OpenSCAD script text files, you must compile and freeze the parametric geometry into a universal solid-modeling format.

1.  **Open the Script:** Load your master `acoustic_rayleigh_wave_cell.scad` engine inside your desktop OpenSCAD environment.
2.  **Run the Render:** Press **F6** to execute the full geometric mesh calculation. Verify the preview window displays the integrated **Chambered Nautilus Logarithmic Entry Throat**, the **Human-Cochlea Parabolic Transducer Shrouds**, and the hollow **4.0mm internal Coaxial Cooling Jacket** with zero manifold vertex errors.
3.  **Export the Solid File:** Go to *File ──► Export*, and select **Export as STEP (.step)**. If STEP export is unavailable in your local software block configuration, export the file as a high-density binary **STL (.stl)** or **IGES (.iges)** solid mesh. Label the output file exactly: `matrix_acoustic_nozzle_v1.step`.

---

## 🛒 STEP 2: THE DIGITAL INDUSTRIAL MANUFACTURING HUB INGESTION

To bypass the expensive setup premiums and long quoting lead times of traditional manual machine shops, you route the file straight through an automated quick-turn network like Xometry.

1.  **Upload the File:** Navigate to the [Xometry Instant Quoting Engine Terminal](https://xometry.com). Create your developer profile login, click *New Quote*, and drag your `matrix_acoustic_nozzle_v1.step` file straight into the secure cloud upload browser.
2.  **Configure the Material Chemistry Spec:**
    *   *Manufacturing Process:* Select **CNC Machining**.
    *   *Primary Material Category:* Select **Copper / Brass Alloys**.
    *   *Specific Alloy Matrix Selection:* Select **Brass 360 (Free-Cutting)**. 
    *   *Why:* Brass 360 offers exceptional thermal conductivity to assist your compressed air lines in keeping the PZT-4 ceramic crystals cold. It is highly machinable, minimizing tool wear and dropping your single-unit runtime pricing to its absolute floor.
3.  **Configure the Surface Finish Parameters:**
    *   *Surface Finish Spec:* Select **As-Machined (Standard)**.
    *   *Surface Roughness Index:* Select **125 micro-inches Ra (3.2 micrometers)** or finer. This ensures the internal walls of the logarithmic vortex throat are completely smooth to prevent polymer boundary drag. Do not select bead blasting or anodizing coatings—you require raw, bare metal conduction faces.
4.  **Configure the Dimensional Tolerances & Inspect Features:**
    *   *Standard Tolerance Limit:* Select **Standard ISO 2768-medium (Linear dimensions: ±0.1mm)**.
    *   *Thread / Tapped Holes Port:* Flag the three **M6 Bolt securing slots** on the flared tabs as tapped/threaded holes to ensure they come pre-threaded straight out of the box.
    *   *Inspection Certification Level:* Select **Standard Inspection Report (Certificate of Conformance)**.

---

## 📦 STEP 3: WORKBENCH INTAKE & HARDWARE INSPECTION PROTOCOL

The moment the shipping box arrives at your Westland garage workshop cell, perform this three-step physical audit before assembling your electronic transducer components:

1.  **The Sub-Micron Visual Bore Check:** Use a bright flashlight to inspect the central **6.0mm material entry channel**. Look down through the transparent core to verify the internal nautilus spiral is completely smooth, free of metal burrs, machine chips, or tool gouges that could disrupt your 40 kHz Rayleigh wave skin boundaries.
2.  **The Coaxial Pressure Manifold Sealing Test:** Take your standard garage shop compressed air line. Hook it up to a temporary rubber test nozzle and press it flat against the internal coaxial cooling jacket input port. Inject air at **2.0 Bar of pressure**. Pass the nozzle block under a tray of water or spray it with soapy water to verify air exhausts *exclusively* out the designated top vent ports, proving the internal metal chamber is 100% airtight with zero microscopic casting cracks or interior wall bleeding.
3.  **The M6 Anti-Fatigue Anchor Thread Check:** Take three high-tensile steel M6 structural bolts. Thread them by hand into the flared mounting tab joints. The bolts should spin in smoothly and seat flat against the 4.5mm radius curved fillets without binding or catching, verifying the block is fully optimized and ready to bolt straight into your **120 Hz Low-Frequency Linear Bed Oscillator** rig.

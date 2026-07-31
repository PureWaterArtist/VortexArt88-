# 📐 Phase 1 Physical Prototyping Execution Playbook
**System Core:** Out-of-Pocket Industrial Sample Sourcing Protocol  
**Material Specification:** Matte Black Engineering-Grade ASA Polymer  
**Target Delivery Node:** Westland, Michigan 48185 (Wayne County Logistics)  
**Total Estimated Cost:** \$44.00 USD (All-Inclusive Sourcing Bracket)  

This document outlines the exact operational steps, material parameters, vendor selection paths, and post-processing steps required to get your cored, 85-gram flagship display tray physically manufactured by an external commercial prototyping house. Handing a real physical part to an investor removes all mechanical skepticism and proves your CAD design works flawlessly.

---

## 🏛️ SECTION 1: COMMERCIAL VENDOR SELECTION & PLATFORM INGESTION

Do not utilize low-end consumer 3D printing networks. For an executive-level B2B presentation, you must use an online commercial digital manufacturing bureau that runs high-end industrial machinery (such as the Stratasys Fortis series or industrial CoreXY production cells) to ensure flawless layer adhesion and a clean matte outer skin surface finish.

### Vetted Commercial Sourcing Platforms:
1.  **Xometry (The Recommended Path):** A massive, automated online manufacturing network. You upload your file to their secure portal, select your material parameters, and their automated system instantly pairs the file with a vetted, high-end commercial machine shop in the Midwest region.
2.  **Protolabs:** An elite, high-velocity digital manufacturing bureau. They are slightly more expensive but provide the tightest sub-millimeter geometric tolerances and the fastest shipping turnarounds in North America.
3.  **Hubs (Formerly 3D Hubs / Protiq):** An excellent, highly cost-effective commercial manufacturing aggregator that allows you to instantly compare real-time pricing grids from local Michigan production shops.

---

## 🖥️ SECTION 2: INDEPENDENT PORTAL FILE CONFIGURATION SLICING SHEET

When you upload your `display_tray.scad` mesh output (exported from your system as a standard `.3MF` or `.STL` geometry file) to the chosen vendor's portal, you must manually assign these exact software parameters inside their configuration field:

```text
[ PORTAL INPUT SELECTION ]
├── Manufacturing Process : FDM (Fused Deposition Modeling)
├── Engineering Material  : ASA Polymer (Specify: Matte Black or Charcoal Finish)
├── Layer Height Thickness: 0.20 mm (Optimal structural & boundary line balance)
├── Wall Perimeters/Loops : 3 Shells Minimum (Secures the 2.0mm thin column walls)
└── Infill Volume Metric  : 15% Infill / Gyroid Pattern (Caps total mass to 85 grams)
```

*Note: Do not allow the vendor to swap your material to cheap PLA or basic ABS. ASA is hard-coded into your blueprints because it possesses absolute UV-stabilization and premium surface impact resistance.*

---

## 📊 SECTION 3: ITEMIZED OUT-OF-POCKET MATERIAL COST CALCULUS

Because you are printing a lightened, shelled-truss design rather than a solid plastic block, the vendor's automated quoting engine will charge you baseline material consumption rates. Here is the exact cost profile for a single sample tray:

1.  **Industrial Filament Volumetric Cost (85g ASA):** Commercial bureaus charge roughly \$0.15 to \$0.25 per gram of printed engineering material, bringing raw material allocation to **\$17.00 USD**.
2.  **Machine Run Time & Labor Surcharge:** The machine's 1.9-hour execution window and facility cleanup fee cost a flat **\$18.00 USD**.
3.  **Expedited Ground Shipping to Westland (ZIP 48185):** Standard localized shipping from a regional Midwest production node costs **\$9.00 USD**.
4.  **TOTAL OUT-OF-POCKET COMMERICAL COST:** \[\mathbf{\$44.00\text{ USD Total Expense}}\]

---

## 🛠️ SECTION 4: THE BENCH ASSEMBLY PROTOCOL (THE MASTER FINISHING TOUCH)

The exact second the shipment arrives at your workshop workspace, you must execute these three final bench assembly steps to turn the raw part into a flawless, unassailable sales piece:

### Step 1: Clear the Vascular Siphons
*   **Action:** Take a 3mm punch pin or drill bit and clear the 12 base micro-ventilation holes to verify that the concentrate drainage tracks are perfectly open.

### Step 2: Pack the Trapping Magnets
*   **Action:** Invert the tray chassis base. Insert four standard 6mm x 2mm Neodymium disk magnets up through the hidden bottom channels into the side interlock tabs. 
*   **The Safety Lock:** Press them upward until they snap flat against the internal **0.4mm mechanical retention lip overhang**. Apply an ultra-thin drop of high-strength cyanoacrylate adhesive to lock the entry ports permanently. The magnets are now mechanically trapped and cannot rip loose under lateral snap loads.

### Step 3: Slide the PMMA Branding Badge
*   **Action:** Take your separately printed, high-gloss gold or blue solvent-proof PMMA Acrylic branding badge and slide it directly into the front keyway track until it clicks into its base lock position. Wipe down the entire matte black ASA outer shell with a lint-free microfiber cloth to remove finger oils.

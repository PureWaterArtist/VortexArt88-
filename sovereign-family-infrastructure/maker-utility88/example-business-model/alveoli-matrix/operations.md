# 🔧 Alveoli-Matrix Air Scrubber — Production & QA Framework
**System Version:** 1.0.0-Air Purification Engine  
**Operational Scope:** Slicer Architecture, Hardware Seating, and Calibration Tests  

---

## 🖨️ SECTION 1: 10-STEP SLICER-TO-FOUNDRY WORKFLOW

### Step 1: OpenSCAD Configuration Pull
*   **Action:** Launch `alveoli_scrubber.scad`. Scale your footprint layout via the `BASE_DIAMETER` setting. Standard luxury desktop footprint operates cleanly at `160.0mm`.

### Step 2: Mesh Generation
*   **Action:** Render the model grid data (**F6**). This manages the inner 45-degree criss-cross collection walls and the tapered chimney chassis. Export the parts as independent `.3MF` files.

### Step 3: OrcaSlicer / Bambu Studio Plate Ingestion
*   **Action:** Import your structural parts into the software slicer interface. Arrange the outer chimney chassis and inner collection core side by side.

### Step 4: Parameter Shell Configurations
*   **Outer Chassis:** Set to `4 Wall Loops` and a `15% Gyroid` infill using standard matte ASA filament.
*   **Inner Collection Core:** Set to `2 Wall Loops` and `0% Infill` (the custom alveolar lattice acts as its own internal strength matrix).

### Step 5: Advanced Material Slicing (Conductive Configuration)
*   **Action:** Apply a specialized print profile for the inner core using Conductive Carbon-Fiber Filament. Set layer thickness to `0.20mm` to maximize path contact across the static charging plates.

### Step 6: Thermal Extrusion Profiles
*   **Outer Chassis (ASA):** Nozzle at `265°C`, Heated Bed at `100°C` (requires a fully enclosed printer chamber like the Bambu Lab P1S to eliminate warp stress boundaries).
*   **Inner Core (Conductive CF):** Nozzle at `250°C`, Heated Bed at `60°C`. Turn your volumetric extrusion speed down to `6 mm³/s` to keep carbon stringing to a absolute minimum.

### Step 7: Local Print Core Allocation
*   **Action:** Compile toolpaths into production G-code lines. Distribute the file across your secure workshop network directly to an open **Bambu Lab P1S execution core**.

### Step 8: Material Vault Pre-Check
*   **Action:** Verify that your printer's input lines are drawing cleanly from your active, dry material vaults to ensure maximum electrical conductivity inside the carbon filaments.

### Step 9: Automatic Calibration Routine
*   **Action:** Initialize the active print cycle. The printer runs its active dampening calibration to eliminate ringing and patterns along the chimney's outer face.

### Step 10: Component Extraction
*   **Action:** Once printing resolves and temperatures return to room limits, pop the spring-steel plate. Flex the sheet to break the vacuum line, lifting off your finished outer chimney and inner conductive core matrix.

---

## 🛠️ SECTION 2: PHYSICAL WORKSPACE ASSEMBLY PROTOCOL

```text
  [ EXTRACTION OF COMPONENT HOUSINGS ]
               │
               ├──► Seat Laser PM2.5 Core into Base Air Sampling Guide Track
               ├──► Press Fit Upper and Lower Room Air Monitoring Thermistors
               └──► Route Copper Output Grounding Lead to Contact Inner Core Slide Track
               │
               ▼
  [ ELECTRONICS & MICROCONTROLLER SEATING ] 
               │
               └──► Slide Pre-Wired RP2040 Board into Sealed Lower Isolation Capsule
               └──► Solder Low-Voltage PWM Line directly to Static Generator Input
               │
               ▼
  [ INTEGRATION OF WASHABLE CORE ] 
               │
               └──► Slide Core down the Inner Guide Tracks of Outer Chimney
               └──► Friction Pins Seat Copper Tape Contacts Tight Against Ground Rails
               └──► Connect 5V USB-C Cable to Active Nightstand Desktop Power Block
```

---

## 📊 SECTION 3: REVOLUTIONARY INFRASTRUCTURE QUALITY ASSURANCE (QA)

Every unit must clear this rigorous three-stage validation testing before being stamped and packaged for residential fulfillment.

### Test 1: Electrical Continuity and Resistance Test
*   **SOP:** Connect a digital multimeter to the lower and upper bounds of the embedded internal slide tracks inside the print chassis.
*   **Failure Metrics:** Total structural resistance across the conductive carbon core path must fall between **120 Ohms and 350 Ohms**. Any reading showing a complete open circuit or erratic resistance fluctuations indicates a layer line print failure or internal air gap, triggering an immediate **FAILURE**. The core must be thrown into the **Polystruder GR PRO Motorized Shredder** to be recycled into fresh material spools.

### Test 2: Smoke Chamber Particulate Sweep Test (Duration: 15 Minutes)
*   **SOP:** Seal the assembled Air Scrubber inside a clear 1-cubic-meter air diagnostics containment hood filled with dense synthetic test smoke. Power on the unit into **State 2: Active Electrostatic Purification**.
*   **Evaluation Parameters:**
    1.  **Purification Speed:** Total airborne smoke particulate density indices must drop by at least **92% within 15 minutes** purely through passive electrostatic siphon capture.
    2.  **Silent Sound Signatures:** Place a digital decibel meter directly outside the glass window. Total audio metrics must register at a flat **0.0 dBA** over ambient room noise. Any acoustic hum or static popping sounds triggers an immediate **FAILURE**.

### Test 3: Environmental Sensor Logic Check
*   **SOP:** Inject a localized sample of concentrated particulate dust directly into the bottom intake vents of the running device.
*   **Evaluation Parameters:**
    1.  **Trigger Response:** The internal laser PM2.5 sensor must log the dirty air pocket, shifting the controller state to **State 3: Alert Hazard** within 400ms.
    2.  **Voltage Scale:** The output to the static generator must jump instantly to maximum capacity (100% PWM cycle), scaling up surface capture performance to match the heavy pollution load.
    

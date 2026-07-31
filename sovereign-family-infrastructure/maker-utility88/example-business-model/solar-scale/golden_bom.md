# 🔌 Golden Master Prototyping Bill of Materials (BOM)
**System Version:** 1.1.0-Alpha Testing Unit  
**Sourcing Strategy:** Precision Engineering-Grade Individual Components  

The prototyping facility must procure these exact, verified manufacturer part numbers to construct the internal electronics core of the first testing tile:

### 1. Photovoltaic & Thermoelectric Cores
*   **Component 1 (Solar Core):** `LONG-125M-H` Tier-1 Monocrystalline Solar Cell Sheet (Cut down to custom hexagonal profile via precision diamond-wheel glass cutter).
*   **Component 2 (Seebeck Array):** 4x `TES1-12704` High-Temperature Thermoelectric Generator Modules (40mm × 40mm × 3.8mm, pre-sealed with high-temperature silicone moisture barriers).
*   **Component 3 (Thermal Interface):** `Arctic MX-4` High-Thermal-Conductivity Non-Electrical Paste (Applied uniformly between base chassis, Seebeck modules, and the underside of the solar cell).

### 2. Embedded Silicon & Bypass Circuit Automation
*   **Component 4 (Microcontroller Node):** `Waveshare RP2040-Zero` Miniature Development Board (Form factor dimensions: 23.5mm × 18mm, low-power sleep state support).
*   **Component 5 (Bypass Switch):** `IRLZ44N` Logic-Level N-Channel Power MOSFET (Configured as an automated self-healing grounding switch driven by GPIO 12).
*   **Component 6 (Ideal Diode Mesh):** `LM5050MK-1` High-Side Ideal Diode Controller paired with a low forward-drop Schottky matrix to prevent reverse power tracking.

### 3. Connections & Hardware Subassemblies
*   **Component 7 (Concentric Grid Pins):** `Cinnfon Pogo-Pin-M3` Spring-Loaded Concentric Waterproof Copper Contact Rings (IP67 internal compression rating, 4-pole routing: 5V+, GND-, DATA+, DATA-).
*   **Component 8 (Acoustic Capture Membrane):** `Piezotech PVDF-28` High-Crystallinity Piezoelectric Film Layer (Thickness: 28 microns, pre-metallized with silver ink contacts, dropped into Layer 4 socket track).

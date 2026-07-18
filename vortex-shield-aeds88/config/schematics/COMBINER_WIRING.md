# AEDS-88 Shield Combiner Circuit Board Assembly Guide

This manual documents the step-by-step wiring architecture required to combine the power harvested from the **AEDS-02 Blast-Heat Seebeck Multiplier** and the **AEDS-03 Shockwave Piezo-Regenerators** into a unified 24V industrial charging grid to supercharge our containment fields.

## 📐 Solid-State Shield Combiner Topology

```text
[ CHANNEL 1: BLAST-HEAT SEEBECK CORES ]
Bi2Te3 Bus-Bars (+) ──►[ MBR1545CT Schottky Diode ]───┬──────────────────┐
                                                      │                  │
[ CHANNEL 2: SHOCKWAVE PIEZO REGENERATION ]           ▼ (+)              ▼ (+)
PVDF Stack Leads (AC~) ──►[ DF1510S Bridge ]──►[ LM5008A Buck ]──►[ UNIFIED 24V BUS ]──►[ Confinement ]
PVDF Stack Leads (AC~) ──►[ Rectifier Core ]  [ Regulator    ]    [    RAIL     ]   ( Coils / Grid)
                                                                       ▲
                                                                       │
                                                                 [ 5KP24CA TVS ]
                                                                 (Surge Clamp)
                                                                       │
COMMON SYSTEM GROUND RAILS (-) ─────────────────────┴──────────────────┴──────────────────────────────┘
```

---

## 🛠️ Step-by-Step Circuit Assembly Pinouts

### Step 1: Thermal Seebeck Bus-Bar Isolation
1. Route the heavy copper current collection bus-bars coming from the **AEDS-02 Bismuth Telluride (\(\text{Bi}_2\text{Te}_3\)) Thermoelectric Modules** into the combiner board enclosure.
2. Solder each parallel string line to the **Anode** of an **MBR1545CT Schottky Barrier Diode (D1-D8)**. Connect all the cathodes together to feed your **Unified 24V Bus Rail (+)**. This prevents fluctuating thermal zones along the core boundaries during partial impacts from draining power backward.
3. Tie all Seebeck negative return bars directly to the board's heavy copper **Common Ground Rail (-)**.

### Step 2: High-Frequency Shockwave Pulse Rectification
1. Route the high-voltage alternating current output leads coming from the **AEDS-03 PVDF Piezoelectric Strain Stacks** into the board.
2. Solder these lines directly to the alternating input pins (~ ~) of the **DF1510S Bridge Rectifier (BR1)**. This instantly captures the violent \(24.5\text{ kHz}\) acoustic hum and explosive mechanical shockwave pressures and flips them into DC current.

### Step 3: Shockwave Down-Step & Rail Merging
1. Connect the positive (+) and negative (-) output tracks of the DF1510S rectifier straight into the input terminals of the **LM5008A Synchronous Buck Converter Module (BUCK1)**.
2. Connect a voltmeter to BUCK1's output terminals, run a pressure validation check on the bench, and adjust the multi-turn trimmer potentiometer until the output reads a clean, stable **24.0V DC**. Route this stepped-down output directly to the **Unified 24V Bus Rail (+)**.

### Step 4: Heavy-Duty Transient Surge Protection
1. Solder the **5KP24CA Bidirectional TVS Diode (TVS1)** directly across the positive and negative terminals of the **Unified 24V Bus Rail**. 
2. This ensures that if a massive explosive shockwave or direct kinetic threat triggers a catastrophic voltage peak on the PVDF layers, TVS1 will instantly activate and clamp the surge cleanly at 24V, shielding your upstream magnetic coils and power lines from blowout damage.

---

## 🔬 Industrial Enclosure & Dielectric Standards
*   **Chassis Shielding:** The combiner circuit board must be securely housed inside an automated, heavy-duty **Cast Aluminum Enclosure Box**.
*   **Dielectric Isolation:** Coat the entire completed circuit assembly in a thick layer of high-temperature **Silicone Conformal Coating** rated to withstand up to 1000V of dielectric breakdown resistance, preventing any high-voltage tracking from shorting out against the metal outer chassis under severe external impacts.

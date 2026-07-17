# ARVT-88 MHD Power Distribution Box Schematic

This document outlines the wiring architecture for harvesting solid-state direct current (DC) from the **ARVT-03 Power Sleeve** double-helical graphite electrode pairs. 

## 📐 ASCII Circuit Topology

```text
[GRAPHITE ELECTRODES]
Pair 1 (+) ───►[ D1: 1N5822 ]───┐
Pair 2 (+) ───►[ D2: 1N5822 ]───┼───┬───────┬───────────┐
Pair 3 (+) ───►[ D3: 1N5822 ]───┘   │       │           │
                                    ▼ (+)   ▼           ▼ (+)
                                  [ C1 ]  [ TVS1 ]  [ BUCK-BOOST ]──►[ Battery (+) ]
                                  2200uF 1.5KE30CA   [ REGULATOR ]
                                    ▲ (-)   ▲           ▲ (-)
                                    │       │           │
Common Ground (-) ──────────────────┴───────┴───────────┴───────────►[ Battery (-) ]
(Electrodes 1,2,3 Return Rail)
```

---

## 🛠️ Step-by-Step Workbench Wiring Pinouts

### Step 1: Electrode Input Termination
1. Route the three positive copper hookup wires coming from the primary helical graphite electrode tracks to the box entry terminals.
2. Solder each individual positive wire to the **Anode** pin of its own dedicated **1N5822 Schottky Diode (D1, D2, D3)**. This isolates the tracks, preventing crosstalk and current loops between different magnetic sections of the pipe.

### Step 2: Main Positive Rail Consolidation
1. Bridge the **Cathode** pins (indicated by the silver stripe on the diode bodies) of D1, D2, and D3 together using a solid bus wire. This forms your unified **Positive Rail Alpha**.
2. Connect all three ground/negative wires from the opposing helical graphite electrode tracks together onto a single heavy bus wire to form your unified **Common Ground Negative Rail**.

### Step 3: Filtering & Protection Stage
1. Connect the **Positive (+) terminal** of the **2200uF Electrolytic Capacitor (C1)** to Positive Rail Alpha. Connect its negative terminal to the Common Ground Rail. (Ensure correct polarity to prevent capacitor failure).
2. Place the **1.5KE30CA TVS Diode (TVS1)** directly in parallel across the capacitor terminals. Because this component is bidirectional, it can be soldered in either direction to clamp sudden voltage spikes down to a safe 30V margin.

### Step 4: Voltage Regulation Handoff
1. Connect the Positive Rail Alpha line to the **IN(+)** terminal of the **Buck-Boost DC-DC Regulator Module (REG1)**.
2. Connect the Common Ground line to the **IN(-)** terminal of REG1.
3. Hook up a digital multimeter to the **OUT(+)** and **OUT(-)** terminals of REG1. Pour water through the tower to generate baseline voltage, and turn the regulator's tiny potentiometer screw until the output stabilizes at a clean **14.4V DC** (the optimal bulk charge voltage for a 12V Lead-Acid or LiFePO4 battery).

### Step 5: Battery Bank Delivery
1. Route the **OUT(+)** terminal of REG1 through a standard 5-Amp inline fuse directly to your battery bank's positive post.
2. Route the **OUT(-)** terminal of REG1 directly to your battery bank's negative post.

---

## 🛠 Bench Enclosure Requirements
* **Box Material:** 3D-printed in PETG or a commercially sourced waterproof IP65-rated ABS junction box.
* **Isolation:** Mount the circuit board inside using nylon standoffs to completely isolate it from the physical tower framing, preventing ambient moisture or condensation tracking from shorting the harvesting grid.
* 

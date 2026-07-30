================================================================================
          MATRIX BIOMIMETIC FOUNDRY — ELECTRONIC CORES HARDWARE SCHEMATIC
================================================================================
 PRODUCT: Alveoli-Matrix Passive Air Scrubber (v1.0.0-Air Purification Engine)
 BUS TRACK LOGIC: 5V Single-Rail USB-C Architecture

                  +-----------------------------------+

                  |      USB-C 5V POWER INPUT         |
                  +-------+-------------------+-------+

                          |                   |
                          | 5V                | GND
                          v                   v
                  +-------+-------------------+-------+

                  |  RP2040 ZERO / MICROCONTROLLER    |
                  +---+-------+-------+-------+---+---+

                      |       |       |       |   |
    GPIO 12 (PWM Out) |       |       |       |   | GPIO 17 (UART TX)
    +-----------------+       |       |       |   +-----------------------+

    |                         |       |       |                           |
    v                         |       |       |                           v
+---+----------------+        |       |       |                  +--------+-----------+

| HIGH-VOLTAGE       |        |       |       |                  | PLANTOWER PM2.5    |
| STATIC GENERATOR   |        |       |       |                  | LASER DUST SENSOR  |
+---+----------------+        |       |       |                  +--------+-----------+

    |                         |       |       |                           ^
    | High-Voltage DC Out     |       |       +---------------------------+ UART RX (GPIO 16)
    v                         v       v
+---+----------------+    GPIO 34   GPIO 35

| COPPER CHARGE RAIL |    (ADC In)  (ADC In)
| (Friction Contacts)|        |       |
+---+----------------+        |       |
    |                         v       v
    | Static Charge      +----+-------+----+
    v                    | SADDLE DUAL-ZONE|
+---+----------------+   | 10K THERMISTORS |

| CONDUCTIVE CORE    |   | (Base vs. Top)  |
| (Carbon-Fiber FDM) |   +-----------------+
+--------------------+

--------------------------------------------------------------------------------
⚠️ RECONCILIATION & SAFETY COMPLIANCE NOTES:
1. SOLID-STATE CORE ISOLATION: The high-voltage, low-current static output line must 
   be strictly insulated inside its dry, heat-sealed internal base channel. It connects 
   to the core using heavy-duty, stainless-steel friction contact pads. 
2. COMMON GROUND SHIELDING: The microcontroller ground bus (GND) must run through a 
   dedicated 100k Ohm safety discharge resistor before connecting to the common shield matrix. 
   This prevents high-voltage back-EMF spikes from frying the internal RP2040 logic.
================================================================================

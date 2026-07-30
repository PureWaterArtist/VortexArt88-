# 🔌 Electronic Circuit Schematic Wiring Guide

This text schematic defines the exact hardware pin-out connections for the Matrix Biomimetic Sensory Hub control board. The entire circuit is powered via a single 5V USB-C input rail.

```text
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
     GPIO 2 (Data Out)|       |       |       |   | GPIO 15 (Touch Sense Input)
     +----------------+       |       |       |   +-----------------------+

     |                        |       |       |                           |
     v                        |       |       |                           v
+----+---------------+        |       |       |                  +--------+-----------+

| LOWER LED MATRIX   |        |       |       |                  | 3D-PRINTED         |
| (8-LED NeoPixel)   |        |       |       |                  | CONDUCTIVE PILLAR  |
+----+---------------+        |       |       |                  +--------------------+

     |                        |       |       |
     | Data Out to Top        |       |       +-------------------------------+
     v                        |       |                                       |
+----+---------------+        |       |                                       |

| UPPER LED MATRIX   |        |       +---------------+                       |
| (8-LED NeoPixel)   |        |                       |                       |
+--------------------+        v                       v                       v
                     GPIO 4 (PWM Speed)      GPIO 26 (Analog In)            GND (Common Ground)

                              |                       |                       |
                              v                       v                       v
                  +-----------+-------+   +-----------+-------+   +-----------+-------+

                  | 5V BRUSHLESS ESC  |   | MAX4466 AMBIENT   |   | SYSTEM COMMONS    |
                  | MOTOR DRIVER BOARD|   | MICROPHONE SENSOR |   | BUS / SHIELDS     |
                  +-------------------+   +-------------------+   +-------------------+
```

### ⚠️ Crucial Electrical Assembly Safety Notes
1.  **Capacitive Touch Isolation:** The wire running from `GPIO 15` must be securely soldered to a copper contact pad that presses directly against the inner wall of the 3D-printed conductive carbon filament pillar. This wire must be physically isolated from the 5V power rails to prevent static discharge from frying the microcontroller unit.
2.  **Current Consumption Limits:** At full load (Motor running at 95% velocity and 16 LEDs set to white at maximum brightness), the entire system draws approximately `850mA`. This sits safely within standard USB 3.0 and USB-C power thresholds (`900mA` to `3A`), meaning you do not need an expensive external power brick.

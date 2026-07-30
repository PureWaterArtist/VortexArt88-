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
      GPIO 5 (Digital)|       |       |       |   | Interrupt GPIO 4 (Digital In)
     +----------------+       |       |       |   +-----------------------+

     |                        |       |       |                           |
     v                        |       |       |                           v
+----+---------------+        |       |       |                  +--------+-----------+

| 5V MOTORIZED BALL  |        |       |       |                  | G1/2" ROTOR WATER  |
| BYPASS VALVE CORE  |        |       |       |                  | FLOW PULSE SENSOR  |
+--------------------+        |       |       |                  +--------------------+

                              |       |       |
                              v       v       +-------------------------------+
            GPIO 26 (Analog In)       GPIO 27 (Analog In)                     |

                              |               |                               |
                              v               v                               v
                  +-----------+-------+   +-----------+-------+   +-----------+-------+

                  | OPTICAL TURBIDITY |   | SOLID-STATE PSI   |   | SYSTEM COMMONS    |
                  | PARTICULATE SENSOR|   | TRANSDUCER METER  |   | BUS / SHIELDS     |
                  +-------------------+   +-------------------+   +-------------------+
                  

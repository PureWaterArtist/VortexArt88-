# 📦 Master Component Sourcing & Logistics Registry

To maintain the exact physical scale specified in the parametric CAD engine (`vortex_hub.scad`), off-the-shelf mechanical and electronic components must be sourced to match these strict dimension profiles:

### 1. Primary Fluid Vessel Chamber
*   **Component:** Custom Double-Cone or Hourglass Borosilicate Glass Sleeve
*   **Dimensions:** 140mm Maximum Outer Diameter, 134mm Internal Diameter, 166.4mm Vertical Height.
*   **Sourcing Route:** Industrial laboratory glass suppliers (e.g., McMaster-Carr or specialized Alibaba scientific suppliers in lots of 100+).

### 2. Rotational Kinetic Components
*   **Drive Magnets:** 12x N52 Grade Neodymium Disc Magnets (10mm Diameter × 3mm Thickness).
*   **Submerged Bearings:** 2x Zirconia (ZrO2) Full Ceramic Micro Ball Bearings (6mm Inner Diameter, 17mm Outer Diameter, 6mm Width). *Note: Standard steel bearings will oxidize and seize in a closed-loop water environment; ceramic is non-negotiable.*
*   **Seals:** 2x Custom Food-Grade Liquid Silicone O-Rings (134mm Diameter, 2.5mm cross-section width).

### 3. Core Silicon & Power Distribution
*   **Main Microcontroller:** RP2040 Zero or Adafruit QT Py (Form-factor must not exceed 25mm × 18mm to sit cleanly within the base core electronics cavity).
*   **Drive Motor:** 5V High-Torque Brushless DC Motor with built-in PWM Speed Controller board (e.g., standard 40mm cooling fan motor cores stripped down or mini micro-centrifuge motors).
*   **Ambient Mic Sensor:** MAX4466 Electret Microphone Amplifier module with Adjustable Gain.
*   **Lighting Arrays:** 2x WS2812B NeoPixel 8-LED Ring Modules (Outer Diameter: 32mm / Inner Diameter: 18mm).

# ARVT-03: Power Sleeve MHD Magnet Array (Optimized)

## 📐 Upgraded Functional Mechanism
The Version 1.1.0 **ARVT-03 Power Sleeve** serves as the solid-state electrical generator for Project ARVT-88. To maximize energy harvesting efficiency from the gravity-accelerated fluid stream, this module has been upgraded from straight static strips to an internal **Double-Helical Tracking Groove**.

Because the water column is forced into a tight helical spin by the upstream cardioid intake and hyperbolic wall steps, the fluid's ions don't travel in a straight downward line—they swirl downward in a 45° spiral. 

By curving our flush-mounted **Graphite Pickup Electrodes** into a matching double-helix track directly inside the channel wall, we increase the physical surface area contact between the conductor electrodes and the moving ionic core by a projected 35%. 

As this hyper-velocity vortex cuts through the intense fields of the external **N52 Neodymium Ring Magnets**, the Lorentz force isolates charges along this curved track, generating a significantly stronger, continuous direct current (DC) electrical output with absolute zero moving parts.

## 🗂 Module Map
```text
modules/ARVT-03-power-sleeve/
├── README.md          # This file (Upgraded Specifications)
├── sleeve-config.json # Machine-readable helical parameter files
└── sleeve_engine.py   # Helical Lorentz force vector calculation script
```

## 🚀 Execution & Verification
To verify the updated 3D helical tracking nodes and audit electrode positioning coordinates along the magnetic field centerline, execute the script inside this directory:

```bash
cd vortex-tower-arvt88/modules/ARVT-03-power-sleeve
python sleeve_engine.py
```

## 🛠 Bench Manufacturing Specifications
* **Recommended Filament:** Non-Conductive Nylon-12, high-dielectric pure PETG, or insulation resin.
* **Perimeter Wall Shells:** 5 Loops (Establishes a completely non-conductive, water-tight dielectric boundary envelope).
* **Infill Strategy:** 50% Density deploying a structural **Gyroid path layout** to suppress acoustic vibrations while allowing even thermal dissipation around the neodymium ring magnets.
* 

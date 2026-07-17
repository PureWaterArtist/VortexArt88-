# ARVT-03: Power Sleeve MHD Magnet Array (Absolute Harmonic)

## 📐 Upgraded Functional Mechanism
The Version 1.4.0 **ARVT-03 Power Sleeve** serves as the solid-state electrical generator for Project ARVT-88. To maximize energy harvesting efficiency from the gravity-accelerated fluid stream, this module has been upgraded from straight static strips to an internal **Double-Helical Tracking Groove** combined with a secondary **Lenz-Law Regenerative Damping Loop**.

Because the water column is forced into a tight helical spin by the upstream cardioid intake and hyperbolic wall steps, the fluid's ions swirl downward in a 45° spiral. By curving our flush-mounted **Graphite Pickup Electrodes** into a matching double-helix track directly inside the channel wall, we increase the physical surface area contact between the conductor electrodes and the moving ionic core by a projected 35%. 

Furthermore, to manage the high-frequency structural vibration caused by the downstream hydraulic ram thumping, an isolated secondary copper wire coil wraps directly around the outer shell of the **N52 Neodymium Ring Magnets**. As the high-velocity vortex water vibrates the magnetic rings slightly, this secondary circuit uses **Lenz's Law** to passively absorb raw mechanical noise, turning destructive acoustics into extra milliwatts of electrical current while stabilizing the plastic chassis.

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

# Project RESO-ARMOR: 100mm Benchtop Self-Healing Test Coupon (Module: testing-coupon)

![Project RESO-ARMOR 100mm Benchtop Test Coupon Blueprint](./media/grid88-coupon-specs.svg)

## 🔬 System Manifest & Low-Cost Verification Philosophy

The **Self-Healing Test Coupon Module (Project Armor-Coupon)** houses the physical dimensions, fluid mixtures, and step-by-step laboratory instructions required to print and verify our living metamaterial core on a standard home workbench. Traditional armor testing requires industrial ballistic ranges, expensive multi-ton hydraulic presses, and high-cost laboratory material diagnostics that gatekeep validation behind corporate institutions.

This directory establishes a fast, open-source path around those barriers using a compact **100mm × 100mm × 8mm test block**. By scaling the footprint down, material volume and factory printing times drop significantly, allowing a maker to order an industrial-grade clear SLA sample for under \$130. This miniature block retains the exact scale-invariant features of the full-size plates—including the **6x6 auxetic star cells and 120-micron capillaries**. Builders can inject exactly 35mL of our nanocellulose bloodstream fluid and manually fracture the casing with a workshop tool to visually witness the pressure-driven self-healing loop clot and patch the crack in less than 3.2 seconds.

---

## 🗂 Sub-Module Symmetrical Directory Map
```
vortex-armor-resilient88/modules/testing-coupon/
├── README.md                 # This file (Test Coupon Module Index Manual)
├── media/                    # Local folder holding visual coupon schematics
│   ├── README.md             # Local media directory reference index manual
│   ├── generate-blueprint.py # Standalone Python 3 asset drawing compiler script
│   └── grid88-coupon-specs.svg # Native vector blueprint showing the 100mm testing footprint
└── config/
    ├── README.md             # Symmetrical configuration directory reference index
    ├── coupon-bom.json       # Machine-readable 100mm dimensions, SLA resolutions, and volume limits
    ├── TEST_PROTOCOL.md      # Human-readable step-by-step benchtop fracture and clotting protocols
    └── HYDRODYNAMICS.md      # Human-readable hyper-laminar Reynolds flow constraints for the test fluid
```    

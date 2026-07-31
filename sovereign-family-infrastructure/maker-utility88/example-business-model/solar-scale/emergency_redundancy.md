# 🛡️ Supply Chain Risk Mitigation & Emergency Redundancy Protocol
**System Version:** 1.0.0-Grid Freedom Matrix  
**Operational Target:** Absolute Material and Silicon Sourcing Continuity  

To insulate the local micro-foundry from single-point logistical failures, the assembly line utilizes these secondary and tertiary material fallback channels.

### 1. Primary Silicon Photovoltaic Sourcing Redundancy
*   **Primary Carrier Track:** Tier-1 pre-tabbed 125mm Monocrystalline Silicon Cells sourced directly via Longi/Jinko pipelines through Alibaba Logistics.
*   **Emergency Fallback Route:** 5x5-inch commercial off-the-shelf monocrystalline solar cells sourced through domestic liquidators (e.g., Electronic Goldmine, Surplus Sales, or Amazon Commercial B2B lots). 
*   **Parametric Adjust:** If fallback sizes deviate by $\pm2\text{mm}$, adjust the `TILE_WIDTH` variable inside `solar_scale.scad` by a matching offset to resize the structural mounting shelf instantly without rebuilding the layout.

### 2. Thermoelectric Seebeck Generator (TEG) Sourcing Redundancy
*   **Primary Carrier Track:** TES1-12704 Industrial Bismuth Telluride modules (40mm × 40mm).
*   **Emergency Fallback Route:** Standard TEC1-12706 Thermoelectric Peltier cooling plates. *Note: Peltier coolers are chemically identical but optimized for cooling; when run in reverse as a generator, they suffer a 15% efficiency drop but successfully maintain baseline nighttime voltage loops.*

### 3. Sustainable PMMA Acrylic Filament Sourcing Redundancy
*   **Primary Carrier Track:** Premium 1.75mm Optical PMMA Filament.
*   **Emergency Fallback Route:** High-Clarity UV-Stabilized Transparent PETG (e.g., Polymaker PolyLite). While PETG does not undergo thermal depolymerization as cleanly as pure Acrylic, it holds identical refractive properties and matches our 42.3-degree micro-prism angle profiles perfectly.

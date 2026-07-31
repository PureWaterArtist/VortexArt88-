# 📐 Prototyping Tolerances & Dimensional Clearances Specification
**System Version:** 1.1.0-Alpha Prototype  
**Target Process:** Multi-Material FDM / Industrial Stereolithography (SLA)  

To ensure the physical components slip together snugly without internal play, binding, or crushing delicate electronics, the manufacturing house must apply these exact dimensional offsets to the CAD output:

### 1. The Solid-State Silicon Bay Clearance
*   **Target Hardware:** Commercial 125mm × 125mm Monocrystalline Silicon Cell (Standard thickness: 0.18mm) paired with Bismuth Telluride TEG Modules (40mm × 40mm, thickness: 3.8mm).
*   **Recessed Socket Pocket Depth:** Set pocket floor depth inside the ASA base chassis to exactly **4.20mm** (3.8mm TEG + 0.18mm Silicon + 0.22mm thermal compression grease layer allowance).
*   **Horizontal XY Border Offset:** Add a uniform **+0.35mm horizontal gap** to the perimeter of the silicon cell bay to accommodate thermal expansion boundaries under summer solar loads.

### 2. Snap-Fit Interlocking Pin Clearances
*   **Male Interlock Pin Target Outer Diameter:** 12.00mm.
*   **Female Keyway Slot Target Inner Diameter:** **12.25mm**. 
*   **The Tolerance Moat:** A flat **0.25mm total air-gap tolerance** is required for FDM printing. Anything tighter will cause the male pin to fuse permanently inside the slot during installation; anything looser will compromise the IP67 waterproof compression seal.

### 3. Clear PMMA Acrylic Face Processing
*   **Optical Surface Treatment:** The Layer 2 micro-prisms must be printed via high-resolution SLA using transparent clear resin, followed by an industrial **UV-stable gloss clear-coat post-processing step**. 
*   **Refractive Index Alignment:** The 42.3-degree angles assume a completely polished, smooth facet face. Raw 3D print layer lines create microscopic ridges that scatter light waves; chemical or thermal polishing is mandatory to achieve true total internal reflection trapping.

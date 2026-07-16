# End-Cap Compression Collars

The **End-Cap Compression Collars** serve as the primary axial locking and compression mechanisms for the entire system assembly. Designed as heavy-duty threaded locking nuts (the polar event anchors), these collars screw directly onto the outer casing jacket—exerting constant vertical compression to hold all internal filtration and vector components perfectly rigid, ensuring absolute leak prevention against high-pressure cyclic thrust.

## 📐 Thread Geometry & Axial Thrust Mechanics

Pressurized fluids moving through a closed cylinder generate significant internal axial thrust forces trying to force the assembly apart along its vertical length. Without a mechanical anchoring point at both ends, the system components will split under load. This collar is engineered with precise parameters to permanently lock down those forces:

* **Continuous 3D Helical Spiral:** The interior housing features a precision-plotted internal thread track scaled with a 132mm internal diameter to provide a standard clear interface over the outer pressure casing jacket.
* **ISO Metric Trapezoidal Profile:** The calculation engine maps a heavy-duty 3mm thread pitch, alternating the vector radius locally to generate rugged, thick thread teeth optimized to absorb extreme mechanical torque without stripping or shearing.
* **Axial Stabilization Lip:** The central core houses a 50mm bore opening backed by a flat internal compression shelf. When tightened down, this lip presses directly against the internal manifold plenums, sandwiching the entire internal stack into a single rigid block.

## 🗂 Folder Structure

```text
end-cap-collars/
├── README.md             # This file (Component Documentation)
├── collars-config.json   # Machine-readable boundary profiles & torque specs
└── collar_threads.py     # Helical thread calculation engine
```

## 🚀 Execution & Verification

To verify the thread engagement vectors and calculate the coordinate matrix for this locking collar independently, navigate to this directory and execute the script:

```bash
cd components/end-cap-collars
python collar_threads.py
```

### Expected Output Structure
The calculation engine pulls variables directly from `collars-config.json` and evaluates the helical orientation across multiple rotational passes:

```text
============================================================
INITIALIZING: END-CAP COLLAR THREAD ENGAGEMENT ENGINE
============================================================
[+] Thread profiles and mechanical defaults successfully parsed.
[*] Simulating axial thrust loading tracks...
[*] Mapping ISO metric thread profile pitch: 3.0mm

[+] SUCCESS: Collar thread grid successfully compiled.
[-] Total structural locking nodes logged: 480
[-] Thread Engagement Node Audit:
    ↳ Axial Z Compression Height: 20.0mm
    ↳ Geometric Helical Vector (X,Y,Z): (66.0, 0.0, 20.0)
============================================================
```

## 🛠 Manufacturing & Torque Standards

Because the thread tracks concentrate severe local stress when tightened down under pressure, this component must be fabricated using solid, maximum-strength manufacturing standards:
* **Recommended Material:** Carbon Fiber Nylon, Polycarbonate, or solid-infill technical tough resin.
* **Perimeter Wall Loops:** 12 (Mandatory to prevent the internal thread teeth from separating or peeling away under load).
* **Infill Density Profile:** 100% Solid Infusion (Ensuring structural integrity across the entire 40mm collar thickness).
* **Max Assembly Torque:** 25.0 Nm (Newton-meters) of localized mechanical tightening limit.
* 

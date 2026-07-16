# Flower of Life Mesh Engine

The **Flower of Life Mesh Engine** is a biomimetic geometry module designed to map interlocking, multi-layered vector grids. By translating the classical overlapping circle matrix into structural 3D coordinates, this module establishes a highly uniform, fractal structural lattice that can be used for structural loading, fluid flow distribution, or data mapping.

## 📐 Geometric Logic

Instead of traditional square or rectangular grids that create uneven mechanical stress points, this engine relies on hexagonal symmetry:
* **The Absolute Center (Layer 0):** The primary origin coordinate point (0,0,0) that anchors the entire grid.
* **Concentric Rings (Layers 1+):** Symmetrical hexagonal rings radiating outward, step-interpolating coordinate steps to simulate perfectly balanced overlapping curves.
* **Z-Axis Depth Mapping:** Each outward structural ring scales proportionally along the depth dimension to prevent linear compression and create an isotropic 3D coordinate space.

## 🗂 Folder Structure

```text
flower-of-life-mesh/
├── README.md              # This file (Component Documentation)
├── fol_lattice_mesh.json  # Saved dictionary file containing vector maps
└── generate_fol_mesh.py   # The mathematical coordinate compilation script
```

## 🚀 Execution & Automation

The script features an automated fail-safe loop. If `fol_lattice_mesh.json` is missing or accidentally deleted, the script will automatically run its mathematical pipeline to regenerate the missing file on the fly. 

To execute the module independently, navigate to this folder and trigger the engine:

```bash
cd components/flower-of-life-mesh
python generate_fol_mesh.py
```

### Expected Console Output
Upon execution, the script will parse your stored vectors, check the file path integrity, and run a matrix balance anchor verification check:

```text
============================================================
INITIALIZING: BIOMIMETIC FLOWER OF LIFE MESH ENGINE
============================================================
[*] Target file found. Initializing operational memory map...
[+] DATA LOADED: Successfully parsed 'fol_lattice_mesh.json'
[-] Total Active Structural Nodes: 37
[-] Matrix Balance Anchor Check:
    ↳ Node ID: 0 (Layer 0)
    ↳ Spatial Vectors (X, Y, Z): (0.0, 0.0, 0.0)
============================================================
```

## 🛠 Integration

The output file `fol_lattice_mesh.json` contains a clean, standard nested coordinate dictionary format. This allows the mapped node coordinates to be imported instantly into external 3D modeling tools (like Blender or OpenSCAD) or passed seamlessly to broader computational pipelines.

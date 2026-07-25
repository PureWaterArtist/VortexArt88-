#!/usr/bin/env python3
"""
PROJECT AETHERIS-SKATE: Global Hoverboard Specifications Vector Blueprint Generator
Path: vortex-hoverboard-kinetic88/media/generate-blueprint.py
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

Programmatically compiles and outputs the uncompressed XML vector drawing data 
file for the 780mm x 220mm personal deck dimensions, dual 110mm cells, and weight limits.
"""

def compile_hoverboard_vector():
    svg_content = """<svg xmlns="http://w3.org" viewBox="0 0 800 600" width="100%" height="100%">
  <!-- Cleanroom Dark Bench Master Specifications Grid Base -->
  <rect width="800" height="600" fill="#010204" />
  <g stroke="#050a15" stroke-width="1" opacity="0.65">
    <path d="M 0,50 L 800,50 M 0,100 L 800,100 M 0,150 L 800,150 M 0,200 L 800,200 M 0,250 L 800,250 M 0,300 L 800,300 M 0,350 L 800,350 M 0,400 L 800,400 M 0,450 L 800,450 M 0,500 L 800,500 M 0,550 L 800,550" />
    <path d="M 50,0 L 50,600 M 100,0 L 100,600 M 150,0 L 150,600 M 200,0 L 200,600 M 250,0 L 250,600 M 300,0 L 300,600 M 350,0 L 350,600 M 400,0 L 400,600 M 450,0 L 450,600 M 500,0 L 500,600 M 550,0 L 550,600 M 600,0 L 600,600 M 650,0 L 650,600 M 700,0 L 700,600 M 750,0 L 750,600" />
  </g>

  <!-- PERSONAL HOVERBOARD DECK Footprint PROFILE (Length: 780mm / Width: 220mm) -->
  <rect x="150" y="220" width="500" height="160" fill="#0f172a" stroke="#475569" stroke-width="3.5" rx="30" />

  <!-- DUAL CONCENTRIC 110MM LIFTING CELLS POSITIONING OVERLAY -->
  <!-- Front Hydro-Lifting Cell -->
  <circle cx="260" cy="300" r="65" fill="none" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="4,2" />
  <circle cx="260" cy="300" r="10" fill="#38bdf8" />
  <!-- Rear Hydro-Lifting Cell -->
  <circle cx="540" cy="300" r="65" fill="none" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="4,2" />
  <circle cx="540" cy="300" r="10" fill="#34d399" />

  <!-- INTEGRATED 250-MICRON QUARTZ PIEZO STANCE CARPET ZONES -->
  <rect x="190" y="240" width="130" height="120" fill="none" stroke="#38bdf8" stroke-width="1.5" opacity="0.4" rx="10" />
  <rect x="480" y="240" width="130" height="120" fill="none" stroke="#34d399" stroke-width="1.5" opacity="0.4" rx="10" />

  <!-- PERIMETER INTRA-DECK VENTURI SLOTS ARCHITECTURE (24 Inlets Grid Rim) -->
  <path d="M 160,225 H 640 M 160,375 H 640" stroke="#0ea5e9" stroke-width="2" stroke-dasharray="8,4" opacity="0.6" />

  <!-- METROLOGICAL CONFIGURATION MEASUREMENT LAYOUTS -->
  <text x="400" y="65" fill="#e2e8f0" font-family="monospace" font-size="14" font-weight="bold" text-anchor="middle">PROJECT AETHERIS-SKATE // CORE BLUEPRINT SPECS &amp; METROLOGY</text>
  <text x="255" y="398" fill="#38bdf8" font-family="monospace" font-size="10" font-weight="bold" text-anchor="middle">FRONT PRESSURE MAT</text>
  <text x="545" y="398" fill="#34d399" font-family="monospace" font-size="10" font-weight="bold" text-anchor="middle">REAR PRESSURE MAT</text>
  <text x="400" y="295" fill="#ef4444" font-family="monospace" font-size="11" font-weight="bold" text-anchor="middle">DUAL LIFT RADIUS: 110mm</text>
  <text x="400" y="315" fill="#0ea5e9" font-family="monospace" font-size="10" font-weight="bold" text-anchor="middle">PERIMETER VENTURI GATES</text>

  <!-- Technical Threshold Boundaries Footer -->
  <text x="400" y="505" fill="#00f2ff" font-family="monospace" font-size="11" font-weight="bold" text-anchor="middle">RATED HOVER CLEARANCE CEILING: 75.0 mm // NET CAPACITOR POTENTIAL: 5,000V</text>
  <text x="400" y="525" fill="#64748b" font-family="monospace" font-size="10" text-anchor="middle">Operational Deck Curb Mass: 13.0 kg // Max Human Rider Payload Capacity: 100.0 kg</text>
  <text x="400" y="555" fill="#475569" font-family="monospace" font-size="13" text-anchor="middle" font-weight="bold">vortex-hoverboard-kinetic88 // ROOT SPECIFICATIONBlueprints v2.0.0</text>
</svg>"""

    with open("grid88-hoverboard-specs.svg", "w") as f:
        f.write(svg_content)
    print("SUCCESS: grid88-hoverboard-specs.svg vector written programmatically.")

if __name__ == "__main__":
    compile_hoverboard_vector()
  

#!/usr/bin/env python3
"""
PROJECT VOX-VORTEX: Global Condenser Specifications Vector Blueprint Generator
Path: vortex-condenser-vox88/media/generate-blueprint.py
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

Programmatically compiles and outputs the uncompressed XML vector drawing data 
file for the 320mm spiral vortex cone, Namib-beetle grid, and graphene sieves.
"""

def compile_condenser_vector_xml():
    svg_data = """<svg xmlns="http://w3.org" viewBox="0 0 800 600" width="100%" height="100%">
  <!-- Cleanroom Dark Bench Master Specifications Grid Base -->
  <rect width="800" height="600" fill="#010204" />
  <g stroke="#050a15" stroke-width="1" opacity="0.65">
    <path d="M 0,50 L 800,50 M 0,100 L 800,100 M 0,150 L 800,150 M 0,200 L 800,200 M 0,250 L 800,250 M 0,300 L 800,300 M 0,350 L 800,350 M 0,400 L 800,400 M 0,450 L 800,450 M 0,500 L 800,500 M 0,550 L 800,550" />
    <path d="M 50,0 L 50,600 M 100,0 L 100,600 M 150,0 L 150,600 M 200,0 L 200,600 M 250,0 L 250,600 M 300,0 L 300,600 M 350,0 L 350,600 M 400,0 L 400,600 M 450,0 L 450,600 M 500,0 L 500,600 M 550,0 L 550,600 M 600,0 L 600,600 M 650,0 L 650,600 M 700,0 L 700,600 M 750,0 L 750,600" />
  </g>

  <!-- 320mm TAPERED VORTEX SEPARATION CONE PROFILE -->
  <path d="M 150,150 L 470,270 V 310 L 150,430 Z" fill="#0f172a" stroke="#475569" stroke-width="3" />
  <path d="M 150,290 C 250,250 350,330 470,290" fill="none" stroke="#38bdf8" stroke-width="6" stroke-dasharray="5,5" opacity="0.8" />
  <text x="300" y="210" fill="#38bdf8" font-family="monospace" font-size="10" font-weight="bold" text-anchor="middle">PASSIVE RANQUE-HILSCH VORTEX CORE // LENGTH: 320mm</text>

  <!-- CENTRAL COLD ORIFICE SEPARATION EXHAUST INNER CORE (6.5mm) -->
  <rect x="470" y="280" width="80" height="20" fill="#1e1b4b" stroke="#38bdf8" stroke-width="2" />
  <text x="510" y="293" fill="#00f2ff" font-family="monospace" font-size="8" font-weight="bold" text-anchor="middle">COLD CORE: 6.5mm</text>

  <!-- BIOMIMETIC NAMIB-BEETLE PLATING INDICATION ARRAYS -->
  <g stroke="#34d399" stroke-width="2" fill="none" opacity="0.9">
    <circle cx="200" cy="490" r="15" />
    <circle cx="200" cy="490" r="2" fill="#34d399" />
    <circle cx="240" cy="490" r="15" />
    <circle cx="240" cy="490" r="2" fill="#34d399" />
    <circle cx="280" cy="490" r="15" />
    <circle cx="280" cy="490" r="2" fill="#34d399" />
  </g>

  <!-- METROLOGICAL BLUEPRINT LABELS & TEXT OVERLAYS -->
  <text x="400" y="55" fill="#34d399" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">PROJECT VOX-VORTEX ATMOSPHERIC WATER SYNTHESIZER MECHANICAL SPECIFICATIONS</text>
  <text x="240" y="530" fill="#34d399" font-family="monospace" font-size="9" font-weight="bold" text-anchor="middle">NAMIB-BEETLE PLATING GRID // APEX PEAKS: 350μm</text>
  <text x="600" y="380" fill="#f43f5e" font-family="monospace" font-size="10" font-weight="bold" text-anchor="middle">GRAPHENE-OXIDE SIEVE // CEILING: 0.02μm</text>

  <!-- LINEAR CAPILLARY PURIFICATION PATHWAY OVERLAY (120μm Grid) -->
  <rect x="450" y="390" width="300" height="50" fill="#020617" stroke="#f43f5e" stroke-width="2" rx="4" />
  <line x1="450" y1="415" x2="750" y2="415" stroke="#be123c" stroke-width="2" stroke-dasharray="4,4" />

  <!-- FOOTER FRAME TEXT BLOCK -->
  <text x="400" y="475" fill="#00f2ff" font-family="monospace" font-size="11" font-weight="bold" text-anchor="middle">OWL FEATHER INTAKE NOISE SUPPRESSION: 0.0 dB // IMMORTAL SOLID-STATE WATER SECURED</text>
  <text x="400" y="565" fill="#475569" font-family="monospace" font-size="14" text-anchor="middle" font-weight="bold">PROJECT VOX-VORTEX // WATER WELL REFERENCEBLUEPRINT v2.0.0</text>
</svg>"""

    with open("grid88-condenser-specs.svg", "w") as f:
        f.write(svg_data)
    print("SUCCESS: grid88-condenser-specs.svg vector blueprint written via standalone script execution.")

if __name__ == "__main__":
    compile_condenser_vector_xml()
  

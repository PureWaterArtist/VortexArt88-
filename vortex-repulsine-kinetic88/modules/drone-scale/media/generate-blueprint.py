#!/usr/bin/env python3
"""
PROJECT REPULSINE: 350mm RC Drone Scale Blueprint Generator
Path: vortex-repulsine-kinetic88/modules/drone-scale/media/generate-blueprint.py
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

Generates the uncompressed XML Vector Layout for the 350mm outer frame footprint,
2212 1400KV brushless outrunner motor hub mount, and 250-micron logic card core.
"""

def build_drone_vector_xml():
    svg_data = """<svg xmlns="http://w3.org" viewBox="0 0 800 600" width="100%" height="100%">
  <!-- Cleanroom Dark Bench Drone Core Grid Base -->
  <rect width="800" height="600" fill="#010204" />
  <g stroke="#050a15" stroke-width="1" opacity="0.65">
    <path d="M 0,50 L 800,50 M 0,100 L 800,100 M 0,150 L 800,150 M 0,200 L 800,200 M 0,250 L 800,250 M 0,300 L 800,300 M 0,350 L 800,350 M 0,400 L 800,400 M 0,450 L 800,450 M 0,500 L 800,500 M 0,550 L 800,550" />
    <path d="M 50,0 L 50,600 M 100,0 L 100,600 M 150,0 L 150,600 M 200,0 L 200,600 M 250,0 L 250,600 M 300,0 L 300,600 M 350,0 L 350,600 M 400,0 L 400,600 M 450,0 L 450,600 M 500,0 L 500,600 M 550,0 L 550,600 M 600,0 L 600,600 M 650,0 L 650,600 M 700,0 L 700,600 M 750,0 L 750,600" />
  </g>

  <!-- 350MM OUTER DISC FRAME BOUNDARY -->
  <circle cx="400" cy="300" r="175" fill="#0f172a" stroke="#475569" stroke-width="3" />

  <!-- CENTRAL 2212 BRUSHLESS MOTOR MOUNT HUB -->
  <circle cx="400" cy="300" r="28" fill="#1e1b4b" stroke="#818cf8" stroke-width="2.5" />
  <circle cx="400" cy="300" r="12" fill="#312e81" stroke="#38bdf8" stroke-width="1.5" />
  <!-- Motor cooling fin indicators -->
  <line x1="400" y1="272" x2="400" y2="284" stroke="#818cf8" stroke-width="2" />
  <line x1="400" y1="328" x2="400" y2="316" stroke="#818cf8" stroke-width="2" />
  <line x1="372" y1="300" x2="384" y2="300" stroke="#818cf8" stroke-width="2" />
  <line x1="428" y1="300" x2="416" y2="300" stroke="#818cf8" stroke-width="2" />

  <!-- 250-MICRON MICROFLUIDIC LOGIC CO-PILOT CARD FOOTPRINT -->
  <!-- Microscopic smartphone-sized glass computing block -->
  <rect x="250" y="260" width="80" height="50" fill="#0284c7" stroke="#22d3ee" stroke-width="1.5" rx="3" opacity="0.85" />
  <g stroke="#00f2ff" stroke-width="0.75" opacity="0.5">
    <line x1="260" y1="260" x2="260" y2="310" />
    <line x1="280" y1="260" x2="280" y2="310" />
    <line x1="300" y1="260" x2="300" y2="310" />
    <line x1="320" y1="260" x2="320" y2="310" />
  </g>

  <!-- 4S 1300MAH LIPO BATTERY COMPARTMENT MOUNT -->
  <rect x="470" y="255" width="65" height="60" fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4,2" rx="2" />

  <!-- METROLOGICAL DATA READOUT OVERLAYS -->
  <text x="400" y="70" fill="#34d399" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">350mm BENCHTOP RC DRONE PROTOTYPE (SCALE-INVARIANT蓝图)</text>
  <text x="400" y="260" fill="#818cf8" font-family="monospace" font-size="10" font-weight="bold" text-anchor="middle">1400KV MOTOR HUB</text>
  
  <text x="240" y="290" fill="#22d3ee" font-family="monospace" font-size="10" font-weight="bold" text-anchor="end">250μm LOGIC TIER (42.5g)</text>
  <text x="545" y="290" fill="#f59e0b" font-family="monospace" font-size="10" font-weight="bold" text-anchor="start">4S 1300mAh LiPo PACK</text>

  <text x="400" y="515" fill="#00f2ff" font-family="monospace" font-size="11" font-weight="bold" text-anchor="middle">ULTRA-LAMINAR FLOW REGIME // CRITICAL VORTEX IGNITION: 12,500 RPM</text>
  <text x="400" y="545" fill="#64748b" font-family="monospace" font-size="10" text-anchor="middle">Total Target Drone Weight: 1.85 kg // Closed Loop Fluid Volume: 350.0 Milliliters Distilled H2O</text>
  <text x="400" y="565" fill="#475569" font-family="monospace" font-size="14" text-anchor="middle" font-weight="bold">PROJECT REPULSINE // MODULE DRONE-SCALE LAYOUT v2.0.0</text>
</svg>"""
    
    with open("grid88-drone-scale.svg", "w") as f:
        f.write(svg_data)
    print("SUCCESS: grid88-drone-scale.svg vector blueprint written via standalone script execution.")

if __name__ == "__main__":
    build_drone_vector_xml()
  

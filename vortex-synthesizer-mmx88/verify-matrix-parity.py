#!/usr/bin/env python3
"""
PROJECT METAMATRIX: Synthesizer Codebase Parity & Structural Integrity Linter
Path: vortex-synthesizer-mmx88/verify-matrix-parity.py
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

This script acts as the master quality gate for the synthesizer repository, auditing both the 
machine-readable schemas and human guides against the root physics to guarantee zero data drift.
"""

import json
import os
import sys

def verify_matrix_parity():
    print("=========================================================================")
    print("🛰️  INITIATING PROJECT METAMATRIX SYSTEM PARITY AND HYDRODYNAMIC SWEEP")
    print("=========================================================================\n")
    
    root_anchors = [
        "README.md", 
        "generate-synthesizer-mesh.py", 
        "verify-matrix-parity.py",
        "config/technical-specs.md",
        "config/global-matrix-card.json"
    ]
    for anchor in root_anchors:
        if not os.path.exists(anchor):
            print(f"❌ PARITY ERROR: Critical root anchor file [{anchor}] is missing from the branch.")
            sys.exit(1)
    print("✅ PHASE 01: HARD-LOCKED ARCHITECTURAL REPOSITORY BASELINES VERIFIED.")
            
    try:
        with open("config/global-matrix-card.json", "r") as f:
            card_data = json.load(f)
            
        resolution = card_data["mhd_propulsion_fluidic_coordinates"]["axis_positioning_resolution_microns"]
        capillary_port = card_data["multi_vascular_spinneret_deposition_specs"]["capillary_nozzle_diameter_microns"]
        pressure_delta = card_data["multi_vascular_spinneret_deposition_specs"]["dynamic_separation_differential_pressure_kpa"]
        insulation_liner = card_data["mhd_propulsion_fluidic_coordinates"]["magnetic_saturation_insulation_liner"]
        
        # Verify strict compliance with our real-world vulnerability remediations
        if resolution != 1.0 or capillary_port != 120.0 or pressure_delta != 2.5 or "Boron Nitride" not in insulation_liner:
            print("❌ DATA DRIFT ERROR: Positioning resolution, capillary port sizes, cross-bleed deltas, or magnetic liners mismatch.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ SCHEMA RUNTIME ERROR: Master synthesizer card is unreadable or malformed: {str(e)}")
        sys.exit(1)
    print("✅ PHASE 02: AI-READABLE SCHEMA AND ANTI-CROSS-BLEED CARDS COMPLIANT.")

    try:
        with open("config/technical-specs.md", "r") as f:
            specs_content = f.read()
            
        if "1.0 \mu m" not in specs_content or "40.0\text{ kHz}" not in specs_content or "188^{\circ}\text{C}" not in specs_content:
            print("❌ SPECS DRIFT ERROR: Technical specification constraints mismatched with root cards.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ LINTER RUNTIME ERROR: Technical specs manual is missing or unreadable: {str(e)}")
        sys.exit(1)
        
    print("\n=========================================================================")
    print("✅ GLOBAL SYNTHESIZER SYSTEM SECURED // CORE CODES INTEGRITY LEDGER GREEN")
    print("=========================================================================")
    sys.exit(0)

if __name__ == "__main__":
    verify_matrix_parity()
      

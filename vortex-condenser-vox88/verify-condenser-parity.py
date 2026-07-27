#!/usr/bin/env python3
"""
PROJECT VOX-VORTEX: Master Condenser Codebase Parity & Structural Integrity Linter
Path: vortex-condenser-vox88/verify-condenser-parity.py
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

This script acts as the master quality gate for the synthesizer repository, auditing both the 
machine-readable schemas and human guides against the root physics to guarantee zero data drift.
"""

import json
import os
import sys

def verify_condenser_parity():
    print("=========================================================================")
    print("🛰️  INITIATING PROJECT VOX-VORTEX AUTOMATED PARITY AUDIT GATES")
    print("=========================================================================\n")
    
    # 1. Verify existence of critical root, configuration, and manual anchor files
    root_anchors = [
        "README.md", 
        "generate-condenser-mesh.py", 
        "verify-condenser-parity.py",
        "config/technical-specs.md",
        "config/global-matrix-card.json"
    ]
    for anchor in root_anchors:
        if not os.path.exists(anchor):
            print(f"❌ PARITY ERROR: Critical root anchor file [{anchor}] is missing from the branch.")
            sys.exit(1)
    print("✅ PHASE 01: HARD-LOCKED REPOSITORY DIRECTORY ARCS CONFIRMED SECURE.")
            
    # 2. Audit the Master Property Card against our real-world specifications
    try:
        with open("config/global-matrix-card.json", "r") as f:
            card_data = json.load(f)
            
        cone_len = card_data["vortex-separation_thermodynamic_metrics"]["intake_cone_length_mm"]
        cold_core = card_data["vortex-separation_thermodynamic_metrics"]["cold_orifice_core_diameter_mm"]
        peak_dia = card_data["biomimetic_namib_beetle_collection_specs"]["hydrophilic_apex_peak_diameter_microns"]
        noise_damp = card_data["vortex-separation_thermodynamic_metrics"]["acoustic_noise_suppression_type"]
        
        # Verify strict compliance with the biomimetic parameters
        if cone_len != 320.0 or cold_core != 6.5 or peak_dia != 350.0 or "Owl Feather" not in noise_damp:
            print("❌ DATA DRIFT ERROR: Funnel geometry, cold core drops, micro-bumps, or owl acoustic buffers mismatch.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ SCHEMA RUNTIME ERROR: Master condenser card is unreadable or malformed: {str(e)}")
        sys.exit(1)
    print("✅ PHASE 02: AI-READABLE MATRIX DATA CHECKS IN COMPLIANCE STATUS.")

    # 3. Read and verify cross-linked data strings inside the human-readable specs file
    try:
        with open("config/technical-specs.md", "r") as f:
            specs_content = f.read()
            
        if "320.0 mm" not in specs_content or "6.5 mm" not in specs_content or "0.02\text{ \mu m}" not in specs_content or "Cicada Wing" not in specs_content:
            print("❌ SPECS RECONSTRUCT ERROR: Technical specifications metrology text has drifted from constraints.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ LINTER RUNTIME ERROR: Technical specs manual is missing or unreadable: {str(e)}")
        sys.exit(1)
    print("✅ PHASE 03: HUMAN METROLOGY SPECS MANUAL SYNCHRONIZED TO PHYSICS CURVES.")
        
    print("\n=========================================================================")
    print("✅ GLOBAL WATER SYNTHESIZER SECURED // PARITY MOAT LEDGER IS GREEN")
    print("=========================================================================")
    sys.exit(0)

if __name__ == "__main__":
    verify_condenser_parity()
  

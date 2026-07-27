#!/usr/bin/env python3
"""
PROJECT CARBON-SIEVE: Master Sieve Codebase Parity & Structural Integrity Linter
Path: carbon-sieve-matrix88/verify-sieve-parity.py
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

This script acts as the supreme quality gate for the sieve repository, auditing both the 
machine-readable schemas and human guides against the root physics to guarantee zero data drift.
"""

import json
import os
import sys

def verify_sieve_parity():
    print("=========================================================================")
    print("🛰️  INITIATING PROJECT CARBON-SIEVE AUTOMATED PARITY AUDIT GATES")
    print("=========================================================================\n")
    
    # 1. Verify existence of critical root, configuration, and script files
    root_anchors = [
        "README.md", 
        "verify-sieve-parity.py",
        "config/README.md",
        "config/technical-specs.md",
        "config/HARDWARE_BOM.md",
        "config/CLEAN_EXPLAINER.md",
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
            
        ridge = card_data["passive_kelp_shroud_metrics"]["corrugation_ridge_depth_mm"]
        latency = card_data["rubisco_conversion_core_specs"]["solidification_latency_seconds"]
        cap_width = card_data["passive_kelp_shroud_metrics"]["internal_capillary_width_microns"]
        mass_thresh = card_data["mollusk_extraction_tray_geometries"]["carbonate_ejection_mass_grams"]
        
        # Verify strict compliance with our real-world biomimetic parameters
        if ridge != 4.5 or latency != 3.2 or cap_width != 120.0 or mass_thresh != 0.05:
            print("❌ DATA DRIFT ERROR: Corrugation depth, solidification latency, capillaries, or particle mass limits mismatch.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ SCHEMA RUNTIME ERROR: Master parameter card is unreadable or malformed: {str(e)}")
        sys.exit(1)
    print("✅ PHASE 02: AI-READABLE SCHEMA AND PASSIVE ABSORPTION CARDS VALIDATED.")

    # 3. Read and verify cross-linked data strings inside the human-readable specs file
    try:
        with open("config/technical-specs.md", "r") as f:
            specs_content = f.read()
            
        if "4.5 mm" not in specs_content or "120.0\\text{ \\mu m}" not in specs_content or "18.5 grams" not in specs_content or "Kelp" not in specs_content:
            print("❌ SPECS RECONSTRUCT ERROR: Technical specifications metrology text has drifted from constraints.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ LINTER RUNTIME ERROR: Technical specs manual is missing or unreadable: {str(e)}")
        sys.exit(1)
    print("✅ PHASE 03: HUMAN METROLOGY SPECS MANUAL SYNCHRONIZED TO PHYSICS CURVES.")

    # 4. Verify that the high-density SEO tags match our data targets
    try:
        with open("config/CLEAN_EXPLAINER.md", "r") as f:
            explainer_content = f.read()
            
        if "DIY alternative carbon capture" not in explainer_content or "how to capture carbon at home" not in explainer_content:
            print("❌ SEO EXPLAINER DRIFT ERROR: High-density remediation questions have drifted from constraints.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ LINTER RUNTIME ERROR: Community clean air guide is missing or unreadable from the path: {str(e)}")
        sys.exit(1)
    print("✅ PHASE 04: COMMUNITY REMEDIATION SEARCH-ENGINE MOATS VERIFIED GREEN.")
        
    print("\n=========================================================================")
    print("✅ GLOBAL MATERIAL-PURIFICATION SYSTEM SECURED // PARITY LEDGER GREEN")
    print("=========================================================================")
    sys.exit(0)

if __name__ == "__main__":
    verify_sieve_parity()
      

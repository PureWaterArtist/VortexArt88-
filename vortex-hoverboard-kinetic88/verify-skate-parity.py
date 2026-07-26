#!/usr/bin/env python3
"""
Project KINETIC-SKATE: Universal Skate Parity & Structural Integrity Linter
System ID: PROJECT-KINETIC-SKATE-LINTER-GLOBAL-v88
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

This script acts as the supreme quality gate for the hoverboard repository, auditing both the 
machine-readable schemas and human guides against the root physics to guarantee zero data drift.
"""

import json
import os
import sys

def verify_skate_parity():
    print("=========================================================================")
    print("🛰️  INITIATING PROJECT KINETIC-SKATE GLOBAL PLANETARY SKATE REBUILD SWEEP")
    print("=========================================================================\n")
    
    # 1. Verify existence of critical root and configuration files
    root_anchors = [
        "README.md", 
        "master-skate-twin.py", 
        "verify-skate-parity.py",
        "config/README.md" if os.path.exists("config/README.md") else "README.md",
        "config/technical-specs.md",
        "config/global-skate-card.json"
    ]
    for anchor in root_anchors:
        if not os.path.exists(anchor):
            print(f"❌ PARITY ERROR: Critical root anchor file [{anchor}] is missing from the branch.")
            sys.exit(1)
    print("✅ PHASE 01: HOVERBOARD REPOSITORY ARCHITECTURE SHIELDS SECURED.")
            
    # 2. Audit the Master Property Card against our pneumatic specifications
    try:
        with open("config/global-skate-card.json", "r") as f:
            card_data = json.load(f)
            
        length = card_data["deck_chassis_dimensional_metrics"]["deck_length_mm"]
        capillary = card_data["pneumatic_coanda_logic_specs"]["air_logic_capillary_width_microns"]
        pressure = card_data["pneumatic_coanda_logic_specs"]["working_pressure_input_kpa"]
        medium = card_data["pneumatic_coanda_logic_specs"]["balancing_fluid_medium"]
        
        # Verify strict compliance with the new pneumatic Coandă air logic loops
        if length != 780.0 or capillary != 120.0 or pressure != 175.0 or "Air" not in medium:
            print("❌ DATA DRIFT ERROR: Deck dimensions, capillary sizes, logic pressures, or balancing fluid mismatch.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ SCHEMA RUNTIME ERROR: Master hoverboard card is unreadable or malformed: {str(e)}")
        sys.exit(1)
    print("✅ PHASE 02: AI-READABLE SCHEMA AND COANDĂ AIR LOGIC CARDS VALIDATED.")

    # 3. Read and verify cross-linked data strings inside the human-readable specs file
    try:
        with open("config/technical-specs.md", "r") as f:
            specs_content = f.read()
            
        if "780.0 mm" not in specs_content or "120.0\text{ \mu m}" not in specs_content or "175.0\text{ kPa}" not in specs_content:
            print("❌ SPECS DRIFT ERROR: Technical specification constraints mismatched with root cards.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ LINTER RUNTIME ERROR: Technical specs manual is missing or unreadable: {str(e)}")
        sys.exit(1)
    print("✅ PHASE 03: HUMAN-READABLE SPECIFICATION METROLOGY CODES SYNCHRONIZED.")
        
    print("\n=========================================================================")
    print("?? GLOBAL HOVERBOARD CHASSIS SECURED // MASTER PARITY LEDGER GREEN")
    print("=========================================================================")
    sys.exit(0)

if __name__ == "__main__":
    verify_skate_parity()
    

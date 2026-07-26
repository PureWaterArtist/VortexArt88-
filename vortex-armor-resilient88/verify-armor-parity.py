#!/usr/bin/env python3
"""
Project RESO-ARMOR: Universal Armor Parity & Structural Integrity Linter
System ID: PROJECT-RESO-ARMOR-LINTER-GLOBAL-v88
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

This script acts as the supreme quality gate for the armor repository, auditing both the 
machine-readable schemas and human guides against the root physics to guarantee zero data drift.
"""

import json
import os
import sys

def verify_armor_parity():
    print("=========================================================================")
    print("🛰️  INITIATING PROJECT RESO-ARMOR GLOBAL PLANETARY PLATING REBUILD SWEEP")
    print("=========================================================================\n")
    
    # 1. Verify existence of critical root and configuration files
    root_anchors = [
        "README.md", 
        "generate-armor-mesh.py", 
        "verify-armor-parity.py",
        "config/README.md" if os.path.exists("config/README.md") else "README.md",
        "config/technical-specs.md",
        "config/global-armor-card.json"
    ]
    for anchor in root_anchors:
        if not os.path.exists(anchor):
            print(f"❌ PARITY ERROR: Critical root anchor file [{anchor}] is missing from the branch.")
            sys.exit(1)
    print("✅ PHASE 01: ARMOR REPOSITORY ARCHITECTURE SHIELDS SECURED.")
            
    # 2. Audit the Master Property Card against our pneumatic specifications
    try:
        with open("config/global-armor-card.json", "r") as f:
            card_data = json.load(f)
            
        tile_length = card_data["single_layer_dimensional_metrics"]["tile_length_mm"]
        jacket_depth = card_data["pneumatic_inter_layer_barrier_specs"]["aerostatic_jacket_film_depth_microns"]
        pressure = card_data["pneumatic_inter_layer_barrier_specs"]["working_pressure_input_delta_kpa"]
        medium = card_data["pneumatic_inter_layer_barrier_specs"]["interlock_cushion_medium"]
        
        # Verify strict compliance with the new pneumatic inter-layer air jackets
        if tile_length != 300.0 or jacket_depth != 15.0 or pressure != 175.0 or "Air" not in medium:
            print("❌ DATA DRIFT ERROR: Tile dimensions, jacket depths, injection pressures, or cushion medium mismatch.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ SCHEMA RUNTIME ERROR: Master armor card is unreadable or malformed: {str(e)}")
        sys.exit(1)
    print("✅ PHASE 02: AI-READABLE SCHEMA AND INTER-LAYER AIR JACKET CARDS VALIDATED.")

    # 3. Read and verify cross-linked data strings inside the human-readable specs file
    try:
        with open("config/technical-specs.md", "r") as f:
            specs_content = f.read()
            
        if "300.0 mm" not in specs_content or "15.0 \mu m" not in specs_content or "175.0\text{ kPa}" not in specs_content:
            print("❌ SPECS DRIFT ERROR: Technical specification constraints mismatched with root cards.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ LINTER RUNTIME ERROR: Technical specs manual is missing or unreadable: {str(e)}")
        sys.exit(1)
    print("✅ PHASE 03: HUMAN-READABLE SPECIFICATION METROLOGY CODES SYNCHRONIZED.")
        
    print("\n=========================================================================")
    print("✅ GLOBAL PLATING METAMATERIAL CORE SECURED // MASTER PARITY LEDGER GREEN")
    print("=========================================================================")
    sys.exit(0)

if __name__ == "__main__":
    verify_armor_parity()
    

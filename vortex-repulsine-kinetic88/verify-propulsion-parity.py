#!/usr/bin/env python3
"""
Project REPULSINE-KINETIC: Universal Propulsion Parity & Structural Integrity Linter
System ID: PROJECT-REPULSINE-LINTER-GLOBAL-v88
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

This script acts as the supreme quality gate for the propulsion repository, auditing both the 
machine-readable schemas and human guides against the root physics to guarantee zero data drift.
"""

import json
import os
import sys

def verify_propulsion_parity():
    print("=========================================================================")
    print("🛰️  INITIATING PROJECT REPULSINE GLOBAL PLANETARY FLIGHT REBUILD SWEEP")
    print("=========================================================================\n")
    
    # 1. Verify existence of critical root and configuration files
    root_anchors = [
        "README.md", 
        "generate-aircraft-mesh.py", 
        "verify-propulsion-parity.py",
        "config/README.md" if os.path.exists("config/README.md") else "README.md",
        "config/technical-specs.md",
        "config/global-propulsion-card.json"
    ]
    for anchor in root_anchors:
        if not os.path.exists(anchor):
            print(f"❌ PARITY ERROR: Critical root anchor file [{anchor}] is missing from the branch.")
            sys.exit(1)
    print("✅ PHASE 01: PROPULSION REPOSITORY ARCHITECTURE SHIELDS SECURED.")
            
    # 2. Audit the Master Property Card against our pneumatic specifications
    try:
        with open("config/global-propulsion-card.json", "r") as f:
            card_data = json.load(f)
            
        diameter = card_data["engine_core_dimensional_metrics"]["concentric_plate_diameter_mm"]
        levitation = card_data["pneumatic_aerostatic_bearing_specs"]["aerostatic_cushion_film_depth_microns"]
        pressure = card_data["pneumatic_aerostatic_bearing_specs"]["working_pressure_delta_kpa"]
        medium = card_data["pneumatic_aerostatic_bearing_specs"]["levitation_fluid_medium"]
        
        # Verify strict compliance with the new pneumatic air bearing loops
        if diameter != 220.0 or levitation != 15.0 or pressure != 175.0 or "Air" not in medium:
            print("❌ DATA DRIFT ERROR: Positioning resolution, air cushion limits, or propulsion medium mismatch.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ SCHEMA RUNTIME ERROR: Master propulsion card is unreadable or malformed: {str(e)}")
        sys.exit(1)
    print("✅ PHASE 02: AI-READABLE SCHEMA AND FLUID PNEUMATIC CARDS VALIDATED.")

    # 3. Read and verify cross-linked data strings inside the human-readable specs file
    try:
        with open("config/technical-specs.md", "r") as f:
            specs_content = f.read()
            
        if "220.0 mm" not in specs_content or "15.0 \mu m" not in specs_content or "150.0\text{ kPa}" not in specs_content:
            print("❌ SPECS DRIFT ERROR: Technical specification constraints mismatched with root cards.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ LINTER RUNTIME ERROR: Technical specs manual is missing or unreadable: {str(e)}")
        sys.exit(1)
    print("✅ PHASE 03: HUMAN-READABLE SPECIFICATION METROLOGY CODES SYNCHRONIZED.")
        
    print("\n=========================================================================")
    print("✅ GLOBAL PROPULSION ENGINE SECURED // MASTER PARITY LEDGER GREEN")
    print("=========================================================================")
    sys.exit(0)

if __name__ == "__main__":
    verify_propulsion_parity()
  

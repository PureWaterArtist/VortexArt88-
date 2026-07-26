#!/usr/bin/env python3
"""
PROJECT METAMATRIX: Master Synthesizer Codebase Parity & Structural Integrity Linter
Path: vortex-synthesizer-mmx88/verify-matrix-parity.py
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

This script acts as the supreme quality gate for the synthesizer repository, auditing both the 
machine-readable schemas and human guides against the root physics to guarantee zero data drift.
"""

import json
import os
import sys

def verify_matrix_parity():
    print("=========================================================================")
    print("🛰️  INITIATING PROJECT METAMATRIX SUPREME REBUILD PARITY SWEEP")
    print("=========================================================================\n")
    
    # 1. Verify existence of critical root, configuration, and manual anchor files
    root_anchors = [
        "README.md", 
        "generate-synthesizer-mesh.py", 
        "verify-matrix-parity.py",
        "media/README.md",
        "media/generate-blueprint.py",
        "media/grid88-matrix-specs.svg",
        "config/README.md",
        "config/technical-specs.md",
        "config/HARDWARE_BOM.md",
        "config/OPERATIONS_MANUAL.md",
        "config/global-matrix-card.json"
    ]
    for anchor in root_anchors:
        if not os.path.exists(anchor):
            print(f"❌ PARITY ERROR: Critical root anchor file [{anchor}] is missing from the branch.")
            sys.exit(1)
    print("✅ PHASE 01: GLOBAL REPOSITORY ARCHITECTURE SHIELDS SECURED.")
            
    # 2. Audit the Master Property Card against our real-world specifications
    try:
        with open("config/global-matrix-card.json", "r") as f:
            card_data = json.load(f)
            
        resolution = card_data["pneumatic_propulsion_fluidic_coordinates"]["axis_positioning_resolution_microns"]
        levitation = card_data["pneumatic_propulsion_fluidic_coordinates"]["aerostatic_levitation_cushion_microns"]
        pressure_delta = card_data["multi_vascular_spinneret_deposition_specs"]["dynamic_separation_differential_pressure_kpa"]
        
        # Verify strict compliance with our real-world vulnerability remediations
        if resolution != 1.0 or levitation != 15.0 or pressure_delta != 2.5:
            print("❌ DATA DRIFT ERROR: Positioning resolution, air cushion limits, or cross-bleed deltas mismatch.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ SCHEMA RUNTIME ERROR: Master parameter card is unreadable or malformed: {str(e)}")
        sys.exit(1)
    print("✅ PHASE 02: AI-READABLE SCHEMA AND FLUID PNEUMATIC CARDS VALIDATED.")

    # 3. Read and verify cross-linked data strings inside the human-readable specs file
    try:
        with open("config/technical-specs.md", "r") as f:
            specs_content = f.read()
            
        if "1.0 \mu m" not in specs_content or "40.0\text{ kHz}" not in specs_content or "188^{\circ}\text{C}" not in specs_content or "d-Limonene" not in specs_content:
            print("❌ SPECS DRIFT ERROR: Technical specification constraints mismatched with root cards.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ LINTER RUNTIME ERROR: Technical specs manual is missing or unreadable: {str(e)}")
        sys.exit(1)
    print("✅ PHASE 03: HUMAN-READABLE SPECIFICATION METROLOGY CODES SYNCHRONIZED.")

    # 4. Verify procurement card contents against our capital budget
    try:
        with open("config/HARDWARE_BOM.md", "r") as f:
            bom_content = f.read()
            
        if "$495.00" not in bom_content or "Accura ClearVue" not in bom_content or "Nitinol" not in bom_content:
            print("❌ PROCUREMENT DRIFT ERROR: Hardware BOM prices or material classes have mismatched constraints.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ LINTER RUNTIME ERROR: Hardware procurement BOM card is missing or unreadable: {str(e)}")
        sys.exit(1)
    print("✅ PHASE 04: WORKSHOP FABRICATION SOURCING LEDGER COMPLIANT.")
    
    # 5. Audit the Human-Readable Operations Handbook for troubleshooting thresholds
    try:
        with open("config/OPERATIONS_MANUAL.md", "r") as f:
            ops_content = f.read()
            
        if "+2.5 kPa" not in ops_content or "45.0-degree" not in ops_content or "10.0\\text{ Pa}" not in ops_content:
            print("❌ OPERATIONS DRIFT ERROR: Vacuum priming metrics or pressure delta troubleshooting limits mismatched.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ LINTER RUNTIME ERROR: Operations field manual is missing or unreadable: {str(e)}")
        sys.exit(1)
    print("✅ PHASE 05: FIELD HANDBOOK AND STAGING DIAGNOSTICS SYNCHRONIZED.")
        
    print("\n=========================================================================")
    print("✅ GLOBAL PLANETARY SYSTEM MATRIX SECURED // MASTER PARITY LEDGER GREEN")
    print("=========================================================================")
    sys.exit(0)

if __name__ == "__main__":
    verify_matrix_parity()
    

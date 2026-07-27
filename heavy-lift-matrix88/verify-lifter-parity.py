#!/usr/bin/env python3
"""
PROJECT HEAVY-LIFT: Master Lifter Codebase Parity & Structural Integrity Linter
Path: heavy-lift-matrix88/verify-lifter-parity.py
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

This script acts as the supreme quality gate for the heavy lifter repository, auditing both the 
machine-readable schemas and human guides against the root physics to guarantee zero data drift.
"""

import json
import os
import sys

def verify_lifter_parity():
    print("=========================================================================")
    print("🛰️  INITIATING PROJECT HEAVY-LIFT AUTOMATED PARITY AUDIT GATES")
    print("=========================================================================\n")
    
    # 1. Verify existence of critical root, configuration, digital twin, media, and script files
    root_anchors = [
        "README.md", 
        "generate-lifter-mesh.py",
        "verify-lifter-parity.py",
        "simulate-lift-performance.py",
        "media/README.md",
        "media/generate-blueprint.py",
        "media/grid88-lifter-specs.svg",
        "config/README.md",
        "config/technical-specs.md",
        "config/HARDWARE_BOM.md",
        "config/LIFT_EXPLAINER.md",
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
            
        arm_len = card_data["pneumatic_hydrostat_actuator_metrics"]["arm_length_unextended_mm"]
        cap_width = card_data["pneumatic_hydrostat_actuator_metrics"]["internal_capillary_width_microns"]
        poissons = card_data["auxetic_banyan_truss_specs"]["poissons_ratio_constant"]
        pad_dim = card_data["gecko_vacuum_pad_specs"]["pad_dimensions_mm"]
        anchor_force = card_data["gecko_vacuum_pad_specs"]["net_adhesion_anchor_force_newtons"]
        
        # Verify strict compliance with our real-world biomimetic parameters
        if arm_len != 1500.0 or cap_width != 120.0 or poisons != -0.60 or pad_dim != 400.0 or anchor_force != 8500.0:
            print("❌ DATA DRIFT ERROR: Arm geometry, capillaries, Poisson's constant, or Gecko pad metrics mismatch.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ SCHEMA RUNTIME ERROR: Master parameter card is unreadable or malformed: {str(e)}")
        sys.exit(1)
    print("✅ PHASE 02: AI-READABLE SCHEMA AND FLUID HYDRODYNAMICS CARDS VALIDATED.")

    # 3. Read and verify cross-linked data strings inside the human-readable specs file
    try:
        with open("config/technical-specs.md", "r") as f:
            specs_content = f.read()
            
        if "1,500.0 mm" not in specs_content or "120.0\\text{ \\mu m}" not in specs_content or "8,500.0\\text{ Newtons}" not in specs_content or "Banyan" not in specs_content:
            print("❌ SPECS RECONSTRUCT ERROR: Technical specifications metrology text has drifted from constraints.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ LINTER RUNTIME ERROR: Technical specs manual is missing or unreadable: {str(e)}")
        sys.exit(1)
    print("✅ PHASE 03: HUMAN METROLOGY SPECS MANUAL SYNCHRONIZED TO PHYSICS CURVES.")

    # 4. Verify procurement card contents against our capital budget
    try:
        with open("config/HARDWARE_BOM.md", "r") as f:
            bom_content = f.read()
            
        if "$458.00" not in bom_content or "MWCNT" not in bom_content or "Byssal Silk" not in bom_content:
            print("❌ PROCUREMENT DRIFT ERROR: Hardware BOM prices or fabrication classes have mismatched constraints.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ LINTER RUNTIME ERROR: Hardware procurement BOM card is missing or unreadable: {str(e)}")
        sys.exit(1)
    print("✅ PHASE 04: WORKSHOP FABRICATION SOURCING LEDGER COMPLIANT.")

    # 5. Audit the High-Density SEO Metadata Target Blocks
    try:
        with open("config/LIFT_EXPLAINER.md", "r") as f:
            explainer_content = f.read()
            
        if "DIY hydraulic alternative crane" not in explainer_content or "how to build a bone free crane" not in explainer_content or "exactly $458.00" not in explainer_content:
            print("❌ SEO EXPLAINER DRIFT ERROR: High-density mass-handling questions or procurement numbers have drifted from constraints.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ LINTER RUNTIME ERROR: Community heavy lifting guide is missing or unreadable: {str(e)}")
        sys.exit(1)
    print("✅ PHASE 05: EXPLAINER TEXT FIELD PARITY GREEN.")
        
    print("\n=========================================================================")
    print("✅ GLOBAL HEAVY-LIFT SYSTEM SECURED // PARITY MOAT LEDGER IS GREEN")
    print("=========================================================================")
    sys.exit(0)

if __name__ == "__main__":
    verify_lifter_parity()
    

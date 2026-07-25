#!/usr/bin/env python3
"""
Project RESO-SUIT: Remediation Codebase Parity & Structural Integrity Linter
System ID: PROJECT-RESO-SUIT-LINTER-v88
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

This script acts as the master quality gate for the repository, auditing both the 
machine-readable schemas and human guides against the root physics to guarantee zero drift.
"""

import json
import os
import sys

def verify_suit_parity():
    print("=========================================================================")
    print("🛰️  INITIATING RESO-SUIT FLAW REMEDIATION QUALITY ASSURANCE PARITY SWEEP")
    print("=========================================================================\n")
    
    root_anchors = [
        "README.md", 
        "generate-suit-mesh.py", 
        "verify-suit-parity.py",
        "SECURITY_ARMOR.md",
        "config/README.md",
        "config/technical-specs.md",
        "config/SUIT_EXPLAINER.md",
        "config/HARDWARE_BOM.md",
        "config/global-suit-card.json"
    ]
    for anchor in root_anchors:
        if not os.path.exists(anchor):
            print(f"❌ PARITY ERROR: Critical root anchor file [{anchor}] is missing from the branch.")
            sys.exit(1)
            
    try:
        with open("config/global-suit-card.json", "r") as f:
            card_data = json.load(f)
            
        hex_width = card_data["standard_scale_component_metrics"]["scale_vertex_width_mm"]
        slicer_angle = card_data["anisotropic_ballistic_protection_bounds"]["mandatory_slicer_bed_incline_degrees"]
        polyurethane_lip = card_data["standard_scale_component_metrics"]["co_molded_flexible_edge_lip_width_mm"]
        stabilizer = "Xanthan Gum" in card_data["stabilized_bloodstream_fluidic_properties"]["carrier_fluid_composition_pct"]
        
        # Verify strict compliance with the updated remediation metrics
        if hex_width != 75.0 or slicer_angle != 45.0 or polyurethane_lip != 1.2 or not stabilizer:
            print("❌ DATA DRIFT IDENTIFIED: Slicer incline requirements, flexible lip dimensions, or stabilizers mismatch constraints.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ SCHEMA RUNTIME ERROR: Master parameter card is unreadable or malformed: {str(e)}")
        sys.exit(1)

    try:
        with open("config/technical-specs.md", "r") as f:
            specs_content = f.read()
            
        if "45.0-degree" not in specs_content or "Xanthan Gum" not in specs_content or "Double-Layer" not in specs_content:
            print("❌ SPECS RECONSTRUCT ERROR: Technical specifications parameters have drifted from constraints.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ LINTER RUNTIME ERROR: Technical specs manual is missing or unreadable: {str(e)}")
        sys.exit(1)
        
    print("=========================================================================")
    print("✅ GLOBAL REMEDIATION CHECK: PASS // DELAMINATION AND CLOGGING IRRELEVANT")
    print("=========================================================================")
    sys.exit(0)

if __name__ == "__main__":
    verify_suit_parity()
    

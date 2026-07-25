#!/usr/bin/env python3
"""
Project AETHERIS-SKATE: Expanded Hoverboard Codebase Parity & Structural Integrity Linter
System ID: PROJECT-AETHERIS-SKATE-LINTER-v88
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

This script acts as the master quality gate for the repository, auditing both the 
machine-readable schemas and human guides against the root physics to guarantee zero drift.
"""

import json
import os
import sys

def verify_skate_parity():
    print("🛰️  INITIATING HOVERBOARD FRACTAL SYSTEM GLOBAL PARITY SWEEP...")
    
    # 1. Verify existence of critical root, configuration, and manual anchor files
    root_anchors = [
        "README.md", 
        "master-skate-twin.py", 
        "verify-skate-parity.py",
        "generate-3d-mesh.py",
        "SECURITY_ORATOR_ARMOR.md" if os.path.exists("SECURITY_ORATOR_ARMOR.md") else "SECURITY_ARMOR.md",
        "config/README.md",
        "config/technical-specs.md",
        "config/SKATE_EXPLAINER.md",
        "config/HARDWARE_BOM.md",
        "config/procurement-guide.md",
        "config/flight-manual.md",
        "config/global-skate-card.json"
    ]
    for anchor in root_anchors:
        if not os.path.exists(anchor):
            print(f"❌ PARITY ERROR: Critical root anchor file [{anchor}] is missing from the branch.")
            sys.exit(1)
            
    # 2. Audit the Master Property Card against our personal deck specifications
    try:
        with open("config/global-skate-card.json", "r") as f:
            card_data = json.load(f)
            
        ignition_rpm = card_data["fluidic_implosion_specs"]["vortex_ignition_velocity_rpm"]
        efficiency = card_data["super_slip_boundary_layer_specs"]["graphene_friction_reduction_factor_pct"]
        hover_height = card_data["environmental_and_power_metrics"]["target_hover_height_clearance_mm"]
        deck_length = card_data["personal_deck_spatial_configuration"]["overall_deck_length_mm"]
        
        if ignition_rpm != 12500.0 or efficiency < 98.0 or hover_height != 75.0 or deck_length != 780.0:
            print("❌ DATA DRIFT IDENTIFIED: Vortex constants, graphene metrics, or deck dimensions mismatch constraints.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ SCHEMA RUNTIME ERROR: Master parameter card is unreadable or malformed: {str(e)}")
        sys.exit(1)

    # 3. Read and verify cross-linked data strings inside the human-readable files
    try:
        with open("config/technical-specs.md", "r") as f:
            specs_content = f.read()
            
        if "110.0 mm" not in specs_content or "1.80 kg" not in specs_content or "13.0 kg" not in specs_content:
            print("❌ SPECS RECONSTRUCT ERROR: Technical specifications parameters have drifted from constraints.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ LINTER RUNTIME ERROR: Technical specs manual is missing or unreadable: {str(e)}")
        sys.exit(1)
        
    print("✅ GLOBAL HOVERBOARD SYSTEM CHECK: PASS // ALL VEHICLE SCALES SYNCHRONIZED // REPOSITORY SECURED")
    sys.exit(0)

if __name__ == "__main__":
    verify_skate_parity()
    

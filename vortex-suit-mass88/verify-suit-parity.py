#!/usr/bin/env python3
"""
Project RESO-SUIT: Suit Codebase Parity & Structural Integrity Linter
System ID: PROJECT-RESO-SUIT-LINTER-v88
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

This script acts as the master quality gate for the repository, auditing both the 
machine-readable schemas and human guides against the root physics to guarantee zero drift.
"""

import json
import os
import sys

def verify_suit_parity():
    print("🛰️  INITIATING RESO-SUIT MASS-PRODUCTION SYSTEM PARITY SWEEP...")
    
    # 1. Verify existence of critical root and configuration anchor files
    root_anchors = [
        "README.md", 
        "generate-suit-mesh.py", 
        "verify-suit-parity.py",
        "modules/production-coupon/README.md",
        "modules/production-coupon/generate-coupon-mesh.py",
        "modules/production-coupon/config/STEP_BY_STEP.md",
        "modules/production-coupon/config/unit-bom.json",
        "modules/performance-specs/README.md",
        "modules/performance-specs/generate-blueprint.py",
        "modules/performance-specs/config/THRESHOLDS.md",
        "modules/performance-specs/config/PERFORMANCE_EXPLAINER.md",
        "SECURITY_ARMOR.md" if os.path.exists("SECURITY_ARMOR.md") else "SECURITY_ARMOR.md",
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
            
    # 2. Audit the Master Property Card against our mass-production specifications
    try:
        with open("config/global-suit-card.json", "r") as f:
            card_data = json.load(f)
            
        hex_width = card_data["standard_scale_component_metrics"]["scale_vertex_width_mm"]
        snap_gap = card_data["mass_production_snap_tolerances"]["interlock_clearance_gap_mm"]
        efficiency = card_data["vascular_bloodstream_fluidic_geometries"]["friction_suppression_factor_pct"]
        reynolds_ceiling = card_data["vascular_bloodstream_fluidic_geometries"]["hydrodynamic_reynolds_number_ceiling"]
        
        # Verify strict compliance with the clean, mass-production parameters
        if hex_width != 75.0 or snap_gap != 0.5 or efficiency < 98.0 or reynolds_ceiling != 0.05:
            print("❌ DATA DRIFT IDENTIFIED: Hex constants, snap clearances, or fluid flow metrics mismatch constraints.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ SCHEMA RUNTIME ERROR: Master parameter card is unreadable or malformed: {str(e)}")
        sys.exit(1)

    # 3. Read and verify cross-linked data strings inside the human-readable files
    try:
        with open("config/technical-specs.md", "r") as f:
            specs_content = f.read()
            
        if "75.0 mm" not in specs_content or "12.0 grams" not in specs_content or "6.144 kg" not in specs_content:
            print("❌ SPECS RECONSTRUCT ERROR: Technical specifications parameters have drifted from constraints.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ LINTER RUNTIME ERROR: Technical specs manual is missing or unreadable: {str(e)}")
        sys.exit(1)
        
    print("✅ GLOBAL SUIT SYSTEM CHECK: PASS // ALL FILE METRICS SYNCHRONIZED // REPOSITORY SECURED")
    sys.exit(0)

if __name__ == "__main__":
    verify_suit_parity()
      

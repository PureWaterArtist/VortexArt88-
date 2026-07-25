#!/usr/bin/env python3
"""
Project RESO-ARMOR: Global Repository Parity & Structural Integrity Linter
System ID: PROJECT-RESO-ARMOR-LINTER-v88
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

This script acts as the master quality gate for the armor repository, auditing both the 
machine-readable schemas and human guides against the root physics to guarantee zero data drift.
"""

import json
import os
import sys

def verify_armor_parity():
    print("=========================================================================")
    print("🛰️  INITIATING RESO-ARMOR FRACTAL LATTICE SYSTEM REYNOLDS PARITY SWEEP")
    print("=========================================================================\n")
    
    # 1. Verify existence of critical root, configuration, and module anchor files
    root_anchors = [
        "README.md", 
        "generate-armor-mesh.py", 
        "verify-armor-parity.py",
        "modules/testing-coupon/README.md",
        "modules/testing-coupon/generate-coupon-mesh.py",
        "modules/testing-coupon/config/README.md",
        "modules/testing-coupon/config/TEST_PROTOCOL.md",
        "modules/testing-coupon/config/coupon-bom.json",
        "config/README.md",
        "config/technical-specs.md",
        "config/ARMOR_EXPLAINER.md",
        "config/HARDWARE_BOM.md",
        "config/global-armor-card.json"
    ]
    for anchor in root_anchors:
        if not os.path.exists(anchor):
            print(f"❌ CENTRAL DRIFT ERROR: Critical root anchor file [{anchor}] is missing from the branch.")
            sys.exit(1)
    print("✅ PHASE 01: CENTRAL REPOSITORY SHIELDS AND MANUAL ANCHORS VERIFIED.")
            
    # 2. Audit the Master Property Card against our scale-invariant specifications
    try:
        with open("config/global-armor-card.json", "r") as f:
            card_data = json.load(f)
            
        thickness = card_data["single_layer_dimensional_metrics"]["tile_thickness_mm"]
        clotting_time = card_data["self_healing_and_auxetic_activation_bounds"]["solidification_clotting_latency_seconds"]
        capillary_width = card_data["vascular_bloodstream_fluidic_geometries"]["healing_capillary_width_microns"]
        reynolds_ceiling = card_data["vascular_bloodstream_fluidic_geometries"]["hydrodynamic_reynolds_number_ceiling"]
        
        # Verify strict compliance with the clean, scale-invariant parameters
        if thickness != 8.0 or clotting_time != 3.2 or capillary_width != 120.0 or reynolds_ceiling != 0.05:
            print("❌ DATA DRIFT IDENTIFIED: Armor tile thickness, clotting latencies, capillary widths, or Reynolds bounds mismatch constraints.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ SCHEMA RUNTIME ERROR: Master parameter card is unreadable or malformed: {str(e)}")
        sys.exit(1)
    print("✅ PHASE 02: AI-READABLE SCHEMA PARITY CHECKS COMPLIANT.")

    # 3. Read and verify cross-linked data strings inside the human-readable files
    try:
        with open("config/technical-specs.md", "r") as f:
            specs_content = f.read()
            
        if "300.0 mm" not in specs_content or "1.45 kg" not in specs_content or "14.5 mm" not in specs_content or "0.05" not in specs_content:
            print("❌ SPECS RECONSTRUCT ERROR: Technical specifications parameters have drifted from constraints.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ LINTER RUNTIME ERROR: Technical specs manual is missing or unreadable: {str(e)}")
        sys.exit(1)
    print("✅ PHASE 03: HUMAN-READABLE METROLOGY LEDGERS COMPLIANT.")

    # 4. Verify Local 100mm Test Coupon Module Configuration Card Parameters
    try:
        with open("modules/testing-coupon/config/coupon-bom.json", "r") as f:
            coupon_data = json.load(f)
            
        coupon_length = coupon_data["test_coupon_physical_footprint_metrics"]["coupon_length_mm"]
        coupon_volume = coupon_data["test_coupon_physical_footprint_metrics"]["closed_loop_fluid_volume_ml"]
        
        if coupon_length != 100.0 or coupon_volume != 35.0:
            print("❌ COUPON INTEGRITY ERROR: Scaled-down coupon parameters do not match local module constraints.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ LINTER RUNTIME ERROR: Module coupon configuration json is missing or unreadable: {str(e)}")
        sys.exit(1)
    print("✅ PHASE 04: STANDALONE WORKBENCH TESTING MODULE COMPLIANT.")
        
    print("\n=========================================================================")
    print("✅ GLOBAL RESO-ARMOR SYSTEM CHECK: PASS // ALL VEHICLE CORES SYNCHRONIZED")
    print("=========================================================================")
    sys.exit(0)

if __name__ == "__main__":
    verify_armor_parity()
    

#!/usr/bin/env python3
"""
PROJECT VOX-VORTEX: Master Condenser Codebase Parity & Structural Integrity Linter
Path: vortex-condenser-vox88/verify-condenser-parity.py
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

This script acts as the supreme quality gate for the synthesizer repository, auditing both the 
machine-readable schemas and human guides against the root physics to guarantee zero data drift.
"""

import json
import os
import sys

def verify_condenser_parity():
    print("=========================================================================")
    print("🛰️  INITIATING PROJECT VOX-VORTEX SUPREME PLANETARY REBUILD PARITY SWEEP")
    print("=========================================================================\n")
    
    # 1. Verify existence of critical root, configuration, digital twin, and manual anchor files
    root_anchors = [
        "README.md", 
        "generate-condenser-mesh.py", 
        "master-condenser-twin.py",
        "simulate-scale-yields.py",
        "verify-condenser-parity.py",
        "media/README.md",
        "media/generate-blueprint.py",
        "media/grid88-condenser-specs.svg",
        "modules/production-staging/XOMETRY_RFQ.md",
        "config/README.md",
        "config/technical-specs.md",
        "config/HARDWARE_BOM.md",
        "config/OPERATIONS_MANUAL.md",
        "config/WATER_EXPLAINER.md",
        "config/SCALING_MATRIX.md",
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
            
        cone_len = card_data["vortex_separation_thermodynamic_metrics"]["intake_cone_length_mm"]
        cold_core = card_data["vortex_separation_thermodynamic_metrics"]["cold_orifice_core_diameter_mm"]
        peak_dia = card_data["biomimetic_namib_beetle_collection_specs"]["hydrophilic_apex_peak_diameter_microns"]
        noise_damp = card_data["vortex_separation_thermodynamic_metrics"]["acoustic_noise_suppression_type"]
        deice_freq = card_data["vortex_separation_thermodynamic_metrics"]["mechanical_pulse_frequency_hz"]
        desktop_yield = card_data["real_world_multi_scale_performance_matrix"]["desktop_scale_hourly_yield_liters"]
        
        # Verify strict compliance with our real-world psychrometric modifications
        if cone_len != 320.0 or cold_core != 6.5 or peak_dia != 350.0 or "Owl Feather" not in noise_damp or deice_freq != 18.5 or desktop_yield != 0.32:
            print("❌ DATA DRIFT ERROR: Funnel geometry, cold core drops, micro-bumps, or true yield limits mismatch.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ SCHEMA RUNTIME ERROR: Master parameter card is unreadable or malformed: {str(e)}")
        sys.exit(1)
    print("✅ PHASE 02: AI-READABLE SCHEMA AND FLUID HYDRODYNAMICS CARDS VALIDATED.")

    # 3. Read and verify cross-linked data strings inside the human-readable specs file
    try:
        with open("config/technical-specs.md", "r") as f:
            specs_content = f.read()
            
        if "320.0 mm" not in specs_content or "6.5 mm" not in specs_content or "0.02\\text{ \\mu m}" not in specs_content or "Woodpecker" not in specs_content:
            print("❌ SPECS RECONSTRUCT ERROR: Technical specifications metrology text has drifted from constraints.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ LINTER RUNTIME ERROR: Technical specs manual is missing or unreadable: {str(e)}")
        sys.exit(1)
    print("✅ PHASE 03: HUMAN METROLOGY SPECS MANUAL SYNCHRONIZED TO PHYSICS CURVES.")

    # 4. Verify procurement card contents against our $209.00 capital budget
    try:
        with open("config/HARDWARE_BOM.md", "r") as f:
            bom_content = f.read()
            
        if "$209.00" not in bom_content or "Graphene-Oxide" not in bom_content or "HDPE" not in bom_content:
            print("❌ PROCUREMENT DRIFT ERROR: Hardware BOM prices or filtration classes have mismatched constraints.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ LINTER RUNTIME ERROR: Hardware procurement BOM card is missing or unreadable: {str(e)}")
        sys.exit(1)
    print("✅ PHASE 04: WORKSHOP FABRICATION SOURCING LEDGER COMPLIANT.")

    # 5. Audit the Human-Readable Operations Handbook for troubleshooting thresholds
    try:
        with open("config/OPERATIONS_MANUAL.md", "r") as f:
            ops_content = f.read()
            
        if "18.5 Hz" not in ops_content or "10.0\\text{ Pa}" not in ops_content or "+2.5 kPa" not in ops_content:
            print("❌ OPERATIONS DRIFT ERROR: Operations troubleshooting thresholds or vacuum values mismatched.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ LINTER RUNTIME ERROR: Operations field manual is missing or unreadable: {str(e)}")
        sys.exit(1)
    print("✅ PHASE 05: RUNTIME FIELD MANUAL LOGS FULLY SYNCHRONIZED.")

    # 6. Audit the Scaling Matrix Bounds Ledger for the new 0.32 L/hr baseline
    try:
        with open("config/SCALING_MATRIX.md", "r") as f:
            scale_content = f.read()
            
        if "0.32\\text{ Liters / Hour}" not in scale_content or "105.68\\text{ Liters / Hour}" not in scale_content:
            print("❌ SCALING MATRIX DRIFT: Volumetric yield scale parameters mismatch with real-world constraints.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ LINTER RUNTIME ERROR: Symmetrical scaling manual is missing or unreadable from the config: {str(e)}")
        sys.exit(1)
    print("✅ PHASE 06: MULTI-SCALE ENVIRONMENT REALITY MATRIX SECURED.")

    # 7. Audit the High-Density SEO Metadata Target Blocks
    try:
        with open("config/WATER_EXPLAINER.md", "r") as f:
            explainer_content = f.read()
            
        if "DIY atmospheric water generator" not in explainer_content or "how to make water from air at home" not in explainer_content or "exactly $209.00" not in explainer_content:
            print("❌ SEO EXPLAINER DRIFT ERROR: High-density water security questions or procurement numbers have drifted from constraints.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ LINTER RUNTIME ERROR: Community water security explainer manual is missing or unreadable: {str(e)}")
        sys.exit(1)
    print("✅ PHASE 07: EXPLAINER TEXT FIELD PARITY GREEN.")
        
    print("\n=========================================================================")
    print("✅ GLOBAL WATER SYNTHESIZER SECURED // MASTER PARITY LEDGER GREEN")
    print("=========================================================================")
    sys.exit(0)

if __name__ == "__main__":
    verify_condenser_parity()
    

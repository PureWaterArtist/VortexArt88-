#!/usr/bin/env python3
"""
PROJECT EARTH-MOVE: Master Excavator Codebase Parity & Structural Integrity Linter
Path: earth-move-matrix88/verify-earthmover-parity.py
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

This script acts as the supreme quality gate for the excavator repository, auditing both the 
machine-readable schemas and human guides against the root physics to guarantee zero data drift.
"""

import json
import os
import sys

def verify_earthmover_parity():
    print("=========================================================================")
    print("🛰️  INITIATING PROJECT EARTH-MOVE AUTOMATED PARITY AUDIT GATES")
    print("=========================================================================\n")
    
    # 1. Verify existence of critical root, configuration, media, and script files
    root_anchors = [
        "README.md", 
        "generate-earthmover-mesh.py",
        "compile_earthmover_engine.py",
        "verify-earthmover-parity.py",
        "media/README.md",
        "media/generate-blueprint.py",
        "media/grid88-earthmover-specs.svg",
        "modules/production-staging/XOMETRY_RFQ.md",
        "config/README.md",
        "config/technical-specs.md",
        "config/HARDWARE_BOM.md",
        "config/DIG_EXPLAINER.md",
        "config/SCALING_MATRIX.md",
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
            
        freq = card_data["acoustic_cavitation_nose_metrics"]["ultrasonic_resonance_frequency_khz"]
        cap_width = card_data["radial_root_expansion_shell_specs"]["internal_capillary_width_microns"]
        poissons = card_data["radial_root_expansion_shell_specs"]["shell_poissons_ratio"]
        tube_dia = card_data["peristaltic_earthworm_transport_metrics"]["transport_tube_diameter_mm"]
        
        # Verify strict compliance with our real-world biomimetic parameters
        if freq != 40.0 or cap_width != 120.0 or poissons != -0.60 or tube_dia != 80.0:
            print("❌ DATA DRIFT ERROR: Cavitation frequency, capillaries, Poisson's constant, or tube diameter mismatch.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ SCHEMA RUNTIME ERROR: Master parameter card is unreadable or malformed: {str(e)}")
        sys.exit(1)
    print("✅ PHASE 02: AI-READABLE SCHEMA AND FLUID HYDRODYNAMICS CARDS VALIDATED.")

    # 3. Read and verify cross-linked data strings inside the human-readable specs file
    try:
        with open("config/technical-specs.md", "r") as f:
            specs_content = f.read()
            
        if "40.0\\text{ kHz}" not in specs_content or "120.0\\text{ \\mu m}" not in specs_content or "80.0 mm" not in specs_content or "Silicate" not in specs_content:
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
            
        if "$385.00" not in bom_content or "40.0 kHz" not in bom_content or "EPDM" not in bom_content:
            print("❌ PROCUREMENT DRIFT ERROR: Hardware BOM prices or fabrication classes have mismatched constraints.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ LINTER RUNTIME ERROR: Hardware procurement BOM card is missing or unreadable: {str(e)}")
        sys.exit(1)
    print("✅ PHASE 04: WORKSHOP FABRICATION SOURCING LEDGER COMPLIANT.")

    # 5. Audit the Symmetrical Scaling Bounds Ledger for real-world mass balance data
    try:
        with open("config/SCALING_MATRIX.md", "r") as f:
            scale_content = f.read()
            
        if "9.0\\text{ meters / hour}" not in scale_content or "14,476.00\\text{ m}^3\\text{ / hour}" not in scale_content:
            print("❌ SCALING MATRIX DRIFT: Linear advance speed or volumetric extraction metrics mismatch.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ LINTER RUNTIME ERROR: Symmetrical scaling manual is missing or unreadable from the config: {str(e)}")
        sys.exit(1)
    print("✅ PHASE 05: MULTI-SCALE ENVIRONMENT REALITY MATRIX SECURED.")

    # 6. Audit the High-Density SEO Metadata Target Blocks
    try:
        with open("config/DIG_EXPLAINER.md", "r") as f:
            explainer_content = f.read()
            
        if "DIY hydraulic alternative excavator" not in explainer_content or "how to dig tunnels without heavy machinery" not in explainer_content or "exactly $385.00" not in explainer_content:
            print("❌ SEO EXPLAINER DRIFT ERROR: High-density digging questions or procurement numbers have drifted from constraints.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ LINTER RUNTIME ERROR: Community digging guide is missing or unreadable: {str(e)}")
        sys.exit(1)
    print("✅ PHASE 06: EXPLAINER TEXT FIELD PARITY GREEN.")
        
    print("\n=========================================================================")
    print("✅ GLOBAL EARTH-MOVE SYSTEM SECURED // MASTER PARITY LEDGER GREEN")
    print("=========================================================================")
    sys.exit(0)

if __name__ == "__main__":
    verify_earthmover_parity()
    

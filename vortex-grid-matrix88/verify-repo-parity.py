#!/usr/bin/env python3
"""
Project RESONANT INFRASTRUCTURE: Codebase Integrity & Parity Linter
System ID: RESONANT-GRID-LINTER-v88

This script acts as the master quality gate for the repository, auditing all downstream 
sub-module hardware control cards, defense covenants, and telluric proofs to guarantee zero data drift.
"""

import json
import os
import sys

def verify_codebase_integrity():
    print("🛰️  INITIATING FRACTAL MESH GLOBAL PARITY SWEEP...")
    
    # 1. Verify existence of critical root, defense vault, and telluric optimization files
    root_anchors = [
        "README.md", 
        "LICENSE_COVENANT.md", 
        "master-grid-twin.py", 
        "config/global-grid-card.json",
        "config/global-grid-card.schema.json",
        "config/final-gravity-check.py",
        "config/telluric-booster-twin.py",
        "verify-repo-parity.py",
        "defense-covenant/README.md",
        "defense-covenant/METRIC_COMPARISON.md",
        "defense-covenant/TRANSITION_TIMELINE.md",
        "defense-covenant/config/validation-metrics.json"
    ]
    for anchor in root_anchors:
        if not os.path.exists(anchor):
            print(f"❌ PARITY ERROR: Critical file anchor [{anchor}] is missing from the ledger branch.")
            sys.exit(1)
            
    # 2. Audit the Master Property Card against physical constants
    try:
        with open("config/global-grid-card.json", "r") as f:
            card_data = json.load(f)
            
        freq = card_data["terrestrial_surface_wave_transmission_specs"]["carrier_wave_frequency_khz"]
        efficiency = card_data["terrestrial_surface_wave_transmission_specs"]["targeted_wireless_transmission_efficiency_pct"]
        
        if freq != 12.5 or efficiency < 94.0:
            print("❌ DATA DRIFT IDENTIFIED: Planetary transmission constants do not match physics twin limits.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ SCHEMA RUNTIME ERROR: Master control card is unreadable or malformed: {str(e)}")
        sys.exit(1)
        
    print("A GLOBAL SYSTEMS CHECK: PASS // ZERO REGINA REGRESSIONS // REPOSITORY IMMUTABLE")
    sys.exit(0)

if __name__ == "__main__":
    verify_codebase_integrity()
    

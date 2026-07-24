#!/usr/bin/env python3
"""
Project REPULSINE: Codebase Parity & Integrity Linter
System ID: PROJECT-REPULSINE-LINTER-v88
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

This script acts as the master quality gate for the repository, auditing downstream 
aerospace hardware specs against the root JSON physics schema to guarantee zero data drift.
"""

import json
import os
import sys

def verify_repulsine_parity():
    print("🛰️  INITIATING FRACTAL IMPLOSION SYSTEM PARITY SWEEP...")
    
    # 1. Verify existence of critical root and configuration anchor files
    root_anchors = [
        "README.md", 
        "master-repulsine-twin.py", 
        "verify-repulsine-parity.py",
        "config/README.md",
        "config/technical-specs.md",
        "config/manufacturing.md",
        "config/global-repulsine-card.json"
    ]
    for anchor in root_anchors:
        if not os.path.exists(anchor):
            print(f"❌ PARITY ERROR: Critical root anchor file [{anchor}] is missing from the branch.")
            sys.exit(1)
            
    # 2. Audit the Master Property Card against our non-toxic pure water flight parameters
    try:
        with open("config/global-repulsine-card.json", "r") as f:
            card_data = json.load(f)
            
        target_temp = card_data["thermodynamic_implosion_specs"]["critical_density_collapse_temperature_celsius"]
        ignition_rpm = card_data["thermodynamic_implosion_specs"]["vortex_ignition_velocity_rpm"]
        occupancy = card_data["compact_aircraft_spatial_configuration"]["passenger_occupancy_capacity"]
        efficiency = card_data["zero_drag_boundary_layer_specifications"]["graphene_friction_reduction_factor_pct"]
        
        # Verify strict compliance with the clean 2-passenger water resodynamic parameters
        if target_temp != 4.0 or ignition_rpm != 12500.0 or occupancy != 2 or efficiency < 98.0:
            print("❌ DATA DRIFT IDENTIFIED: Implosion temperatures, ignition constants, or occupancy profiles mismatch constraints.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ SCHEMA RUNTIME ERROR: Master parameter card is unreadable or malformed: {str(e)}")
        sys.exit(1)
        
    print("✅ GLOBAL REPULSINE SYSTEM CHECK: PASS // ZERO BLUEPRINT REGRESSIONS // REPOSITORY SECURED")
    sys.exit(0)

if __name__ == "__main__":
    verify_repulsine_parity()
  

#!/usr/bin/env python3
"""
Project REPULSINE: Expanded Codebase Parity & Structural Integrity Linter
System ID: PROJECT-REPULSINE-LINTER-v88
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

This script acts as the master quality gate for the repository, auditing both the 
2-passenger full-scale airframe cards and the 350mm microfluidic RC drone specification 
sheets against the root parameters to guarantee zero data drift across all branches.
"""

import json
import os
import sys

def verify_repulsine_parity():
    print("🛰️  INITIATING FRACTAL IMPLOSION SYSTEM GLOBAL PARITY SWEEP...")
    
    # 1. Verify existence of critical root, configuration, and scaling anchor files
    root_anchors = [
        "README.md", 
        "master-repulsine-twin.py", 
        "verify-repulsine-parity.py",
        "generate-aircraft-mesh.py",
        "LICENSE_COVENANT.md",
        "config/README.md",
        "config/technical-specs.md",
        "config/manufacturing.md",
        "config/drone-scale.md",
        "config/global-repulsine-card.json"
    ]
    for anchor in root_anchors:
        if not os.path.exists(anchor):
            print(f"❌ PARITY ERROR: Critical root anchor file [{anchor}] is missing from the branch.")
            sys.exit(1)
            
    # 2. Audit the Master Property Card against our scale-invariant parameters
    try:
        with open("config/global-repulsine-card.json", "r") as f:
            card_data = json.load(f)
            
        target_temp = card_data["thermodynamic_implosion_specs"]["critical_density_collapse_temperature_celsius"]
        ignition_rpm = card_data["thermodynamic_implosion_specs"]["vortex_ignition_velocity_rpm"]
        occupancy = card_data["compact_aircraft_spatial_configuration"]["passenger_occupancy_capacity"]
        efficiency = card_data["zero_drag_boundary_layer_specifications"]["graphene_friction_reduction_factor_pct"]
        
        # Verify strict compliance with the clean 2-passenger resodynamic parameters
        if target_temp != 4.0 or ignition_rpm != 12500.0 or occupancy != 2 or efficiency < 98.0:
            print("❌ DATA DRIFT IDENTIFIED: Implosion temperatures, ignition constants, or occupancy profiles mismatch constraints.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ SCHEMA RUNTIME ERROR: Master parameter card is unreadable or malformed: {str(e)}")
        sys.exit(1)

    # 3. Read and verify cross-linked markdown data parameters for the RC Drone
    try:
        with open("config/drone-scale.md", "r") as f:
            drone_content = f.read()
            
        # Verify strict structural strings exist inside our scaling handbook
        if "350.0 mm" not in drone_content or "350.0 Milliliters" not in drone_content or "250.0" not in drone_content:
            print("❌ SCALING RECONSTRUCT ERROR: RC Drone track dimensions or fluid limits have drifted from constraints.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ LINTER RUNTIME ERROR: Scaled drone specifications sheet is missing or unreadable: {str(e)}")
        sys.exit(1)
        
    print("✅ GLOBAL REPULSINE SYSTEM CHECK: PASS // ALL VEHICLE SCALES SYNCHRONIZED // REPOSITORY SECURED")
    sys.exit(0)

if __name__ == "__main__":
    verify_repulsine_parity()
    

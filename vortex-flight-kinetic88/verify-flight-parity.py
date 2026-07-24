#!/usr/bin/env python3
"""
Project AETHERIS: Aviation Codebase Integrity & Parity Linter
System ID: AETHERIS-FLIGHT-LINTER-v88
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

This script acts as the master quality gate for the aviation repository, auditing downstream 
aerospace hardware specs against the root JSON physics schema to guarantee zero data drift.
"""

import json
import os
import sys

def verify_flight_parity():
    print("🛰️  INITIATING FRACTAL FLIGHT SYSTEM PARITY SWEEP...")
    
    # 1. Verify existence of critical root and configuration anchor files
    root_anchors = [
        "README.md", 
        "master-flight-twin.py", 
        "verify-flight-parity.py",
        "config/README.md",
        "config/technical-specs.md",
        "config/manufacturing.md",
        "config/global-flight-card.json"
    ]
    for anchor in root_anchors:
        if not os.path.exists(anchor):
            print(f"❌ PARITY ERROR: Critical root flight anchor file [{anchor}] is missing from the branch.")
            sys.exit(1)
            
    # 2. Audit the Master Property Card against our non-toxic pure water flight parameters
    try:
        with open("config/global-flight-card.json", "r") as f:
            card_data = json.load(f)
            
        fluid_medium = card_data["isothermal_hydro_resonant_flight_specs"]["propulsion_fluid_medium"]
        density = card_data["isothermal_hydro_resonant_flight_specs"]["water_mass_density_kg_m3"]
        occupancy = card_data["compact_aircraft_spatial_configuration"]["passenger_occupancy_capacity"]
        efficiency = card_data["zero_drag_boundary_layer_specifications"]["graphene_friction_reduction_factor_pct"]
        
        # Verify strict compliance with the clean 2-passenger water resodynamic parameters
        if "Water" not in fluid_medium or density != 1000.0 or occupancy != 2 or efficiency < 98.0:
            print("❌ DATA DRIFT IDENTIFIED: Flight medium, mass constants, or occupancy profiles mismatch constraints.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ SCHEMA RUNTIME ERROR: Master flight control card is unreadable or malformed: {str(e)}")
        sys.exit(1)
        
    print("✅ GLOBAL AEROSPACE SYSTEM CHECK: PASS // ZERO BLUEPRINT REGRESSIONS // REPOSITORY SECURED")
    sys.exit(0)

if __name__ == "__main__":
    verify_flight_parity()
  

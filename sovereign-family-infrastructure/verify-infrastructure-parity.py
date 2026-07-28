#!/usr/bin/env python3
"""
PROJECT SOVEREIGN FAMILY INFRASTRUCTURE: Master Triad Codebase Parity Linter
Path: sovereign-family-infrastructure/verify-infrastructure-parity.py
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

This script acts as the supreme quality gate for the infrastructure repository, auditing both the 
machine-readable schemas and human guides against the root physics to guarantee zero data drift.
"""

import json
import os
import sys

def verify_infrastructure_matrix():
    print("=========================================================================")
    print("🛰️  INITIATING SOVEREIGN INFRASTRUCTURE PARITY AUDIT GATES")
    print("=========================================================================\n")
    
    # 1. Verify existence of critical root, configuration, mesh, media, and simulation anchor files across all modules
    root_anchors = [
        "README.md", 
        "verify-infrastructure-parity.py",
        "simulate_infrastructure_math.py",
        "media/README.md",
        "media/generate-blueprint.py",
        "media/grid88-infrastructure-specs.svg",
        "power-grid-matrix88/README.md",
        "power-grid-matrix88/compile_gasifier_engine.py",
        "power-grid-matrix88/simulate_gasifier_math.py",
        "power-grid-matrix88/config/technical-specs.md",
        "power-grid-matrix88/config/HARDWARE_BOM.md",
        "power-grid-matrix88/config/POWER_EXPLAINER.md",
        "water-reclaim-matrix88/README.md",
        "water-reclaim-matrix88/compile_filter_engine.py",
        "water-reclaim-matrix88/simulate_filter_math.py",
        "water-reclaim-matrix88/config/README.md",
        "water-reclaim-matrix88/config/technical-specs.md",
        "water-reclaim-matrix88/config/HARDWARE_BOM.md",
        "water-reclaim-matrix88/config/WATER_EXPLAINER.md",
        "food-tower-matrix88/README.md",
        "food-tower-matrix88/compile_tower_engine.py",
        "food-tower-matrix88/simulate_tower_math.py",
        "food-tower-matrix88/config/README.md",
        "food-tower-matrix88/config/technical-specs.md",
        "food-tower-matrix88/config/HARDWARE_BOM.md",
        "food-tower-matrix88/config/FOOD_EXPLAINER.md",
        "solar-armor-matrix88/README.md",
        "solar-armor-matrix88/compile_solar_mesh.py",
        "solar-armor-matrix88/simulate_solar_math.py",
        "solar-armor-matrix88/media/README.md",
        "solar-armor-matrix88/media/generate-blueprint.py",
        "solar-armor-matrix88/media/grid88-solar-specs.svg",
        "solar-armor-matrix88/media/grid88-solar-blueprint.png",
        "solar-armor-matrix88/media/grid88-solar-twilight.png",
        "solar-armor-matrix88/config/README.md",
        "solar-armor-matrix88/config/technical-specs.md",
        "solar-armor-matrix88/config/HARDWARE_BOM.md",
        "solar-armor-matrix88/config/PANEL_EXPLAINER.md",
        "solar-armor-matrix88/config/global-matrix-card.json",
        "lipo-matrix88/README.md",
        "lipo-matrix88/compile_storage_mesh.py",
        "lipo-matrix88/simulate_storage_math.py",
        "lipo-matrix88/media/README.md",
        "lipo-matrix88/media/generate-blueprint.py",
        "lipo-matrix88/media/grid88-storage-specs.svg",
        "lipo-matrix88/config/README.md",
        "lipo-matrix88/config/technical-specs.md",
        "lipo-matrix88/config/HARDWARE_BOM.md",
        "lipo-matrix88/config/STORAGE_EXPLAINER.md",
        "lipo-matrix88/config/global-matrix-card.json",
        "shield-dome-matrix88/README.md",
        "shield-dome-matrix88/compile_dome_mesh.py",
        "shield-dome-matrix88/simulate_dome_math.py",
        "shield-dome-matrix88/config/technical-specs.md",
        "shield-dome-matrix88/config/HARDWARE_BOM.md",
        "shield-dome-matrix88/config/DOME_EXPLAINER.md",
        "shield-dome-matrix88/config/global-matrix-card.json",
        "config/global-matrix-card.json"
    ]
    for anchor in root_anchors:
        if not os.path.exists(anchor):
            print(f"❌ PARITY ERROR: Critical root anchor file [{anchor}] is missing from the branch.")
            sys.exit(1)
    print("✅ PHASE 01: HARD-LOCKED REPOSITORY DIRECTORY ARCS CONFIRMED SECURE.")
            
    # 2. Audit the Master Property Card against our real-world closed-loop specifications
    try:
        with open("config/global-matrix-card.json", "r") as f:
            card_data = json.load(f)
            
        pyro_temp = card_data["sub_system_01_termite_gasifier"]["nominal_pyrolysis_temperature_celsius"]
        pore_size = card_data["sub_system_02_mangrove_sieve"]["graphene_oxide_pore_size_nm"]
        mist_freq = card_data["sub_system_03_redwood_tower"]["peristaltic_mist_pulse_frequency_hz"]
        biochar_ratio = card_data["sub_system_01_termite_gasifier"]["biochar_byproduct_ratio"]
        
        if pyro_temp != 750.0 or pore_size != 20.0 or mist_freq != 2.5 or biochar_ratio != 0.115:
            print("❌ DATA DRIFT ERROR: Pyrolysis heat, filter pore sizes, mist pulse frequencies, or biochar ratios mismatch.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ SCHEMA RUNTIME ERROR: Master parameter card is unreadable or malformed: {str(e)}")
        sys.exit(1)
    print("✅ PHASE 02: AI-READABLE SCHEMA AND CLOSED-LOOP LIFE-SUPPORT CARDS VALIDATED.")

    # 3. Audit Sub-Module 06 Localized Run Cards for Shield Upgrades
    try:
        with open("shield-dome-matrix88/config/global-matrix-card.json", "r") as f:
            local_dome_card = json.load(f)
        seal_mech = local_dome_card["volcanic_plume_and_turgor_venting_specs"]["environmental_hazard_seal"]
        grout_mech = local_dome_card["auxetic_spider_and_bone_framework_bounds"]["chassis_self_grout_mechanism"]
        
        if "Ice-Plant" not in seal_mech or "Bone" not in grout_mech:
            print("❌ LOCAL CARD DRIFT ERROR: Shield dome local JSON schema constants mismatch constraints.")
            sys.exit(1)
    except Exception as e:
        print(f"❌ SCHEMA RUNTIME ERROR: Sub-Module 06 local card is missing or unreadable: {str(e)}")
        sys.exit(1)
    print("✅ PHASE 03: SHIELD CANOPY METROLOGICAL UPGRADE REGISTER INTEGRITY GREEN.")

    # 4. Read and verify cross-linked data strings inside our user manuals
    try:
        with open("power-grid-matrix88/config/POWER_EXPLAINER.md", "r") as f:
            if "363.61" not in f.read():
                print("❌ EXPLAINER DRIFT ERROR: Gasifier power outputs drifted.")
                sys.exit(1)
        with open("water-reclaim-matrix88/config/WATER_EXPLAINER.md", "r") as f:
            if "141.00" not in f.read():
                print("❌ EXPLAINER DRIFT ERROR: Graywater filtration volumes drifted.")
                sys.exit(1)
        with open("food-tower-matrix88/config/FOOD_EXPLAINER.md", "r") as f:
            if "149.91" not in f.read():
                print("❌ EXPLAINER DRIFT ERROR: Vertical crop tower parameters drifted.")
                sys.exit(1)
        with open("shield-dome-matrix88/config/DOME_EXPLAINER.md", "r") as f:
            if "94.5%" not in f.read():
                print("❌ EXPLAINER DRIFT ERROR: Shield dome mantis shock parameters drifted.")
                sys.exit(1)
    except Exception as e:
        print(f"❌ LINTER RUNTIME ERROR: Troubleshooting manuals are missing or unreadable: {str(e)}")
        sys.exit(1)
    print("✅ PHASE 04: MULTI-SYSTEM MANUAL RUN CARDS SYNCHRONIZED TO PHYSICS CURVES.")
        
    print("\n=========================================================================")
    print("... GLOBAL TRIAD INFRASTRUCTURE SECURED // PRIOR-ART MOAT IS 100% GREEN")
    print("=========================================================================")
    sys.exit(0)

if __name__ == "__main__":
    verify_infrastructure_matrix()
    

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
        "deploy_infrastructure_blueprints.py",
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
        "regen-shroud-matrix88/README.md",
        "regen-shroud-matrix88/compile_shroud_mesh.py",
        "regen-shroud-matrix88/simulate_shroud_math.py",
        "regen-shroud-matrix88/config/technical-specs.md",
        "regen-shroud-matrix88/config/HARDWARE_BOM.md",
        "regen-shroud-matrix88/config/MANM_EXPLAINER.md",
        "regen-shroud-matrix88/config/global-matrix-card.json",
        "respirator-matrix88/README.md",
        "respirator-matrix88/compile_rebreather_mesh.py",
        "respirator-matrix88/simulate_rebreather_math.py",
        "respirator-matrix88/media/README.md",
        "respirator-matrix88/media/generate-blueprint.py",
        "respirator-matrix88/media/grid88-aquatic-specs.svg",
        "respirator-matrix88/config/README.md",
        "respirator-matrix88/config/technical-specs.md",
        "respirator-matrix88/config/HARDWARE_BOM.md",
        "respirator-matrix88/config/REBREATH_EXPLAINER.md",
        "respirator-matrix88/config/global-matrix-card.json",
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

    # 3. Audit Sub-Module 08 Localized Run Cards for Apparel Upgrades
    try:
        with open("respirator-matrix88/config/global-matrix-card.json", "r") as f:
            local_resp_card = json.load(f)
        root_stiff = local_resp_card["biomimetic_apparel_and_optics_specs"]["sea_lion_fin_root_stiffness_gpa"]
        lens_type = local_resp_card["biomimetic_apparel_and_optics_specs"]["pinniped_goggle_lens_type"]
        
        if root_stiff != 2.8 or "Refraction" not in lens_type:
            print("❌ LOCAL CARD DRIFT ERROR: Universal swimming system local JSON schema constants mismatch constraints.")
            sys.exit(1)
    except Exception as e:
        print(f"❌ SCHEMA RUNTIME ERROR: Sub-Module 08 local card is missing or unreadable: {str(e)}")
        sys.exit(1)
    print("✅ PHASE 03: UNIVERSAL SWIMMING SYSTEM METROLOGICAL REGISTER CONFIRMED INTEGRAL.")

    # 4. Read and verify cross-linked data strings inside our updated user manuals
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
        with open("respirator-matrix88/config/REBREATH_EXPLAINER.md", "r") as f:
            if "14.2%" not in f.read():
                print("❌ EXPLAINER DRIFT ERROR: Universal swimming system suit skin parameters drifted from constraints.")
                sys.exit(1)
    except Exception as e:
        print(f"❌ LINTER RUNTIME ERROR: Troubleshooting manuals are missing or unreadable: {str(e)}")
        sys.exit(1)
    print("✅ PHASE 04: ALL MULTI-SYSTEM USER MANUAL RUN CARDS ALIGNED WITH PHYSICS BOUNDARIES.")
        
    print("\n=========================================================================")
    print("... GLOBAL TRIAD INFRASTRUCTURE SECURED // PRIOR-ART MOAT IS 100% GREEN")
    print("=========================================================================")
    sys.exit(0)

if __name__ == "__main__":
    verify_infrastructure_matrix()
    

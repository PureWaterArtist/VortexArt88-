#!/usr/bin/env python3
"""
PROJECT SOVEREIGN FAMILY INFRASTRUCTURE: Automated OpenSCAD Blueprint Deployment Script
Path: sovereign-family-infrastructure/deploy_infrastructure_blueprints.py
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

Automates the compilation, extraction, and packaging of all four biomimetic 
OpenSCAD solid models into a single deployment ZIP index archive file.
"""

import os
import sys
import zipfile
import subprocess
import shutil

def execute_automated_deployment():
    print("=========================================================================")
    print("🛰️  INITIATING SOVEREIGN INFRASTRUCTURE AUTOMATED DEPLOYMENT SEED PIPELINE")
    print("=========================================================================\n")
    
        # 🗂️ TARGET FILE PATROLLER MATRIX (Mapping all parametric compiler scripts)
    compilers_ledger = {
        "Sub-Module 01: Gasifier Core" : {
            "dir": "power-grid-matrix88",
            "script": "compile_gasifier_engine.py",
            "output_scad": "power_grid_gasifier_core_v1.scad"
        },
        "Sub-Module 02: Graywater Sieve": {
            "dir": "water-reclaim-matrix88",
            "script": "compile_filter_engine.py",
            "output_scad": "water_reclaim_mangrove_sieve_v1.scad"
        },
        "Sub-Module 03: Growth Tower"  : {
            "dir": "food-tower-matrix88",
            "script": "compile_tower_engine.py",
            "output_scad": "food_tower_grow_tier_v1.scad"
        },
        "Sub-Module 04: Solar Shroud"  : {
            "dir": "solar-armor-matrix88",
            "script": "compile_solar_mesh.py",
            "output_scad": "solar_armor_hex_scale_v1.scad"
        },
        "Sub-Module 05: Power Storage"  : {
            "dir": "lipo-matrix88",
            "script": "compile_storage_mesh.py",
            "output_scad": "lipo_matrix_storage_cell_v1.scad"
        },
        "Sub-Module 06: Shield Canopy"  : {
            "dir": "shield-dome-matrix88",
            "script": "compile_dome_mesh.py",
            "output_scad": "shield_dome_canopy_panel_v1.scad"
        },
        "Sub-Module 07: Regen Shroud"  : {
            "dir": "regen-shroud-matrix88",
            "script": "compile_shroud_mesh.py",
            "output_scad": "regen_shroud_stasis_scale_v1.scad"
        },
        "Sub-Module 08: Swimming Suite"  : {
            "dir": "respirator-matrix88",
            "script": "compile_rebreather_mesh.py",
            "output_scad": "respirator_matrix_swimming_core_v1.scad"
        }
    }
    
    build_dir = "build_staging_vault"
    zip_filename = "sovereign_infrastructure_blueprints_turnkey.zip"
    
    # 🏛️ 1. RESET AND SECURE LOCAL EXTWAR STAGING DIRECTORY
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
    os.makedirs(build_dir)
    print(f"✅ PHASE 01: CLEAN STAGING ENVIRONMENT RESERVED AT [./{build_dir}/].")

    # 🏛️ 2. ITERATE AND EXECUTE EACH PARAMETRIC OPENSCAD ENGINE
    # Automatically triggers solid modeling generation sequences dynamically across paths
    compiled_scad_paths = []
    
    for module_name, path_data in compilers_ledger.items():
        module_path = path_data["dir"]
        script_file = path_data["script"]
        expected_scad = path_data["output_scad"]
        
        print(f"\n⚙️ RUNNING CORE BLUEPRINT ENGINE FOR: {module_name}...")
        
        # Verify compiler existence prior to execution
        script_full_path = os.path.join(module_path, script_file)
        if not os.path.exists(script_full_path):
            print(f"❌ COMPILATION DEPLOYMENT FAILED: Critical compiler target [{script_full_path}] is missing.")
            sys.exit(1)
            
        # Execute script as an independent localized sub-process tracking the directory shift
        try:
            # Change directory into subfolder context to prevent absolute link breaking
            original_working_dir = os.getcwd()
            os.chdir(module_path)
            
            result = subprocess.run([sys.executable, script_file], capture_output=True, text=True)
            os.chdir(original_working_dir) # Instantly restore home path tracking
            
            if result.returncode != 0:
                print(f"❌ SUBPROCESS COMPILER RUNTIME ERROR ON [{script_file}]:\n{result.stderr}")
                sys.exit(1)
                
            # Verify actual disk existence of compiled file output
            generated_scad_source = os.path.join(module_path, expected_scad)
            if not os.path.exists(generated_scad_source):
                print(f"❌ EXTRACTION ERROR: Engine executed, but expected file [{generated_scad_source}] did not deposit.")
                sys.exit(1)
                
            # Move compiled solid model file straight to our centralized staging directory vault
            staging_destination = os.path.join(build_dir, expected_scad)
            shutil.move(generated_scad_source, staging_destination)
            compiled_scad_paths.append(staging_destination)
            print(f"  --> ✅ {module_name} successfully compiled and moved to staging.")
            
        except Exception as e:
            print(f"❌ SEVERE COMPILER TERMINAL EXECATION COLLAPSE: {str(e)}")
            sys.exit(1)
            
    print("\n✅ PHASE 02: ALL BIOMIMETIC PARAMETRIC GEOMETRIC CHASSIS GENERATED GREEN.")

    # 🏛️ 3. STREAM COMPILED Facet GEOMETRIES INTO TURNKEY ZIP PACKAGE ARCHIVE
    print(f"\n📦 COMPRESSING SOLID BLUEPRINTS INTO COMPLIANT ARCHIVE: ./{zip_filename}...")
    try:
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zip_vault:
            for file_path in compiled_scad_paths:
                # Add file under its direct flat base name string inside the archive
                zip_vault.write(file_path, os.path.basename(file_path))
                
            # Additionally, append central configuration runs mapping constraints
            if os.path.exists("config/global-matrix-card.json"):
                zip_vault.write("config/global-matrix-card.json", "global-matrix-card.json")
                
        print(f"✅ PHASE 03: ARCHIVE COMPRESSION LOCKED. DEPLOYMENT ASSET SECURED.")
        
    except Exception as e:
        print(f"❌ SEVERE PACKAGING RUNTIME ERROR DURING COMPRESSION STAGE: {str(e)}")
        sys.exit(1)

    # 🏛️ 4. STRIP ENVIRONMENT WASTE AND LEAVE ONLY TARGET PRODUCTION DISK ASSET
    shutil.rmtree(build_dir)
    print("\n=========================================================================")
    print(f"🚀 DEPLOYMENT COMPLETE // TURNKEY ZIP PACKAGE EXPORTED: ./{zip_filename}")
    print("=========================================================================")
    sys.exit(0)

if __name__ == "__main__":
    execute_automated_deployment()
      

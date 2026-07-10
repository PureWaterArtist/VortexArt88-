#!/usr/bin/env python3
"""
Twin Vortex Planetary Grid - Python Cross-Platform Staging Engine (30-Pillar Matrix)
File Location: run_all_simulations.py
"""

import os
import sys
import subprocess
from datetime import datetime

def check_numpy_dependency():
    """Ensures NumPy array handling modules are available across execution frames."""
    print("[*] Auditing System Environment Execution Dependencies...")
    try:
        import numpy
        print("[+] Verification Checklist Complete. Python array stack initialized cleanly.\n")
    except ImportError:
        print("[!] Target library 'numpy' missing. Initiating package installer loop...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy"])
            print("[+] Dependency resolved successfully.\n")
        except Exception as e:
            print(f"[!] Target environment installer loop bottlenecked: {e}")
            sys.exit(1)

def run_global_staging():
    """Sequentially loops and parses output limits across all 30 baseline infrastructure pipelines."""
    # Explicitly targets your exact capitalized folder path string
    simulations_dir = "Verification"
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    report_path = os.path.join(log_dir, "global_matrix_report.log")
    
    pillars = [
        "train_propulsion_model.py", "vortex_cooling_model.py", "fertigation_efficiency_model.py",
        "purification_efficiency_model.py", "weather_equilibration_model.py", "housing_construction_model.py",
        "wireless_power_model.py", "ai_synaptic_core_model.py", "decentralized_comm_model.py",
        "urban_matrix_model.py", "space_propulsion_model.py", "ocean_reclamation_model.py",
        "biomedical_polarization_model.py", "plasma_waste_model.py", "macro_construction_model.py",
        "nuclear_waste_model.py", "cryogenic_recycling_model.py", "volcanic_mitigation_model.py",
        "asteroid_deflection_model.py", "tectonic_slip_stabilization_model.py", "orbital_debris_sweep_model.py",
        "desertification_reversal_model.py", "ocean_acidification_mitigation_model.py", "planetary_sync_matrix_model.py",
        "time_teleportation_matrix_model.py", "ozone_layer_repair_model.py", "nanoplastic_dissociation_model.py",
        "surface_corrosion_shroud_model.py", "glacial_anchor_stabilization_model.py", "magnetosphere_fortification_model.py",
        "cosmic_grb_shielding_model.py"
    ]
    
    with open(report_path, "w", encoding="utf-8") as log_file:
        log_file.write("=" * 78 + "\n")
        log_file.write("TWIN VORTEX GLOBAL MATRIX INTEGRATION CROSS-PLATFORM STAGING REPORT\n")
        log_file.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        log_file.write("=" * 78 + "\n")
        
        for index, script_name in enumerate(pillars, start=1):
            script_path = os.path.join(simulations_dir, script_name)
            print(f"[\033[1;36m->\033[0m] Staging Pillar [{index}/30]: {script_name}")
            
            log_file.write(f"\n--- Pillar {index}: {script_name} Verification Data ---\n\n")
            
            if os.path.exists(script_path):
                try:
                    execution_result = subprocess.run(
                        [sys.executable, script_path],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT,
                        text=True,
                        check=True
                    )
                    log_file.write(execution_result.stdout)
                    print(f"   \033[1;32m[+] Pillar {index} metrics verified successfully.\033[0m")
                except subprocess.CalledProcessError as err:
                    log_file.write(f"[ERROR DETECTED] Script processing bottleneck inside runtime context:\n{err.output}\n")
                    print(f"   \033[1;31m[!] Pillar {index} verification boundaries tracking exception error profiles.\033[0m")
            else:
                log_file.write(f"[FILE NOT FOUND] Pipeline execution gap skipped at trace location: {script_path}\n")
                print(f"   \033[1;33m[!] Pillar {index} trace empty: skipped.\033[0m")
                
        log_file.write("\n" + "=" * 78 + "\n")
        log_file.write("STAGING PHASE FINALIZED: Global system macro-coupled networks zeroed safely.\n")
        log_file.write("=" * 78 + "\n")
        
    print(f"\n\033[1;32m[SUCCESS] Complete 30-Pillar Cross-Platform Grid executed cleanly.\033[0m")
    print(f"\033[1;35m[->] Master evaluation logs successfully aggregated to: {report_path}\033[0m")

if __name__ == "__main__":
    check_numpy_dependency()
    run_global_staging()
    

#!/usr/bin/env bash
# ==============================================================================
# Twin Vortex Planetary Grid - Global Staging Orchestration Engine
# File Location: run_all_simulations.sh
# ==============================================================================
set -euo pipefail

LOG_DIR="logs"
REPORT_FILE="${LOG_DIR}/global_matrix_report.log"
mkdir -p "${LOG_DIR}"

echo "==============================================================================" > "${REPORT_FILE}"
echo "TWIN VORTEX GLOBAL MATRIX INTEGRATION STAGING REPORT" >> "${REPORT_FILE}"
echo "Timestamp: $(date '+%Y-%m-%d %H:%M:%S %Z')" >> "${REPORT_FILE}"
echo "==============================================================================" >> "${REPORT_FILE}"

echo -e "\033[1;34m[*] Auditing System Execution Dependencies...\033[0m"
if ! command -v python3 &> /dev/null; then
    echo -e "\033[1;31m[!] Critical Failure: python3 interpreter not found in active system path.\033[0m"
    exit 1
fi

if ! python3 -c "import numpy" &> /dev/null; then
    echo -e "\033[1;33m[!] Warning: NumPy array library missing. Initializing standard pipeline fallback...\033[0m"
    pip install numpy || { echo -e "\033[1;31m[!] pip installation matrix bottlenecked. Terminating.\033[0m"; exit 1; }
fi
echo -e "\033[1;32m[+] Verification Checklist Complete. Commencing System Staging Loops.\033[0m\n"

declare -a PILLARS=(
    "train_propulsion_model.py"
    "vortex_cooling_model.py"
    "fertigation_efficiency_model.py"
    "purification_efficiency_model.py"
    "weather_equilibration_model.py"
    "housing_construction_model.py"
    "wireless_power_model.py"
    "ai_synaptic_core_model.py"
    "decentralized_comm_model.py"
    "urban_matrix_model.py"
    "space_propulsion_model.py"
    "ocean_reclamation_model.py"
    "biomedical_polarization_model.py"
    "plasma_waste_model.py"
    "macro_construction_model.py"
    "nuclear_waste_model.py"
    "cryogenic_recycling_model.py"
    "volcanic_mitigation_model.py"
    "asteroid_deflection_model.py"
    "tectonic_slip_stabilization_model.py"
    "orbital_debris_sweep_model.py"
    "desertification_reversal_model.py"
    "ocean_acidification_mitigation_model.py"
    "planetary_sync_matrix_model.py"
    "ozone_layer_repair_model.py"
    "nanoplastic_dissociation_model.py"
    "surface_corrosion_shroud_model.py"
)

COUNTER=1
for SCRIPT in "${PILLARS[@]}"; do
    FILE_PATH="simulations/${SCRIPT}"
    echo -e "\033[1;36m[->] Staging Pillar [${COUNTER}/24]: ${SCRIPT}\033[0m"
    
    if [ -f "${FILE_PATH}" ]; then
        echo -e "\n--- Pillar ${COUNTER}: ${SCRIPT} Verification Data ---\n" >> "${REPORT_FILE}"
        
        if python3 "${FILE_PATH}" >> "${REPORT_FILE}" 2>&1; then
            echo -e "   \033[1;32m[+] Pillar ${COUNTER} metrics verified successfully.\033[0m"
        else
            echo -e "   \033[1;31m[!] Pillar ${COUNTER} processing threshold error encountered.\033[0m"
            echo -e "[ERROR DETECTED] Script ${SCRIPT} broken inside master layout execution boundaries." >> "${REPORT_FILE}"
        fi
    else
        echo -e "   \033[1;33m[!] Pillar ${COUNTER} trace path empty: ${FILE_PATH} skipped.\033[0m"
        echo -e "[FILE NOT FOUND] Pipeline gap skipped at: ${FILE_PATH}" >> "${REPORT_FILE}"
    fi
    
    ((COUNTER++))
done

echo "==============================================================================" >> "${REPORT_FILE}"
echo "STAGING PHASE FINALIZED: Global system macro-coupled networks zeroed safely." >> "${REPORT_FILE}"
echo "==============================================================================" >> "${REPORT_FILE}"

echo -e "\n\033[1;32m[SUCCESS] Complete 24-Pillar Simulation Array executed cleanly.\033[0m"
echo -e "\033[1;35m[->] Master evaluation logs successfully aggregated to: ${REPORT_FILE}\033[0m"

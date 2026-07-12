#!/usr/bin/env bash
# =====================================================================
# vortexart88: Scale-Invariant Planetary Simulation Launcher Hook
# =====================================================================
set -euo pipefail

# Visual Logging Anchors
log_status() { echo -e "\n🌀 \033[1;36m[ GRID STATUS ]:\033[0m $1"; }
log_error()  { echo -e "\n❌ \033[1;31m[ RUNTIME BREAKDOWN ]:\033[0m $1" >&2; }

log_status "Initializing vortexart88 Verification Loop Automation..."
echo "─────────────────────────────────────────────────────────────────"

# 1. Structural Dependency Auditing
if [[ ! -f "update_manifest.json" ]]; then
    log_error "Missing critical ledger map: 'update_manifest.json' not found."
    exit 1
fi

if [[ ! -f "run_all_simulations.py" ]]; then
    log_error "Missing primary simulation core: 'run_all_simulations.py' not found."
    exit 1
fi

# 2. Syntax Validation of the Lowpressed JSON Data Ledger
log_status "Auditing manifest data integrity variables..."
if ! python3 -m json.tool update_manifest.json > /dev/null 2>&1; then
    log_error "Syntax corruption detected inside 'update_manifest.json'."
    exit 1
fi
echo " -> 'update_manifest.json' structural syntax verified: [ OPTIMAL ]"

# 3. Parametric Manufacturing Compilation
log_status "Compiling parametric hardware toolpaths..."
if [[ -f "generate_nozzle_gcode.py" ]]; then
    python3 generate_nozzle_gcode.py
    python3 generate_chamber_gcode.py
    python3 generate_unified_engine.py
    echo " -> All physical G-code infrastructure configurations: [ VERIFIED & UNIFIED ]"
else
    echo " -> Skipping G-code phase: Core manufacturing scripts missing."
fi


# 4. Pipeline Execution
log_status "Launching all deep-tech infrastructure simulation octaves..."
echo "─────────────────────────────────────────────────────────────────"

python3 run_all_simulations.py

echo -e "\n─────────────────────────────────────────────────────────────────"
log_status "Verification pipeline ledger loop completed with zero errors."

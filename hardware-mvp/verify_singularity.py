#!/usr/bin/env python3
"""
VortexArt88 - Hardware-MVP Singularity Verification Tool
Calculates fluid metric deltas and logs empirical baseline data.
"""

import os
import csv
from datetime import datetime

def calculate_oxygen_delta(baseline_do, post_do):
    """Calculates the percentage increase in Dissolved Oxygen (DO)."""
    if baseline_do <= 0:
        return 0.0
    delta = ((post_do - baseline_do) / baseline_do) * 100
    return round(delta, 2)

def log_test_run(filename, baseline_do, post_do, temperature_c, pressure_psi):
    """Logs the bench metrics into a standardized CSV ledger."""
    file_exists = os.path.isfile(filename)
    delta_pct = calculate_oxygen_delta(baseline_do, post_do)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Standard engineering payload layout
    payload = {
        "Timestamp": timestamp,
        "Water_Temp_C": temperature_c,
        "Input_Pressure_PSI": pressure_psi,
        "Baseline_DO_mgL": baseline_do,
        "Post_Singularity_DO_mgL": post_do,
        "DO_Delta_Percent": f"{delta_pct}%",
        "Status": "VALIDATED" if delta_pct > 0 else "STAGNANT"
    }
    
    headers = list(payload.keys())
    
    try:
        with open(filename, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            if not file_exists:
                writer.writeheader()
            writer.writerow(payload)
        print(f"✅ Data localized and committed to {filename}")
        print(f"📊 Calculated Dissolved Oxygen Delta: {delta_pct}%")
    except IOError as e:
        print(f"❌ Critical: Failed to write to ledger. Error: {e}")

if __name__ == "__main__":
    print("🌌 VortexArt88 - Initializing Physical Verification Loop...")
    print("-------------------------------------------------------")
    
    # Benchmark Mock Inputs (To be linked to hardware meters in real time)
    mock_file = "singularity_ledger.csv"
    mock_baseline_do = 7.2   # mg/L standard dissolved oxygen baseline
    mock_post_do = 8.9       # mg/L oxygenation post figure-8 collision
    mock_temp = 19.5         # Celsius
    mock_psi = 14.7          # Standard atmospheric loop pressure
    
    log_test_run(mock_file, mock_baseline_do, mock_post_do, mock_temp, mock_psi)
          

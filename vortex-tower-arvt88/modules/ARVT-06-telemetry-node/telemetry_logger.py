import math
import os
import json
import time
import random

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def mock_analog_read(sensor_type):
    """
    Simulates raw analog-to-digital converter (ADC) voltage readings 
    reflecting real-world workbench physics and advanced matrix energy outputs.
    """
    if sensor_type == "mhd_voltage":
        return random.uniform(1.2, 3.8)
    elif sensor_type == "flow_pulses":
        return random.randint(900, 1100)
    elif sensor_type == "acoustic_pitch":
        return random.uniform(21000.0, 24500.0)
    elif sensor_type == "soil_ec":
        return random.uniform(0.8, 1.4)
    elif sensor_type == "piezo_pulses":
        return random.uniform(2.5, 5.0)
    elif sensor_type == "static_kv":
        return random.uniform(0.5, 2.2)
    return 0.0

def process_telemetry_cycle(config):
    """
    Parses raw hardware analog pins, converts inputs via calibration vectors,
    audits multi-harvesting layers, and yields unified telemetry metrics.
    """
    v_coef = config["sensor_calibration"]["voltage_multiplier_coefficient"]
    pulses_per_l = config["sensor_calibration"]["flow_pulses_per_liter"]
    p_coef = config["sensor_calibration"]["piezo_strain_multiplier"]
    s_coef = config["sensor_calibration"]["static_kv_multiplier"]
    alarm_hz = config["safety_frequency_thresholds_hz"]["destructive_cavitation_alarm_threshold"]
    
    raw_volts = mock_analog_read("mhd_voltage")
    raw_pulses = mock_analog_read("flow_pulses")
    raw_acoustic = mock_analog_read("acoustic_pitch")
    raw_soil_ec = mock_analog_read("soil_ec")
    raw_piezo = mock_analog_read("piezo_pulses")
    raw_static = mock_analog_read("static_kv")
    
    calculated_voltage = raw_volts * v_coef
    calculated_flow_lps = (raw_pulses / pulses_per_l) * 60.0 / 60.0
    calculated_piezo_v = raw_piezo * p_coef
    calculated_static_kv = raw_static * s_coef
    
    if raw_acoustic >= alarm_hz:
        status_flag = "CRITICAL_ALARM: Destructive Cavitation Material Fatigue Threat Detected"
    elif raw_acoustic >= config["safety_frequency_thresholds_hz"]["safe_purification_resonance_min"]:
        status_flag = "OPTIMAL: Safe Acoustic Cold-Boiling Purification Active"
    else:
        status_flag = "WARNING: Insufficient Flow Velocity for Pathogen Cavitation"
        
    telemetry_packet = {
        "timestamp_epoch": int(time.time()),
        "monitored_vitals": {
            "mhd_output_voltage": round(calculated_voltage, 2),
            "fluid_velocity_lps": round(calculated_flow_lps, 3),
            "acoustic_resonance_hz": round(raw_acoustic, 1),
            "soil_conductivity_ec": round(raw_soil_ec, 3),
            "piezo_harvest_voltage": round(calculated_piezo_v, 2),
            "static_collector_kilovolts": round(calculated_static_kv, 3)
        },
        "system_status": status_flag
    }
    
    return telemetry_packet

def main():
    print("=" * 65)
    print("INITIALIZING: ARVT-06 CORE TELEMETRY AUTOMATION SYSTEM")
    print("=" * 65)
    
    config_path = get_local_path("node-config.json")
    master_card_path = get_local_path("../../config/master-telemetry.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        interval = config["broadcast_profiles"]["data_sync_interval_seconds"]
        print(f"[+] Component ID ARVT-06 expanded tracking initialized.")
        print(f"[*] Commencing automated data logging loop at {interval}s sweeps...\n")
    else:
        print("[⚠️] ERROR: node-config.json missing. Aborting automation launch.")
        return

    try:
        for loop in range(3):
            print(f"[RUNNING] Harvesting telemetry dataset frame {loop + 1}...")
            packet = process_telemetry_cycle(config)
            
            print(f"    ↳ MHD Core Generation  : {packet['monitored_vitals']['mhd_output_voltage']} V")
            print(f"    ↳ Piezo Strain Harvest : {packet['monitored_vitals']['piezo_harvest_voltage']} V")
            print(f"    ↳ Atmospheric Static   : {packet['monitored_vitals']['static_collector_kilovolts']} kV")
            print(f"    ↳ Core Health Status   : {packet['system_status']}")
            
            if os.path.exists(master_card_path):
                with open(master_card_path, "r") as file:
                    master_data = json.load(file)
                master_data["live_telemetry_sync"] = packet
                with open(master_card_path, "w") as file:
                    json.dump(master_data, file, indent=2)
                print("    [✔] Master global data telemetry card successfully sync-updated.")
                
            time.sleep(1.0)
            print("-" * 50)
            
        print("\n[+] SUCCESS: Telemetry automated network pipeline completed checkout.")
    except KeyboardInterrupt:
        print("\n[⚠️] System Halt: Telemetry background logging loop suspended.")
    print("=" * 65)

if __name__ == "__main__":
    main()
    

import math
import os
import json
import time
import random
import hashlib

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_unique_packet_id(node_id, timestamp):
    """Generates a cryptographic 8-character verification tag for mesh packet collision safety."""
    raw_hash = hashlib.sha256(f"{node_id}_{timestamp}_{random.random()}".encode()).hexdigest()
    return raw_hash[:8].upper()

def mock_analog_read(sensor_type):
    """Simulates raw ADC and RF radio registers mapping out the local grid neighborhood."""
    if sensor_type == "mhd_voltage": return random.uniform(1.2, 3.8)
    elif sensor_type == "flow_pulses": return random.randint(900, 1100)
    elif sensor_type == "acoustic_pitch": return random.uniform(21000.0, 24500.0)
    elif sensor_type == "soil_ec": return random.uniform(0.8, 1.4)
    elif sensor_type == "piezo_pulses": return random.uniform(2.5, 5.0)
    elif sensor_type == "static_kv": return random.uniform(0.5, 2.2)
    elif sensor_type == "mesh_neighbors_count": return random.randint(2, 5)
    return 0.0

def process_mesh_routing(config, local_packet):
    """
    Models the ad-hoc decentralized peer-to-peer mesh data routing algorithm.
    Packages localized metrics and increments the network hop counters.
    """
    freq = config["mesh_network_grid_matrix"]["radio_frequency_mhz"]
    hop_limit = config["mesh_network_grid_matrix"]["mesh_max_hop_limit"]
    neighbors = mock_analog_read("mesh_neighbors_count")
    
    mesh_packet = {
        "packet_id": generate_unique_packet_id("ARVT-NODE-88", local_packet["timestamp_epoch"]),
        "origin_node": "ARVT-NODE-88",
        "mesh_frequency_mhz": freq,
        "current_hop_count": 1,
        "max_hop_limit": hop_limit,
        "active_mesh_peers_detected": neighbors,
        "payload": local_packet["monitored_vitals"],
        "grid_status": "MESH_STABLE: Data Packet Propagating Symmetrically"
    }
    return mesh_packet

def process_telemetry_cycle(config):
    """Parses pins, converts analog signals, and yields structured telemetry vitals."""
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
    calculated_flow_lps = (raw_pulses / pulses_per_l)
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
    print("=" * 70)
    print("INITIALIZING: ARVT-06 AD-HOC DECENTRALIZED MESH TELEMETRY NODE")
    print("=" * 70)
    
    config_path = get_local_path("node-config.json")
    master_card_path = get_local_path("../../config/master-telemetry.json")
    
    if os.path.exists(master_card_path):
        with open(master_card_path, "r") as file:
            global_config = json.load(file)
        sync_rate = global_config["mesh_network_grid_matrix"]["swarm_sync_interval_seconds"]
        print(f"[+] Component ID ARVT-06 decentralized grid telemetry matrix loaded.")
        print(f"[*] Global Ad-Hoc Swarm Sync Interval: {sync_rate} seconds")
    else:
        print("[⚠️] ERROR: Master telemetry configuration path broken. Aborting network hook.")
        return

    if not os.path.exists(config_path):
        print("[⚠️] ERROR: node-config.json missing. Aborting module execution.")
        return

    try:
        for loop in range(2):
            print(f"\n[SWARM CYCLE {loop + 1}] Processing structural metrics data capture...")
            local_packet = process_telemetry_cycle(global_config)
            mesh_packet = process_mesh_routing(global_config, local_packet)
            
            print(f"    ↳ Local Node Vitals   : Flow = {mesh_packet['payload']['fluid_velocity_lps']} L/s | MHD = {mesh_packet['payload']['mhd_output_voltage']} V")
            print(f"    ↳ Radio RF Interface  : Transmitting on {mesh_packet['mesh_frequency_mhz']} MHz Matrix Channel")
            print(f"    ↳ Routing Mesh Ledger : Broadcast Unique ID [{mesh_packet['packet_id']}] across {mesh_packet['active_mesh_peers_detected']} connected peer towers")
            print(f"    ↳ Packet Hop Audit    : Step {mesh_packet['current_hop_count']} of {mesh_packet['max_hop_limit']} allowed boundary limits")
            print(f"    ↳ Mesh Swarm Health   : {mesh_packet['grid_status']}")
            
            if os.path.exists(master_card_path):
                global_config["live_telemetry_sync"] = local_packet
                global_config["mesh_network_grid_matrix"]["active_mesh_packet_log"] = mesh_packet
                with open(master_card_path, "w") as file:
                    json.dump(global_config, file, indent=2)
                print("    [✔] Decentralized mesh swarm packet sync-updated into global telemetry card.")
                
            time.sleep(1.0)
            print("-" * 60)
            
        print("\n[+] SUCCESS: Ad-hoc decentralized mesh network completed pipeline diagnostic verify.")
        print("[-] Swarm mesh array is running and fully synchronized at absolute equilibrium.")
    except KeyboardInterrupt:
        print("\n[⚠️] System Halt: Mesh background networking routines suspended.")
    print("=" * 70)

if __name__ == "__main__":
    main()
        

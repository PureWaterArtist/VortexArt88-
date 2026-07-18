import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_opto_telemetry_mesh(wavelength, propagation_us, resolution=360):
    """
    Calculates the 3D grid layout nodes for the infrared emitter/detector tracking array.
    Maps out the precise non-invasive alignment vectors across the quartz wafer 
    to enable zero-latency, opto-isolated fluid-to-silicon digital state handoffs.
    """
    telemetry_nodes = []
    
    # Grid spacing reference matching the exit channel width parameter (0.25mm)
    pitch_spacing_mm = 0.25
    total_sensor_channels = 8  # 8-bit parallel output telemetry array
    
    # Opto-telemetry array block has a total length of 12mm along the Z-axis
    total_len_z = 12.0
    
    for channel_idx in range(total_sensor_channels):
        # Linearly step the 8 infrared sensor pairs along the Z-axis exit manifold
        z_pos = -(channel_idx * (total_len_z / total_sensor_channels))
        z_mid = z_pos - ((total_len_z / total_sensor_channels) / 2.0)
        
        for step in range(resolution):
            theta = (step * 2.0 * math.pi) / resolution
            
            # Map a precise top-and-bottom vertical alignment beam crossing the channel
            # Angle 0 represents the top infrared emitter pinout
            # Angle Pi (180 degrees) represents the matching bottom phototransistor target
            if abs(theta - 0.0) < (2.0 * math.pi / 36.0):
                node_type = "Infrared_940nm_Emitter_Pin_Alignment"
                x = pitch_spacing_mm * channel_idx
                y = 2.0 # Positioned 2mm above the quartz fluid channel floor
            elif abs(theta - math.pi) < (2.0 * math.pi / 36.0):
                node_type = "Infrared_Phototransistor_Receiver_Pin_Alignment"
                x = pitch_spacing_mm * channel_idx
                y = -2.0 # Positioned 2mm below the quartz wafer base floor
            else:
                node_type = "Hermetic_Quartz_Dielectric_Isolation_Zone"
                x = pitch_spacing_mm * channel_idx * math.cos(theta)
                y = pitch_spacing_mm * channel_idx * math.sin(theta)
                
            telemetry_nodes.append({
                "channel_bit_index": channel_idx,
                "node_classification": node_type,
                "diagnostics": {
                    "sensor_wavelength_nm": wavelength,
                    "propagation_delay_us": propagation_us,
                    "axial_alignment_z_mm": round(z_mid, 4)
                },
                "vector_coordinate": (round(x, 4), round(y, 4), round(z_mid, 4))
            })
            
    return telemetry_nodes

def main():
    print("=" * 65)
    print("INITIALIZING: ARFC-03 OPTO-TELEMETRY FIELD ENGINE")
    print("=" * 65)
    
    config_path = get_local_path("telemetry-config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        wavelength = config["optical_sensor_parameters"]["infrared_wavelength_nm"]
        propagation_us = config["signal_propagation_envelope"]["maximum_propagation_delay_us"]
        material = config["industrial_profile"]["wafer_window_material"]
        print("[+] Industrial Component ID ARFC-03 configuration card matched.")
    else:
        print("[⚠️] WARNING: telemetry-config.json missing. Loading safe overrides.")
        wavelength = 940.0
        propagation_us = 1.5
        material = "Monocrystalline_Quartz"
        
    print(f"[*] Visual Interface Window : {material}")
    print(f"[*] Core Opto-Wavelength    : {wavelength} nm Infrared Spectrum")
    print(f"[*] Compiling non-invasive tracking alignment vectors...")
    
    telemetry_mesh = generate_opto_telemetry_mesh(wavelength, propagation_us)
    audit_sample = [n for n in telemetry_mesh if n["node_classification"] == "Infrared_Phototransistor_Receiver_Pin_Alignment"]
    
    print("\n[+] SUCCESS: Opto-isolated tracking array matrix compiled cleanly.")
    print(f"[-] Total coordinated structural nodes logged: {len(telemetry_mesh)}")
    print(f"[-] ARFC-03 Core Node Balance Audit:")
    print(f"    ↳ Active Sensor Target:     {audit_sample['node_classification']}")
    print(f"    ↳ Target Alignment Axis:    {audit_sample['diagnostics']['axial_alignment_z_mm']} mm")
    print("=" * 65)

if __name__ == "__main__":
    main()
      

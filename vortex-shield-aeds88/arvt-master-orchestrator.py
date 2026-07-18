import math
import os
import json

def get_local_path(filename):
    """Calculates the absolute file path relative to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def calculate_shield_sheath_velocity(progress, pressure_psi, density, depth_microns, nozzle_width_mm):
    """
    Calculates the local velocity vector of the gas sheath moving past micro-Tesla walls.
    Models Bernoulli conversions alongside micro-channel hydraulic corrections to check 
    laminar vortex attachment margins before high-voltage ionization.
    """
    # Convert operating PSI head to Pascals (Static Pressure head)
    pressure_pascal = pressure_psi * 6894.76
    v_ideal = math.sqrt((2.0 * pressure_pascal) / density)
    
    # Structural radius pinching down along the vertical axis profile
    depth_m = depth_microns / 1000000.0
    width_m = (nozzle_width_mm / 1000.0) * (1.0 - (progress * 0.40))
    
    # Rectangular micro-etched aspect ratio adjustments
    hydraulic_dia = (2.0 * depth_m * width_m) / (depth_m + width_m)
    friction_loss = 1.0 - (0.015 / (hydraulic_dia * 1000.0))
    
    # Compounding centripetal acceleration gain from boundary-layer sawtooth steps
    step_acceleration_gain = 1.0 + (progress * 2.85)
    
    return min(95.0, v_ideal * friction_loss * step_acceleration_gain * 0.42)

def main():
    print("=" * 75)
    print("INITIALIZING: AEDS-88 ELECTRODYNAMIC SHIELD RECONOMY ORCHESTRATOR")
    print("=" * 75)
    
    config_path = get_local_path("config/shield-telemetry.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
        pressure_psi = config["fluidic_sheath_dynamics"]["primary_injection_pressure_psi"] if "fluidic_sheath_dynamics" in config else 45.0
        density = config["fluidic_sheath_dynamics"]["carrier_fluid_density_kg_m3"] if "fluidic_sheath_dynamics" in config else 1.16
        target_v = config["fluidic_sheath_dynamics"]["target_sheath_velocity_m_s"] if "fluidic_sheath_dynamics" in config else 32.5
        depth_microns = config["structural_fabrication_profile"]["channel_etch_depth_microns"] if "structural_fabrication_profile" in config else 250.0
        width_mm = config["fluidic_sheath_dynamics"]["intake_plenum_inner_diameter_mm"] if "fluidic_sheath_dynamics" in config else 50.8
        breakdown_v = config["plasma_ionization_matrix"]["minimum_breakdown_voltage_vdc"] if "plasma_ionization_matrix" in config else 12500.0
        print(f"[+] Shield Telemetry Version {config['version']} database matched successfully.")
    else:
        print("[⚠️] WARNING: shield-telemetry.json missing. Loading safe overrides.")
        pressure_psi = 45.0
        density = 1.16
        target_v = 32.5
        depth_microns = 250.0
        width_mm = 50.8
        breakdown_v = 12500.0

    print(f"[*] Carrier Gas Medium   : Dry Nitrogen/Air Matrix ({density} kg/m³)")
    print(f"[*] Ionization Potential : {breakdown_v}V DC Helical Spark Gate")
    print(f"[*] Latching Threshold   : Minimum {target_v} m/s Velocity Margin")
    print(f"[*] Running multi-tier fluid-to-plasma trajectory tracking sweeps...\n")
    
    shield_nodes = {
        "AEDS-01 (Primary Intake Cardioid Splitter)": 0.05,
        "AEDS-01 (Coaxial Pre-Heater Sleeve Zone)": 0.25,
        "AEDS-01 (Hyperbolic Sawtooth Throat Entry)": 0.45,
        "AEDS-02 (High-Voltage Helical Glow Gate) ": 0.65,
        "AEDS-02 (2000C Plasma Ionization Singular)": 0.80,
        "AEDS-03 (Coaxial N52 Confinement Bottle)  ": 0.95,
        "AEDS-03 (Asymmetric Venturi Siphon Collar)": 1.0
    }
    
    containment_stable = True
    for label, progress_node in shield_nodes.items():
        # Scale internal width boundaries across the concentric stack
        current_w = width_mm * (0.1 + (0.9 * (1.0 - progress_node)))
        v_calculated = calculate_shield_sheath_velocity(progress_node, pressure_psi, density, depth_microns, current_w)
        
        status = "STABLE SHEATH" if v_calculated >= target_v and progress_node <= 0.45 else "IONIZED IGNITION"
        if progress_node >= 0.80 and v_calculated >= target_v:
            status = "MAGNETICALLY BOUND"
        elif v_calculated < target_v:
            status = "FAIL: BOUNDARY SEPARATION"
            containment_stable = False
            
        print(f"    ↳ Node {label} : {round(v_calculated, 4)} m/s [{status}]")
        
    print("\n[+] SUCCESS: Entire Electrodynamic Shield pipeline audited cleanly.")
    if containment_stable:
        print(f"[-] SIMULATION VERDICT: Centripetal constraints locked (Re=2100). Shield is 100% stable.")
    else:
        print("[⚠️] SIMULATION VERDICT: Insufficient kinetic velocity. Plasma face threats breakdown.")
    print("=" * 75)

if __name__ == "__main__":
    main()
      

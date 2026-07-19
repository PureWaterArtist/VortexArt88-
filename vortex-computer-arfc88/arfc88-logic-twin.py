#!/usr/bin/env python3
# =========================================================================
# PROJECT ARFC-88: FLUIDIC COMPUTER MATRIX (DIGITAL TWIN SANDBOX)
# Verification Module: Coandă Wall-Attachment & Pulse Switching Twin
# Licensed under CERN-OHL-S-2.0 (Strongly Reciprocal Open Hardware)
# =========================================================================

import numpy as np

def run_logic_gate_simulation():
    print("=" * 75)
    print(" PROJECT ARFC-88: COANDĂ EFFECT FLUIDIC COMPUTATION TWIN")
    print("=" * 75)
    
    # --- METROLOGY INPUT VARIABLES (Keyed to hardware-bom.json) ---
    supply_pressure_kpa = 35.0     # Baseline fluid power stream continuous pressure
    control_pulse_kpa = 4.2        # Trigger pressure applied to side control ports
    channel_width_mm = 2.0         # Width of the fluidic logic channels
    attachment_angle_deg = 12.5    # Asymmetric boundary wall divergence profile
    
    print(f"[*] Parsing Fluidic Logic State Telemetry...")
    print(f"    -> Supply Line Pressure         : {supply_pressure_kpa:.1f} kPa")
    print(f"    -> Control Jet Pulse Pressure   : {control_pulse_kpa:.1f} kPa")
    print(f"    -> Logic Channel Trace Width    : {channel_width_mm:.1f} mm")
    print(f"    -> Coandă Boundary Wall Angle   : {attachment_angle_deg:.1f}°")
    print("-" * 75)
    
    # 1. COANDĂ EFFECT STABILITY AND DISPLACEMENT EVALUATION
    # Reynolds number verification for low-turbulence laminar stream attachment
    air_kinematic_viscosity = 1.5e-5 # m^2/s at standard sea level ambient
    estimated_velocity_ms = np.sqrt((2 * (supply_pressure_kpa * 1000)) / 1.2)
    reynolds_number = (estimated_velocity_ms * (channel_width_mm / 1000)) / air_kinematic_viscosity
    
    print(f"[*] Fluidic Vector Kinematic Status:")
    print(f"    -> Computed Jet Core Velocity   : {estimated_velocity_ms:.2f} m/s")
    print(f"    -> Trace Reynolds Number ($Re$)   : {reynolds_number:.1f}")
    
    # Check if fluid jet profile stabilizes inside laminar-to-transient computing limits
    if 2000 < reynolds_number < 15000:
        print(" [SUCCESS] Stable Boundary-Layer Attachment Confirmed via Reynolds Limits.")
    else:
        print(" [WARNING] High Turbulence Expected. Risk of spontaneous state flipping.")
    print("-" * 75)
    
    # 2. STATE SWITCHING LOGIC (BINARY STATE TRANSITION EVALUATION)
    # The switching ratio determines if the control pulse is high enough to trip the stream
    critical_switching_threshold = supply_pressure_kpa * np.sin(np.radians(attachment_angle_deg))
    switching_differential = control_pulse_kpa - critical_switching_threshold
    
    print(f"[*] Logic Gate State Execution Analytics:")
    print(f"    -> Critical Switching Threshold : {critical_switching_threshold:.2f} kPa")
    print(f"    -> Applied Vector Overpressure  : {switching_differential:.2f} kPa")
    
    # Evaluate Boolean logic execution based on pressure vector shift math
    if switching_differential > 0:
        print(" [SUCCESS] Fluidic Supply Stream Successfully Tripped to Alternate Channel.")
        print("           Binary Logic Event Registered: STATE CHANGE [0 ──► 1] SUCCESSFUL.")
    else:
        print(" [FAILED] Control pressure insufficient. Supply jet remains attached to native wall.")
        print("          Gate Execution Status: STATE PRESERVED [REMAINS 0].")
    print("=" * 75)

if __name__ == "__main__":
    run_logic_gate_simulation();
  

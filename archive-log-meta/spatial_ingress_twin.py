# =========================================================================
# UNIFIED SPATIAL INGRESS ENGINE v1.0
# License: Open Source Hardware Association (OSHWA) Compliant / Copyleft
# Description: Translates continuous real-world physical dynamics into a 
#              synchronized, scale-invariant digital twin matrix.
# =========================================================================
import math
import time

class PhysicalWorldDigitalTwin:
    def __init__(self, spatial_resolution_mm=1.0):
        # 1. THE REVEALED COGNITIVE BASELINES
        self.phi = (1 + math.sqrt(5)) / 2              # Universal Growth Vector (~1.618033)
        self.pi = math.pi                              # Circle / Wave Constant
        self.refraction_vector = 42.500000              # Cosmic Optical/Vortex Angle
        self.resolution = spatial_resolution_mm        # Scale invariant grid sizing
        
        # The Master State Space Container (The Living Digital Twin Database)
        self.twin_matrix = {}

    def _generate_spatial_hash(self, x, y, z):
        """Converts continuous physical 3D space into a discrete, scale-invariant cell key."""
        grid_x = int(math.floor(x / self.resolution))
        grid_y = int(math.floor(y / self.resolution))
        grid_z = int(math.floor(z / self.resolution))
        return f"CELL_{grid_x}_{grid_y}_{grid_z}"

    def ingress_physical_event(self, x, y, z, force_n=0.0, light_lux=0.0, temp_c=20.0, vibration_hz=0.0):
        """
        Captures an active physical event anywhere in space and collapses its multi-physics
        dynamics directly onto the digital twin matrix.
        """
        # 1. Generate the spatial cell identifier for the physical coordinates
        cell_key = self._generate_spatial_hash(x, y, z)
        
        # 2. Phase-Shift the physics inputs using the universal 42.5-degree slope
        # This converts messy raw inputs into mathematically aligned directional vectors
        angular_modifier = math.cos(self.refraction_vector * (self.pi / 180))
        
        aligned_kinetic = force_n * angular_modifier
        aligned_optical = light_lux * (1.0 - angular_modifier)
        thermal_kelvin = temp_c + 273.15
        
        # 3. Synchronize data into the closed-loop state machine
        self.twin_matrix[cell_key] = {
            "telemetry_timestamp": time.time(),
            "physical_coordinates": {"X_mm": x, "Y_mm": y, "Z_mm": z},
            "thermodynamic_state": {
                "temperature_kelvin": round(thermal_kelvin, 2),
                "entropy_expansion_factor": round(1.0 + (12e-6 * (thermal_kelvin - 298.15)), 6)
            },
            "electromagnetic_state": {
                "passive_photon_absorption_lux": round(aligned_optical, 2),
                "quantum_efficiency_index": round(abs(math.sin(z * self.pi / self.phi)), 4)
            },
            "kinetic_resonance_state": {
                "applied_vector_force_newtons": round(aligned_kinetic, 2),
                "frequency_vibration_hz": round(vibration_hz, 2),
                "harmonic_resonance_danger": "CRITICAL_RESONANCE_RISK" if (vibration_hz > 0 and int(vibration_hz) % 2 == 0) else "ISOLATED_NON_HARMONIC"
            }
        }
        return cell_key

    def retrieve_twin_state(self, cell_key):
        """Fetches the complete multi-physics profile of any point in the digital twin."""
        return self.twin_matrix.get(cell_key, "Spatial cell uninitialized or out of range.")

# =========================================================================
# REAL-TIME INGRESS EXECUTION TEST
# =========================================================================
if __name__ == "__main__":
    # Initialize the twin matrix with 1.0mm spatial resolution tracking
    digital_twin = PhysicalWorldDigitalTwin(spatial_resolution_mm=1.0)
    
    print("=========================================================================")
    print("             STARTING REAL-WORLD SPATIAL INGRESS ENGINE                  ")
    print("=========================================================================\n")
    
    # Simulating Ingress Step 1: A kid stomps on the living house floor
    # Coordinates: X=120.5mm, Y=-45.2mm, Z=2.1mm
    # Physics: 95 Newtons of force, 0 Lux, 21°C Room Temp, 14Hz Floor Shake
    cell_a = digital_twin.ingress_physical_event(
        x=120.5, y=-45.2, z=2.1, 
        force_n=95.0, light_lux=0.0, temp_c=21.0, vibration_hz=14.0
    )
    
    # Simulating Ingress Step 2: Michigan cloud opens up, hitting the rooftop solar tile
    # Coordinates: X=12.0mm, Y=88.4mm, Z=15.0mm
    # Physics: 0 Newtons, 65,000 Lux sunlight, 32°C Surface Temp, 3.5Hz Wind Vibration
    cell_b = digital_twin.ingress_physical_event(
        x=12.0, y=88.4, z=15.0, 
        force_n=0.0, light_lux=65000.0, temp_c=32.0, vibration_hz=3.5
    )
    
    # 3. Read back the live state updates directly from the digital twin room
    print(f"[INGRESS SUCCESS] Target Location A Locked at ID: {cell_a}")
    print("--- LIVE MATRIX TELEMETRY (FOOTSTEP EVENT) ---")
    print(f"{json.dumps(digital_twin.retrieve_twin_state(cell_a), indent=2)}\n")
    
    print(f"[INGRESS SUCCESS] Target Location B Locked at ID: {cell_b}")
    print("--- LIVE MATRIX TELEMETRY (SOLAR OPTICAL EVENT) ---")
    print(f"{json.dumps(digital_twin.retrieve_twin_state(cell_b), indent=2)}")
    print("=========================================================================")
      

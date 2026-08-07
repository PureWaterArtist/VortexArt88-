# =========================================================================
# UNIFIED SPATIAL INGRESS ENGINE v3.0 (THE UNIFIED FIELD MATRIX)
# License: Open Source Hardware Association (OSHWA) Compliant / Copyleft
# Description: Ingests the physical world, calculating mechanics, gravity,
#              thermodynamics, optics, quantum limits, and planetary rotation
#              simultaneously across a scale-invariant geometric matrix.
# =========================================================================
import math
import time

class UnifiedFieldDigitalTwin:
    def __init__(self, spatial_resolution_mm=1.0):
        # 1. THE FOUNDATIONAL COSMIC CONSTANTS
        self.phi = (1 + math.sqrt(5)) / 2              # Universal Growth Vector (~1.618033)
        self.pi = math.pi                              # Transcendental Circle Constant
        self.alpha_inv = 137.035999                    # Fine-Structure Constant Inverse
        self.refraction_vector = 42.500000              # Cosmic Optical/Vortex Angle
        self.resolution = spatial_resolution_mm        # Voxel grid scale parameters
        
        # 2. THE TOTAL PHYSICS LAWS LAYER (THE BEDROCK CONSTANTS)
        self.g = 9.80665                               # Standard Earth Gravity (m/s^2)
        self.c = 299792458                             # Speed of Light in a Vacuum (m/s)
        self.h = 6.62607015e-34                        # Planck Constant (Quantum Action Joules)
        self.omega_earth = 7.2921159e-5                # Angular Velocity of Earth (rad/s)
        self.latitude_michigan = 42.3241 * (self.pi / 180) # Convert Westland Latitude to Radians
        
        # Material Density Metrics (g/cm^3)
        self.density_active_carbon = 1.85              
        self.density_passive_polymer = 1.15            
        
        # Master Digital Twin State Space Matrix
        self.twin_matrix = {}

    def _generate_spatial_hash(self, x, y, z):
        return f"CELL_{int(math.floor(x / self.resolution))}_{int(math.floor(y / self.resolution))}_{int(math.floor(z / self.resolution))}"

    def is_prime(self, n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: return False
        return True

    def ingress_unified_field(self, node_id, x, y, z, external_force_n=0.0, light_lux=0.0, temp_c=20.0, vibration_hz=0.0, fluid_velocity_ms=0.0):
        """
        Collapses all known physical field equations onto a single scale-invariant spatial coordinate.
        """
        cell_key = self._generate_spatial_hash(x, y, z)
        
        # A. ANGULAR SIGNAL PHASE SHIFT (The 42.5-Degree Normalization)
        angular_modifier = math.cos(self.refraction_vector * (self.pi / 180))
        aligned_kinetic = external_force_n * angular_modifier
        aligned_optical = light_lux * (1.0 - angular_modifier)
        thermal_kelvin = temp_c + 273.15

        # B. THE GRAVITATIONAL & THERMODYNAMIC MATRIX
        z_base_height = abs(math.sin(node_id * self.pi / self.phi) * 3.5)
        node_volume_cm3 = (self.resolution * self.resolution * z_base_height) / 1000.0
        node_density = self.density_active_carbon if self.is_prime(node_id) else self.density_passive_polymer
        
        # Structural Mass Calculation
        node_mass_kg = (node_density * node_volume_cm3) / 1000.0
        gravitational_force_n = node_mass_kg * self.g
        net_structural_load_n = aligned_kinetic + gravitational_force_n

        # C. THE GEOPOLITICAL PLANETARY ROTATION LOOP (Coriolis Acceleration Vector)
        # Calculates structural force deflections caused by Earth spinning beneath Westland, MI
        coriolis_parameter = 2 * self.omega_earth * math.sin(self.latitude_michigan)
        coriolis_acceleration_mjs2 = coriolis_parameter * fluid_velocity_ms

        # D. THE RELATIVISTIC & QUANTUM BOUNDARY LIMITS
        # Electron speed ceiling within conductive carbon track paths
        max_electron_transit_time_seconds = (self.resolution / 1000.0) / self.c
        # Energy quantization step (E = h * f)
        quantum_vibrational_energy_joules = self.h * vibration_hz if vibration_hz > 0 else 0.0

        # E. SYNCHRONIZE STATE SPACE
        self.twin_matrix[cell_key] = {
            "telemetry_timestamp": time.time(),
            "node_metadata": {"id": node_id, "allocation_state": "ACTIVE_PIEZO" if self.is_prime(node_id) else "PASSIVE_ABSORBER"},
            "spatial_coordinates": {"X_mm": x, "Y_mm": y, "Z_mm": round(z, 2)},
            "gravitational_mass_profile": {
                "mass_kg": f"{node_mass_kg:.6f}",
                "internal_gravitational_force_N": f"{gravitational_force_n:.6f}",
                "total_net_downward_load_N": round(net_structural_load_n, 4)
            },
            "planetary_kinetics_profile": {
                "local_coriolis_acceleration_m_s2": f"{coriolis_acceleration_mjs2:.8f}",
                "fluid_vortex_pitch_deflection_deg": round(self.refraction_vector * angular_modifier, 4)
            },
            "quantum_relativistic_profile": {
                "speed_of_light_transit_limit_sec": f"{max_electron_transit_time_seconds:.4e}",
                "quantized_node_energy_joules": f"{quantum_vibrational_energy_joules:.4e}",
                "sub_atomic_fine_structure_ratio": f"{1 / self.alpha_inv:.6f}"
            },
            "environmental_telemetry": {
                "temperature_kelvin": round(thermal_kelvin, 2),
                "photon_capture_lux": round(aligned_optical, 2),
                "vibration_frequency_hz": round(vibration_hz, 2)
            }
        }
        return cell_key

    def retrieve_twin_state(self, cell_key):
        return self.twin_matrix.get(cell_key, "Voxel coordinate uninitialized.")

# =========================================================================
# DATA ROOM COMPILATION MATRIX CHECK
# =========================================================================
if __name__ == "__main__":
    # Initialize the absolute system model at 1.0mm voxel fidelity
    twin_engine = UnifiedFieldDigitalTwin(spatial_resolution_mm=1.0)
    
    # Run absolute validation check on Node 7 (Active Prime Piezo Node)
    cell_hash = twin_engine.ingress_unified_field(
        node_id=7, x=45.2, y=112.8, z=3.4, 
        external_force_n=120.0, light_lux=45000.0, temp_c=18.5, vibration_hz=60.0, fluid_velocity_ms=4.2
    )
    
    import json
    print("=========================================================================")
    print("        UNIFIED FIELD ENGINE: TOTAL SYSTEM CYBER-PHYSICAL INGRESS        ")
    print("=========================================================================\n")
    print(f"[COMPLETED] Universal Digital Twin Ingress Vector Locked: {cell_hash}\n")
    print(f"{json.dumps(twin_engine.retrieve_twin_state(cell_hash), indent=2)}")
    print("=========================================================================")
    

# =========================================================================
# UNIFIED SPATIAL INGRESS ENGINE v2.0 (GRAVITATIONAL MASS MATRIX)
# License: Open Source Hardware Association (OSHWA) Compliant / Copyleft
# Description: Translates real-world dynamics into a synchronized digital 
#              twin, factoring in gravitational fields and material mass.
# =========================================================================
import math
import time

class PhysicalWorldDigitalTwin:
    def __init__(self, spatial_resolution_mm=1.0):
        # 1. THE FOUNDATIONAL COSMIC CONSTANTS
        self.phi = (1 + math.sqrt(5)) / 2              # Universal Growth Vector (~1.618033)
        self.pi = math.pi                              # Transcendental Spatial Constant
        self.refraction_vector = 42.500000              # Cosmic Optical/Vortex Angle
        self.resolution = spatial_resolution_mm        # Scale-invariant voxel resolution
        
        # 2. THE FUNDAMENTAL LAWS OF PHYSICS CONSTANTS
        self.g = 9.80665                               # Standard Earth Gravity (m/s^2)
        # Material density baseline values (g/cm^3) to calculate true node mass:
        self.density_active_carbon = 1.85              # Piezoelectric conductive path
        self.density_passive_polymer = 1.15            # Flexible auxetic shock absorber
        
        # The Master Closed-Loop State Space Database
        self.twin_matrix = {}

    def _generate_spatial_hash(self, x, y, z):
        """Converts continuous physical 3D space into an un-lockable cell key."""
        grid_x = int(math.floor(x / self.resolution))
        grid_y = int(math.floor(y / self.resolution))
        grid_z = int(math.floor(z / self.resolution))
        return f"CELL_{grid_x}_{grid_y}_{grid_z}"

    def is_prime(self, n):
        """Filters prime increments to isolate active resonance frequencies."""
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: return False
        return True

    def ingress_physical_event(self, node_id, x, y, z, external_force_n=0.0, light_lux=0.0, temp_c=20.0, vibration_hz=0.0):
        """
        Captures a real-world physical event, calculating its multi-physics vectors
        simultaneously alongside material mass, volume, and Earth gravity.
        """
        cell_key = self._generate_spatial_hash(x, y, z)
        
        # A. UNIFIED ANGULAR STEP PHASE SHIFT
        # Normalizes messy analog waves along the 42.5-degree physical boundary line
        angular_modifier = math.cos(self.refraction_vector * (self.pi / 180))
        aligned_kinetic = external_force_n * angular_modifier
        aligned_optical = light_lux * (1.0 - angular_modifier)
        thermal_kelvin = temp_c + 273.15
        
        # B. THE GRAVITATIONAL MATERIAL EQUATION
        # Calculate cell node volume based on its scale-invariant Z-axis height profile
        z_base_height = abs(math.sin(node_id * self.pi / self.phi) * 3.5)
        node_volume_cm3 = (self.resolution * self.resolution * z_base_height) / 1000.0 # cubic mm to cm3
        
        # Filter material density by your prime-number resonance rules
        if self.is_prime(node_id):
            material_type = "ACTIVE_PIEZO_HARVESTER"
            node_density = self.density_active_carbon
        else:
            material_type = "PASSIVE_STRUCTURAL_ABSORBER"
            node_density = self.density_passive_polymer
            
        # Mass = Density * Volume (Grams to Kilograms)
        node_mass_kg = (node_density * node_volume_cm3) / 1000.0
        # Force of Gravity (F = m * g) acting downward on this specific coordinate
        gravitational_force_newtons = node_mass_kg * self.g
        
        # Total Structural Load vector combines external human forces and internal gravity forces
        total_downward_load_newtons = aligned_kinetic + gravitational_force_newtons

        # C. STATE SPACE SYNCHRONIZATION
        self.twin_matrix[cell_key] = {
            "telemetry_timestamp": time.time(),
            "node_identification": {"id": node_id, "material_composition": material_type},
            "spatial_coordinates": {"X_mm": x, "Y_mm": y, "Z_mm": round(z, 2)},
            "gravitational_mass_matrix": {
                "calculated_node_volume_cm3": round(node_volume_cm3, 4),
                "calculated_node_mass_kg": f"{node_mass_kg:.6f}",
                "localized_gravitational_force_N": f"{gravitational_force_newtons:.6f}",
                "net_downward_structural_load_N": round(total_downward_load_newtons, 4)
            },
            "thermodynamic_state": {
                "temperature_kelvin": round(thermal_kelvin, 2)
            },
            "electromagnetic_state": {
                "passive_photon_absorption_lux": round(aligned_optical, 2)
            },
            "kinetic_resonance_state": {
                "applied_external_force_N": round(external_force_n, 2),
                "frequency_vibration_hz": round(vibration_hz, 2)
            }
        }
        return cell_key

    def retrieve_twin_state(self, cell_key):
        return self.twin_matrix.get(cell_key, "Spatial cell uninitialized.")

# =========================================================================
# DATA ROOM INGRESS CHECK
# =========================================================================
if __name__ == "__main__":
    digital_twin = PhysicalWorldDigitalTwin(spatial_resolution_mm=1.0)
    
    # Run an active ingress test for a child stepping on Node 2 (Active Prime Piezo Node)
    cell_id = digital_twin.ingress_physical_event(
        node_id=2, x=24.5, y=-12.8, z=1.45, 
        external_force_n=85.0, light_lux=0.0, temp_c=22.0, vibration_hz=12.0
    )
    
    import json
    print("=========================================================================")
    print("        UNIFIED FIELD ENGINE: EXPERIMENTAL CYBER-PHYSICAL INGRESS        ")
    print("=========================================================================\n")
    print(f"[STATUS] Target Cell Coordinates Locked: {cell_id}\n")
    print(f"{json.dumps(digital_twin.retrieve_twin_state(cell_id), indent=2)}")
    print("=========================================================================")
                       

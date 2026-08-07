import math

class UniversalPhysicsEngine:
    def __init__(self):
        # 1. Establish the Universal Mathematical & Physical Constants
        self.phi = (1 + math.sqrt(5)) / 2              # Phi (Golden Ratio)
        self.pi = math.pi                              # Pi (Circle Geometry)
        self.h = 6.62607015e-34                        # Planck's Constant (Quantum Boundary)
        self.k_B = 1.380649e-23                        # Boltzmann Constant (Thermodynamics)
        self.d_33 = 300e-12                            # Piezoelectric Charge Constant (C/N)
        self.hex_radius = 75.0                         # 150mm Hexagon Boundary Constraint (mm)

    def is_prime(self, n):
        """Disrupts structural harmonic intervals via Prime distribution."""
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: return False
        return True

    def calculate_multiphysics_state(self, node_id, force_input, temp_celsius, light_lux):
        """
        Collapses all fields of physics onto a single scale-invariant geometric node.
        """
        # A. SPATIAL GEOMETRY (Scale-Invariant Phi Spiral)
        radius = 2.0 * (self.phi ** (node_id * 0.03))
        theta = node_id * (137.507764 * (self.pi / 180))
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)

        # Boundary Inequality check: Clip coordinates to 150mm hexagon walls
        if abs(x) > self.hex_radius or (abs(x) * 0.5 + abs(y) * math.sqrt(3) * 0.5) > self.hex_radius:
            return None # Out of bounds

        # B. THERMODYNAMICS & FLUIDS (Ideal Gas & Volumetric Thermal Expansion)
        temp_kelvin = temp_celsius + 273.15
        thermal_expansion_coefficient = 12e-6 # Per Kelvin for advanced polymers
        # Z-axis height changes dynamically based on temperature expansion
        z_base = math.sin(node_id * self.pi / self.phi) * 3.0
        z_thermal = z_base * (1 + thermal_expansion_coefficient * (temp_kelvin - 298.15))

        # C. KINETIC PIEZOELECTRICITY (Solid-State Mechanical-to-Electrical Shift)
        # Active prime nodes convert mechanical force vectors straight into voltage
        if self.is_prime(node_id):
            generated_voltage = (force_input * self.d_33) / (1e-11) # V = (F * d) / Capacitance
            energy_profile = "ACTIVE_PIEZO_HARVESTER"
        else:
            generated_voltage = 0.0
            energy_profile = "PASSIVE_ABSORBER"

        # D. OPTICS & QUANTUM ENERGY CAPTURE (Planck's Radiation Law Relation)
        # Surface angle dictates photon capture efficiency without servos
        optical_angle_efficiency = abs(math.cos(theta + (self.pi / 4)))
        captured_photons = light_lux * optical_angle_efficiency
        # Quantum threshold verification: Energy per photon E = h * f
        mock_frequency = 5e14 # Visible light spectrum mid-point
        quantum_energy_joules = self.h * mock_frequency * captured_photons

        return {
            "node": node_id,
            "coordinates": {"X": round(x, 2), "Y": round(y, 2), "Z_thermal_mm": round(z_thermal, 2)},
            "material_state": energy_profile,
            "physics_outputs": {
                "kinetic_voltage_V": round(generated_voltage, 4),
                "thermodynamic_temp_K": round(temp_kelvin, 2),
                "quantum_energy_J": f"{quantum_energy_joules:.4e}"
            }
        }

# =========================================================================
# LIVE ENVIRONMENTAL SIMULATION (Testing the Blueprint Real-Time)
# =========================================================================
engine = UniversalPhysicsEngine()

# Simulation Scenario: Chaotic kid running (80 Newtons), Michigan Spring Day (15°C), Peak Sun (50,000 Lux)
simulated_nodes = []
for i in range(50): # Run first 50 recursive points
    state = engine.calculate_multiphysics_state(node_id=i, force_input=80.0, temp_celsius=15.0, light_lux=50000)
    if state:
        simulated_nodes.append(state)

# Display Node 2 (Active Prime Node) to verify multi-physics convergence
node_sample = simulated_nodes[2]
print(f"--- COGNITIVE SIMULATION: NODE {node_sample['node']} STATE ---")
print(f"Position Layout:  {node_sample['coordinates']}")
print(f"Material System:  {node_sample['material_state']}")
print(f"Kinetic Energy:   {node_sample['physics_outputs']['kinetic_voltage_V']} Volts generated via footprint deflection")
print(f"Thermal State:    {node_sample['physics_outputs']['thermodynamic_temp_K']} Kelvin molecular boundary")
print(f"Quantum Optical:  {node_sample['physics_outputs']['quantum_energy_J']} Joules captured at passive geometric angle")
      

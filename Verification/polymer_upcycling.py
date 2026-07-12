import math


def simulate_polymer_upcycling(
    rpm: float, degradation_factor: float, structural_stages: int = 5
) -> dict:
    """Models the molecular shear-vortex alignment and tensile strength of recycled plastic polymer matrices.

    Args:
        rpm (float): Rotational speed of the fluidic depolymerization vortex.
        degradation_factor (float): The wear level of the input raw plastic (0.1
          = pristine waste, 0.9 = heavily degraded ocean microplastics).
        structural_stages (int): The processing zones within the fluidic shear column.

    Returns:
        dict: A manufacturing telemetry profile detailing shear stress and upcycled filament structural integrity.
    """
    phi = (1 + math.sqrt(5)) / 2  # Golden ratio scaling constant
    omega = (rpm * 2 * math.pi) / 60  # Angular velocity in rad/s

    telemetry_profile = {
        "operation_status": "VORTEX_DEPOLYMERIZATION_ACTIVE",
        "input_material_degradation": degradation_factor,
        "vortex_shear_velocity_rad_s": round(omega, 2),
        "molecular_zone_metrics": [],
    }

    cumulative_tensile_strength = 0.0

    for stage in range(1, structural_stages + 1):
        # The vortex radius narrows downward to increase localized centripetal fluid pressure
        zone_radius_meters = 0.5 / (stage * phi)

        # Fluid shear rate calculation inside the spinning vortex column
        shear_rate = omega / (zone_radius_meters + 1e-5)

        # Shear stress overcomes the random, tangled arrangement of degraded polymer chains
        molecular_alignment_factor = math.log10(shear_rate + 1) * (
            1.0 - (degradation_factor * 0.5)
        )

        # Convert alignment factor to a physical tensile retention percentage capped at 100%
        tensile_efficiency = min(
            100.0, (molecular_alignment_factor * phi) * 12.5
        )
        cumulative_tensile_strength += tensile_efficiency

        telemetry_profile["molecular_zone_metrics"].append(
            {
                "zone_id": stage,
                "vortex_constriction_radius_m": round(zone_radius_meters, 4),
                "fluid_shear_rate_s1": round(shear_rate, 2),
                "polymer_chain_alignment_pct": round(tensile_efficiency, 2),
            }
        )

    # Average structural integrity score of the upcycled bio-polymer output filament
    telemetry_profile["output_filament_tensile_integrity_pct"] = round(
        cumulative_tensile_strength / structural_stages, 2
    )

    return telemetry_profile


# Run simulation for a localized workbench recycling vortex unit processing degraded ocean plastics
waste_upcycling_telemetry = simulate_polymer_upcycling(
    rpm=4200.0, degradation_factor=0.65
)

print(
    f"--- VortexArt88 Plastic Upcycling Simulation Matrix Output ---"
)
print(
    f"Output Filament Tensile Integrity: {waste_upcycling_telemetry['output_filament_tensile_integrity_pct']}%"
)
for zone in waste_upcycling_telemetry["molecular_zone_metrics"][:3]:
    print(
        f"  Zone {zone['zone_id']}: Shear Rate: {zone['fluid_shear_rate_s1']} s^-1 | Chain Alignment: {zone['polymer_chain_alignment_pct']}%"
    )
  

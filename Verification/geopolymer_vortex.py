import math


def calculate_crystallization_density(
    rpm: float, viscosity: float, layers: int = 6
) -> dict:
    """Models the centripetal molecular alignment and density matrix of the geopolymer sol-gel.

    Args:
        rpm (float): Rotational speed of the manufacturing vortex crucible.
        viscosity (float): Base resistance factor of the liquid obsidian geopolymer mix.
        layers (int): The structural concentric layers of the output hexagonal plate.

    Returns:
        dict: A manufacturing telemetry profile detailing compression forces and crystallization yield.
    """
    # Golden ratio scaling constant for molecular structural integrity
    phi = (1 + math.sqrt(5)) / 2

    # Calculate angular velocity (omega) in radians per second
    omega = (rpm * 2 * math.pi) / 60

    manufacturing_profile = {
        "telemetry_status": "OPTIMAL_ALIGNMENT",
        "rotational_velocity_rad_s": round(omega, 2),
        "concentric_layer_metrics": [],
    }

    total_yield = 0.0

    for layer in range(1, layers + 1):
        # Radius decreases as we move toward the center of the implosive vortex core
        radius_meters = 1.0 / (layer * phi)

        # Centripetal acceleration: a = omega^2 * r
        centripetal_acceleration = (omega**2) * radius_meters

        # Molecular compaction density scales logarithmically with the inward centripetal pressure
        compaction_factor = math.log(centripetal_acceleration + 1) * (
            1 / viscosity
        )

        # Crystallization yield percentage capped at absolute 100% molecular lattice perfection
        crystallization_yield = min(100.0, (compaction_factor * phi) * 10)

        total_yield += crystallization_yield

        manufacturing_profile["concentric_layer_metrics"].append(
            {
                "layer_id": layer,
                "boundary_radius_m": round(radius_meters, 4),
                "centripetal_g_force": round(
                    centripetal_acceleration / 9.81, 2
                ),
                "lattice_alignment_pct": round(crystallization_yield, 2),
            }
        )

    # Average out the total structural yield of the manufactured obsidian geopolymer plate
    manufacturing_profile["total_matrix_integrity_pct"] = round(
        total_yield / layers, 2
    )

    return manufacturing_profile


# Run simulation for a workbench-scale localized manufacturing crucible running at 3600 RPM
foundry_telemetry = calculate_crystallization_density(rpm=3600.0, viscosity=0.85)

print(
    f"--- VortexArt88 Material Manufacturing Simulation Matrix Output ---"
)
print(
    f"Overall Plate Structural Integrity: {foundry_telemetry['total_matrix_integrity_pct']}%"
)
for layer in foundry_telemetry["concentric_layer_metrics"][:3]:
    print(
        f"  Layer {layer['layer_id']}: G-Force: {layer['centripetal_g_force']}G | Lattice Alignment: {layer['lattice_alignment_pct']}%"
    )

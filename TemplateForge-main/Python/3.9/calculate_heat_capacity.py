def calculate_heat_capacity(
    specific_heat_capacity: float,
    mass: float,
    initial_temperature: float,
    final_temperature: float,
    temperature_unit: str = "K",
) -> float:
    """
    Calculates the amount of heat transferred or gained by a body.

    Args:
        mass: Mass of the body in kg.
        specific_heat_capacity: Specific heat capacity of the substance, J/(kg * K).
        initial_temperature: Initial temperature of the body, K, or C.
        final_temperature: Final temperature of the body, K or C.
        temperature_unit: Unit of temperature. Possible values: "K", "C", where:
            K - Kelvin; C - Celsius; D - Delisle

    Returns:
        The amount of heat transferred or gained by the body in J.

    Raises:
        ValueError: If temperature_unit is not a valid unit of temperature.
    """

    if temperature_unit not in [
        "K",
        "C",
        "D",
    ]:
        raise ValueError(f"Invalid temperature unit: {temperature_unit}")

    else:
        if temperature_unit == "K":
            pass
        elif temperature_unit == "C":
            initial_temperature += 273.15
            final_temperature += 273.15
        result = mass * specific_heat_capacity * (final_temperature - initial_temperature)

        return result

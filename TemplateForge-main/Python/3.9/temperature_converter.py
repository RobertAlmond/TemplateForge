def convert_temperature(temperature, from_unit, to_unit):
    """
    Converts a temperature from one unit to another.

    Args:
        temperature: The temperature to convert.
        from_unit: The unit of the input temperature.
        to_unit: The unit of the output temperature.

    Returns:
        The converted temperature.

    Raises:
        ValueError: If the input temperature is not a number.
        ValueError: If the input or output units are not supported.
    """

    if not isinstance(temperature, (float, int)):
        raise ValueError("Input temperature must be a number.")

    if from_unit not in ["Celsius", "Kelvin", "Fahrenheit"]:
        raise ValueError("Unsupported input unit: %s" % from_unit)

    if to_unit not in ["Celsius", "Kelvin", "Fahrenheit"]:
        raise ValueError("Unsupported output unit: %s" % to_unit)

    if from_unit == "Celsius":
        if to_unit == "Kelvin":
            return temperature + 273.15
        elif to_unit == "Fahrenheit":
            return (temperature * 9/5) + 32
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return temperature - 273.15
        elif to_unit == "Fahrenheit":
            return (temperature - 273.15) * 9/5 + 32
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (temperature - 32) * 5/9
        elif to_unit == "Kelvin":
            return (temperature + 459.67) * 5/9


import sympy
import decimal
import re
import urllib.request
import urllib.error


def is_connected(attempts: int = 5, *sites: str or list[str]):
    """Checks if there is an internet connection.

    Args:
        attempts: The number of attempts to connect to each website.
        sites: A list of websites to check. If sites = None, sites = ['https://www.google.com',
                 'https://www.yahoo.com',
                 'https://www.bing.com',
                 'https://www.facebook.com',
                 'https://www.twitter.com',
                 'https://www.wikipedia.org', ]

    Returns:
        True if there is an internet connection, False otherwise.
    """
    if sites:
        for url in sites:
            if not re.match(r'^https?://.+$', url):
                raise ValueError(f'{url} is not a valid website address.')

    if not sites:
        sites = ['https://www.google.com',
                 'https://www.yahoo.com',
                 'https://www.bing.com',
                 'https://www.facebook.com',
                 'https://www.twitter.com',
                 'https://www.wikipedia.org', ]

    for url in sites:
        for _ in range(attempts):
            try:
                urllib.request.urlopen(url)
                return True
            except urllib.error.URLError:
                pass
                return False


def calculate_distance(speed: float or int or sympy.Number or decimal.Decimal,
                       time: float or int or sympy.Number or decimal.Decimal):

    """Calculates the distance traveled by an object given its speed and the time it traveled.

    Args:
        speed: The speed of the object in meters per second.
        time: The time it took to travel the distance in seconds.

    Returns:
        The distance traveled by the object in meters, kilometers, feet, or inches.
    """

    return speed * time


def calculate_speed(distance: float or int or sympy.Number or decimal.Decimal,
                    time: float or int or sympy.Number or decimal.Decimal):

    """Calculates the speed of an object given the distance traveled and the time it took to travel that distance.

    Args:
        distance: The distance traveled in meters.
        time: The time it took to travel the distance in seconds.

    Returns:
        The speed of the object in meters per second.
    """

    return distance / time


def calculate_time(distance: float or int or sympy.Number or decimal.Decimal,
                   speed: float or int or sympy.Number or decimal.Decimal):
    """
    Calculates the time it takes to travel a given distance at a given speed.

    Args:
        distance: The distance to travel in meters per second.
        speed: The speed at which to travel in seconds.

    Returns:
        The time it takes to travel the distance in meters.

    Raises:
        TypeError: If the arguments are not of the correct type.
    """

    return distance / speed


def calculate_energy_from_mass(mass: int or float or decimal.Decimal or sympy.Number):
    """
    Calculates the energy in joules from a given mass.

    Args:
        mass: The mass in kilograms.

    Returns:
        The energy in joules.

    Raises:
        ValueError: If the mass is not a valid type.
    """

    if mass < 0:
        raise ValueError("Mass cannot be negative.")

    speed_of_light = 299792458
    return (mass * speed_of_light) ** 2


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


def calculate_root(base: float, exponent: int, method: str = "newton") -> float:
    """
    Computes the root of base raised to the power of exponent using the specified method.

    Args:
        base: The number for which the root is computed. Must be a non-negative number.
        exponent: The degree of the root.
        method: The method to use for computing the root. Supported methods are "newton" and "babylonian".

    Returns:
        The root of base raised to the power of exponent.

    Raises:
        ValueError: If base is negative, exponent is less than 1, or if the specified method is not supported.
    """

    if base < 0:
        raise ValueError("Root not defined for negative numbers.")
        # Although there are complex and imaginary numbers, it is not
        # possible to take the root of a negative number in this function.
    if exponent < 1:
        raise ValueError("Exponent must be a positive integer.")

    if method == "newton":
        guess = base / 2
        while abs(guess ** exponent - base) > 1e-10:
            guess = (guess + base / guess ** exponent) / 2
        return guess

    elif method == "babylonian":
        guess = base / 2
        while True:
            next_guess = (exponent * guess + base / guess ** (exponent - 1)) / (exponent + 1)
            if abs(guess - next_guess) < 1e-10:
                return guess
            guess = next_guess

    else:
        raise ValueError(f"Unsupported method: {method}")


def calculate_square_root(base: float, method: str = "standart") -> float:
    """
    Computes the square root of base using the specified method.

    Args: base: The number for which the square root is computed. Must be a non-negative number. method: The method
    to use for computing the square root. Supported methods are "standart", "newton" and "babylonian".

    Returns:
        The square root of base.

    Raises:
        ValueError: If base is negative or if the specified method is not supported.
    """

    if base < 0:
        raise ValueError("Square root not defined for negative numbers.")

    if method == "standart":
        return base**(1/2)

    if method == "newton":
        guess = base / 2
        while abs(guess * guess - base) > 1e-10:
            guess = (guess + base / guess) / 2
        return guess

    elif method == "babylonian":
        guess = base / 2
        while True:
            next_guess = (guess + base / guess) / 2
            if abs(guess - next_guess) < 1e-11:
                return guess
            guess = next_guess

    else:
        raise ValueError(f"Unsupported method: {method}")


def cube_root(base: float, method: str = "newton") -> float:
    """
    Computes the cube root of base using the specified method.

    Args:
        base: The number for which the cube root is computed. Must be a non-negative number.
        method: The method to use for computing the cube root. Supported methods are "newton" and "babylonian".

    Returns:
        The cube root of base.

    Raises:
        ValueError: If base is negative or if the specified method is not supported.
    """

    if base < 0:
        raise ValueError("Cube root not defined for negative numbers.")

    if method == "newton":
        guess = base / 3
        while abs(guess ** 3 - base) > 1e-10:
            guess = (guess + base / guess ** 2) / 3
        return guess
    elif method == "babylonian":
        guess = base / 3
        while True:
            next_guess = (2 * guess + base / guess ** 2) / 3
            if abs(guess - next_guess) < 1e-10:
                return guess
            guess = next_guess
    else:
        raise ValueError(f"Unsupported method: {method}")

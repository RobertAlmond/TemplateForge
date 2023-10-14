# Required modules: sympy, decimal

import sympy
import decimal


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

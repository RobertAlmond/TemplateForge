# Required modules: sympy and decimal
# Version of this template without module "decimal" - calculate_speed2.py
# Version of this template without module "sympy" - calculate_speed3.py
# Version of this template without module "decimal and "sympy" - calculate_speed4.py

import sympy
import decimal


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

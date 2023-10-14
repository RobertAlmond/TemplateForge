# Required modules: sympy and decimal
# Version of this template without module "decimal" - calculate_speed2.py
# Version of this template without module "sympy" - calculate_speed3.py
# Version of this template without module "decimal and "sympy" - calculate_speed4.py

import sympy
import decimal


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

# Required modules: sympy
# Version of this template without module "sympy" - calculate_speed4.py

import sympy


def calculate_speed(distance: float or int or sympy.Number,
                    time: float or int or sympy.Number):
    """Calculates the speed of an object given the distance traveled and the time it took to travel that distance.

    Args:
        distance: The distance traveled in meters.
        time: The time it took to travel the distance in seconds.

    Returns:
        The speed of the object in meters per second.
    """

    return distance / time

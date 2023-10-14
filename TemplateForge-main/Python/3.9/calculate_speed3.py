# Required modules: sympy and decimal
# Version of this template without module "decimal" - calculate_speed4.py

import decimal


def calculate_speed(distance: float or int or decimal.Decimal,
                    time: float or int or decimal.Decimal):
    """Calculates the speed of an object given the distance traveled and the time it took to travel that distance.

    Args:
        distance: The distance traveled in meters.
        time: The time it took to travel the distance in seconds.

    Returns:
        The speed of the object in meters per second.
    """

    return distance / time

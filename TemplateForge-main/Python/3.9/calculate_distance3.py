# Required modules: decimal
# Version of this template without module "decimal" - calculate_distance4.py

import decimal


def calculate_distance(speed: float or int or decimal.Decimal,
                       time: float or int or decimal.Decimal):

    """Calculates the distance traveled by an object given its speed and the time it traveled.

    Args:
        speed: The speed of the object in meters per second.
        time: The time it took to travel the distance in seconds.

    Returns:
        The distance traveled by the object in meters, kilometers, feet, or inches.
    """

    return speed * time

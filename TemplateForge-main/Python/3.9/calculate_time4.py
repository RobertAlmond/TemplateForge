def calculate_time(distance: float or int,
                   speed: float or int):
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

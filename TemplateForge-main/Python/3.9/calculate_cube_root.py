# Additional information
#
# https://en.wikipedia.org/wiki/Cube_root
# https://en.wikipedia.org/wiki/Nth_root


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

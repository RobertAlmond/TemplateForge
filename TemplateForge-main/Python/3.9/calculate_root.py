# Additional information
#
# https://en.wikipedia.org/wiki/Square_root
# https://pidruchnyk.com.ua/793-algebra-merzlyak-8-klas-2016.html pages 88-90
# https://en.wikipedia.org/wiki/Nth_root


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

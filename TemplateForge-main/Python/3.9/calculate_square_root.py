# Additional information
#
# https://en.wikipedia.org/wiki/Square_root
# https://pidruchnyk.com.ua/793-algebra-merzlyak-8-klas-2016.html pages 88-90
# https://en.wikipedia.org/wiki/Nth_root


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

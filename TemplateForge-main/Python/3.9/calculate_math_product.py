def calculate_product(lower_bound: int, upper_bound: int, method: str = "iterative") -> int:
    if not isinstance(lower_bound, int) or not isinstance(upper_bound, int):
        raise TypeError("Arguments 'lower_bound' and 'upper_bound' must be integers.")

    if lower_bound > upper_bound:
        raise ValueError(
            f"In this function lower_bound({lower_bound}) couldn't be higher than upper_bound({upper_bound})")

    if method == "iterative":
        result = 1

        for i in range(lower_bound, upper_bound + 1):
            result *= i

        return result

    elif method == "recursive":
        result = lower_bound

        while lower_bound <= upper_bound:
            result *= lower_bound
            lower_bound += 1

        return result

    else:
        raise ValueError(f"Unsupported method: {method}")

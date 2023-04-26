def calculate_pi(n_terms: int) -> float:
    """calculate_pi

    Calculates the first n_terms of the Leibniz formula to pi

    Args:
        n_terms (int): The number of terms to be calculates

    Returns:
        float: The value of the pi
    """
    numerator: float = 4.0
    denominator: float = 1.0
    operation: float = 1.0
    pi: float = 0.0

    for _ in range(n_terms):
        pi += operation * (numerator / denominator)
        denominator += 2.0
        numerator *= -1.0
    return pi


if __name__ == "__main__":
    print(calculate_pi(1_000_000))

import pytest
from calculating_pi import calculate_pi


@pytest.mark.parametrize(
    "n_terms, result",
    [
        (-1, 0.0),
        (0, 0.0),
        (1, 4.0),
        (6, (4 - 4 / 3 + 4 / 5 - 4 / 7 + 4 / 9 - 4 / 11)),
    ],
)
def test_calculating_pi(n_terms: int, result: float) -> None:
    assert calculate_pi(n_terms) == result

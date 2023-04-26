import fibonacci
import pytest


@pytest.mark.parametrize(
    "n,expect_output",
    (
        [
            (0, 0),
            (1, 1),
            (2, 1),
            (5, 5),
            (10, 55),
            (20, 6765),
        ]
    ),
)
class TestFibonacci:
    def test_fib2(self, n: int, expect_output: int) -> None:
        assert fibonacci.fib2(n) == expect_output

    def test_fibonacci_memo(self, n: int, expect_output: int) -> None:
        assert fibonacci.fibonacci_memo(n) == expect_output

    def test_fibonacci_iterative(self, n: int, expect_output: int) -> None:
        assert fibonacci.fibonacci_iterative(n) == expect_output

    def test_fibonacci(self, n: int, expect_output: int) -> None:
        assert fibonacci.fibonacci(n) == expect_output

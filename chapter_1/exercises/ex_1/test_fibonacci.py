from collections import deque

import pytest
from fibonacci import Fibonacci


class TestFibonacci:
    def test_new_Fibonacci(
        self, new_Fibonacci: Fibonacci, new_Fibonacci_args: Fibonacci
    ) -> None:
        assert new_Fibonacci.get_sequence() == deque([0, 1])
        assert new_Fibonacci_args.get_sequence() == deque(
            [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        )

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
    def test_getitem_Fibonacci(
        self, new_Fibonacci: Fibonacci, n: int, expect_output: int
    ) -> None:
        assert new_Fibonacci[n] == expect_output

    def test_iterator_Fibonacci(self, new_Fibonacci: Fibonacci) -> None:
        for i, j in zip(
            new_Fibonacci.get_fibonacci_iterator(20),
            [
                0,
                1,
                1,
                2,
                3,
                5,
                8,
                13,
                21,
                34,
                55,
                89,
                144,
                233,
                377,
                610,
                987,
                1597,
                2584,
                4181,
                6765,
            ],
        ):
            assert i == j

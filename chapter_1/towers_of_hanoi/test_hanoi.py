from collections import deque

import hanoi
import pytest


@pytest.mark.parametrize(
    "n_disc",
    range(1, 21),
)
def test_hanoi(n_disc: int) -> None:
    tower_a: hanoi.Stack[int] = hanoi.Stack()
    tower_b: hanoi.Stack[int] = hanoi.Stack()
    tower_c: hanoi.Stack[int] = hanoi.Stack()

    for i in range(1, n_disc + 1):
        tower_a.push(i)

    hanoi.hanoi(tower_a, tower_c, tower_b, n_disc)

    assert tower_a == deque()
    assert tower_b == deque()
    assert tower_c == deque(range(1, n_disc + 1))

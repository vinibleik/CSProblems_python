from collections import deque
from typing import Deque, Generic, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: Deque[T] = deque()

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)

    def __eq__(self, __value: object) -> bool:
        return self._container == __value


def hanoi(
    begin: Stack[int], end: Stack[int], temp: Stack[int], n: int
) -> None:
    if n == 1:
        end.push(begin.pop())
    else:
        hanoi(begin, temp, end, n - 1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n - 1)


NUM_DISCS: int = 20

if __name__ == "__main__":
    tower_a: Stack[int] = Stack()
    tower_b: Stack[int] = Stack()
    tower_c: Stack[int] = Stack()

    for i in range(1, NUM_DISCS + 1):
        tower_a.push(i)
    print(tower_a)
    print(tower_b)
    print(tower_c, "\n")

    hanoi(tower_a, tower_c, tower_b, NUM_DISCS)

    print(tower_a)
    print(tower_b)
    print(tower_c)

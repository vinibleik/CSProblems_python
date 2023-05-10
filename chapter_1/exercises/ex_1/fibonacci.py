from collections import deque
from typing import Deque, Iterator


class Fibonacci:
    def __init__(self, n: int = 0) -> None:
        self.__sequence: Deque[int] = deque([0, 1])
        if n > 1:
            self.__update_fibonacci_sequence(n)

    def __next_fibonacci_number(self) -> int:
        return self.__sequence[-1] + self.__sequence[-2]

    def __update_fibonacci_sequence(self, n: int) -> None:
        while n >= len(self.__sequence):
            self.__sequence.append(self.__next_fibonacci_number())

    def get_fibonacci_iterator(self, n: int = 0) -> Iterator[int]:
        if n >= len(self.__sequence):
            self.__update_fibonacci_sequence(n)
        yield from self.__sequence

    def get_sequence(self, n: int = 0) -> Deque[int]:
        return self.__sequence

    def __getitem__(self, n: int) -> int:
        if n >= len(self.__sequence):
            self.__update_fibonacci_sequence(n)
        return self.__sequence[n]

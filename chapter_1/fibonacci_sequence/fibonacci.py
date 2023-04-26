import functools
import timeit
from statistics import mean
from typing import Dict, Generator

memo: Dict[int, int] = {0: 0, 1: 1}  # Base cases


def fib2(n: int) -> int:
    return n if n < 2 else fib2(n - 2) + fib2(n - 1)


def fibonacci_memo(n: int) -> int:
    """fibonacci_memo Return the n-th number of fibonacci sequence

    If I don't know the answer I calculate it, else I just return it.

    Args:
        n (int): n-th number

    Returns:
        int: n-th number of fibonacci sequence
    """
    if n not in memo:
        memo[n] = fibonacci_memo(n - 2) + fibonacci_memo(n - 1)

    return memo[n]


# @functools.lru_cache(maxsize=None)
@functools.cache
def fibonacci(n: int) -> int:
    """fibonacci_memo Return the n-th number of fibonacci sequence

    Fibonacci function implemented with cache memoization
    When this function is called with a new argument, its return will be cached.
    And then this function is called with the same argument, this cached value will be returned without perform the same calculations.

    Args:
        n (int): n-th number

    Returns:
        int: n-th number of fibonacci sequence
    """
    return n if n < 2 else fibonacci(n - 2) + fibonacci(n - 1)


def fibonacci_iterative(n: int) -> int:
    """fibonacci_iterative Return the n-th number of fibonacci sequence

    Iterative version of fibonacci function

    Args:
        n (int): n-th number

    Returns:
        int: n-th number of fibonacci sequence
    """
    if n == 0:
        return n

    last: int = 0  # fib(0)
    after: int = 1  # fib(1)

    for _ in range(1, n):
        last, after = after, last + after

    return after


def fibonacci_generator(n: int) -> Generator[int, None, None]:
    yield 0  # fib(0)
    if n > 0:
        yield 1  # fib(1)

    last: int = 0  # fib(0)
    after: int = 1  # fib(1)

    for _ in range(1, n):
        last, after = after, last + after
        yield after


if __name__ == "__main__":
    time = timeit.repeat(
        "fibonacci_iterative(50)",
        setup="from __main__ import fibonacci_iterative",
        repeat=10,
    )
    print(f"Mean fibonacci_iterative(50): {mean(time)*1000:.3f}ms")
    print(fibonacci(100))

    time = timeit.repeat(
        "fibonacci(100)", setup="from __main__ import fibonacci", repeat=10
    )
    print(f"Mean fibonacci cached(100): {mean(time)*1000:.3f}ms")
    print(fibonacci(100))

    time = timeit.repeat(
        "fibonacci_memo(100)",
        setup="from __main__ import fibonacci_memo",
        repeat=10,
    )
    print(f"Mean fibonacci_memo(100): {mean(time)*1000:.3f}ms")
    print(fibonacci_memo(100))

    time = timeit.timeit(
        "fib2(20)", setup="from __main__ import fib2", number=100
    )
    print(f"Fibonacci without memo: {time*1000:.3f}ms")
    print(fib2(20))

    print("Fibonacci sequence:")
    for i in fibonacci_generator(10):
        print(i)

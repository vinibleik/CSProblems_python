import pytest
from fibonacci import Fibonacci


@pytest.fixture
def new_Fibonacci() -> Fibonacci:
    return Fibonacci()


@pytest.fixture
def new_Fibonacci_args() -> Fibonacci:
    return Fibonacci(10)

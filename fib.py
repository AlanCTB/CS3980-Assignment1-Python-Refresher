#fib.py
#Author: Alan Chen
from functools import lru_cache
import time


def timer(func):
    """Decorator to measure the execution time of a function."""
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Finished in {execution_time:.8f}s: f({args[0]}) -> {result}")
        return result
    return wrapper

@lru_cache
@timer
def fib(n: int) -> int:
    """Computes the n Fibonacci numbers recursively."""
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    fib(100)
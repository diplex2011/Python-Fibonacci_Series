"""Fibonacci Series"""
# ? It is simply the series of numbers which starts from 0 and 1 and then continued by the addition of the preceding two numbers.
# create function that prints F.Series up to n


def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()


fib(100)

# return a list containing Fibonacci Series up to n


def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


print(fib2(100))

# ? alternate function fibonacci:using memoization (caching value)
fibonacci_cache = {}


def fibonacci(n):
    # If we have cached the value, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    fibonacci_cache[n] = value
    return value


for n in range(1, 100):
    print(n, ":", fibonacci(n))

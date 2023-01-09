def fibonacci_iter(n, a, b):
    if n == 0:
        return a
    else:
        return fibonacci_iter(n - 1, b, a + b)

def fibonacci(n):
    return fibonacci_iter(n, 0, 1)

print(fibonacci(6))
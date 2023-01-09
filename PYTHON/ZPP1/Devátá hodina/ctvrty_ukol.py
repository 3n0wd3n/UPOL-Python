def faktorial_iterateble_only(n):
    result = 1
    while n != 0:
        result *= n
        n -= 1
    return result
print(faktorial_iterateble_only(5))
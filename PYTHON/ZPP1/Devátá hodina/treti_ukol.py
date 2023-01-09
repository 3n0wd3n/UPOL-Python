def faktorial_iter(n, result):
    if n == 0:
        return result
    else:
        return faktorial_iter(n - 1, result * n)
    
def faktorial(n):
    return faktorial_iter(n, 1)

print(faktorial(5))
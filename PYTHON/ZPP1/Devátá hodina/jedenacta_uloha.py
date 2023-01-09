def power_iter(n, m, result):
    if m == 0:
        return result
    else:
        return power_iter(n, m - 1, n * result)

def power(n, m):
    return power_iter(n, m, 1)

print(power(4, 2))
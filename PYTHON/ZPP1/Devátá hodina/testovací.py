def power(n, m):
    if m == 0:
        x = 1
        y = print(x)
        return y
    else:
        z = print(n * power(n, m - 1))
        return z

print(power(3, 2))
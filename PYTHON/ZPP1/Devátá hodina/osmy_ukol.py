def mult(n, m):
    result = 0
    while m != 0:
        result += n
        m -= 1
    return result
print(mult(2, 5))
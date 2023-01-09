def mult_iter(n, m, result):
    if m == 0:
        return result
    else:
        return mult_iter(n, m - 1, result + n)

def mult(n, m):
    return mult_iter((n, m, 0))
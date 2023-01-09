def add(n, m):
    if m == 0:
        return n 
    else:
        return 1 + add(n, m - 1)

def mult(n, m):
    if m == 0:
        return 0
    else:
        return add(n, mult(n, m - 1))
    
def power(n, m):
    if m == 0:
        return 1
    else:
        return mult(n, power(n, m - 1))

print(power(3, 2))
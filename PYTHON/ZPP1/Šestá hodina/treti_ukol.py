"""
Pro dané přirozené číslo n > 1 vypočítejte přibližnou hodnotu zlatého řezu rovnou poměru an/an-1, kde ai je i-tý člen Fibonacciho posloupnosti.
"""
n = 50

a = 0
b = 1
for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c

golden_ratio = b / a
print(golden_ratio)
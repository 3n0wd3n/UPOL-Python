"""
Najděte největšího společného dělitele pomocí euklida a whilu.
"""
m = int(input('prvni cislo '))
n = int(input('druhe cislo '))

m1 = m
n1 = n

while m1 != 0:
    t = (n1 % m1)
    n1 = m1
    m1 = t
print("vysledek je ", n1)
gcd = n1

lcd = (n * m) // gcd
print(lcd)

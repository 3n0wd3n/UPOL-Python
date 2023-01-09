"""
# Vstup
a = int(input("Vložte první číslo: "))
b = int(input("Vložte druhé číslo: "))

# Program
result = a < b

# Výstup
print(result)
"""

# Větvení
"""
# Vstup
a = 5

# Program
if a < 10:
    print(a)
"""
"""
# Vstup (Zacílení na obsolutní hodnotu čísla)
x = -5

# Program
if x < 0:
    x = -x

# Výstup
print(x)
"""
"""
# Seřazení čísel

# Vstup
a = 4
b = 2

# Program
if b < a:
    c = a
    a = b
    b = c

# Výstup
print(a)
print(b)
"""
"""
# Vnořování podmínek

# Vstup
a = int(intput("Zadej číslo pro zjištění sudosti a jestli je číslo dělitelné 3: "))

# Program
if a % 2 == 0:
    if a % 3 == 0:
        print(1)
    print(2)
"""

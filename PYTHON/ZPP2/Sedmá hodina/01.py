def division(n, m):
    """Vrátí výsledek celočíselného dělení čísla n číslem m."""
    return n // m

def two_division(m):
    """Vrátí výsledek celočíselného dělení čísla dva číslem m."""
    return division(2, m)

def f():
    return f()

print(1)
print(a)

"""    
b = 0
c = two_division(b)
d = c * 2
print(d)
"""

"""
>>> int("dva")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'dva'
>>> int('1')
1
>>> 10.0 ** 10 ** 10
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
OverflowError: (34, 'Numerical result out of range')
"""
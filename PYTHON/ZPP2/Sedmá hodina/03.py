def division(n, m):
    return n // m

"""
print(division(8, 2))
print(division(8, 0))
"""

def safe_division(n, m):
    if m == 0:
        return 0
    else:
        return n // m

"""
print(safe_division(8, 2))
print(safe_division(8, 0))
print(safe_division(8, 'a'))
"""
"""
try:
    print(1)
    print(1/0)
    print(2)
except:
    print('chyba')
"""

"""
try:
    print(1/1)
except:
    print('chyba')
"""

def safe_division2(n, m):
    try:
        return division(n, m)
    except:
        return 0
"""
try:
    print(1/0)
except ZeroDivisionError:
    print('chyba')

try:
    print(1/'a')
except ZeroDivisionError:
    print('chyba')
"""

"""
try:
    try:
        print(1/'a')
    except ZeroDivisionError:
        print('chyba')
except TypeError:
    print('chyba typu')
"""

"""
try:
    print(1/'a')
except ZeroDivisionError:
    print('chyba')
except TypeError:
    print('chyba typu')
"""

def safe_division3(n, m):
    try:
        return division(n, m)
    except ZeroDivisionError:
        return 0

print(safe_division3(8, 2))
print(safe_division3(8, 0))
print(safe_division3(8, 'a'))
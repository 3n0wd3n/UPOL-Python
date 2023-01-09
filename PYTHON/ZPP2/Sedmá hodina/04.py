def division(n, m):
    return n // m

"""
print(division(8, 2))
print(division(8, 0))
"""
"""
try:
    print(1//0)
except ZeroDivisionError as error:
    print('Pozor nastala chyba:')
    print(error)
    raise error
"""

def my_division1(n, m):
    try:
        return division(n, m)
    except ZeroDivisionError as error:
        print(error)
        raise error
"""
try:
    print(1//0)
except ZeroDivisionError:
    raise ValueError('Chyba při výpočtu.')
"""

def my_division2(n, m):
    try:
        return division(n, m)
    except ZeroDivisionError:
        raise ValueError('Argument m nesmí být nula.')
# Můj první modul.
print('my_module loaded')
def square(n):
    """Vrátí čtverec čísla."""
    return n * n

def sum_of_squares(a, b):
    """Vrátí součet čtverců."""
    return square(a) + square(b)

def successor(n):
    """Vrátí následovníka čísla."""
    return n + 1

SPEED_OF_LIGHT = 299792458 # metrech za sekundu

# Modul nesmí mít stav.
def make_counter():
    return [0]

def incf_counter(counter):
    """Přište jedna k počítadlu."""
    counter[0] += 1
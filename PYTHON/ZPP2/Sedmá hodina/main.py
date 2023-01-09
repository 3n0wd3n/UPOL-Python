# Napište funkci, která získá od uživatele celé číslo. Pokud uživatel nezadá číslo, funkce jej informuje a pokusí se z něj získat číslo znovu.

# input
# int

def int_input(prompt):
    return int(input(prompt))

"""
int_input('Zadejte číslo: ')
"""

def int_input_repeat(prompt):
    while True:
        try:
            return int_input(prompt)
        except ValueError:
            print('Nezadali jste číslo. Zkuste to znovu.')

"""
int_input_repeat('Zadejte číslo: ')
"""
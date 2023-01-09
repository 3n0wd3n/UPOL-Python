# Vytvořit soubor numbers.txt, který bude obsahovat postupně čísla od nuly po zadané číslo, kde na každém řádku bude jedno číslo.

# Příklad: pro číslo 5 bude soubor numbers.txt vypadat:
# 0
# 1
# 2
# 3
# 4

# Není možné si nejdříve vytvořit řetězec s obsahem a poté jej uložit. Musíte čísla zapisovat postupně.

def store_numbers_range(filename, n):
    """Uloží čísla od nuly do n (bez n) do souboru."""
    file = open(filename, 'w')
    try:
        for i in range(n):
            file.write(str(i))
            if i != n - 1:
                file.write('\n')
    finally:
        file.close()

store_numbers_range('numbers2.txt', 30)
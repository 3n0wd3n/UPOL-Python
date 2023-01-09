"""
    Rozhodněte zdali jsou dvě čísla nesoudělná.
"""

a = int(input("Zadejte první číslo: "))
b = int(input("Zadejte druhé číslo: "))
counter = 0

for i in range(b):
    k = i + 1
    if a % k == 0 and b % k == 0:
        counter = counter + 1
je_nesoudelne = counter == 1
print(je_nesoudelne)

"""
    Program vezme dvě čísla 'a' a 'b'. Vezme to číslo, které je
    menší předpokládá se, že číslo 'b' je menší, jinak bychom museli
    přidat podmínku z minulého cvičení, která se kouká které to číslo je větší
    a které menší. Tím menším z nich provede cyklus b-krát. Do ká si
    uložíme výraz 'i + 1' abychom začínali od jedničky. A pak testujeme
    podmínku pro kterou platí, že abychom připsali do proměnné
    'counter' výraz 'counter + 1' musí obě čísla mít zbytek po dělení nulový.
    Cyklus se opakuje do té doby, dokud neprojede cyklus všechny 
    hodnoty 'b'. Nazávěr vyhodnocujeme, jestli v 'counter(u)' je jen 
    jedna hodnota nebo víc. Pokud je tam hodnot víc vrací 'counter'
    hodnotu 'False', pokud je tam jedna hodnota pak 'True'.

"""
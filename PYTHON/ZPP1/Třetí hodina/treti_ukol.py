"""
    Vytiskněte všechny společné dělitele dvou čísel.
"""

# Řešení učitele bez toho anižbychom pohlídali aby kod nemusel kontrolovat nadbytečné čísla.

# n = 6
# m = 6

# for i in range(n):
#     k = i + 1
#     if n % k == 0 and m % k == 0:
#         print(k)

# -------------------------------------------

# Moje řešení - kod hlída případy kdy druhé zadané číslo je větší než to první aby nemusel procházet nedbytečný počet čísel.

while True:
    a = int(input("Zadejte první číslo: "))
    b = int(input("Zadejte druhé číslo: "))

    if a > b:
        for i in range(b):
            k = i + 1
            if a % k == 0 and b % k == 0:
                print(k)

    else:
        l = a
        a = b
        b = l
        for i in range(b):
            k = i + 1
            if a % k == 0 and b % k == 0:
                print(k)

"""
    Jako první se načtou čísla do proměnných. Potom se pomocí podmínek vyhodnoti
    jestli je první čislo větší než druhé, protože na základě toho, pak budeme
    určovat kolikrat se cyklus provede aby nebylo nadbytečné opakování v případě že by druhé číslo
    bylo několika násobně větší než to první. Jakmile se tohle vyhodnotí spouští se cyklus
    b-krát, následně se do proměnné 'k' dosadí výraz 'i + 1', který jednoduše dělá to, 
    že nam bude v proměnné průběžně bude měnit hodnoty na základě toho v jakém jsme cyklu 
    plus o jedničku navrch abychom při prvním projetí cyklu nazačínali s nulou. 
    Potom se provádí podmínka která hlídá zda oba argumenty maji zbytek podělení roven nule
    pokud ano, tak se vypíše proměnná 'k'.
"""
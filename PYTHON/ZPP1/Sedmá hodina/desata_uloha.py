"""
Odstraňte ze seznamu všechny prvky, které jsou dělitelné zadaným číslem.
"""


def jsou_delitelne(n):
    seznam = [2, 3, 1, 4, 5, 9, 25, 15, 100]
    novy_seznam = []
    if n > 0:
        for i in range(len(seznam)):
            temp = seznam[i]
            if temp % n != 0:
                novy_seznam = novy_seznam + [temp]

    else:
        print("Dělitel musí být větší jak nula!")

    return novy_seznam


while True:
    delitel = int(input("Zadejte dělitele: "))
    print(jsou_delitelne(delitel))

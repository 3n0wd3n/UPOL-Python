"""
Napište funkci, která odstraní všechny výskyty zadané hodnoty ze seznamu.
"""


def vyskyty(x):
    pole = [2, 67, 3, 5, 6, 7, 99, 13, 1, 11,
            12, 21, 3, 7, 4, 6, 8, 2, 5, 4, 1, 0]
    nove_pole = []
    for i in range(len(pole)):
        temp = pole[i]
        if temp != x:
            nove_pole = nove_pole + [temp]
    return nove_pole


print(vyskyty(5))

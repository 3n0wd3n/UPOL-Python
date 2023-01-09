"""
Uživatel zadá číslo, které odkazuje na počet členu, které chce vyspat do seznamu 
a ten počet členů je posloupnost Fibbonaciho posloupnosti.

0, 1, 1, 2, 3, 5...
n = 5
sez = []

Shrnutí:

Napište funkci, která pro n vrací seznam prvních n prvků Fibonnaciho posloupnosti. 
Pro definiici se podívejte na ukol 6.3
"""

def fibbonaci(n):
    listing = []
    number_one = 0
    number_two = 1
    for i in range(n):
        temp = number_one + number_two
        listing = listing + [temp]
        number_one = number_two
        number_two = temp
    return listing
print(fibbonaci(12))

# #řešení učitele
# def fibbonaci(n):
#     result = []
#     a = 0
#     b = 1
#     for i in range(n):
#         result = result + [a]
#         c = a + b
#         a = b
#         b = c
#     return result
# print(fibbonaci(12))


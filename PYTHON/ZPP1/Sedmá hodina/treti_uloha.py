"""
Napište funkci, která pro daný seznam čísel spočítá produkt jeho prvků.
Produkt získá tak, že vynásobí všechny prvky seznamu. Co by měla funkce vrátit pro prázdný seznam?
"""

def product(list_):
    pruduct_of_numbers = 1
    for i in range(len(list_)):
        temp = list_[i]
        pruduct_of_numbers = pruduct_of_numbers * temp
    return pruduct_of_numbers
print(product([1, 2, 3]))

# Řešení učitele

# def product(list_):
#     pruduct_of_numbers = 1
#     for i in range(len(list_)):
#         temp = list_[i]
#         if temp == 0:
#             result = 0
#             break
#         pruduct_of_numbers = pruduct_of_numbers * temp
#     return pruduct_of_numbers
# print(product([1, 2, 3]))


"""
    Vystiskněte pro číslo 'n' všechna čísla menší než 'n' a ta čísla musí být s tím 'n' nesoudělná.
"""
n = int(input("Zadejte číslo pro, která chcete znát všechna jeho nesoudělná čísla:  "))

for j in range(n):
    l = j + 1
    counter = 0
    for i in range(l):
        k = i + 1
        if n % k == 0 and l % k == 0:
            counter = counter + 1
    if counter == 1:
        print(l)


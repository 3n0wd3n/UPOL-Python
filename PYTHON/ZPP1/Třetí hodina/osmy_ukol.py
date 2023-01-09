"""
    Vytiskněte pravoúhlý trojúhelník
    *
    **
    ***
    ****
"""

hvezdicky = int(input("Zadejte číslo: "))

for i in range(hvezdicky):
    k = i + 1
    print(k * "*")
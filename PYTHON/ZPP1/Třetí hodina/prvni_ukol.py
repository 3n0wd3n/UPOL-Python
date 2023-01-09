"""
    Je dáná aritmetická posloupnost a to tak, že máme první člen 'a1' a diference 'd' je rozdíl 
    sousedních členů. Číslo 'n' je počet člénů té posloupnosti. Nesmíme použít vzorec pro n-tý člen. Vytiskni prvních 'n' členů.
"""

# ----------------------------

# Můj způsob řešení

# prvni_clen = int(input("Vložte první člen a1: "))
# druhy_clen = int(input("Vložte druhý člen a2: "))
# pocet_clenu = int(input("Vložte počet 'n' členů: "))
# n = pocet_clenu

# diference = druhy_clen - prvni_clen
# finalni_cislo = prvni_clen
# for i in range(n):
#     finalni_cislo = finalni_cislo + diference
#     print(finalni_cislo)

# ---------------------------

# Správné řešení (podle učitele)

# a1 = 1
# d = 2
# n = 4

# a = a1
# for i in range(n):
#     print(a)
#     a = a + d

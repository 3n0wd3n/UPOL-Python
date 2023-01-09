"""
    Je dána aritmetická posloupnost a to tak, že máme první člen 'a1' a diference 'd' je rozdíl sousedních členů. 
    Sečtěte prvních n-členů dané posloupnosti bez použití vzorce.
"""

# Řešení s kubou

# prvni_clen = int(input("Vložte první člen a1: "))
# diference = int(input("Vložte diferenci: "))
# pocet_clenu = int(input("Vložte počet 'n' členů: "))
# kuba_ma_pravdu = prvni_clen
# misa_je_slozitej = 0

# for i in range(pocet_clenu):
#     misa_je_slozitej = kuba_ma_pravdu + misa_je_slozitej
#     kuba_ma_pravdu = kuba_ma_pravdu + diference
# print(misa_je_slozitej)

# Řešení učitele

# a1 = 2
# d = 2
# n = 5
# a = a1
# suma = 0
# for i in range(n):
#     suma = suma + a
#     a = a + d
# print(suma)

# Samostatné řešení

prvni_clen = 1
druhy_clen = 3
pocet_clenu = 5

diference = druhy_clen - prvni_clen

a1 = prvni_clen
d = diference
n = pocet_clenu

soucet = 0
for i in range(n):
    soucet = soucet + a1
    a1 = a1 + d
    # soucet = soucet + a1
print("Opravdový výsledek: ", end="")
print(soucet)


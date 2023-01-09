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
            # k = k + 1
            if a % k == 0 and b % k == 0:
                print(k)

    else:
        l = a
        a = b
        b = l
        for i in range(b):
            k = i + 1
            # k = k + 1
            if a % k == 0 and b % k == 0:
                print(k)
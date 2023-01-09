# Jestli je dané číslo palindrom --> vraťte nulu

# x = int(input("Zadejte čtyř-ciferné číslo: ")) # Vstup od uživatele (MĚJME X = 1234)

# c3 = x % 10                                    # C3 = 4
# x = x // 10                                    # X = 123
# c2 = x % 10                                    # C2 = 3
# x = x // 10                                    # X = 12
# c1 = x % 10                                    # C1 = 2
# x = x // 10                                    # X = 1
# c0 = x % 10                                    # C0 = 1

# print(c3)                                       # Výpis jednotlivých čísel
# print(c2)                                       #        |
# print(c1)                                       #        |
# print(c0)                                       #        |
# print(" ")                                      #        V
# if c3 == c0 and c2 == c1:
#     print(0)
# else:
#     print("Nejedná se o PALINDROM.")

# Mějme trojciferné číslo. Chceme vrátit jeho jednotlivé cifry.

# random_number = 123
# number_one = random_number % 10
# first_number = random_number // 10
# number_two = first_number % 10
# second_number = first_number // 10
# number_three = second_number % 10
# print(number_three)
# print(number_two)
# print(number_one)

# Uživatel zadá číslo (přirozené) a my chceme součet všech jeho čísel menších nebo rovno nule tomu n-přirozenému číslu.

# n = int(input("Zadej přirozené číslo: "))       # Vstup od uživatele

# adding_steps = 0                                # Počítadlo
# for i in range(n, 0, -1):
#     adding_steps += i
# print(adding_steps)

# Druhý způsob 
# n = int(input("Vložte číslo: "))

# citac = 0
# for i in range(n):
#     k = i + 1
#     citac = citac + k
# print(citac)

# Program vráti nulu právě když je zadané číslo dělitelné 2, 3 a 5

# x = int(input("Zadejte číslo: "))

# prvni_cislo = 2
# druhe_cislo = 3
# treti_cislo = 5

# if (((x % prvni_cislo) == 0) and ((x % druhe_cislo) == 0) and ((x % treti_cislo) == 0)):
#     print("YES BRO !!")
# else:
#     print("Eee-e")

#-----------------------------------------------------------------------------------------------------#

# ŘEŠENÍ PALINDROM

# Vstup od uživatele:
# x = int(input("Zadejte 4-ciferné číslo: "))

# Program:

# Nejprve získáme cifry čísla x
# c4 = x % 10
# x = x // 10
# c3 = x % 10
# x = x // 10
# c2 = x % 10
# c1 = x // 10

# # Rozdíly odpovídajících cifer
# r1 = c4 - c1
# r2 = c3 - c2

# # Soušet rozdílů
# palindrom = r1 * r1 + r2 * r2  # můžeme napsat i takto r1 ** 2 + r2 ** 2

# # Výstup
# print(palindrom)

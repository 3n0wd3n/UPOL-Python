"""
ÚKOL:
* * *
*   *
* * *
"""
# Můj kod

n = int(input("Vložte číslo: "))

print('*' * n)                    # Vrchní část
k = " " * (n - 2)                 #Uložím do proměnné počáteční číslo zmenšené o dvě, kterým následné násobím mezery tak abych docílil mezery
for i in range(n - 2):
    print("*" + k + "*")
print('*' * n)                    # Spodní část

# Jackie kod


# outer = int(input("Zadej velikost čtverce: "))

# inner = outer - 2
# print('*' * outer)
# for i in range(inner):
#     print('*' + ' ' * inner + '*')
# print('*' * outer)
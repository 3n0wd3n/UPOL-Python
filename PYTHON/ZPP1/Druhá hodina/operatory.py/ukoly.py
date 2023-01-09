# První úkol je = zjisti znaménko čísla
"""
# Vstup
x = int(input("Zadejte číslo: "))

# Program
if x > 0:
    print(1)
elif x == 0:
    print(0)
elif x < 0:
    print(-1)
else:
    print("Špatně zadané")
"""
# Druhý úkol je = zjistěte zda-li zadaná čísla a, b, c jsou definovaná tak aby a bylo z intervalu (b, c)
"""
# Vstup
a = int(input("Zadejte první číslo: "))
b = int(input("Zadejte druhé číslo: "))
c = int(input("Zadejte třetí číslo: "))

# Program
if a > b and a < c:
    print(True)
elif a > b and c > a:
    print(False)
else:
    print("Není z intervalu od b do c.")
"""

# Třetí úkol je = seřaďte čísla podle velikosti.
"""
# Vstup
a = int(input("Zadejte první číslo: "))
b = int(input("Zadejte druhé číslo: "))
c = int(input("Zadejte třetí číslo: "))

# Program
if a > b and a > c:
    if b > c:
        print(a)
        print(b)
        print(c)
    elif c > b:
        print(a)
        print(c)
        print(b)
    else:
        print("Bad input")
elif b > a and b > c:
    if a > c:
        print(b)
        print(a)
        print(c)

    elif c > a:
        print(b)
        print(c)
        print(a)
        print("Bad input")
elif c > a and c > b:
    if a > b:
        print(c)
        print(a)
        print(b)
    elif b > a:
        print(c)
        print(b)
        print(a)
        print("Bad input")
else:
    print("Špatné zadání")
"""
"""
# Čtvrtý úkol je = je dán bod x, y a vraťte kvadrant ve kterém se číslo nalézá. Jestli bod leží na osách nevracejte nic.
while (True):
 # Vstup
    x = int(input("Zadejte číslo x: "))
    y = int(input("Zadejte číslo y: "))

    # Program
    if x > 0 and y > 0:
        print("První kvadrant")
    elif x < 0 and y > 0:
        print("Druhý kvadrant")
    elif x < 0 and y < 0:
        print("Třetí kvadrant")
    elif x > 0 and y < 0:
        print("Čtvrtý kvadrant")
    else:
        print("Bad input")
"""
# Pátý úkol je = je dána úsečka p, q (px, py a qx, qy). Vraťte kvadranty ve kterých leží její body.
# Šestý úkol je = jsou dána čtyři čísla a otázka je jestli tyto čísla tvoří aritmetickou posloupnost.
"""
# Vstup
a = int(input("Zadejte první číslo: "))
b = int(input("Zadejte druhé číslo: "))
c = int(input("Zadejte třetí číslo: "))
d = int(input("Zadejte čtvrtý číslo: "))

# Program
if a > b and a > c and a > d:
    nejvetsi_cislo = a
    if b > c and b > d:
        druhe_nejvetsi_cislo = b
        if c > d:
            treti_nejvetsi_cislo = c , posledni_cislo = d
        if d > c:
            treti_nejvetsi_cislo = d , posledni_cislo = c
    if c > b and c > d:
        druhe_nejvetsi_cislo = c
        if b > d:
            treti_nejvetsi_cislo = b , posledni_cislo = d
        if d > b:
            treti_nejvetsi_cislo = d , posledni_cislo = b
    if d > b and d > c:
        druhe_nejvetsi_cislo = d
        if b > c:
            treti_nejvetsi_cislo = b , posledni_cislo = c
        if c > b:
            treti_nejvetsi_cislo = c , posledni_cislo = b
if b > a and b > c and b > d:
    nejvetsi_cislo = b
    if a > c and a > d:
        druhe_nejvetsi_cislo = a
        if c > d:
            treti_nejvetsi_cislo = c , posledni_cislo = d
        if d > c:
            treti_nejvetsi_cislo = d , posledni_cislo = c
    if c > a and c > d:
        druhe_nejvetsi_cislo = c
        if a > d:
            treti_nejvetsi_cislo = a , posledni_cislo = d
        if d > a:
            treti_nejvetsi_cislo = d , posledni_cislo = a
    if d > a and d > c:
        druhe_nejvetsi_cislo = d
        if a > c:
            treti_nejvetsi_cislo = a , posledni_cislo = c
        if c > a:
            treti_nejvetsi_cislo = c , posledni_cislo = a
if c > a and c > b and c > d:
    nejvetsi_cislo = c
    if a > b and a > d:
        druhe_nejvetsi_cislo = a
        if b > d:
            treti_nejvetsi_cislo = b , posledni_cislo = d
        if d > b:
            treti_nejvetsi_cislo = d , posledni_cislo = b
    if b > d and b > a:
        druhe_nejvetsi_cislo = b
        if a > d:
            treti_nejvetsi_cislo = a , posledni_cislo = d
        if d > a:
            treti_nejvetsi_cislo = d , posledni_cislo = a
    if d > a and d > b:
        druhe_nejvetsi_cislo = d
        if a > b:
            treti_nejvetsi_cislo = a , posledni_cislo = b
        if b > a:
            treti_nejvetsi_cislo = b , posledni_cislo = a
if d > a and d > b and d > c:
    nejvetsi_cislo = d
    if a > c and a > b:
        druhe_nejvetsi_cislo = a
        if c > b:
            treti_nejvetsi_cislo = c , posledni_cislo = b
        if b > c:
            treti_nejvetsi_cislo = b , posledni_cislo = c
    if b > a and b > c:
        druhe_nejvetsi_cislo = b
        if a > c:
            treti_nejvetsi_cislo = a , posledni_cislo = c
        if c > a:
            treti_nejvetsi_cislo = c , posledni_cislo = a
    if c > a and c > b:
        druhe_nejvetsi_cislo = c
        if a > b:
            treti_nejvetsi_cislo = a , posledni_cislo = b
        if b > a:
            treti_nejvetsi_cislo = b , posledni_cislo = a

print(nejvetsi_cislo)
print(druhe_nejvetsi_cislo)
print(treti_nejvetsi_cislo)
print(posledni_cislo)
d = nejvetsi_cislo - druhe_nejvetsi_cislo
print((b - a) == d and (d - c) == d)
"""
# Sedmý úkol je = jsou dány vnitřní úhly trojúhelníku ALFA, BETA, GAMA --> zjistěte jestli je trojúhelník ostroúhly(0), tupoúhlý(2), provoúhly(1).
"""
# Vstupy
alfa = int(input("Zadejte úhel alfa: "))
beta = int(input("Zadejte úhel beta: "))
gama = int(input("Zadejte úhel gama: "))

# Program
if alfa == 90 or beta == 90 or gama == 90:
    print(1)
elif alfa > 90 or beta > 90 or gama > 90:
    print(2)
elif (alfa < 90 and beta < 90):
    print(0)
"""
"""
# Vstupy
alfa = int(input("Zadejte úhel alfa: "))
beta = int(input("Zadejte úhel beta: "))
gama = int(input("Zadejte úhel gama: "))

# Program
if alfa == 90 or beta == 90 or gama == 90:
    print(1)
if alfa > 90 or beta > 90 or gama > 90:
    print(2)
if alfa < 90 and beta < 90 and gama < 90:
    print(0)
"""

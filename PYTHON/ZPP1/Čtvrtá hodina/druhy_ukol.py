"""
Vraťte cifraci přirozeného čísla. Cifrace čísla 'n' je číslo 'n' v případě, 
že 'n' je jednociferné. V opačném případě je to cifrace ciferného součtu čísla 'n'.
Například pro číslo 99, nejprve dostaneme 9 + 9 = 18, protože 18 není jednociferné číslo, proces opakujeme.
Ciferný součet čísla 18 = 1 + 8 = 9 a to je výsledek cifrace.
"""
n = 123
ciferny_soucet = n
n1 = n

while n1 // 10 != 0:
    ciferny_soucet = 0
    while n1 != 0:
        cifra = n1 % 10
        n1 = n1 // 10
        ciferny_soucet += cifra
    n1 = ciferny_soucet

print(ciferny_soucet)
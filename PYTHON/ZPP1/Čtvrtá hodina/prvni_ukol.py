"""
Vraťte ciferný součet přirozeného čísla
123
1 + 2 + 3 = 6
"""

n = 123
n1 = n
ciferny_soucet = 0

while n1 != 0:
    cifra = n1 % 10
    n1 = n1 // 10
    ciferny_soucet += cifra

print(ciferny_soucet)
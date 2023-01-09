"""
Vytisknět rozklad přirozeného číla na prvočíslo.
"""

n = int(input(" Please Enter any Number: "))
i = 2
while n > 2:
    if n % i == 0:
        n /= i
        print(i)
    else:
        i += 1
"""
Je dána přesnost d, řekněmě 10e-10. Předchozí program nám dává posloupnost stále se zlepšujíích odhadů zlatého řezu.
Upravte jej tak, aby výpočet skončil ve chvíli, kdy se sousední členy odhadů zlatého řezu budou lišit o méně než d.
"""
d = 1e-10

a = 0
b = 1

is_first = True
golden_ratio_old = d + 1
golden_ratio = 0
while is_first or abs(golden_ratio - golden_ratio_old) >= d:
    print(a)
    c = a + b
    a = b
    b = c
    golden_ratio_old = golden_ratio
    golden_ratio = b / a
    is_first = False
print(golden_ratio)
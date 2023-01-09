"""
Vytiskněte prvních n členů Fibonacciho posloupnosti. První člen je oven nule, druhý jedné a další je roven součtu je
roven součtu dvou předcházejícíh. Posloupnost tedy ztačíná 0,1,1,2,3,5,8 ....
"""
# Můj kod
# n = int(input("Zadejte počet n členů Fibonacciho posloupnosti: "))

# prvni_clen = 0
# druhy_clen = 1

# for i in range(n):
#     fibonacci = prvni_clen + druhy_clen
#     print(fibonacci)
#     prvni_clen = druhy_clen
#     druhy_clen = fibonacci

# Kod učitele
n = 5

a = 0
b = 1
for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c
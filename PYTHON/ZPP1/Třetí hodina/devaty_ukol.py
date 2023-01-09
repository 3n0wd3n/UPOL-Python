"""
Vytiskni rovnostranný trojúhelník
   *
  * *
 * * *
* * * *
   *
  ***
 *****
*******
"""

# Jackie style

# triangle = int(input("Zadej počet řádků: "))
# row = 0
# while row < triangle:
#     space = triangle - row - 1
#     while space > 0:
#         print(end=' ')
#         space -= 1
#     cross = row + 2
#     while cross > 1:
#         print('*', end=' ')
#         cross -= 1
#     row += 1
#     print()

# Majyks easy way :D

hvezdicky = int(input("Zadejte číslo: "))
mezery = hvezdicky
for i in range(hvezdicky):
    k = i + 1
    mezery = (mezery - 1)
    print(mezery * " ", ((k * 2) - 1) * "*")
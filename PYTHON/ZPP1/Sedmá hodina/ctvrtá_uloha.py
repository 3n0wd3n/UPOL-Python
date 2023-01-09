"""
Napište funkci reverse, která vrátí pro seznam s
seznam jehož prvky budou seznamu s v opačném pořádí.

Tedy:
reverse([2, 3, 4])
[4, 3, 2]
"""
def reverse(list_s):
    new_list_s = []
    for i in range(len(list_s)):
        temp = list_s[i]
        new_list_s = [temp] + new_list_s
    return new_list_s
print(reverse([2, 3, 4]))


"""
Je dáno "n". Vytiskněte prvních "n" dokonalých čísel.
Číslo "k" je dokonalé, jestliže je součtem všech svých dělitelů
"k" menších než "k" je roven "k".

Příklad:
6 = 1 + 2 + 3.
"""
# Druhá část programu 
# n = int(input("Zadejte počet prvních 'n' čísel pro který se má cyklus provést: "))

    # # První část programu
    # k = int(input("Zadejte číslo k: "))
    # divisor_sum = 0


    # for i in range(k - 1):
    #     divisor = i + 1
    #     if k % divisor == 0:
    #         divisor_sum += divisor
    # is_perfect = divisor_sum == k

    # print(is_perfect)

n = int(input("Zadejte počet prvních 'n' čísel pro který se má cyklus provést: "))
divisor_sum = 0
counter = 0
t = 1
while counter != n:
    divisor_sum = 0
    for i in range(t - 1):
        divisor = i + 1
        if t % divisor == 0:
            divisor_sum += divisor
    if t == divisor_sum:
        counter += 1
        print(t)
    t = t + 1    


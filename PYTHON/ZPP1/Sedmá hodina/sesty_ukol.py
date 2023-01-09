"""
Naprogramujte funkci, která rozhodne zda-li je hodnota
prvkem seznamu.
"""
def patri_do_seznamu(n):
    counter = 0
    for i in range(len(seznam)):
        temp = seznam[i]
        if n == temp:
            counter += 1
    return counter
seznam = [2, 3, 8, 23, 28, 298]
cislo_ze_seznamu = int(input("Vložte číslo, které si myslíte, že patří do seznamu: "))
x = (patri_do_seznamu(cislo_ze_seznamu))
if x == 1:
    print("Správně!!")
else:
    print("Smůla.")

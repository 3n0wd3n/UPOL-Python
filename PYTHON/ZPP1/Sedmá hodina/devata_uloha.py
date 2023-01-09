"""
Rozhodněte zda jeden seznam začíná prvky druhého seznamu.
"""


def totozny_zacatek(x):
    prvni_seznam = [2, 3, 1, 4, 5, 9]
    druhy_seznam = [2, 3, 1, 4, 5, 9, 6, 7, 1]
    if x > len(prvni_seznam):
        return False
    else:
        counter = 0
        for i in range(x):
            temp = prvni_seznam[i]
            temp_dva = druhy_seznam[i]
            if temp == temp_dva:
                counter += 1
        if counter == x:
            print("Prvních", x, "členů se rovná.")
        else:
            print("Prvních", x, "členů se nerovná.")


kolik_prvnich_prvku_se_bude_porovnavat = int(
    input("Zadejte kolik prvních prvků seznamů chcete porovnat: "))
print(totozny_zacatek(kolik_prvnich_prvku_se_bude_porovnavat))

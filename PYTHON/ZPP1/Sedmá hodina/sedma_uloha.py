"""
Napište funkci, která zjistí, zda je seznam uspořdaný od nejmenších hodnot k největším.
"""
def je_usporadany(seznam):
    counter = 0
    for i in range(len(seznam)):
        temp = seznam[i]
        if temp >= counter:
            counter = temp
        else:
            return counter
    return counter
# seznam = [1, 2, 3, 4, 5, 6]
seznam = [1, 2, 3, 4, 7, 6]
x = (je_usporadany(seznam))
if x == len(seznam):
    print("Uspořádaná.")
else:
    print("Není uspořádaná.")
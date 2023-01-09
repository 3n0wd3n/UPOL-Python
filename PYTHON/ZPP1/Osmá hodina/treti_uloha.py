"""
Pro řetězec obsahující slova oddělená mezerou vraťte seznam těchto slov.
"""

def string_list(list):
    space = " "
    word = ""
    pole = []

    counter = 1
    for j in range(len(list)):
        temp = list[j]
        if temp == space:
            counter += 1
    print(counter)
        
    for i in range(len(list) + counter):
        letter = list[i]
        if letter != space:
            word = word + letter
        else:
            pole = pole + [word]
            word = ""
    return pole




user_string = str(input("Vložte řetěze s mezerami: "))
print(string_list(user_string))
"""
Převedte řetězce znaků číslic na číslo zapsané těmito číslicemi. Tedy
pro řetězce "456" vraťte číslo 456.
"""
string = "123"

number = 0
for i in range(len(string)):
    char = string[i]
    digit = ord(char) - 48
    number *= 10
    number += digit
    print(i, char, digit, number)
print(number)
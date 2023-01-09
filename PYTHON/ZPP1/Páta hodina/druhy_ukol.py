"""
Převedte zadané číslo na řetězec znaků jeho číslic.
Například pro číslo 123 vratě retězec "123".
"""
number = 123

string = ""
n = number
while n != 0:
    digit = n % 10
    n //= 10
    char = chr(digit + 48)
    string = char + string
print(string)

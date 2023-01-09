"""
Odstrante nadbytečné mezery.
"""
string = "jablko hruška košík"

result = ""

s = string
if s != "":
    s += " "

word = ""
len_s = len(s)
for i in range(len_s):
    char = s[i]
    if char == " " and word != "":
        result += word
        if i != len_s - 1:
            result += " "
        word = ""
    elif char != " ":
        word += char
print(result)
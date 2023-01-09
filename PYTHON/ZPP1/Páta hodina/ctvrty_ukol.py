"""
Vytiskněte všechny slova obsažená v řetězci, kde sousední slova jsou oddělena mezerou.
Například pro "jablko banan hruska" vytiskněte:
jablko
banan
hruska
"""
string = "jablko hruška košík"

s = string
if s != "":
    s += " "

word = ""
for i in range(len(s)):
    char = s[i]
    if char == " ":
        print(word)
        word = ""
    else:
        word += char

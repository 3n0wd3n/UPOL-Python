"""
Rozhodněte, zda je česká věta zadaná jako řetězec palindrom.
Řetězec neobsahuje diakritická znaménka. Při kontrole ignorujte velikost písmen, mezery a interpunkci.
Tedy řetězec "Kobyla ma maly bok." je palindrom.
"""
string = "Kobyla ma maly bok."

normalized = ""
for i in range(len(string)):
    char = string[i]
    char_ord = ord(char)
    if 65 <= char_ord and char_ord <= 90:
        char_ord += 32
        char = chr(char_ord)
    if 97 <= char_ord and char_ord <= 122:
        normalized += char
print(normalized)
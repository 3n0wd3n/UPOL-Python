string = "Kobyla ma maly bo."

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
counter = 0
for j in range(len(normalized)):
    char_two = normalized[j]
    digit = ord(char_two) - 48
    counter *= 100
    counter += digit
print(counter)
counter_two = counter
k = 0
while counter != 0:
    l = counter % 100
    k = 100 * k + l
    counter //= 100
if k == counter_two:
    print("Je to palindrom!")
else:
    print("Není to palindrom!")

# Vytiskněte obsah souboru file2.txt bez textu v závorkách. Je povoleno číst soubor znak po znaku. 

# Program vytiskne: Asi  si koupím  slunečník .

file = open('file2.txt')
skip = False
try:
  char = file.read(1)
  while char != '':
    if char == "(":
      skip == True
    elif char == ")":
      skip == False
    else:
      if not skip:
        print(char, end="")
    char = file.read(1)
finally:
  file.close()

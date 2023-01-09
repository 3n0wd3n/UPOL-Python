# Program přidá uživatelem zadané jméno do souboru people.txt

for i in range(3):
  try:
    name = input(str("What is your name: "))
    file = open('append_text.txt', 'a')
    file.write(name + '\n')
  finally:
    file.close()
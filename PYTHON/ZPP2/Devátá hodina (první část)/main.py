#Uložit do zadaného souboru pouze sudá čísla nacházející se v jiném zadaném souboru.
#Není možné celý soubor načíst do paměti --> Musíme po částech.

# input_file = open('numbers.txt')
# try:
#   output_file = open('even_numbers3.txt', 'w')
#   try:
#     line = input_file.readline()
#     while line != '':
#       number = int(line)
#       if number % 2 == 0:
#         output_file.write(line)
#       line = input_file.readline()
#   finally:
#     output_file.close()
# finally:
#   input_file.close()

def file_numbers_filter(predicate, source, target):
    """Zapíše do souboru target pouze čísla, která splňují predikát."""
    input_file = open(source)
    try:
        output_file = open(target, 'w')
        try:
            line = input_file.readline()
            while line != '':
                number = int(line)
                if predicate(number):
                    output_file.write(line)
                line = input_file.readline() 
        finally:
            output_file.close()
    finally:
        input_file.close()

file_numbers_filter(lambda n: n % 2 == 0, 'numbers.txt', 'even_numbers4.txt')

# Napište funkci file_sum, která vrátí součet celých čísel v souboru, kde každé číslo je na jednom řádku.

def file_sum(filename):
    result = 0 
    file = open(filename)
    try:
        line = file.readline()
        while line != '':
            result += int(line)
            line = file.readline()
    finally:
        file.close()
    return result

print(file_sum('file.txt')) # 23


def file_reduce(operation, initial, filename):
    result = initial
    file = open(filename)
    try:
        line = file.readline()
        while line != '':
            result = operation(result, line)
            line = file.readline()
    finally:
        file.close()
    return result

print(file_reduce(lambda result, line: result + int(line), 0, 'file.txt'))
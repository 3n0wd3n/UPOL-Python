# Uložit do zadaného souboru pouze sudá čísla nacházející se v jiném zadaném souboru.
# Můžete předpokládat, že se vám obsah souboru vejde do paměti.

def load_file_content(filename):
    """Vrátí obsah souboru ve formě řetězce."""
    file = open(filename)
    try:
        return file.read()
    finally:
        file.close()

def store_file_content(filename, content):
    """Uloží řetězec do souboru."""
    file = open(filename,'w')
    try:
        file.write(content)
    finally:
        file.close()

def list_map(function, lst):
    """Vrátí seznam výsledků aplikací funkce na prvky seznamu."""
    result = []
    for element in lst:
        new_element = function(element)
        result += [new_element]
    return result

def list_filter(predicate, lst):
    """Vrátí seznam, který bude obsahovat pouze prvky seznamu lst, které splňují predikát."""
    result = []
    for element in lst:
        if predicate(element):
            result += [element]
    return result

def parse_numbers(string):
    """Převede řetězec, kde na každém řádku je jedno celé číslo, na seznam čísel."""
    lines = string.splitlines()
    return list_map(int, lines)

parse_numbers('1\n2\n33')

def is_even(n):
    """Rozhodne, zda je číslo sudé."""
    return  n % 2 == 0

# is_even(4)

def filter_even(lst):
    """Vrátí seznam pouze sudých čísel seznamu lst."""
    return list_filter(is_even, lst)

# filter_even([1, 2, 3, 4])

def stringify_numbers(numbers):
    """Převede seznam čísel na řetězec, kde na každém řádku bude zápis jednoho čísla."""
    lines = list_map(str, numbers)
    return '\n'.join(lines)

# stringify_numbers([1, 2, 3])

# parse_numbers(stringify_numbers([1, 2, 3]))
# stringify_numbers(parse_numbers('1\n2\n3'))

def load_numbers(filename):
    """Vrátí seznam čísel v souboru."""
    return parse_numbers(load_file_content(filename))

# load_numbers('numbers.txt')

def store_numbers(filename, numbers):
    """Uloží seznam čísel do souboru."""
    store_file_content(filename, stringify_numbers(numbers))

# store_numbers('test.txt', [1, 2, 3])

def file_numbers_filter_even(source, target):
    """Uloží do souboru target pouze sudá čísla ze souboru source."""
    numbers = load_numbers(source)
    even_numbers = filter_even(numbers)
    store_numbers(target, even_numbers)

file_numbers_filter_even('numbers.txt', 'even_numbers.txt')

def file_numbers_filter(predicate, source, target):
    """Uloží do souboru target pouze čísla ze souboru source, která splňují zadaný predikát."""
    numbers = load_numbers(source)
    result_numbers = list_filter(predicate, numbers)
    store_numbers(target, result_numbers)

file_numbers_filter(is_even, 'numbers.txt', 'even_numbers2.txt')
file_numbers_filter(lambda n: n < 30, 'numbers.txt', 'less_then_30_numbers.txt')
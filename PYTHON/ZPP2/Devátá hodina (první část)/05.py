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

def note():
 """ŠPATNĚ --> dlouhý ucelený kod ve funkci, která není rozložená na menší částí, takže je těžší děla testy"""
 pass

# def separate_even_numbers(filename_before, filename_after ):
#     list_item = load_file_content(filename_before)
#     lines = list_item.splitlines()
#     arr = list_map(int, lines)
#     temp = []
#     for i in range(len(arr)):
#       if arr[i] % 2 == 0:
#         temp += [arr[i]]
#     arr = list_map(str, temp)
#     store_file_content(filename_after, arr)

# print(separate_even_numbers('file2.txt', 'even_numbers.txt'))

def parse_numbers(string):
  """Převede řetězec, kde na každém řádku je jedno celé číslo, na seznam čísel."""
  lines = string.splitlines()
  return list_map(int, lines)

def is_even(n):
  """Rozhodne zda-li je číslo sude."""
  return n % 2 == 0

def filter_even(lst):
  """Vrátí seznam poze sudých čísel seznamu lst."""
  return list_filter(is_even, lst)

def stringify_numbers(numbers):
  """Převedeme seznam čísel na řetezec, kde na každém řádku bude zápis jedno čísla."""
  lines = list_map(str, numbers)
  return '\n'.join(lines)

def load_numbers(filename):
  """Vrátí seznam čísel v souboru."""
  return parse_numbers(load_file_content(filename))

def store_numbers(filename, numbers):
  """Uloží seznam čísel do souboru."""
  store_file_content(filename, stringify_numbers(numbers))

def file_numbers_filter_even(source, target):
  """Uloží do souboru target pouze sudá čísla ze souboru source."""
  numbers = load_numbers(source)
  even_numbers = filter_even(numbers)
  store_numbers(target, even_numbers)

file_numbers_filter_even('numbers.txt','even_numbers.txt')

def file_numbers_filter(predicate, source, target):
  """Uloží do soboru target poze čísla ze souboru souce, která splňuje zadaný predikát."""
  numbers = load_numbers(source)
  result_numbers = list_filter(predicate, numbers)
  store_numbers(target, result_numbers)

file_numbers_filter(is_even, 'numbers.txt', 'even_numbers2.txt')
file_numbers_filter(lambda n: n < 30, 'numbers.txt', 'less_then_30_numbers.txt.txt')
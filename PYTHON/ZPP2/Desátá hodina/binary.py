# bit je číslo 0 nebo 1.

# bit_not, bit_and, bit_or, bit_xor

def bit_not(x):
  """Bitová negace"""
  return 1 - x

def bit_and(x, y):
  """Bitový součin"""
  return x * y

def bit_or(x, y):
  """Bitový součet"""
  return min(x + y, 1)

def bit_xor(x, y):
  """Exkluzivní bytový součet"""
  return (x + y) % 2 

# Pomocné funkce.

def list_map(function, lst):
    """Vrátí seznam výsledků aplikací funkce na prvky seznamu."""
    result = []
    for element in lst:
        new_element = function(element)
        result += [new_element]
    return result

"""
list_map(lambda n: n ** 2, [1, 2, 3])
"""

def list_zip(list1, list2):
    """"Vrátí seznam dvojic, kde každá dvojice je tvořena prvkem prvního seznamu a pozičně odpovídajícímu prvku druhého seznamu."""
    result = []
    for i in range(len(list1)):
        result += [[list1[i], list2[i]]]
    return result

"""
print(list_zip([1, 2, 3], [4, 5, 6]))
"""

def two_list_map(function, list1, list2):
    """Vrátí seznam výsledků aplikací funkce na každý prvek seznamu list1 a pozičně odpovídající prvek seznamu list2."""
    return list_map(lambda pair: function(pair[0], pair[1]), list_zip(list1, list2))

"""
print(two_list_map(lambda n,m: n + m, [1, 2, 3], [4, 5, 6]))
"""
# bit_list je seznam bitů.

def bit_list_not(bit_list):
  """Vrátí seznam/list takový, kerý odpovídá negaci původního seznamu"""
  negation_list = list_map(bit_not, bit_list)
  return negation_list

print(bit_list_not([0, 1, 0, 1])) # [1, 0, 1, 0]

def bit_list_and(bit_list1, bit_list2):
  """Bitový součin seznamu"""
  return two_list_map(bit_and, bit_list1, bit_list2)

print(bit_list_and([0, 0, 1, 1], [0, 1, 0, 1])) # # [0, 0, 0, 1]

def bit_list_or(bit_list1, bit_list2):
    """Bitový součet seznamů bitů."""
    return two_list_map(bit_or, bit_list1, bit_list2)

"""
print(bit_list_or([0, 0, 1, 1], [0, 1, 0, 1])) # [0, 1, 1, 1]
"""

def bit_list_xor(bit_list1, bit_list2):
    """Exklusivní bitový součet seznamů bitů."""
    return two_list_map(bit_xor, bit_list1, bit_list2)

"""
print(bit_list_xor([0, 0, 1, 1], [0, 1, 0, 1])) # [0, 1, 1, 0]
"""

#bit_list_left_shift, bit_list_right_shift

def bit_list_left_shift(bit_list, n):
    """Posune seznam bitů o n bitů doleva."""
    if n == 0:
        return bit_list
    else:
        return bit_list_left_shift(bit_list + [0], n - 1)

print(bit_list_left_shift([1, 0, 1], 2)) # [1, 0, 1, 0, 0]

def bit_list_right_shift(bit_list, n):
    """Posune seznam bitů o n bitů doprava."""
    if n == 0:
        return bit_list
    else:
        return bit_list_right_shift(bit_list[:-1], n - 1)

print(bit_list_right_shift([1, 0, 1], 2)) # [1]

def fill_zeros(bit_list, n):
  """Doplní na začátek bitového seznamu n nul"""
  if n == 0:
    return bit_list
  else:
    return fill_zeros([0] + bit_list, n - 1)

def align_size(bit_list, n):
  """Doplní na začátek bitového seznamu nuly tak, aby výsledek měl délku n."""
  return fill_zeros(bit_list, n - len(bit_list))

print(align_size([1, 0, 1], 5)) # [0, 0, 1, 0, 1]

def set_bit_on(bit_list, n):
  """Nastaví na jedničku bit na n-tem indexu."""
  mask = [1]
  mask = bit_list_left_shift(mask, n)
  mask = align_size(mask, len(bit_list))
  return bit_list_or(bit_list, mask)


print(set_bit_on([1, 0, 0, 0, 1], 1)) # [1, 0, 0, 1, 1] 

def set_bit_off(bit_list, n):
  """Nastaví na nulu bit na n-tem indexu."""
  mask = [0]
  mask = bit_list_left_shift(mask, n)
  mask = align_size(mask, len(bit_list))
  return bit_list_or(bit_list, mask)

# set_bit_off([0, 1, 1, 1, 0], 1) # [0, 1, 1, 0, 0]

def get_bit(bit_list, i):
    """Vrátí bitový seznam, který bude mít na prvním místě i-tý bit bitového seznamu bit_list a jinak nuly."""
    result = bit_list_right_shift(bit_list, i)
    mask = [1]
    mask = align_size(mask, len(result))
    return bit_list_and(result, mask)

"""
get_bit([1, 0, 1, 0], 1) # [0, 0, 1]
"""

#Reprezentace celého nezáporného čísla
def unsigned_int_to_bit_list(n):
  """Převod z dekadické soustavy do binarni"""
  bit_list = []
  while n != 0:
    bit = n % 2
    bit_list = [bit] + bit_list
    n //= 2
  return bit_list

print(unsigned_int_to_bit_list(5)) # [1, 0, 1]
print(unsigned_int_to_bit_list(6)) # [1, 1, 0]

def bit_list_to_unsigned_int(bit_list):
  """Převod z binární soustavy do dekadické"""
  integer =  0
  for i in range(len(bit_list)):
    temp = bit_list[i]
    if temp != 0:
      integer = integer + 2 ** i
  return integer

print(bit_list_to_unsigned_int([0, 1, 1, 0])) # 6
print(bit_list_to_unsigned_int([1, 0, 1])) # 5
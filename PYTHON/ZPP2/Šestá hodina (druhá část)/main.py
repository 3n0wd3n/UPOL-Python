# Úkol: Odstraňte ze spojového seznamu všechny násobky zadaného čísla. Uveďte dvě verze. První nesmí změnit vstupní spojový seznam a druhá může.

# Všechny funkce musí mít komentáře.
# Každá funkce musí mít pod sebou dostatečný test.

# První verze do 30. března 8:45
# Odevzdávejte e-mailem a do hlavičky uveďte: ZPP2_1_1
# Řešení vložte do přílohy jako soubor.
# Opravy možné do 4. května 8:45
# Odpovědi na připomínky do jednoho týdne.

# Spojové seznamy a jejich změna

# Spojové seznamy a jejich změna

# Prázdný spojový seznam je pouze hodnota EMPTY.
EMPTY = []

# Neprázdný spojový seznam určuje první prvek a zbytek. Zbytek je opět spojový seznam.

def cons(value, lilist):
    """Vytvoří nový spojový seznam, kde první prek bude value a zbytek lilist."""
    return [value, lilist]

def get_first(lilist):
    """Vrátí první prvek neprázdného spojového seznamu."""
    return lilist[0]

def get_rest(lilist):
    """Vrátí zbytek neprázdného spojového seznamu."""
    return lilist[1]

def set_first(lilist, value):
    """Nastaví první prvek spojového seznamu."""
    lilist[0] = value

def set_rest(lilist, rest_ll):
    """Nastaví zbytek spojového seznamu."""
    lilist[1] = rest_ll

ll1 = cons(1, cons(2, cons(3, EMPTY)))

"""
ll1 = cons(1, EMPTY)
print(ll1)
set_first(ll1, 2)
print(ll1)
set_rest(ll1, cons(3, EMPTY))
print(ll1)
"""
# z minulého semináře
def nth_rest(lilist, n):
    """Vrátí spojový seznam bez prvních n prvků. Iterativní verze."""
    for i in range(n):
        lilist = get_rest(lilist)
    return lilist

# print(nth_rest(ll1, 2))

def nth(lilist, n):
    """Vrátí prvek na indexu n spojového seznamu."""
    ll = nth_rest(lilist, n)
    return get_first(ll)

def is_empty(lilist):
    """Rozhodne, zda je spojový seznam prázdný."""
    return lilist == EMPTY

def get_second(lilist):
    """Vrátí druhý prvek spojového seznamu."""
    return get_first(get_rest(lilist))

# print(get_second(ll1))

def get_third(lilist):
    """Vrátí třetí prvek spojového seznamu."""
    return get_second(get_rest(lilist))

# print(get_third(ll1))

# jednoduché funkce

def set_second(lilist, value):
    """Nastaví druhý prvek spojového seznamu."""
    set_first(get_rest(lilist), value)
    pass

ll1 = cons(1, cons(2, cons(3, EMPTY)))
set_second(ll1, 4)
print(ll1)

def set_third(lilist, value):
    """Nastaví třetí prvek spojového seznamu."""
    set_second(get_rest(lilist), value)
    pass

ll1 = cons(1, cons(2, cons(3, EMPTY)))
set_third(ll1, 4)
print(ll1)

# Přidání hodnoty na konec
def append_value(lilist, val):
    """Přidá nakonec spojového seznamu hodnotu  tak, že jej nezmění"""
    if is_empty(lilist):
      return cons(val, EMPTY)
    else:
      append_rest = append_value(get_rest(lilist), val)
      return cons(get_first(lilist), append_rest)
  
ll1 = cons(1, cons(2, EMPTY))
print(ll1)
ll2 = append_value(ll1, 3)
print(ll1) # [1, [2, []]]
print(ll2) # [1, [2, [3, []]]]

def get_last(lilist):
    """Vráti poslední neprázdný spojový seznam spojového seznamu."""
    while not is_empty(get_rest(lilist)):
      lilist = get_rest(lilist)
    return lilist
print(get_last(cons(1, cons(2, cons(3, EMPTY)))))

def add_to_end(lilist, val):
    """Přidá na konec spojového seznamu hodnotu tak, že jej může změnit. POUŽÍT SET_REST()"""
    if is_empty(lilist):
      return cons(val, EMPTY)
    else:
      last = get_last(lilist)
      set_rest(last, [val, EMPTY])
      return lilist

# def add_to_end(lilist, val): 
#     set_rest(get_last(lilist), cons(val, EMPTY))

ll1 = cons(1, cons(2, EMPTY))
print(ll1)
add_to_end(ll1, 3)
print(ll1) # [1, [2, [3, []]]]

# Odstranění hodnoty z konce
def remove_last(lilist):
    """Odstraní poslední prvek neprázdného spojového seznamu tak, že jej nezmění."""
    if is_empty(get_rest(lilist)):
      return EMPTY
    else:
      remove_from_rest = remove_last(get_rest(lilist))
      return cons(get_first(lilist), remove_from_rest)

ll1 = cons(1, cons(2, cons(3, EMPTY)))
print(remove_last(ll1))

def get_butlast(lilist):
    """Vrátí předposlední neprázdný spojový seznam spojového seznamu."""
    while not is_empty(get_rest(get_rest(lilist))):
      lilist = get_rest(lilist)
    return lilist

ll1 = cons(1, cons(2, cons(3, EMPTY)))
print(get_butlast(ll1)) # [2, [3, []]]

def delete_last(lilist):
    """Odstraní poslední prvek neprázdného spojového seznamu. Může jej změnit."""
    if is_empty(get_rest(lilist)):
      return EMPTY
    else:
      butlast = get_butlast(lilist)
      set_rest(butlast, EMPTY)
      return lilist

"""
ll1 = cons(1, cons(2, cons(3, EMPTY)))
print(ll1)
delete_last(ll1)
print(ll1) # [1, [2, []]]
"""

# Odstranění prvku na indexu
def remove_nth(lilist, n):
    """Odstraní ze spojového seznamu prvek na indexu n. Nezmění spojový seznam."""
    if n == 0:
      return get_rest(lilist)
    else:
      return cons(get_first(lilist), remove_nth(get_rest(lilist), n - 1))

"""
ll1 = cons(1, cons(2, cons(3, cons(4, EMPTY))))
print(remove_nth(ll1, 2))
print(remove_nth(ll1, 3))
print(remove_nth(ll1, 0))
"""

# def is_multiple(m, n):
#   if (m == n or m % n == 0) and m != 1:
#     return True
#   else:
#     return False

# def multiples(lilist, n):
#   while not is_empty(lilist):
#     first_number = get_first(lilist)
#     boolean = is_multiple(first_number, n)
#     if boolean:
#       print(remove_nth(lilist, 0))
#     lilist = get_rest(lilist)
#   return lilist

# ll1 = cons(1, cons(2, cons(3, cons(4, EMPTY))))
# print(multiples(ll1, 2))

# def is_multiple(m, n):
#     """Vrátí logickou hodnotu TRUE(v případě, že je číslo m dělitelné číslem n), nebo FALSE (v opačném případě)"""
#     if m == n or m % n == 0:
#       return True
#     else:
#       return False

# def multiples(lilist, n):
#     """Odstraní násobek zadaného čísla n spojového seznamu."""
#     lilist_two = lilist
#     counter = 0
#     while not is_empty(lilist):
#       first_number = get_first(lilist)
#       boolean = is_multiple(first_number, n)
#       if boolean:
#         lilist_two = remove_nth(lilist_two, counter)
#         counter -= 1
#       lilist = get_rest(lilist)
#       counter += 1
#     return lilist_two

# ll1 = cons(1, cons(2, cons(3, cons(4, EMPTY))))
# changed = multiples(ll1, 2)
# print("První", changed)

# Napadlo mě to udělat ještě tak, že prohodim ten prvek na určitém indexu s prvkem na prvnim indexu a zavolam get_rest

# def is_multiple(m, n):
#     """Vrátí logickou hodnotu TRUE(v případě, že je číslo m dělitelné číslem n), nebo FALSE (v opačném případě)"""
#     if m == n or m % n == 0:
#       return True
#     else:
#       return False

# def multiples(lilist, n):
#     """Odstraní násobek zadaného čísla n spojového seznamu."""
#     lilist_two = lilist
#     counter = 0
#     while not is_empty(lilist):
#       first_number = get_first(lilist)
#       boolean = is_multiple(first_number, n)
#       if boolean:
#         nth_ = nth(lilist_two, counter)
#         first = nth(lilist_two, 0)
#         lilist_two[counter] = [first]
#         lilist_two[0] = [nth_]
#         # lilist_two = cons(nth_, lilist_two)
#         print("a", nth_, first, lilist_two, counter)
#         lilist_two = get_rest(lilist_two)
#         counter -= 1
#       lilist = get_rest(lilist)
#       counter += 1
#     return lilist_two

# ll1 = cons(1, cons(2, cons(3, cons(4, EMPTY))))
# changed = multiples(ll1, 2)
# print("První", changed)


# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

"""
# TADY JSOU FUNKCE, KTERÉ NESMÍ ZMĚNIT POLE #

"""

# def reverse(lilist_two):
#     lilist = []
#     while not is_empty(lilist_two):
#       temp = get_first(lilist_two)
#       lilist = cons(temp, lilist)
#       lilist_two = get_rest(lilist_two)
#     return lilist

# def is_multiple(m, n):
#     """Vrátí logickou hodnotu TRUE(v případě, že je číslo m dělitelné číslem n), nebo FALSE (v opačném případě)"""
#     if m == n or m % n == 0:
#       return True
#     else:
#       return False

# def multiples(lilist, n):
#     """Odstraní násobek zadaného čísla n spojového seznamu. Nezmění původní seznam"""
#     if n == 0:
#       return lilist
#     lilist_two = []
#     while not is_empty(lilist):
#       first_number = get_first(lilist)
#       boolean = is_multiple(first_number, n)
#       if not boolean:
#             lilist_two = cons(first_number, lilist_two)
#       lilist = get_rest(lilist)
#     lilist_two = reverse(lilist_two)
#     return lilist_two

# ll1 = cons(1, cons(2, cons(3, cons(4, cons(5, cons(6, cons(7, EMPTY)))))))
# changed = multiples(ll1, 2)
# print("Result: ", changed)


"""
# TADY JSOU FUNKCE, KTERÉ MŮŽOU ZMĚNIT POLE #

"""

def lenght(lilist):
    """Vrátí délku pole."""
    counter = 0
    while not is_empty(lilist):
      lilist = get_rest(lilist)
      counter += 1
    return counter

def is_multiple(m, n):
    """Vrátí logickou hodnotu TRUE(v případě, že je číslo m dělitelné číslem n), nebo FALSE (v opačném případě)"""
    if m == n or m % n == 0:
      return True
    else:
      return False

def delete_all_multiples(lilist, n):
    """Odstraní násobek zadaného čísla n spojového seznamu. Může jej změnit."""
    if n == 0:
      return lilist
    for i in range(lenght(lilist)):
      first_number = get_first(lilist)
      boolean = is_multiple(first_number, n)
      if not boolean:
          add_to_end(lilist, first_number)
      rest_result = get_rest(lilist)
      set_rest(lilist, rest_result)
      # lilist = get_rest(lilist)
    return lilist

ll1 = cons(1, cons(2, cons(3, cons(4, cons(5, cons(6, cons(7, EMPTY)))))))
delete_all_multiples(ll1, 3)
print("Result: ", ll1)

# def delete_all_multiples(lilist, n):
#     """Odstraní ze spojového seznamu všechna sudá čísla. Seznam lilist může změnit."""
#     if is_empty(lilist):
#         return EMPTY
#     else:
#         rest_result = delete_all_multiples(get_rest(lilist), n)
        
#         set_rest(lilist, rest_result)
#         return lilist

# ll2 = EMPTY
# ll1 = cons(1, cons(2, cons(3, cons(4, cons(5, cons(6, cons(7, EMPTY)))))))
# delete_all_multiples(ll1, 3)
# print("Result: ", ll1)
# delete_all_multiples(ll2, 3)
# print("Result: ", ll2)
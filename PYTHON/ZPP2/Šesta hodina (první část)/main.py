# Zapouzdřený spojový seznam

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

# Odstranění prvku na indexu
def delete_second(lilist):
    third_rest = get_rest(get_rest(lilist))
    set_rest(lilist, third_rest)

"""
ll1 = cons(1, cons(2, cons(3, EMPTY)))
print(ll1)
delete_second(ll1)
print(ll1) # [1, [3, []]]
"""

def delete_nth(lilist, n):
    """Odstraní ze spojového seznamu prvek na indexu n. Může změnit spojový seznam."""
    if n == 0:
        return get_rest(lilist)
    else:
        current = lilist
        for i in range(n - 1):
            current = get_rest(current)
        delete_second(current)
        return lilist

"""
ll1 = cons(1, cons(2, cons(3, cons(4, EMPTY))))
print(ll1) # [1, [2, [3, [4, []]]]]
ll1 = delete_nth(ll1, 2)
print(ll1) # [1, [2, [4, []]]]
ll1 = delete_nth(ll1, 1)
print(ll1) # [1, [4, []]]
ll1 = delete_nth(ll1, 1)
print(ll1) # [1, []]
ll1 = delete_nth(ll1, 0)
print(ll1) # []
"""

# Zapouzdřený spojový seznam elilist - (encapsulation linked list)

def make_elilist(lilist):
    """Zapouzdří spojový seznam."""
    return [lilist]

def get_lilist(elilist):
    """Vrátí zapouzdřený seznam."""
    return elilist[0]

def set_lilist(elilist, lilist):
    """Nastaví spojový seznam zapouzdření."""
    elilist[0] = lilist

def e_delete_first(elilist):
    """Odstraní první prvek seznamu."""
    set_lilist(elilist, get_rest(get_lilist(elilist)))

"""
ll1 = cons(1, cons(2, EMPTY))
e1 = make_elilist(ll1)
print(e1)
e_delete_first(e1)
print(e1)
"""

# Napište funkci, která odstraní ze zapouzdřeného spojového seznamu prvek na indexu n. Funkce nesmí nic vracet. Může změnit zapozdřený seznam. Funkci otestujte.

def e_delete_nth(elilist, n):
  """Odstraní n-tý prvek seznamu."""
  set_lilist(elilist, delete_nth(get_lilist(elilist), n))

# JL: Výborně. 
"""
ll1 = cons(1, cons(2, EMPTY))
e1 = make_elilist(ll1)
print(e1)
e_delete_nth(e1, 0)
print(e1)
"""

# Využijte zapouzdření spojového seznamu k implementaci zásobníku.
# - make_stack
# - is_stack_empty
# - push
# - pop

def is_stack_empt(elilist):
  ll = get_lilist(elilist)
  if ll == EMPTY:
    # return set_lilist(elilist, EMPTY)ˇ
    return True
  else:
    return False

"""
ll1 = cons(1, cons(2, EMPTY))
ll2 = EMPTY
e2 = make_elilist(ll2)
e1 = make_elilist(ll1)
print(e1)
print(is_stack_empty(e1))
print(e2)
print(is_stack_empty(e2))
"""

def make_stack():
  """Vytvoří zásobník"""
  return [EMPTY]

def get_top(stack):
  """Vrátí spojový seznam prvků"""
  return stack[0]

def set_top(stack, lilist):
  """Nastaví spojový seznam prvků."""
  stack[0] = lilist

def is_empty(lilist):
    """Rozhodne, zda je spojový seznam prázdný."""
    return lilist == EMPTY

def is_stack_empty(stack):
  """Rozhodne, zda je zásobník prázdný."""
  return is_empty(get_top(stack))

def push(value, stack):
  """Přidání hodnoty na zásobník."""
  set_top(stack, cons(value, get_top(stack)))

"""
s = make_stack()
print(s)
push(1, s)
print(s)
push(2, s)
print(s)
"""

def pop(stack):
  """Odebrání prvku z vrcholu zásobníku."""
  ll = get_top(stack)
  set_top(stack, get_rest(ll))
  return get_first(ll)

"""
s = make_stack()
print(s)
push(1, s)
print(s)
push(2, s)
print(s)
print(pop(s))
print(s)
print(pop(s))
print(s)
"""

# Implementujte frontu (queue) pomocí zapozdřeného spojového seznamu
# - make_queue
# - is_queue_empty
# - enqueue
# - dequeue


def make_queue():
    """Vytvoří frontu."""
    return [EMPTY, EMPTY]

def get_front(queue):
    """Vrátí spojový seznam prvků fronty."""
    return queue[0]

def set_front(queue, front):
    """Nastaví spojový seznam prvků."""
    queue[0] = front

def get_back(queue):
    """Vrátí spojový seznam obsahující pouze poslední prvek fronty."""
    return queue[1]

def set_back(queue, back):
    """Nastaví spojový seznam s posledním prvkem fronty."""
    queue[1] = back

def is_queue_empty(queue):
    """Rozhodne, zda je fronta prázdná."""
    return is_empty(get_front(queue))

def enqueue(value, queue):
    """Přidá hodnotu na konec fronty."""
    tail = cons(value, EMPTY)
    if is_queue_empty(queue):
        set_front(queue, tail)
        set_back(queue, tail)
    else:
        back = get_back(queue)
        set_rest(back, tail)
        set_back(queue, tail)

q = make_queue()
print(q)
enqueue(1, q)
print(q)
enqueue(2, q)
print(q)

def dequeue(queue):
  """Odebere hodnotu ze začátku fronty a vrátí ji."""
  ll1 = get_front(queue)
  ll2 = get_rest(ll1)
  set_front(queue, ll2)
  if is_empty(ll2):
    set_back(queue, EMPTY)
  return get_first(ll1)

print(dequeue(q))
print(q)
print(dequeue(q))
print(q)
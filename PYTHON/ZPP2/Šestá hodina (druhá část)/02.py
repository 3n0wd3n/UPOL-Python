# Zásobník pomocí spojového seznamu

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

def is_empty(lilist):
    """Rozhodne, zda je spojový seznam prázdný."""
    return lilist == EMPTY

# Využijte zapouzdření spojového seznamu k implementaci zásobníku. 
# - make_stack
# - is_stack_empty
# - push
# - pop

def make_stack():
    """Vytvoří zásobník."""
    return [EMPTY]

def get_top(stack):
    """Vrátí spojový seznam prvků."""
    return stack[0]

def set_top(stack, lilist):
    """Nastaví spojový seznam prvků."""
    stack[0] = lilist

def is_stack_empty(stack):
    """Rozhodne, zda je zásobník prázdný."""
    return is_empty(get_top(stack))

def push(value, stack):
    """Přidá hodnotu na vrchol zásobníku."""
    set_top(stack, cons(value, get_top(stack)))

def pop(stack):
    """Odebere hodnotu z vrcholu zásobníku a vrátí ji."""
    ll = get_top(stack)
    set_top(stack, get_rest(ll))
    return get_first(ll)

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
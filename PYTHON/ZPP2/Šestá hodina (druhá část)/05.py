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


def is_empty(lilist):
	"""Rozhodne, zda je spojový seznam prázdný."""
	return lilist == EMPTY


# Jednoduché funkce
def length(lilist):
	"""Vrátí délku spojového seznamu. Iterativní verze."""
	result = 0
	while not is_empty(lilist):
		result += 1
		lilist = get_rest(lilist)
	return result


"""
ll1 = cons(1, cons(2, cons(3, EMPTY)))
print(length(ll1))
"""


def get_last(lilist):
	"""Vrátí poslední neprázdný spojový seznam spojového seznamu."""
	while not is_empty(get_rest(lilist)):
		lilist = get_rest(lilist)
	return lilist


"""
print(get_last(cons(1, cons(2, cons(3, EMPTY))))) # [3, []]
"""


def is_cycle(lilist):
	current = lilist
	while not is_empty(current):
		current = get_rest(current)
		if current is lilist:
			return True
	return False


ll1 = cons(1, cons(2, cons(3, EMPTY)))
last = get_last(ll1)
set_rest(last, ll1)

ll2 = cons(1, cons(2, cons(3, EMPTY)))
last = get_last(ll2)
set_rest(last, ll2)
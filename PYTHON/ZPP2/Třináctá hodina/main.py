# Uzel B-stromu (node) je seznam [keys, children, parent], kde
# - keys je seznam klíčů,
# - children je seznam potomků nebo None (pro list),
# - parent je rodič nebo None (pro kořen)

KEYS_INDEX = 0
CHILDREN_INDEX = 1
PARENT_INDEX = 2

def make_node(keys, children = None):
    """Vytvoří nový uzel."""
    node = [keys, None, None]
    set_children(node, children)
    return node

def get_keys(node):
    """Vrátí klíče uzlu."""
    return node[KEYS_INDEX]

def get_children(node):
    """Vrátí potomky uzlu."""
    return node[CHILDREN_INDEX]

def get_parent(node):
    """Vrátí rodiče uzlu."""
    return node[PARENT_INDEX]

def is_leaf(node):
    """Rozhodne, zda je uzel list."""
    return node[CHILDREN_INDEX] == None

def is_root(node):
    """Rozhodne, zda je uzel kořen."""
    return node[PARENT_INDEX] == None

def get_n(node):
    """Vrátí počet klíčů."""
    return len(get_keys(node))

def set_keys(node, keys):
    """Nastaví klíče uzlu."""
    node[KEYS_INDEX] = keys

def set_children(node, children):
    """Nastaví potomky uzlu."""
    old_children = node[CHILDREN_INDEX]
    if old_children != None:
        for old_child in old_children:
            old_child[PARENT_INDEX] = None
    node[CHILDREN_INDEX] = children
    if children != None:
       for child in children:
          child[PARENT_INDEX] = node


# Vytvoření:
node1 = make_node([1, 3])
node2 = make_node([6])
node3 = make_node([12, 15, 16])
node4 = make_node([5, 10], [node1, node2, node3])

# Je rodič správný?
children = get_children(node4)
child1 = children[0]
parent1 = get_parent(child1)
parent1 is node4

# Nastavení klíčů:
set_keys(node4, [4, 10])

# Nastavení dětí:
node5 = make_node([13, 17])
set_children(node4, [node1, node2, node5])
children = get_children(node4)
child3 = children[2]
get_parent(child3)



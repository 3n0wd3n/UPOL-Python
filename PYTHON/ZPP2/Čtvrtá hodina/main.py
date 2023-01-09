EMPTY = []

# lilist ... linked list
def cons(val, lilist):
    return [val, lilist]

ll1 = cons(1, cons(2, cons(3, EMPTY)))
ll2 = cons(4, cons(5, cons(6, EMPTY)))

def get_first(lilist):
    return lilist[0]

def get_rest(lilist):
    return lilist[1]

def is_empty(lilist):
    return lilist == EMPTY

# 1. get_second(lilist)
def get_second(lilist):
    return get_first(get_rest(lilist))
print(get_second(ll1))
# JL: Použijte get_first a get_rest.

# print(get_second(ll1)) #  2

# 2. get_thrid(lilist)
def get_third(lilist):
  return get_first(get_rest(get_rest(lilist)))
print(get_third(ll1))

# print(get_third(ll1)) #  3

# 3. nth(lilist, n)
# n = 0 .. první prvek

def nth_rest(lilist, n):
  for i in range(n):
    lilist = get_rest(lilist)
  return lilist

def nth(lilist, n):
  for i in range(n):
    lilist = get_rest(lilist)
  return get_first(lilist)

print(nth(ll1, 2))

# print(nth(ll1, 2)) # 2

# 4. lenght(lilist)

def lenght(lilist):
    counter = 0
    while not is_empty(lilist):
      lilist = get_rest(lilist)
      counter += 1
    return counter
print(lenght(ll1))

# JL: Použijte is_empty a get_rest.
#print(lenght(ll1)) #3

# 5. lenght_recursiv(lilist)
def lenght_recursiv(lilist):
  if is_empty(lilist):
    return 0
  else:
    return 1 + lenght_recursiv(get_rest(lilist))

print(lenght_recursiv(ll1))

#print(lenght_recursiv(ll1)) #3

# 6. lilist_range(n)
def lilist_range(n):
    lilist = EMPTY
    for i in range(n):
      lilist = cons(n - i, lilist)
    return lilist


#print(lilist_range(3)) #[0, [1, [2, []]]]

# 7. reverse(lilist)
def reverse(lilist):
    result = EMPTY
    while not is_empty(lilist):
          first = get_first(lilist)
          result = cons(first, result)
          lilist = get_rest(lilist)
    return result
print(reverse(ll1))

#print(reverse(ll1)) # [3, [2, [1, []]]]

# 8. is_member(val, lilist)
def is_member(val, lilist):
    counter = 0
    boole = False
    while not is_empty(lilist):
          value = nth(lilist, counter)
          if value == val:
            boole = True
          lilist = get_rest(lilist)
    return boole
print(is_member(3, ll1))


def is_member(val, lilist):
    while not is_empty(lilist):
          if get_first(lilist) == val:
            return True
          lilist = get_rest(lilist)
    return False
print(is_member(1, ll1))

#print(is_member(4, lilist)) # FALSE

# 9. is_member_rec(val, lilist)
def is_member_rec(val, lilist):
    if is_empty(lilist):
      return False
    elif get_first(lilist) == val:
      return True
    else:
      return is_member_rec(val, get_rest(lilist))

print(is_member_rec(4, ll1))

#print(is_member_rec(1, lilist)) # TRUE

# 10. append(lilist, lilist2)
def append(lilist, lilist2):
    lilist = reverse(lilist)
    while not is_empty(lilist):
      first1 = get_first(lilist)
      lilist2 = cons(first1, lilist2)
      lilist = get_rest(lilist)
    return lilist2
print(append(ll1, ll2))

#print(append(ll1, ll2)) #[1, [2, [3, [4, [5, [6, []]]]]]]


# 11. * lilist_map(function, lilist)

#print(lilist_map(lambda i: i + 1, ll1)) # [2, [3, [4, []]]]

# 12. * lilist_filter(predicate, lilist)

#print(lilist_filter(lambda i: i % 2 == 0, ll1)) #[2, []]

# 13. * lilist_reduce(function, initial, lilist)

#print(lilist_reduce(lambda a, b: a + b, 0, ll1)) #6

# 14. * Napsat lilist_map a lilist_filter pomocí list_reduce

# 15. is_sorted(lilist)
def is_sorted(lilist):
#     boolen = False
#     lenght_ = lenght(lilist)
#     counter = 0
#     while not is_empty(lilist):
#       first = get_first(lilist)
#       second = get_second(lilist)
#       if first <= second:
#         counter += 1
#       lilist = get_rest(lilist)
#     if lenght_ == counter:
#       boolen = True
#     return boolen
    lenght_ = lenght(lilist)
    for i in range(lenght_ - 1):
      first = get_first(lilist)
      second = get_second(lilist)
      if (first > second):
        return False
      lilist = get_rest(lilist)
    return True

print(is_sorted(cons(2, cons(1, EMPTY))))

#print(is_sorted(ll1)) # True
#print(is_sorted(cons(2, cons(1, EMPTY)))) # False

# 16. is_member_in_sorted(val, lilist)
def is_member_in_sorted(val, lilist):
  sorted_area = is_sorted(lilist)
  member = False
  if sorted_area:
    member = is_member(val, lilist)
  return member
print(is_member_in_sorted(1, ll1))

# 17. add_to_sorted(val, lilist)
def add_to_sorted(val, lilist):
  sorted_area = is_sorted(lilist)
  member = is_member_in_sorted(val, lilist)
  if not member and sorted_area:
    print(lilist)
    return append(lilist, [val, EMPTY])
  return False
print(add_to_sorted(4, ll1))

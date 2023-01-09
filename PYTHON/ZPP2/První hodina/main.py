def list_map(function, lst):
    result = []
    for el in lst:
        new_el = function(el)
        result += [new_el]
    return result


def list_filter(predicate, lst):
    result = []
    for el in lst:
        if predicate(el):
            result += [el]
    return result


# 1.
def map_abs(lst):
    return list_map(abs, lst)


print(map_abs([-1, 2, -5]))  # [1, 2, 5]


# 2.
def map_len(lst):
    return list_map(len, lst)


print(map_len([[1, 2], [], [3]]))  # [2, 0, 1]


# 3.
def successor(num):
    return num + 1


def map_row_successor(lst):
    return list_map(successor, lst)


def map_matrix_suc(matrix):
    return list_map(map_row_successor, matrix)


print(map_matrix_suc([[1, 2], [0, 1]]))  # [[2, 3], [1, 2]]


# 4.
def lenght(lst):
    return len(lst) > 0


def filter_nonempty(lst):
    return list_filter(lenght, lst)


print(filter_nonempty([[], [1, 2], [], [3]]))  # [[1, 2], [3]]


# 5. Vrátit čtverce kladných čísle zadaného seznamu.
def square(num):
    return num**2


def map_square(lst):
    return list_map(square, lst)


def is_positive(num):
    return num > 0


def filter_positive(lst):
    return list_filter(is_positive, lst)


def list_positive_square(lst):
    return map_square(filter_positive(lst))


print(list_positive_square([1, -2, 3, -3]))  # [1, 9]

# 6. bod je [x, y]
# Funkce převrátí seznam bodů podle x-ové osy.
# points_x_swap([[0, 0], [1, 1], [2, 1]]) # [[0, 0], [1, -1], [2, -1]]


# 7. (*)
def functi(num):
    return


def funct(num):
    return num + functi(num)


def list_sum(lst):
    return list_map(funct, lst)


def obecne(function, x, lst):
    ciselnej_operator = x
    for i in lst:
        ciselnej_operator = function(ciselnej_operator, i)
    return ciselnej_operator


def scitani(lst):
    return obecne(soucet_dvou, 0, lst)


def soucet_dvou(x, y):
    return x + y


print(scitani([1, 2, 3, 4]))


def odcitani(lst):
    return obecne(odecteni_dvou, lst[0] + lst[0], lst)


def odecteni_dvou(x, y):
    return x - y


print(odcitani([1, 2, 3, 4]))

# 8. (*)


def nasobeni(lst):
    return obecne(nasobeni_dvou, 1, lst)


def nasobeni_dvou(x, y):
    return x * y


print(nasobeni([1, 2, 3, 4]))

#print(list_product([1, 2, 3, 4])) # 24


###########################################


# list_reduce
def list_reduce(operation, neutral, lst):
  result = neutral
  for el in lst:
    result = operation(result, el)
  return result

# 1.
def concate(result, el):
  return result + el

def list_concat(lst):
  return list_reduce(concate, [], lst)

print(list_concat([[1, 2], [3, 4], [], [5]])) # [1, 2, 3, 4, 5]


# 2.
def reversing(result, el):
  return [el] + result

def reverse(lst):
  return list_reduce(reversing, [], lst)

print(reverse([1, 2, 3, 4])) # [4, 3, 2, 1]


# 3.
def summation(result, el):
  return el[0] + result

def bin_sum(lst):
  return list_reduce(summation, 0, lst)

print(bin_sum([[1, 2], [1, 2], [5, 0]])) # [7, 4]

"""
# 4. *
list_filter
"""

# compose
def compose(f, g):
  def result_function(val):
    return g(f(val))
  return result_function

def successor(num):
  return num + 1

def square(num):
  return num ** 2

def inverse(num):
  return (-1) * num

# 5.
# fourth_power(2) # 16
fourth_power = compose(square, square)
print(fourth_power(2))

# 6.
inverse_of_square = compose(square, inverse)
print(inverse_of_square(2)) # -4

# 7.
add_three = compose(square, successor)
print(add_three(2)) # 5

# 8.

def list_reduce(function, initial, lst):
  result = initial
  for el in lst:
    result = function(result, el)
  return result

def are_every(predicate, lst):
  return list_reduce(
  lambda result, el: False if not result else predicate(el), 
  True, 
  lst)

print(are_every(lambda num: num % 2 == 0, [2, 4, 6]))
print(are_every(lambda num: num % 2 == 0, [2, 4, 6, 1]))
print(are_every(lambda num: num % 2 == 0, []))

def are_all_less(number, lst):
  return are_every(
    lambda arg: arg < number,
    lst)

print(are_all_less(4, [1, 2, 3]))
print(are_all_less(4, [1, 2, 3, 8]))

def list_zip(list1, list2):
  result =[]
  for i in range(len(list1)):
      el1 = list1[i]
      el2 = list2[i]
      result += [[el1, el2]]
      # el = []
      # el1 = list1[i]
      # el2 = list2[i]
      # el += [el1]
      # el += [el2]
      # result += [el]
  return result


print(list_zip([1, 2, 3], [4, 5, 6]))

############################################¨

def list_reduce(function, initial, lst):
    result = initial
    for el in lst:
        result = function(result, el)
    return result

def are_every(predicate, lst):
    return list_reduce(
        lambda result, el: False if not result else predicate(el),
        True,
        lst)

def list_zip(list1, list2):
    result = []
    for i in range(len(list1)):
        result += [[list1[i], list2[i]]]
    return result

def is_multiple(n, m):
    return n % m == 0

def curry2(function, arg1):
    return lambda arg2: function(arg1, arg2)

# 1. are_all_div_by
# použijete: are_every a is_multiple
# are_all_div_by(2, [2, 4, 8, 6]) # True

def are_all_div_by(divisor ,lst):
  return are_every(
    lambda arg: is_multiple(arg, divisor),
    lst)

print(are_all_div_by(2, [2, 4, 8, 6]))

# 2. are_all_even
# použít: are_all_div_by a curry2
# are_all_even([2, 4, 6]) # True

are_all_even = curry2(are_all_div_by, 2)

print(are_all_even([1, 4, 6]))

# 3. are_all_pairs_div
# použít: curry2 a are_every a is_multiple
# are_all_pairs_div([[4, 2], [6, 3], [7, 1]]) # True

are_all_pairs_div = curry2(are_every,
lambda pair: is_multiple(pair[0], pair[1]))

print(are_all_pairs_div([[4, 2], [6, 3], [7, 1]])) 

# 4. are_all_div
# použít: are_all_pairs_div a list_zip
# are_all_div([4, 6, 7], [2, 3, 1]) # True


# list_reduce(...)

sum_neutral = 0

def sum_operation(result, el):
  return result + el

def list_sum(lst):
  result = sum_neutral
  for el in lst:
    result = sum_operation(result, el)
  return result

print(list_sum([1, 2, 3, 4])) # 10

product_neutral = 1

def product_operation(result, el):
  return result * el

def list_product(lst):
  result = product_neutral
  for el in lst:
    result = product_operation(result, el)
  return result

print(list_product([1, 2, 3, 4])) # 24


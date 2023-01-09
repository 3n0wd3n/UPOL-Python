def list_reduce(operation, neutral, lst):
  result = neutral
  for el in lst:
    result = operation(result, el)
  return result

sum_neutral = 0

def sum_operation(result, el):
  return result + el

print(list_reduce(sum_operation, sum_neutral, [1, 2, 3, 4 ]))  

def list_sum(lst):
  return list_reduce(sum_operation, sum_neutral, lst)

print(list_sum([1, 2, 3, 4])) # 10

product_neutral = 1

def product_operation(result, el):
  return result * el

print(list_reduce(product_operation, product_neutral, [1, 2, 3, 4 ]))

def list_product(lst):
  return list_reduce(product_operation, product_neutral, lst)

print(list_product([1, 2, 3, 4])) # 24


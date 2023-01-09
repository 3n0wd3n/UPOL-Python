def list_sum(lst):
  result = 0
  for el in lst:
    result += el
  return result

print(list_sum([1, 2, 3, 4])) # 10

def list_product(lst):
  result = 1
  for el in lst:
    result *= el
  return result

print(list_product([1, 2, 3, 4])) # 24
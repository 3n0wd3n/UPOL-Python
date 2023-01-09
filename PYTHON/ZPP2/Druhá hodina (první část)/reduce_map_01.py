def list_reduce(operation, neutral, lst):
  result = neutral
  for el in lst:
    result = operation(result, el)
  return result

def map_succ_operation(result, el):
  return result + [el + 1]

print(list_reduce(map_succ_operation, [], [1, 2, 3]))
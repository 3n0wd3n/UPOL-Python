def list_reduce(operation, neutral, lst):
  result = neutral
  for el in lst:
    result = operation(result, el)
  return result

def create_map_operation(function):
  def map_operation(result, el):
    return result + [function(el)]
  return map_operation

def successor(num):
  return num + 1

map_succ_operation = create_map_operation(successor)

print(list_reduce(map_succ_operation, [], [1, 2, 3]))

def square(num):
  return num ** 2

map_square_operation = create_map_operation(square)

print(list_reduce(map_square_operation, [], [1, 2, 3]))
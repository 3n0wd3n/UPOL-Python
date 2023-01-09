def list_reduce(operation, neutral, lst):
  result = neutral
  for el in lst:
    result = operation(result, el)
  return result

def create_map_operation(function):
  def map_operation(result, el):
    return result + [function(el)]
  return map_operation

def list_map(function, lst):
  map_operation = create_map_operation(function)
  return list_reduce(map_operation, [], lst)

def successor(num):
  return num + 1

print(list_map(successor, [1, 2, 3]))

def square(num):
  return num ** 2

print(list_map(square, [1, 2, 3]))
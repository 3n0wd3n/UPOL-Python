def successor(num):
  return num + 1

def square(num):
  return num ** 2

def compose(f, g):
  def result_function(val):
    return g(f(val))
  return result_function

successor_of_square = compose(square, successor)

print(successor_of_square(3))

square_of_successor = compose(successor, square)

print(square_of_successor(3))
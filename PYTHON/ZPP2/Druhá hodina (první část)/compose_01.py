def successor(num):
  return num + 1

def square(num):
  return num ** 2

def successor_of_square(num):
  return successor(square(num))

def square_of_successor(num):
  return square(successor(num))
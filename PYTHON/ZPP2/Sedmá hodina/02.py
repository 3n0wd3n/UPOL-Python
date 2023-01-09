def factorial(n):
  """Vrátí faktoriál celého nezáporného čísla."""
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

"""
print(factorial(5))
print(factorial(-1))
"""

def factorial_iter(n):
  """Vrátí faktoriál celého nezáporného čísla."""
  result = 1
  i = n
  while i != 0:
    result *= i
    i -= 1
  return result

"""
print(factorial_iter(5))
print(factorial_iter(-1))
"""

def factorial_iter2(n):
  """Vrátí faktoriál celého nezáporného čísla."""
  result = 1
  for i in range(2, n+1):
    result = result * i
  return result

"""
print(factorial_iter2(5))
print(factorial_iter2(-1))
"""

def factorial_iter3(n):
  """Vrátí faktoriál celého nezáporného čísla."""
  if n < 0:
      raise ValueError(f'Číslo n nesmí být záporné. Zadáno: {n}')
  result = 1
  for i in range(2, n+1):
    result = result * i
  return result

"""
print(factorial_iter3(5))
print(factorial_iter3(-1))
"""
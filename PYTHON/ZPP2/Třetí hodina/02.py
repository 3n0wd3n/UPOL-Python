def square(number):
  return number ** 2

# lambda p1, ..., pn: e
# p1, ..., pn jsou parametry
# e je výraz

square2 = lambda number: number ** 2

add = lambda a,b: a + b

add2 = lambda a: lambda b: a + b

def my_abs(num):
  if num < 0:
    return -num
  else:
    return num

# e1 if c else e2

# if c:
#     return e1
# else:
#     return e2

my_abs2 = lambda num: -num if num < 0 else num
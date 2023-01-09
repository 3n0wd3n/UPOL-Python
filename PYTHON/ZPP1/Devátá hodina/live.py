def make_fract(num, den):
  if den == 0:
    return num // den
  else:
    return [num, den]

#print(make_fract(1, 2))

def get_num(fract):
  return fract[0]
  
# print(get_num(make_fract(1, 2)))

def get_den(fract):
  return fract[1]

# print(get_den(make_fract(1, 2)))

def print_fract(fract):
  print('make_fract(', end='')
  print(get_num(fract), end=', ')
  print(get_den(fract), end='')
  print(')')

# print_fract(make_fract(1, 2))

def are_fracts_equal(fract1, fract2):
  num1 = get_num(fract1)
  den1 = get_den(fract1)
  num2 = get_num(fract2)
  den2 = get_den(fract2)
  return  num1 * den2 == num2 * den1

# print(are_fracts_equal(make_fract(1, 2), make_fract(1, 2)))
# print(are_fracts_equal(make_fract(1, 2), make_fract(2, 4)))
# print(are_fracts_equal(make_fract(1, 2), make_fract(1, 4)))

def add_fracts(fract1, fract2):
  num1 = get_num(fract1)
  den1 = get_den(fract1)
  num2 = get_num(fract2)
  den2 = get_den(fract2)
  num_result = num1 * den2 + num2 * den1
  den_result = den1 * den2
  return make_fract(num_result, den_result)

#print_fract(add_fracts(make_fract(1, 2), make_fract(1, 2)))
#print_fract(add_fracts(make_fract(1, 3), make_fract(1, 2)))

def mult_fracts(fract1, fract2):
  num1 = get_num(fract1)
  den1 = get_den(fract1)
  num2 = get_num(fract2)
  den2 = get_den(fract2)
  num_result = num1 * num2
  den_result = den1 * den2
  return make_fract(num_result, den_result)

# print_fract(mult_fracts(make_fract(1, 2), make_fract(2, 1)))

def compute_gcd(n, m):
  while m != 0:
    tmp = m
    m = n % m
    n = tmp
  return n

# print(compute_gcd(6, 8))
# print(compute_gcd(10, 15))
# print(compute_gcd(8, 9))

def reduce_fract(fract):
  num = get_num(fract)
  den = get_den(fract)
  gcd = compute_gcd(num, den)
  return make_fract(num // gcd, den // gcd)

# print_fract(reduce_fract(make_fract(5, 10)))
# print_fract(reduce_fract(mult_fracts(make_fract(1, 2), make_fract(2, 1))))

def add_inverse_fract(fract):
  num = get_num(fract)
  den = get_den(fract)
  return make_fract(-num, den)

# f1 = make_fract(1, 2)
# print_fract(add_fracts(f1 , add_inverse_fract(f1)))

def sub_fracts(fract1, fract2):
  return add_fracts(fract1, add_inverse_fract(fract2))

# print_fract(sub_fracts(make_fract(1, 1), make_fract(1, 3)))

def mult_inverse_fract(fract):
  num = get_num(fract)
  den = get_den(fract)
  return make_fract(den, num)

# f1 = make_fract(1, 2)
# print_fract(mult_fracts(f1 , mult_inverse_fract(f1)))

def div_fracts(fract1, fract2):
  return mult_fracts(fract1, mult_inverse_fract(fract2))

# print_fract(div_fracts(make_fract(1, 1), make_fract(1, 3)))

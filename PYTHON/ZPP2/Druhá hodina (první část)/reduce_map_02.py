def create_add_function(step):
  def add_function(num):
    return num + step
  return add_function
  
successor = create_add_function(1)
add_two = create_add_function(2)

print(create_add_function(3)(5))
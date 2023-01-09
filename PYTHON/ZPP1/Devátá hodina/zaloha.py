def make_empty_table():
    array = []
    return array
#print(make_empty_table())

def get_table_row(table, row_number):
  return table[row_number]
#print(get_table_row([[1, 'a'], [2, 'b']], 0))

def get_table_row_count(table):
  lenght_of_table = len(table)
  return lenght_of_table
#print(get_table_row_count([[1, 'a'], [2, 'b'], 4, 5]))

def get_row_cell(row, column):
  return row[column]
#print(get_row_cell([1, 'a', True], 1))

def get_row_cell_count(row):
  row_cell_count = len(row)
  return row_cell_count
#print(get_row_cell_count([1, 'a', True]))

def are_rows_equal(row1, row2):
  row_cell_count = get_row_cell_count(row1)
  row_cell_count_two = get_row_cell_count(row2)
  if row_cell_count == row_cell_count_two:
    counter = 0
    for i in range(row_cell_count):
      row_cell = get_row_cell(row1,i)
      row_cell_two = get_row_cell(row2,i)
      if row_cell == row_cell_two:
        counter += 1
    if counter == row_cell_count:
      return True
    return False
  return False
#print(are_rows_equal([1, 2, 3, 8], [1, 2, 3 ,8]))

def print_row(row):
  row_cell_count = get_row_cell_count(row)
  for i in range(row_cell_count):
    row_cell = get_row_cell(row, i)
    print(row_cell, end = "\t")

#print_row([1, 'a', True])

def print_table(table):
  table_row_count = get_table_row_count(table)
  for i in range(table_row_count):
    print_row(get_table_row(table, i))
    print()
   
#print_table([[1, 'a'], [2, 'b']])

def add_row_to_table(table, row):
  return table + [row]

#print(add_row_to_table([[1, 2], [3, 4]], [5, 6]))

def contains_row(table, row):
  table_row_count = get_table_row_count(table)
  counter = 0
  for i in range(table_row_count):
    table_row = get_table_row(table, i)  
    rows_equal = are_rows_equal(table_row, row)
    if rows_equal == True:
      counter += 1
  if counter > 0:
    return True
  return  False

#print(contains_row([[1, 2], [3, 4]], [1, 2]))

def intersection(table1, table2):
  empty_table = make_empty_table()
  table_row_count = get_table_row_count(table1)
  for i in range(table_row_count):
    tab1 = get_table_row(table1, i)
    temp = contains_row(table2, tab1)
    if temp == True:
      empty_table = add_row_to_table(empty_table, tab1)
  return empty_table

print_table(intersection([[1, 'c'], [2, 'a'], [3, 'b']], [[4, 'b'], [1, 'c'], [1, 'a']]))
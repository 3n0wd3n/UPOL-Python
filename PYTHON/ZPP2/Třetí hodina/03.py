def list_reduce(function, initial, lst):
    result = initial
    for el in lst:
        result = function(result, el)
    return result

def list_filter(predicate, lst):
    reduce_function = lambda result, val: result + [val] if predicate(val) else result
    return list_reduce(reduce_function, [], lst)

def list_map(function, lst):
    reduce_function = lambda result, val: result + [function(val)]
    return list_reduce(reduce_function, [], lst)

square = lambda number: number ** 2

print(list_map(square, [1, 2, 3])) # [1, 4, 9]

is_even = lambda number: number % 2 == 0

print(list_filter(is_even, [1, 2, 3])) # [2]
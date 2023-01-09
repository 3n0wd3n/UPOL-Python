# def add(n, m):
#     if m == 0:
#         return n
#     else:
#         return add(n + 1, m - 1)

# print(add(2, 2))

def add (n , m ):
    print ('Calling add with ', n , 'and ', m )
    if m == 0:
        result = n
    else :
        result = add( n + 1 , m - 1)
    print ('Result of calling add with ', n , 'and ', m , 'is ', result )
    return result

print(add(2, 2))
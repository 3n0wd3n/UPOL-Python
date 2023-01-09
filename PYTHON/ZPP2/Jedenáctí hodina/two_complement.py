from bit_list import align_size as align_bit_list_size, bit_list_not

# Reprezentace celých nezáporných čísel.
def unsigned_int_to_bit_list(integer):
    """Převede celé nezáporné číslo na seznam bitů."""
    bit_list = []
    while integer != 0:
        bit = integer % 2
        bit_list = [bit] + bit_list
        integer //= 2
    return bit_list

"""
unsigned_int_to_bit_list(5) # [1, 0, 1]
"""

def bit_list_to_unsigned_int(bit_list):
    """Převede seznam bitů na celé nezáporné číslo."""
    integer = 0
    for i in range(len(bit_list)):
        if bit_list[i] == 1:
            integer += 2 ** (len(bit_list) - i - 1)
    return integer

"""
bit_list_to_unsigned_int([1, 0, 1])
"""
def number_to_bit_list(number, size):
    """Převede celé číslo na seznam bitů podle dvojkového doplňkového kódu."""
    if number >= 0:
        bit_list = unsigned_int_to_bit_list(number)
        if size <= len(bit_list):
            raise ValueError('Size of bit list is to small.')
        return align_bit_list_size(bit_list, size)
    else:
        return bit_list_not(number_to_bit_list(-number-1, size))
        

"""
number_to_bit_list(-124, 8) # [1, 0, 0, 0, 0, 1, 0, 0]
number_to_bit_list(-3, 3) # [1, 0, 1]
number_to_bit_list(3, 3) # [0, 1, 1]
"""

def bit_list_to_number(bit_list):
    """Převede seznam bitů na celé číslo podle dvojkového doplňkového kódu."""
    sign_bit = bit_list[0]
    if sign_bit == 0:
        return bit_list_to_unsigned_int(bit_list)
    else:
        return -bit_list_to_number(bit_list_not(bit_list))-1
"""
bit_list_to_number(bit_list)

bit_list_to_number([0, 1, 1]) # 3
bit_list_to_number([1, 0, 1]) # -3

bit_list_to_number(number_to_bit_list(-124, 8))
"""

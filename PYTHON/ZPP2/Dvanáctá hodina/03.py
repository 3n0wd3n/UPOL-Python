from binary_file import read_byte_list, write_byte_list

SIZE = 3

# Matice 3x3
# [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
# Hodnoty jsou v rozdahu 0 - 255.

def store_matrix(file_name, matrix):
    """Uloží matici do souboru."""
    file = open(file_name, 'bw')
    try:
        for row in matrix:
            write_byte_list(file, row)
    finally:
        file.close()
    
"""
store_matrix('matrix.b', [[0, 1, 2], [3, 4, 5], [6, 7, 8]])
"""

def load_matrix(file_name):
    """Načte matici ze souboru."""
    file = open(file_name, 'br')
    try:
        matrix = []
        for i in range(SIZE):
            row = read_byte_list(file, SIZE)
            matrix += [row]
        return matrix
    finally:
        file.close()
"""
load_matrix('matrix.b')
"""

def load_cell(file_name, i, j):
    """Načte ze souboru buňku na i-tém řádku v j-tém sloupci."""
    file = open(file_name, 'br')
    try:
        position = SIZE * i + j
        file.seek(position)
        byte_list = read_byte_list(file, 1)
        return byte_list[0]
    finally:
        file.close() 

"""
load_cell('matrix.b', 1, 1) # 4
"""

def replace_cell(file_name, cell1, cell2):
    """V matici nahradí všechny výskyty cell1 za cell2."""
    file = open(file_name, 'br+')
    try:
        byte_list = read_byte_list(file, 1)
        while len(byte_list) == 1:
            cell = byte_list[0]
            if cell == cell1:
                position = file.tell()
                file.seek(position - 1)
                write_byte_list(file, [cell2])
            byte_list = read_byte_list(file, 1)
    finally:
        file.close() 

"""
replace_cell('matrix.b', 0, 5)
"""
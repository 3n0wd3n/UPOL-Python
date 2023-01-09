from binary_file import read_byte_list, write_byte_list

SIZE = 2

# Matici 2x2
# [[0, 1], [2, 3]]
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
store_matrix('matrix.b', [[0, 1], [2, 3]])
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
# Úkol 1: Ukládat matice různých rozměrů.
store_matrix('matrix1.b', [[0, 1, 2], [3, 4, 5], [6, 7, 8]])
store_matrix('matrix2.b', [[0, 1], [2, 3]])
store_matrix('matrix3.b', [[0]])

load_matrix('matrix1.b') # [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
load_matrix('matrix2.b') # [[0, 1], [2, 3]])
load_matrix('matrix3.b') # [[0]]

# a) Velikost souboru. Není optimální řešení.
# b) Uložit velikost na začátek.

# Úkol 2: Práce s obdelníkovými maticemi 
store_matrix('matrix2.b', [[0, 1, 3], [4, 5, 6]])

# Úkol 3: Zvýšit rozsah hodnot na dva bajty. 

# Úkol 4: Snížit rozsah hodnot na čtyři bity. Dvě buňky jsou v jednom bajtu.
"""
Bez použítí operátoru == a != na porovnání seznamů napište 
funkci, která rozhodne, zda jsou dva seznamy rovny.txt
"""
def are_equal(list1, list2):
    if len(list1) != len(list2):
        return False
    else:
        result = False 
        for i in range(len(list1)):
            element1 = list1[i]
            element2 = list2[i]
            result = result and element1 == element2
        return result
print(are_equal([1, 2, 3],[2, 1, 3]))
"""
Rozhodněte zda je jeden seznam podseznamem druhého.
"""

# def je_podseznamem(seznam, podseznam):
#     lenght = len(podseznam)
#     counter = 0
#     for i in range(len(podseznam)):
#         temp = podseznam[i]
#         for j in range(len(seznam)):
#             temp_ = seznam[j]
#             if temp == temp_:
#                 counter += 1
#     x = lenght == counter
#     return x

# print(je_podseznamem([1, 2, 2, 3], [2, 2]))

# Řešení učitele

def starts_from(start_index, list1, list2):
    starts_from__result = True
    for i in range(len(list1)):
        element1 = list1[i]
        element2 = list2[i + start_index]
        if element1 != element2:
            starts_from__result = False
    return starts_from__result

# print(is_sublist(1, [1, 2][1, 2, 3])))

def is_sublist(list1, list2):
    is_sublist_result = False
    for i in range(len(list2) - len(list1) + 1):
        if starts_from(i, list1, list2):
            is_sublist_result = True
    return is_sublist_result

print(is_sublist([1, 2, 3], [2, 1, 2]))

# Kubův kod

# def Sublist(array, subarray):
#     for i in range(len(array)):
#         truth = True
#         for j in range(len(subarray)):
#             if array[i] == subarray[j]:
#                 truth &= True
#                 if i + 1 < len(array):
#                     i += 1
#                 if j == len(subarray) - 1 and truth == True:
#                     return truth
#             else:
#                 truth = False
#     return truth

# print(Sublist([1, 2, 3], [2, 1, 2]))
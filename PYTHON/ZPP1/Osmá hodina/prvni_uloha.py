"""
Odstraní duplicitníé hdonoty v seznamu ale zároven zanechá pořadí
"""
def remove_duplicates(input_list):
    result = []
    for i in range(len(input_list)):
        element = input_list[i]
        is_member = False
        for j in range(len(result)):
            result_element = result[j]
            if element == result_element:
                is_member = True
                break
        if not is_member:
            result = result + [element]
    return result

print(remove_duplicates([1, 2, 2, 1, 3]))
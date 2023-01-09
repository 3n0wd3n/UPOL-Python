"""
Umeli byste předchozí úkol napsat tak, aby se při
výpočtu používaly poslední dva prvky tvořeného seznamu?
"""
def fibbonaci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    result = [0, 1]
    for i in range(n):
        last_index = len(result) - 1
        butlast_index = len(result) - 2
        last_element = result[last_index]
        butlast_element = result[butlast_index]
        next_element = last_element + butlast_element
        result = result + [next_element]
    return result
print(fibbonaci(5))

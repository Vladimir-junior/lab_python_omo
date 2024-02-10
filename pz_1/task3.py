from random import randint

def list_operation(n):
    l = []
    p = 1

    for i in range(n):
        l.append(randint(1, 100))

    for index, j in enumerate(l):
        if index % 2 != 0:
            p *= j

    max_element = max(l)
    l.remove(max_element)
    new_l = l[:]
    new_l.sort(reverse=True)
    max_element_3 = new_l[:3]
    result = {
        "list": l,
        "proizvedenie": p,
        "max_element": max_element,
        "new_list": l,
        "3_max_elements": max_element_3
    }

    return result

number = int(input())
print(list_operation(number))

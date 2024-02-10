from random import choice, randint
import string

def dict_connect(n):
    list1 = []
    list2 = []
    for i in range(n):
        list1.append(choice(string.ascii_letters))
    for j in range(n):
        list2.append(randint(1, 100))
    result_dict = dict(zip(list1, list2))

    return result_dict


number = int(input("size:"))

print(dict_connect(number))
def get_type(value):
    if type(value) == dict:
        if not value:
            return "Словарь пуст."
        return f"Ключ с минимальным значением: {min(value, key=value.get)}."
    elif type(value) == list:
        zero_element_index = [i for i, x in enumerate(value) if x == 0]
        if len(zero_element_index) < 2:
            return "В списке должно быть как минимум два нулевых элемента."
        product_zero_numbers = 1
        product_list = value[zero_element_index[0]:zero_element_index[1]]
        product_list.pop(0)
        for i in product_list:
            product_zero_numbers *= i
        new_list = list(set(value))
        return f"произведение между первым и вторым нулевыми элементами: {product_zero_numbers}, cписок без повторяющихся элементов: {new_list}"
    elif type(value) == int:
       if value == 0:
           return "Число равно 0, делители не определены."
       dividers = [i for i in range(1, value + 1) if value % i == 0]
       return f"Делители числа {value} = {dividers}."
    elif type(value) == str:
        if value == "":
            return "Строка пуста."
        elif value == " ":
            return "Строка пуста."
        revers_value = value[::-1]
        palindrome = value == revers_value
        l_v = 0
        l_c = 0
        for e in value:
            if e in 'ауоиэыяюеёАУОИЭЫЯЮЕЁ':
                l_v += 1
        for e in value:
            if e in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
                l_c += 1
        return f"Строка является палиндромом: {palindrome}, количество гласныхи {l_v}, согласных {l_c}."
    else:
        return "Неподдерживаемый тип данных."


def main():
    # ---------test-------
    print(get_type({'a': 3, 'b': 1, 'c': 2}))
    # print(get_type({}))
    # print(get_type([1, 2, 3]))
    # print(get_type([]))
    # print(get_type([1, 0, 2, 0, 3, 4, 0]))
    # print(get_type(12))
    # print(get_type(0))
    # print(get_type("наган"))
    # print(get_type(""))
    # print(get_type("привет"))

if __name__ == '__main__':
    main()
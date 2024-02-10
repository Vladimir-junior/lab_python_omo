dict_info = {
    "Кольцо З" : ["Золотое кольцо с бриллиантами", 230, 7],
    "Кольцо З" : ["Золотое кольцо с изумрудом", 470, 8],
    "Кольцо С" : ["Серебреное обручальное кольцо с фианитами", 170, 11],
    "Цепочка З" : ["Золотая цепочка", 345, 9],
    "Цепочка БЗ" : ["Белое золотая цепочка", 324, 5],
    "Браслет С" : ["Серебреный браслет", 215, 6]
}

def menu_shop(value):
    match value:
        case '1':
            discr = input("Введите название: ")
            l = (dict_info.get(discr))
            print(f'\n{l[0]}')
        case '2':
            discr = input("Введите название: ")
            l = (dict_info.get(discr))
            print(f'\n{l[1]}')
        case '3':
            discr = input("Введите название: ")
            l = (dict_info.get(discr))
            print(f'\n{l[2]}')
        case '4':
            for i, j in dict_info.items():
                print(f"[{i}] -> {j}")
        case '5':
            # while n != 0:
            discr = input("Введите название: ")
            n = int(input("Введите количество: "))
            l = (dict_info.get(discr))
            l[2] -= n
            price = l[1] * n
            print(f'\n Общая цена: {price}')

        case '6':
            return False
        case _:
            print("Неверный выбор. Пожалуйста, введите номер пункта меню.")
    return True


def main():
    while True:
        print("\n-----------------------")
        print ("1. Просмотр описания.\n2. Просмотр цены.\n3. Просмотр количества.\n4. Всю информацию.\n5. Покупка.\n6. До свидания")
        print("-----------------------\n")
        value = input("Выберите пункт меню: ")
        if not menu_shop(value):
            break

main()

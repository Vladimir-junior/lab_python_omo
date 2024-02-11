def menu_shop_jewelry(value: str, dict_info: dict) -> bool:
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
            total_price = 0
            while True:
                print('Введите название изделия, n – выход из покупки.')
                discr = input("Введите название: ")
                if discr == 'n':
                    break
                l = dict_info.get(discr)
                if l:
                    n = input("Введите количество: ")
                    if n.isdigit():
                        n = int(n)
                        if n <= l[2]:
                            l[2] -= n
                            price = l[1] * n
                            total_price += price
                            print(f'\nОбщая цена: {price}')
                            print(f'Общая сумма: {total_price}')
                        else:
                            print("Недостаточно товара на складе.")
                    else:
                        print("Введите корректное количество.")
                else:
                    print("Такого изделия не найдено.")
        case '6':
            return False
        case _:
            print("Неверный выбор. Пожалуйста, введите номер пункта меню.")
    return True


def main():
    dict_info = {
        "Кольцо звезда": ["Золотое кольцо с бриллиантами", 230, 10],
        "Кольцо зленый глаз": ["Золотое кольцо с изумрудом", 470, 15],
        "Кольцо счастья": ["Серебреное обручальное кольцо с фианитами", 170, 3],
        "Цепочка легенда": ["Золотая цепочка", 345, 8],
        "Цепочка белый ангел": ["Белое золотая цепочка", 324, 11],
        "Браслет прелесть": ["Серебреный браслет", 215, 9]
    }
    while True:
        print("\n-----------------------")
        print ("1. Просмотр описания.\n2. Просмотр цены.\n3. Просмотр количества.\n4. Всю информацию.\n5. Покупка.\n6. До свидания")
        print("-----------------------\n")
        value = input("Выберите пункт меню: ")
        if not menu_shop_jewelry(value, dict_info):
            break

if __name__ == '__main__':
    main()
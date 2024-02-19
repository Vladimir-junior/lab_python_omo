def block_tef(x, y):
    try:
        result = x / y
    except TypeError:
        print("Ошибка: невозможно выполнить деление для данных типов.")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль.")
    else:
        print("Результат:", result)
    finally:
        print("Блок прошел проверку.")


def main():
    print("-----------------------")
    block_tef(6, 2)
    print("-----------------------")
    block_tef(8, 0)
    print("-----------------------")
    block_tef("12", 2)
    print("-----------------------")
    block_tef(10, "10")
    print("-----------------------")


if __name__ == '__main__':
    main()

def sum_number(num: str) -> int:
    result = 0
    for i in num:
        result += int(i)
    return result


if __name__ == '__main__':
    print(sum_number(input('Введите число: ')))


def sum_number(num: str) -> int:
    result = 0
    for i in num:
        result += int(i)
    return result


if __name__ == '__main__':
    print(sum_number(input('Enter a number: ')))

# v_2
# def sum_number(num: str) -> int:
#     result = 0
#     for i in num:
#         result += int(i)
#     return result
#
#
# def sum_number_v2(num: str) -> int:
#     return sum(map(int, num))

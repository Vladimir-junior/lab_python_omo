def get_odd_product(arr: list) -> int:
    result_product = 1
    for i, el in enumerate(arr):
        if i % 2 != 0:
            result_product *= el
    return result_product


def remove_max_number(arr: list) -> list:
    max_el = max(arr)
    return [e for e in arr if e != max_el]


def get_max_3_numbers(arr: list) -> list:
    return sorted(arr)[-3:]


def main():
    arr = [7,1,2,4,5,6,8,12]
    print(get_odd_product(arr))
    new_arr = remove_max_number(arr)
    print(new_arr)
    print(get_max_3_numbers(new_arr))


if __name__ == '__main__':
    main()
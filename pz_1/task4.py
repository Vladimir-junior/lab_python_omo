def two_list_to_dict(arr_1: list, arr_2: list) -> dict:
    return dict(zip(arr_1, arr_2))

def main():
    arr_1 = [1, 2, 3, 4, 5]
    arr_2 = ['a', 'b', 'c', 'd', 'e']
    print(two_list_to_dict(arr_1, arr_2))

if __name__ == '__main__':
    main()


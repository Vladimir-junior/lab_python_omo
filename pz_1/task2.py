def world_examination(st: str) -> list[str]:
    result = []
    for i in st.split():
        if i == i[::-1]:
            result.append(i)

    return result


if __name__ == '__main__':
    print(world_examination(input('Введите строку: ')))
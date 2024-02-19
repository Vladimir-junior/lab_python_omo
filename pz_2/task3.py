def get_matrix(m: int, n: int) -> list:
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            element = int(input(f"Введите элемент [{i+1},{j+1}]: "))
            row.append(element)
        matrix.append(row)
    return matrix

def sum_of_rows(matrix):
    if not matrix:
        print("Матрица пустая.")
        return []

    sums = []
    for row in matrix:
        row_sum = sum(row)
        sums.append(row_sum)
    return sums


def main():
    m = int(input("Введите количество строк матрицы: "))
    n = int(input("Введите количество столбцов матрицы: "))
    matrix = get_matrix(m, n)
    print("------------")
    for row in matrix:
        print(row)
    print("------------")
    print(sum_of_rows(matrix))

if __name__ == '__main__':
    main()




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
    sums = []
    for row in matrix:
        row_sum = sum(row)
        sums.append(row_sum)
    return sums


def main():
    m = int(input("Введите количество строк матрицы: "))
    n = int(input("Введите количество столбцов матрицы: "))
    matrix = get_matrix(m, n)
    sums = sum_of_rows(matrix)
    print("------------")
    for i, row in enumerate(matrix):
        print(f'{row} = {sums[i]}')
    print("------------")

if __name__ == '__main__':
    main()




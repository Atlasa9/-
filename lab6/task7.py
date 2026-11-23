# Дана матрица размера M × N. Поменять местами столбцы, содержащие минимальный и максимальный элементы матрицы.

def main():
    m = int(input("Введите количество строк M: "))
    n = int(input("Введите количество столбцов N: "))

    if m <= 0 or n <= 0:
        print("Размеры должны быть положительными")
        return

    matrix = []

    for i in range(m):
        row = list(map(float, input(f"Строка {i + 1} ({n} чисел через пробел): ").split()))
        if len(row) != n:
            print("Количество элементов строки должно быть равно", n)
            return
        matrix.append(row)

    min_value = matrix[0][0]
    max_value = matrix[0][0]
    min_column = 0
    max_column = 0

    for i in range(m):
        for j in range(n):
            if matrix[i][j] < min_value:
                min_value = matrix[i][j]
                min_column = j
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_column = j

    for i in range(m):
        matrix[i][min_column], matrix[i][max_column] = matrix[i][max_column], matrix[i][min_column]

    print("Преобразованная матрица:")
    for i in range(m):
        print(*matrix[i])

if __name__ == "__main__":
    main()
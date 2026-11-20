# Дана матрица размера M × N. Преобразовать матрицу, поменяв местами минимальный и максимальный элемент в каждой строке.

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

    for i in range(m):
        min_index = 0
        max_index = 0

        for j in range(1, n):
            if matrix[i][j] < matrix[i][min_index]:
                min_index = j
            if matrix[i][j] > matrix[i][max_index]:
                max_index = j

        matrix[i][min_index], matrix[i][max_index] = matrix[i][max_index], matrix[i][min_index]

    print("Преобразованная матрица:")
    for i in range(m):
        print(*matrix[i])

if __name__ == "__main__":
    main()
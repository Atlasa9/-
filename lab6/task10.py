# Дана квадратная матрица A порядка M. Найти сумму элементов каждой ее диагонали, параллельной главной (начиная с одноэлементной диагонали).

def main():
    m = int(input("Введите количество строк M: "))
    n = m

    if m <= 0:
        print("Размеры должны быть положительными")
        return

    matrix = []

    for i in range(m):
        row = list(map(float, input(f"Строка {i + 1} ({n} чисел через пробел): ").split()))
        if len(row) != n:
            print("Количество элементов строки должно быть равно", n)
            return
        matrix.append(row)

    for offset in range(-(m - 1), m):
        total = 0

        i = max(0, -offset)
        j = max(0, offset)

        while i < m and j < m:
            total += matrix[i][j]
            i += 1
            j += 1

        if offset == 0:
            print("Главная диагональ — сумма:", total)
        else:
            print("Диагональ j-i =", offset, "— сумма:", total)

if __name__ == "__main__":
    main()

# Дана целочисленная матрица размера M × N. Найти номер первого из ее столбцов, содержащих только нечетные числа. Если таких столбцов нет, то вывести 0.

def main():
    m = int(input("Введите количество строк M: "))
    n = int(input("Введите количество столбцов N: "))

    if m <= 0 or n <= 0:
        print("Размеры должны быть положительными")
        return

    matrix = []

    for i in range(m):
        row = list(map(int, input(f"Строка {i + 1} ({n} чисел через пробел): ").split()))
        if len(row) != n:
            print("Количество элементов строки должно быть равно", n)
            return
        matrix.append(row)

    column_number = 0

    for j in range(n):
        all_odd = True

        for i in range(m):
            if matrix[i][j] % 2 == 0:
                all_odd = False
                break

        if all_odd:
            column_number = j + 1
            break

    print("Номер столбца:", column_number)

if __name__ == "__main__":
    main()
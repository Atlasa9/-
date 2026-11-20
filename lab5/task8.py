# Дан массив A размера N. Найти минимальный элемент из его элементов с четными номерами: A2, A4, A6

numbers = list(map(int, input("Введите элементы массива через пробел: ").split()))
n = len(numbers)

if n < 2:
    print("Требуется не менее 2 элементов.")
else:

    minimal = numbers[1]

    for i in range(3, n, 2):
        if numbers[i] < minimal:
            minimal = numbers[i]

    print("Минимальный элемент с чётными номерами:", minimal)
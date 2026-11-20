# Дан массив A размера N.
# Вывести вначале его элементы с нечетными номерами в порядке возрастания номеров, а затем — элементы с четными номерами в порядке убывания номеров

n = int(input("Введите размер массива N: "))
if n <= 0:
    print("N должно быть положительным.")
else:
    a = list(map(int, input(f"Введите {n} целых чисел через пробел: ").split()))
    
    if len(a) != n:
        print(f"Ошибка: введено {len(a)} чисел, а ожидалось {n}.")
    else:
        result = []

        for i in range(0, n, 2):
            result.append(a[i])

        start_even = n - 2 if n % 2 == 0 else n - 1

        if start_even >= 1:
            for i in range(start_even, 0, -2):
                result.append(a[i])

        print("Результат:", *result)
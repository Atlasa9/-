# Дан целочисленный массив размера N, содержащий ровно два одинаковых элемента. Найти номера одинаковых элементов и вывести эти номера в порядке возрастания

numbers = list(map(int, input("Введите элементы массива через пробел: ").split()))
n = len(numbers)

if n < 2:
    print("Требуется не менее 2 элементов.")
else:
    found = False

    for i in range(n - 1):
        for j in range(i + 1, n):
            if numbers[i] == numbers[j]:
                print("Номера одинаковых элементов:", i + 1, j + 1)
                found = True
                break

        if found:
            break

    if not found:
        print("Одинаковых элементов нет.")
# Сортировка выбором

def selection_sort(numbers):
    for i in range(len(numbers) - 1):
        min_index = i

        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j

        if min_index != i:
            numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

def main():
    numbers = list(map(int, input("Введите целые числа через пробел: ").split()))

    if not numbers:
        print("Список пуст.")
        return

    selection_sort(numbers)
    print("Отсортированный массив:", numbers)

if __name__ == "__main__":
    main()
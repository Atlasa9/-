# Сортировка вставками

def insertion_sort(numbers):

    for i in range(1, len(numbers)):
        current = numbers[i]
        j = i - 1

        while j >= 0 and numbers[j] > current:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j + 1] = current

def main():
    numbers = list(map(int, input("Введите целые числа через пробел: ").split()))

    if not numbers:
        print("Список пуст.")
        return

    insertion_sort(numbers)
    print("Отсортированный массив:", numbers)

if __name__ == "__main__":
    main()
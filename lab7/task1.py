# Сортировка пузырьком

def bubble_sort(numbers):

    i = 0
    while i < len(numbers) - 1:
        swapped = False

        for j in range(len(numbers) - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True

        if not swapped:
            break

        i += 1

def main():
    numbers = list(map(int, input("Введите целые числа через пробел: ").split()))

    if not numbers:
        print("Список пуст.")
        return

    bubble_sort(numbers)
    print("Отсортированный массив:", numbers)

if __name__ == "__main__":
    main()
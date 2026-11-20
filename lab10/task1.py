# Бинарный поиск

def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2

        if numbers[middle] == target:
            return middle
        if numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1

def main():
    numbers = list(map(int, input("Введите целые числа через пробел: ").split()))
    target = int(input("Введите искомое число: "))

    if not numbers:
        print("Список пуст.")
        return

    position = binary_search(numbers, target)

    if position != -1:
        print(f"Элемент {target} найден на позиции {position} (нумерация с 1: {position + 1}).")
    else:
        print(f"Элемента {target} в списке нет.")

if __name__ == "__main__":
    main()
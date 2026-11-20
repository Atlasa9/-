# Бинарный поиск: Напишите функцию, которая рекурсивно выполняет бинарный поиск заданного элемента в отсортированном массиве.

def binary_search(numbers, target, left, right):

    if left > right:
        return -1

    middle = (left + right) // 2

    if numbers[middle] == target:
        return middle

    if target < numbers[middle]:
        return binary_search(numbers, target, left, middle - 1)
    return binary_search(numbers, target, middle + 1, right)

if __name__ == "__main__":
    numbers = list(map(int, input("Введите целые числа по возрастанию через пробел: ").split()))
    target = int(input("Введите искомое число: "))

    index = binary_search(numbers, target, 0, len(numbers) - 1)

    if index != -1:
        print(f"Элемент {target} найден на позиции {index}.")
    else:
        print(f"Элемент {target} не найден.")
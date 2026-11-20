# Напишите рекурсивное решение головоломки "Ханойская башня".

def hanoi(n, source, target, auxiliary):

    if n == 1:
        print(f"Перенести диск 1: {source} -> {target}")
        return

    hanoi(n - 1, source, auxiliary, target)

    print(f"Перенести диск {n}: {source} -> {target}")

    hanoi(n - 1, auxiliary, target, source)

if __name__ == "__main__":
    n = int(input("Введите количество дисков (>= 1): "))

    if n < 1:
        print("Количество дисков должно быть положительным.")
    else:
        hanoi(n, source="A", target="C", auxiliary="B")
# Разложение числа на сумму простых чисел: Напишите функцию, которая рекурсивно разлагает заданное число на сумму простых чисел.

def prime_sum(n):
    if n == 2:
        return [2]
    if n == 3:
        return [3]

    return [2] + prime_sum(n - 2)

if __name__ == "__main__":
    n = int(input("Введите целое число n (>= 2): "))

    if n < 2:
        print("Разложение на сумму простых чисел невозможно.")
    else:
        terms = prime_sum(n)
        print(str(n) + " = " + " + ".join(map(str, terms)))
# Возведение в степень: Напишите функцию, которая рекурсивно возводит число x в степень n.

def power(x, n):
    if n == 0:
        return 1

    if n < 0:
        return power(1 / x, -n)

    half = power(x, n // 2)
    result = half * half

    if n % 2 == 1:
        result = result * x
    return result

if __name__ == "__main__":
    x = float(input("Введите x: "))
    n = int(input("Введите целую степень n: "))

    if x == 0 and n < 0:
        print("Ноль нельзя возвести в отрицательную степень.")
    else:
        print("Результат:", power(x, n))
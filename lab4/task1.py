# Факториал числа: Напишите функцию, которая рекурсивно вычисляет факториал заданного числа n.

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

n = int(input("Введите целое число n: "))

if n < 0:
    print("Факториал определён только для n >= 0")
else:
    print(f"{n}! = {factorial(n)}")
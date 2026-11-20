# Дано вещественное число A и целое число N (> 0). Используя один цикл, найти сумму 1 + A + A^2 + A^3 + . . . + A^N

a = float(input("Введите вещественное число A: "))
n = int(input("Введите целое число N (> 0): "))

if n <= 0:
    print("Ошибка: N должно быть больше 0.")
else:
    power = 1.0
    total = 0.0
    for i in range(n + 1):
        total += power
        power *= a

    print(f"Сумма: {total:.6f}")
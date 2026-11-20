# Дано целое число N (> 0). Найти произведение 1.1 * 1.2 * 1.3 * . . . (N сомножителей)

n = int(input("Введите целое число N (> 0): "))

if n <= 0:
    print("Ошибка: N должно быть больше 0.")
else:
    product = 1.0
    for i in range(1, n + 1):
        factor = 1.0 + i * 0.1
        product *= factor

    print(f"Произведение: {product:.6f}")
# Даны два ненулевых числа. Найти сумму, разность, произведение и частное их модулей

first = float(input("Введите первое число: "))
second = float(input("Введите второе число: "))

if first == 0 or second == 0:
    print("Числа должны быть ненулевыми")

else:
    first_abs = abs(first)
    second_abs = abs(second)

print(f"Сумма модулей: {first_abs + second_abs}")
print(f"Разность модулей: {first_abs - second_abs}")
print(f"Произведение модулей: {first_abs * second_abs}")
print(f"Частное модулей: {first_abs / second_abs}")
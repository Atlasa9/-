# Дано вещественное число — цена 1 кг конфет. Вывести стоимость 0.1, 0.2, . . . , 1 кг конфет

price_per_kg = float(input("Введите цену за килограмм конфет: "))

for tenths in range(1, 11):
    weight = tenths / 10
    print(f"{weight:.1f} кг: {price_per_kg * weight:.2f} руб.")
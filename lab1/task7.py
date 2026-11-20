# Даны три точки A, B, C на числовой оси. Найти длины отрезков AC и BC и их сумму

a, b, c = map(float, input("Введите координаты трех точек (a b c): ").split())

ac = abs(c - a)
bc = abs(c - b)

print(f"Длина отрезка AC: {ac}")
print(f"Длина отрезка BC: {bc}")
print(f"Сумма отрезков AC и BC: {ac + bc}")
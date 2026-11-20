# Даны координаты трех вершин треугольника: (x1, y1), (x2, y2), (x3, y3). Найти его периметр и площадь

import math

x1, y1, x2, y2, x3, y3 = map(float, input("Введите координаты трех точек (x1 y1 x2 y2 x3 y3): ").split())

a = math.hypot(x2 - x3, y2 - y3)
b = math.hypot(x1 - x3, y1 - y3)
c = math.hypot(x1 - x2, y1 - y2)

P = a + b + c
S = abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2

print(f"Площадь прямоугольника (S) = {S}")
print(f"Периметр прямоугольника (P) = {P}")
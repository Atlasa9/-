# На плоскости расположены три точки: A, B, C.
# Определить, какая из двух последних точек (B или C) расположена ближе к A, и вывести эту точку и ее расстояние от точки A.

import math

xa, ya = map(float, input("Введите координаты точки A: ").split())
xb, yb = map(float, input("Введите координаты точки B: ").split())
xc, yc = map(float, input("Введите координаты точки C: ").split())

dist_b = math.hypot(xb - xa, yb - ya) # расстояние от A до B
dist_c = math.hypot(xc - xa, yc - ya) # расстояние от A до C

if dist_b < dist_c:
    print(f"Точка B ближе, расстояние = {dist_b}")
elif dist_c < dist_b:
    print(f"Точка C ближе, расстояние = {dist_c}")
else:
    print("Точки B и C равноудалены от A")

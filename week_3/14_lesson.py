"""
Даны вещественные числа a, b, c, d, e, f. Известно, что система линейных уравнений:

ax + by = e
cx + dy = f

имеет ровно одно решение. Выведите два числа x и y, являющиеся решением этой системы.

Формат ввода
Вводятся шесть чисел a, b, c, d, e, f
- коэффициенты уравнений системы.
"""
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
if a == 0:
    y = e / b
    x = (f - d * y) / c
else:
    y = (a * f - e * c) / (a * d - b * c)
    x = (e - b * y) / a
print(x, y)

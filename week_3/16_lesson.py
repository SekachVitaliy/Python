"""
Даны числа a, b, c, d, e, f. Решите систему линейных уравнений

ax + by = e
cx + dy = f

Формат ввода
Вводятся 6 чисел a, b, c, d, e, f — коэффициенты уравнений.

Формат вывода
Вывод программы зависит от вида решения этой системы.

Если система не имеет решений, то программа должна вывести единственное число 0.

Если система имеет бесконечно много решений, каждое из которых имеет вид y=px+q, то программа должна вывести число 1,
а затем значения p и q.

Если система имеет единственное решение (x₀,y₀), то программа должна вывести число 2, а затем значения x₀ и y₀.

Если система имеет бесконечно много решений вида x=x₀, y — любое, то программа должна вывести число 3,
а затем значение x₀.

Если система имеет бесконечно много решений вида y=y₀, x — любое, то программа должна вывести число 4,
а затем значение y₀.

Если любая пара чисел (x,y) является решением, то программа должна вывести число 5.
"""
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

det = a * d - b * c
det_x = e * d - b * f
det_y = a * f - e * c

isRes = False

# тривиальное решение
if a == 0 and b == 0 and c == 0 and d == 0 and e == 0 and f == 0:
    print(5)
    isRes = True

# решение вида x - любое, y - заданное
if isRes is False and a == 0 and c == 0:
    if b != 0 and d != 0:
        y1 = e / b
        y2 = f / d

        if y1 == y2:
            print(4, y1)
            isRes = True
        else:
            print(0)
            isRes = True
    elif b == 0 and d == 0:
        print(0)
        isRes = True
    elif b == 0:
        if e != 0:
            print(0)
            isRes = True
        else:
            y = f / d
            print(4, y)
            isRes = True
    elif d == 0:
        if f != 0:
            print(0)
            isRes = True
        else:
            y = e / b
            print(4, y)
            isRes = True

# решение вида x - заданное, y - любое
if isRes is False and b == 0 and d == 0:
    if a != 0 and c != 0:
        x1 = e / a
        x2 = f / c

        if x1 == x2:
            print(3, x1)
            isRes = True
        else:
            print(0)
            isRes = True
    elif a == 0 and c == 0:
        print(0)
        isRes = True
    elif a == 0:
        if e != 0:
            print(0)
            isRes = True
        else:
            x = f / c
            print(3, x)
            isRes = True
    elif c == 0:
        if f != 0:
            print(0)
            isRes = True
        else:
            x = e / a
            print(3, x)
            isRes = True

# решение вида y = px + q
if isRes is False and b * c == d * a and e * c == f * a:
    if b != 0:
        p = -a / b
        q = e / b
        print(1, p, q)
        isRes = True
    elif d != 0:
        p = -c / d
        q = f / d
        print(1, p, q)
        isRes = True
    else:
        print(0)
        isRes = True

# общее решение
if isRes is False and det != 0:
    x = det_x / det
    y = det_y / det
    print(2, x, y)
    isRes = True

# отсутствие решений
if isRes is False and det == 0:
    print(0)
    isRes = True

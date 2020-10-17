"""
По данным целым числам n и k (0≤k≤n) вычислите C из n по k.
Решение оформите в виде функции C(n, k).
Для решения используйте рекуррентное соотношение:

И равенства:
С(n, 1)=n
C(n, n)=1

Формат ввода
Вводятся удовлетворяющие условию задачи числа n и k.

Формат вывода
Выведите ответ на задачу.
"""


def factorial(n):
    f = 1
    i = 2
    while i <= n:
        f *= i
        i += 1
    return f


def C(n, k):
    return int(factorial(n) / factorial(k) / factorial(n - k))


n = float(input())
k = float(input())
print(C(n, k))

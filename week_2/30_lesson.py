"""
Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.

Формат ввода
Вводится целое положительное число.
"""
n = int(input())
divisor = 2
min_divisor = divisor
while divisor <= n:
    if n % divisor == 0:
        min_divisor = divisor
        break
    divisor = divisor + 1

print(min_divisor)

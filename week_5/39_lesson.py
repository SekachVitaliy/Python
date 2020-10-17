"""
В списке все элементы попарно различны. Поменяйте местами минимальный и максимальный элемент этого списка.

Формат ввода
Вводится список целых чисел. Все числа списка находятся на одной строке.

Формат вывода
Выведите ответ на задачу.
"""
List = list(map(int, input().split()))
min = min(List)
max = max(List)
index_min = List.index(min)
index_max = List.index(max)
List[index_max] = min
List[index_min] = max
print(*List)

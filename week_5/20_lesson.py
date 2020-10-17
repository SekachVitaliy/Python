"""
Найдите наибольшее значение в списке и индекс последнего элемента, который имеет данное значение за один проход по
списку, не модифицируя этот список и не используя дополнительного списка.

Выведите два значения.
"""
intList = list(map(int, input().split()))
for i in range(len(intList)):
    if i == 0:
        pos = 0
        number = intList[i]
    if intList[i] >= number:
        pos = i
        number = intList[i]
print(number, pos)

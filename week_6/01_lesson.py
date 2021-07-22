"""
Даны два целочисленных списка A и B, упорядоченных по неубыванию. Объедините их в один упорядоченный список С (то
есть он должен содержать len(A)+len(B) элементов). Решение оформите в виде функции merge(A, B), возвращающей новый
список. Алгоритм должен иметь сложность O(len(A)+len(B)). Модифицировать исходные списки запрещается. Использовать
функцию sorted и метод sort запрещается.

Формат ввода
Программа получает на вход два неубывающих списка, каждый в отдельной строке.

Формат вывода
Программа должна вывести последовательность неубывающих чисел, полученных объединением двух данных списков.
"""


def merge(list1, list2):
    result, it1, it2 = [], iter(list1), iter(list2)
    el1 = next(it1, None)
    el2 = next(it2, None)
    while el1 is not None or el2 is not None:
        if el1 is None or (el2 is not None and el2 < el1):
            result.append(el2)
            el2 = next(it2, None)
        else:
            result.append(el1)
            el1 = next(it1, None)
    print(*result)


a = list(map(int, input('').split()))
b = list(map(int, input('').split()))
merge(a, b)

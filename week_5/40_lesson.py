"""
Дан список, заполненный произвольными целыми числами. Найдите в этом списке два числа, произведение которых
максимально. Выведите эти числа в порядке неубывания. Решение должно иметь сложность O(n), где n - размер списка. То
есть сортировку использовать нельзя.
"""
a = list(map(int, input().split()))
negative_max = min(a)
natural_max = max(a)
a.remove(negative_max)
a.remove(natural_max)
negative_prev = min(a)
natural_prev = max(a)
if negative_max * negative_prev > natural_max * natural_prev:
    print(min(negative_prev, negative_max), max(negative_prev, negative_max))
else:
    print(min(natural_prev, natural_max), max(natural_prev, natural_max))

"""
В данном списке из n≤10⁵ целых чисел найдите три числа,произведение которых максимально.
Решение должно иметь сложность O(n), где n - размер списка. То есть сортировку использовать нельзя.

Выведите три искомых числа в любом порядке.
"""
a = list(map(int, input().split()))
if len(a) <= 3:
    print(*a)
else:
    max_pos_1 = max(a)
    min_neg_1 = min(a)
    a.remove(max_pos_1)
    a.remove(min_neg_1)
    max_pos_2 = max(a)
    min_neg_2 = min(a)
    a.remove(max_pos_2)
    max_pos_3 = max(a)
    if max_pos_1 * max_pos_2 * max_pos_3 > min_neg_2 * min_neg_1 * max_pos_1:
        print(max_pos_1, max_pos_2, max_pos_3)
    else:
        print(min_neg_1, min_neg_2, max_pos_1)

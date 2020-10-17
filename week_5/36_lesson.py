"""
Дан список, упорядоченный по неубыванию элементов в нем.Определите, сколько в нем различных элементов.

Формат ввода
Вводится список чисел. Все числа списка находятся на одной строке.

Формат вывода
Выведите ответ на задачу.
"""
List = list(map(int, input().split()))
res = 0
s = []
for i in range(len(List)):
    if List.count(List[i]) == 1:
        res += 1
    else:
        for j in range(len(s)):
            if s[j] == List[i]:
                break
        else:
            s.append(List[i])
print(res + len(s))

"""
Зачет проводится отдельно в каждом классе. Победителями олимпиады становятся школьники, которые набрали наибольший
балл среди всех участников в данном классе. Для каждого класса определите максимальный балл, который набрал школьник,
не ставший победителем в данном классе.

Формат вывода
Выведите три целых числа.
"""
classes = {}
fin = open('input.txt', 'r', encoding='utf8')
for line in fin:
    number, grade = line.split()[-2:]
    if number in classes:
        classes[number].append(int(grade))
    else:
        classes[number] = [int(grade)]
res = [str(sorted(set(classes[key]))[-2]) for key in sorted(classes, key=int)]
print(*res)

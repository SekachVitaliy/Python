"""
В условиях предыдущей задачи определите количество школьников, ставших победителями в каждом классе. Победителями
объявляются все, кто набрал наибольшее число баллов по данному классу. Гарантируется, что в каждом классе был хотя бы
один участник.

Формат вывода
Выведите три числа: количество победителей олимпиады по 9 классу, по 10 классу, по 11 классу.
"""
fin = open('input.txt', encoding='utf8')
maxes = [0, 0, 0]
count = [0, 0, 0]
for line in fin:
    surname, name, clas, grade = line.split(' ')
    if clas == '9':
        if int(grade) > maxes[0]:
            maxes[0] = int(grade)
            count[0] = 1
        elif int(grade) == maxes[0]:
            count[0] += 1
    elif clas == '10':
        if int(grade) > maxes[1]:
            maxes[1] = int(grade)
            count[1] = 1
        elif int(grade) == maxes[1]:
            count[1] += 1
    elif clas == '11':
        if int(grade) > maxes[2]:
            maxes[2] = int(grade)
            count[2] = 1
        elif int(grade) == maxes[2]:
            count[2] += 1
print(*count)

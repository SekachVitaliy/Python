"""
Дана строка. Замените в этой строке все появления буквы h на букву H, кроме первого и последнего вхождения.

Формат ввода
Вводится строка.

Формат вывода
Выведите ответ на задачу.
"""
string = input()
first_h = string.find('h')
last_h = string.rfind('h')
out = string[0:first_h+1]
last = string[last_h:]
string = string.replace('h', 'H')
middle = string[first_h+1:last_h]
out = out + middle + last
print(out)

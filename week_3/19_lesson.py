"""
Дана строка, в которой буква h встречается минимум два раза.Удалите из этой строки первое и последнее вхождение
буквы h,а также все символы, находящиеся между ними.

Формат ввода
Вводится строка.

Формат вывода
Выведите ответ на задачу.
"""
string = input()
len = len(string)
back = string[::-1]
first_h = string.find('h')
second_h = back.find('h')
out = string[0:first_h] + string[len - second_h:]
print(out)

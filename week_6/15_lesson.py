"""
В олимпиаде по информатике принимало участие N человек. Определите школы, из которых в олимпиаде принимало участие
больше всего участников. В этой задаче необходимо считывать данные построчно, не сохраняя в памяти данные обо всех
участниках, а только подсчитывая число участников для каждой школы.

Формат ввода
Информация о результатах олимпиады записана в файле, каждая из строк которого имеет вид:
фамилия имя школа балл
Фамилия и имя — текстовые строки, не содержащие пробелов. Школа — целое число от 1 до 99. Балл — целое число от 0 до
100.

Формат вывода
Выведите номера этих школ в порядке возрастания.
"""
schools = {}
out = []
fin = open('input.txt', encoding='utf8')
for line in fin:
    surname, name, school, grade = line.split(' ')
    if school in schools:
        schools[school] += 1
    else:
        schools[school] = 1
max_quantity = max(schools.items(), key=lambda x: x[1])[1]
out_schools = list(filter(lambda x: x[1] == max_quantity, schools.items()))
for school in out_schools:
    out.append(int(school[0]))
print(*sorted(out), sep=' ')

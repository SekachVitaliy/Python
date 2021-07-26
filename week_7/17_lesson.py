"""
Дан текст. Выведите слово, которое в этом тексте встречается чаще всего. Если таких слов несколько, выведите то,
которое меньше в лексикографическом порядке.

Формат ввода
Вводится текст.

Формат вывода
Выведите ответ на задачу.
"""
fin = open('input.txt', 'r', encoding='utf-8')
myDict = dict()
out = []
text = fin.read()
for word in text.split():
    if word in myDict:
        myDict[word] += 1
    else:
        myDict[word] = 1
value = sorted(myDict.values(), reverse=True)[0]
for key in myDict.keys():
    if myDict[key] == value:
        out.append(key)
print(sorted(out)[0])

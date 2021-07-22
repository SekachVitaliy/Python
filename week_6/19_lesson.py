"""
Формат входных данных аналогичен предыдущей задаче. Выведите список всех партий, участвовавших в выборах,
отсортировав его в порядке убывания количества голосов избирателей, а при равном количестве голосов - в
лексикографическом порядке.
"""
fin = open('input.txt', 'r', encoding='utf8')
parties = {}
votes = False
file = [line.rstrip() for line in fin]
for item in file:
    if item == 'PARTIES:':
        votes = False
    elif item == 'VOTES:':
        votes = True
    elif not votes:
        parties[item] = 0
    else:
        for consignment in parties:
            if item == consignment:
                parties[consignment] += 1
out = []
for consignment in parties:
    out.append({'consignment': consignment, 'n': int(parties[consignment])})

out = sorted(out, key=lambda i: (-i['n'], i['consignment']))
for i in range(len(out)):
    print(out[i]['consignment'])

# За многие годы заточения узник замка Иф проделал в стене прямоугольное отверстие размером D×E. Замок Иф сложен из
# кирпичей, размером A×B×C. Определите, сможет ли узник выбрасывать кирпичи в море через это отверстие (очевидно,
# стороны кирпича должны быть параллельны сторонам отверстия).
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
x1 = d - a
x2 = d - b
x3 = d - c
x4 = e - a
x5 = e - b
x6 = e - c
if x1 >= 0 and x4 >= 0:
    print('Yes')
elif x1 >= 0 and x5 >= 0:
    print('Yes')
elif x1 >= 0 and x6 >= 0:
    print('Yes')
elif x2 >= 0 and x4 >= 0:
    print('Yes')
elif x2 >= 0 and x5 >= 0:
    print('Yes')
elif x2 >= 0 and x6 >= 0:
    print('Yes')
elif x3 >= 0 and x4 >= 0:
    print('Yes')
elif x3 >= 0 and x5 >= 0:
    print('Yes')
elif x3 >= 0 and x6 >= 0:
    print('Yes')
else:
    print('No')

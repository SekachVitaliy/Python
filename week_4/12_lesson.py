"""
Использование глобальных переменных
"""


def f():
    global a
    print(a)
    a = 1

    
a = 0
f()
print(a)

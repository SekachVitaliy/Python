s = 'aaaaaa'
while s.find('aa') != -1:
    s = (s.replace('aa', 'a'))
    print(s.count('a'))
print(s)

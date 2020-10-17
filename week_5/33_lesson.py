a = list(map(int, input().split()))
i = 0
while i < len(a):
    if a[i] % 2 != 0:
        a.pop(i)
    else:
        i += 1
print(*a)

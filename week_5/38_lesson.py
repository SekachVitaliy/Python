List = list(map(int, input().split()))
List.insert(0, List.pop())
print(*List)

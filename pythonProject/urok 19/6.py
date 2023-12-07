a = list(input().split())
for x in a:
    a[a.index(x)] = len(a[a.index(x)])
print(*a)

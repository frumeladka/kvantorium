lst = list(map(int, input().split()))
ans = []
for i in range(len(lst)):
    ans.append(min(lst))
    lst.pop(lst.index(min(lst)))
print(*ans)

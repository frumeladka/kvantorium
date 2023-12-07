lst = []
n = 0
ans = []
lst.append(input())
lst.append(input())
lst.append(input())
lst.append(input())
lst.append(input())
lst.append(input())
while n != 6:
    if ' ' not in lst[n]:
        ans.append(lst[n])
    n += 1
print(*ans)

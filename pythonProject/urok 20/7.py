lst = list(map(float, input().split()))
for ind, dat in enumerate(lst):
    if dat < 0:
        lst[ind] = -1.0
print(*lst)

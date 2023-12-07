a = list(map(int, input().split()))
for ind, dat in enumerate(a):
    a[ind] = dat**2
print(*a)
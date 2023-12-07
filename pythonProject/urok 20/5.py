a = input().split()
for ind, dat in enumerate(a):
    a[ind] = dat + ' ' + dat
print(*a)
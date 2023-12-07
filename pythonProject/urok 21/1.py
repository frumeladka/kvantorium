N = int(input())
s1 = [[1]*N]*N
for ind, a in enumerate(s1):
    s1[ind][-1] = 5
for i in s1:
    print(*i)

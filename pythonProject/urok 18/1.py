p = [0] * 10
while sum(p) != 6:
    a = int(input())
    if p[a] == 1:
        continue
    p[a] = 1
print(*p)

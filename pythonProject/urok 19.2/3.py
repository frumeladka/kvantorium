m, n = map(int, input().split())
if m % 2 == 0:
    m += 1
print(*list(range(m, n+1, 2)))

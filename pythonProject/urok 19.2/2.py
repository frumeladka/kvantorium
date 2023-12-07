m, n = map(int, input().split())
if m < n:
    print(*list(range(m, n+1)))
else:
    print(*list(range(m, n-1, -1)))

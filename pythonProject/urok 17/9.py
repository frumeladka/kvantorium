n = int(input())
a = 0
ans = 1000
while a < n:
    ans *= 1.05
    a += 1
print(round(ans, 2))

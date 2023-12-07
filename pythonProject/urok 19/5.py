a = list(map(abs, map(int, input().split())))
sumA = 0
for x in a:
    if x % 2 == 1:
        sumA += x
print(sumA)
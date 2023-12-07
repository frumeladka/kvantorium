a = 100
n = []
while a < 1000:
    if a % 47 == 43 and a % 3 == 0:
        n.append(a)
    a += 1
print(*n)

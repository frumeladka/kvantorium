a = []
while True:
    n = int(input())
    if 0 < n <= 5:
        a.append(n)
    else:
        break
print(a.count(5))

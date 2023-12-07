a, b = map(int, input().split())
lst = []
while a <= b:
    lst.append(a**2)
    a += 1
print(*lst)

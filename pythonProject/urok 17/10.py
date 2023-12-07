a, b = map(int, input().split())
s = 0
lst = []
while s <= b:
    lst.append(a+s)
    s += 1
while lst[0] % 2 == 0:
    lst.pop(0)
print(*lst[::2])

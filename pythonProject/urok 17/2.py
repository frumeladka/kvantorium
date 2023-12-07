a = float(input())
s = 2
lst = []
while s <= 10:
    lst.append(round(a*s, 2))
    s += 1
print(*lst)

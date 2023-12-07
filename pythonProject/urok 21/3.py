lst = []
a = int(input())
for i in range(2, a):
    for a in range(2, i):
        if i % a == 0:
            break
    else:
        lst.append(i)
print(*lst)

a = int(input())
n = 0
lst = [1, 1]
while n <= a-3:
    lst.append(lst[n]+lst[n+1])
    n += 1
print(*lst)

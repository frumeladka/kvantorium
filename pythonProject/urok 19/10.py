n = int(input())
lst = []
for i in range(1, n):
    if i % 3 == 0 or i % 5 == 0:
        lst.append(i)
print(sum(lst))

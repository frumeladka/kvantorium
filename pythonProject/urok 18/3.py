lst = list(input().split())
n = 0
a = 'Нет'
while n != len(lst):
    if len(lst[n]) <5:
        break
    n+=1
else:
    a = 'ДА'

print(a)

lst = list(input().split())
n = 0
while n != len(lst):
    if (lst[n][0]).lower() == (lst[n][-1]).lower():
        print('ДА')
        break
    n += 1
else:
    print('НЕТ')

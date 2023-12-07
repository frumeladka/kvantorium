a = input().split()
for x in range(len(a)):
    a[x] = a[x].lower()
for i in range(len(a)-1):
    ind = -1 if a[i][-1] != 'ь' and 'ы' and 'ъ' else -2
    if a[i][ind] != a[i+1][0]:
        print('НЕТ')
        break
else:
    print('ДА')
print(a)

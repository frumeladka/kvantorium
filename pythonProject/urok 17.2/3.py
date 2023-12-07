a = []
s = ['стоп', 'хватит', 'достаточно']
while True:
    n = input()
    if n not in s:
        a.append(n)
    else:
        break
print(len(a))

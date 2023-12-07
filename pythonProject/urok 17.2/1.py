a = []
while True:
    n = input()
    if n != 'КОНЕЦ':
        a.append(n)
    else:
        a.append('КОНЕЦ')
        break
print(*a)

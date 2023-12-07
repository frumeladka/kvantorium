a = list(input().split())
if 'Москва' in a:
    a.remove('Москва')
    print(*a)
else:
    print(*a)




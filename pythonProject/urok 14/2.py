a = input().replace(' ', '')
if a.lower() == a[::-1].lower():
    print('ДА')
else:
    print('НЕТ')

a, b, c = map(int, input().split())
if a == b and a == c and b == c:
    print('Равносторонний')
elif a == b or a == c or b == c:
    print('Равнобедренный')
else:
    print('Разносторонний')

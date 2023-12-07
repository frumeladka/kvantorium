a = int(input())
b = int(input())
operation = input()
if operation in ('+','-','*','/'):
    if operation == '+':
        print(a+b)
    elif operation == '-':
        print(a-b)
    elif operation == '*':
        print(a*b)
    else:
        if b != 0:
            print(a/b)
        else:
            print('На ноль делить нельзя')
else:
    print('Неверная операция!')

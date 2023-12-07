a = input()
while True:
    n = a.replace('--', '-')
    if a == n:
        print(a)
        break
    else:
        a = n

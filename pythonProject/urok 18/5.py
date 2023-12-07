n = int(input())
N = 0
lst = []
if n < 100:
    while N <= n:
        if N + 15 <= n:
            lst.append(N+15)
        N += 15
    print(*lst)
else:
    print('слишком большое значение n')
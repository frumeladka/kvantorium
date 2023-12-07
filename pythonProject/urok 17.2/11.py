a = int(input())
print(sum(map(int, (list(str(a))))))
print(len(str(a)))
n = 0
ans = 1
while n < len(str(a)):
    ans = int(list(str(a))[n]) * ans
    n += 1
print(ans)
print(sum(map(int, (list(str(a)))))//len(str(a)))
print(list(str(a))[0])
print(int(list(str(a))[0]) + int(list(str(a))[-1]))

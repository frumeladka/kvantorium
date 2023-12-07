num = list(input())
num = num[::-1]
a = 0
while a < len(num):
    print(*num[a])
    a += 1


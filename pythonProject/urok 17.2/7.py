n = int(input())
a = 0
while n >= 25:
    n -= 25
    a += 1
while n >= 10:
    n -= 10
    a += 1
while n >= 5:
    n -= 5
    a += 1
while n >= 1:
    n -= 1
    a += 1
print(a)

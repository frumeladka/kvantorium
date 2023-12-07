lst = 1
while True:
    a = int(input())
    if a > 0:
        lst = lst * a
    elif a == 0:
        break
print(lst)

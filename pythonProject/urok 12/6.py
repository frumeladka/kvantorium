lst = list(input().split())
print(*lst[0:-1], int(lst[-1]) % 2 != 0)

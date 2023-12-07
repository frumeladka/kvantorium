a = int(input())
s = len(str(a))-1
ans = 1
while s != -1:
    ans = ans * int(str(a)[s])
    s -= 1
print(ans)

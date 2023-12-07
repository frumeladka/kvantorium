m, n = map(int, input().split())
for i in range(m, n):
    if i % 17 == 0 or str(i)[-1] == '9' or i % 15 == 0:
        print(i)

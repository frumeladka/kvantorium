a = [[], [], [], [], []]
a[0] = list(map(int, input().split()))
a[1] = list(map(int, input().split()))
a[2] = list(map(int, input().split()))
a[3] = list(map(int, input().split()))
a[4] = list(map(int, input().split()))
ans = 'ДА'
for x in range(5):
    for y in range(5):
        if x != y:
            if a[x][y] != a[y][x]:
                ans = 'НЕТ'
                break
print(ans)

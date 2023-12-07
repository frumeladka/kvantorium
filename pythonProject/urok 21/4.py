a = [[0, 0, 0, 0,0], [], [], [], [], [], [0, 0, 0, 0, 0]]
a[1] = list(map(int, input().split()))
a[2] = list(map(int, input().split()))
a[3] = list(map(int, input().split()))
a[4] = list(map(int, input().split()))
a[5] = list(map(int, input().split()))
ans = 'ДА'
for y in range(1, 6):
    for x in range(5):
        if a[y][x] == 1:
            if x != 0:
                if a[y-1][x-1] == 1 or a[y][x-1] == 1 or a[y+1][x-1] == 1:
                    ans = 'НЕТ'
                    break
            elif x != 4:
                if a[y-1][x+1] == 1 or a[y][x+1] == 1 or a[y+1][x+1] == 1:
                    ans = 'НЕТ'
                    break
            if a[y+1][x] == 1 or a[y-1][x] == 1:
                ans = 'НЕТ'
                break
print(ans)

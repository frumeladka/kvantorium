lst = list(map(float, input().split()))
lowest = lst[0]
step = 0
for ind, dat in enumerate(lst):
    if ind == len(lst):
        break
    elif lowest > dat:
        lowest = dat
print(lowest)


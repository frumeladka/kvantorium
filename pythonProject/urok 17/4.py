lst = []
while True:
    lst.append(int(input()))
    if lst[-1] == 0:
        print(sum(lst))
        break

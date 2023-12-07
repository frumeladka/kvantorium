a = input()
n = 0
lst = []
colvo = 0
while colvo < a.count('ра'):
    lst.append(a.find('ра', n))
    n = a.find('ра', n)+1
    colvo += 1
print(*lst)

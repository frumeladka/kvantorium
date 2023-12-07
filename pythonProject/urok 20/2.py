a = input()
s = '0123456789'
if a[0:3] == '+7(' and a[3] in s and a[4] in s and a[5] in s and a[6] == ')' and a[7] in map(str, range(10)) and a[8] in map(str, range(10)) and a[9] in map(str, range(10)) and a[10] == '-' and a[11] in map(str, range(10)) and a[12] in map(str, range(10)) and a[13] == '-' and a[14] in map(str, range(10)) and a[15] in map(str, range(10)):
    print('Yes')
else: print('No')

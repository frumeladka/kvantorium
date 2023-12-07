m, d = map(int, input().split())
s = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m1, m2, d1, d2 = 0, 0, 0, 0
if s[m-1] == d:
    m1 = m
    d1 = d-1
    m2 = m+1
    d2 = 1
elif d == 1:
    m1 = m-1
    d1 = s[m-1]
    m2 = m
    d2 = d + 1
else:
    m1 = m
    d1 = d-1
    m2 = m
    d2 = d+1
print(f"{str(m1).rjust(2, '0')}.{str(d1).rjust(2, '0')} {str(m2).rjust(2, '0')}.{str(d2).rjust(2, '0')}")

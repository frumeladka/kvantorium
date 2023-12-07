m = int(input())
p = int(input())
n = int(input())
print(f'1 {m}')
for i in range(2, n+1):
    print(f'{i} {m/100*(p+100)}')
    m = m/100*(p+100)

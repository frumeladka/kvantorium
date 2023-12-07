a, b, c = map(int, input().split())
print(((a + b) > c) and ((b+c) > a) and ((a + c) > b))
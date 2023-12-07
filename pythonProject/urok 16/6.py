m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
a, b, c = map(int, input().split())
msg = [m[a-1] if a != 1 and 4 else '#'+m[a-1], m[b-1] if b != 1 and 4 else '#'+m[b-1], m[c-1] if c != 1 and 4 else '#'+m[c-1]]
print(*msg)

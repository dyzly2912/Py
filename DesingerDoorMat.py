N, M = map(int, input().split())
pattern = '.|.'

for i in range(1, N, 2):
    print((pattern * i).center(M,'-'))
print('WELCOME'.center(M,'-'))
for i in reversed(range(1, N, 2)):
    print((pattern * i).center(M,'-'))
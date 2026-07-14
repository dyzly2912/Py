from itertools import groupby

S = groupby(input())
L = []
for k, c in S:
    L.append((len(list(c)),int(k)))
print(*L)

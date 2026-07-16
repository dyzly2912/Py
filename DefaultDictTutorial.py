from collections import defaultdict

n, m = map(int, input().split())
A = []
B = []
for i in range(n):
    A.append(input())
for i in range(m):
    B.append(input())
d = defaultdict(list)
for i in range(n):
    d[A[i]].append(i+1)

for b in B:
    if b in d:
        print(*d[b])
    else:
        print(-1)

# Cách viết sạch hơn để so sánh
from collections import defaultdict
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

word_positions = defaultdict(list)
for i in range(1, n + 1):
    word = input().rstrip()
    word_positions[word].append(i)

for _ in range(m):
    query = input().rstrip()
    if query in word_positions:
        print(*word_positions[query])
    else:
        print(-1)
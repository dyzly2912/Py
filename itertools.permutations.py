# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

String, k = input().split()
k = int(k)
L = ((permutations(sorted(String),k)))
for x in L:
    print(''.join(x))

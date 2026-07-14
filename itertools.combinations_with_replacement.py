# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

String, k = input().split()

k = int(k)
sort = "".join(sorted(String))

L = combinations_with_replacement(sort,k)

for x in L:
    print(''.join(x))
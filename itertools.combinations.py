# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

String, k = input().split()
k = int(k)
s = "".join(sorted(String))
for i in range(1, k + 1):
    for j in combinations(s,i):
        print(''.join(j))
    

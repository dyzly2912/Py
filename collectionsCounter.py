from collections import Counter

x = int(input().strip())
shoe_sizes = list(map(int, input().split()))
inventory = Counter(shoe_sizes)

n = int(input().strip())
earnings = 0
for _ in range(n):
    size, price = map(int, input().split())
    if inventory[size] > 0:
        earnings += price
        inventory[size] -= 1

print(earnings)

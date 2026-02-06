from itertools import product

# Read K and M
K, M = map(int, input().split())

lists = []

# Read K lists
for _ in range(K):
    data = list(map(int, input().split()))
    lists.append(data[1:])  # ignore first element

# Compute maximum value
result = max(sum(x*x for x in combo) % M for combo in product(*lists))

print(result)

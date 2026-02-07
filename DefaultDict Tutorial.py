# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

# Read n and m
n, m = map(int, input().split())

# Dictionary to store positions
positions = defaultdict(list)

# Read Group A words
for i in range(1, n + 1):
    word = input().strip()
    positions[word].append(i)

# Read Group B words and print result
for _ in range(m):
    word = input().strip()
    if word in positions:
        print(*positions[word])
    else:
        print(-1)

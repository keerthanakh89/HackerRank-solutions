# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

s, k = input().split()
k = int(k)

for p in permutations(sorted(s), k):
    print("".join(p))

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())

comb = list(combinations(letters, k))
count = sum(1 for c in comb if 'a' in c)

print(count / len(comb))

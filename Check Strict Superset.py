# Read set A
A = set(map(int, input().split()))

# Number of other sets
n = int(input())

# Assume A is a strict superset unless proven otherwise
is_strict = True

for _ in range(n):
    S = set(map(int, input().split()))
    if not (A > S):   # strict superset check
        is_strict = False
        break

print(is_strict)

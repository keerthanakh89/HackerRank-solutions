# Read number of test cases
t = int(input())

for _ in range(t):
    # Read set A
    n = int(input())
    A = set(map(int, input().split()))
    
    # Read set B
    m = int(input())
    B = set(map(int, input().split()))
    
    # Check subset
    print(A.issubset(B))

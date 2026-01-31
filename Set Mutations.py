# Read number of elements in set A
n = int(input())

# Read elements of set A
A = set(map(int, input().split()))

# Read number of other sets (operations)
m = int(input())

# Perform each mutation operation
for _ in range(m):
    operation, _ = input().split()
    other_set = set(map(int, input().split()))
    
    # Apply the operation dynamically
    getattr(A, operation)(other_set)

# Print the sum of elements in set A
print(sum(A))

# Read number of elements
n = int(input())

# Read the set elements
s = set(map(int, input().split()))

# Read number of commands
m = int(input())

# Process each command
for _ in range(m):
    command = input().split()
    
    if command[0] == "pop":
        s.pop()
    elif command[0] == "remove":
        s.remove(int(command[1]))
    elif command[0] == "discard":
        s.discard(int(command[1]))

# Print the sum of remaining elements
print(sum(s))

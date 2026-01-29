# Number of students subscribed to English newspaper
n = int(input())
english = set(map(int, input().split()))

# Number of students subscribed to French newspaper
m = int(input())
french = set(map(int, input().split()))

# Find union of both sets
total_students = english.union(french)

# Print total number of students with at least one subscription
print(len(total_students))

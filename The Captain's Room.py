# Read group size
k = int(input())

# Read room numbers
rooms = list(map(int, input().split()))

# Convert to set for unique rooms
unique_rooms = set(rooms)

# Apply the formula
captain_room = (sum(unique_rooms) * k - sum(rooms)) // (k - 1)

print(captain_room)

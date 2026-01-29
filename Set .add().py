# Read number of country stamps
n = int(input())

# Create an empty set
countries = set()

# Add each country to the set
for _ in range(n):
    countries.add(input().strip())

# Print the number of distinct country stamps
print(len(countries))

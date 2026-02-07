# Enter your code here. Read input from STDIN. Print output to STDOUTfrom collections import Counter
from collections import Counter
# Number of shoes
n = int(input())

# Shoe sizes
shoe_sizes = list(map(int, input().split()))

# Create Counter
inventory = Counter(shoe_sizes)

# Number of customers
customers = int(input())

total_money = 0

# Process each customer
for _ in range(customers):
    size, price = map(int, input().split())
    
    if inventory[size] > 0:
        total_money += price
        inventory[size] -= 1

# Output total earnings
print(total_money)

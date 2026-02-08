from collections import OrderedDict

n = int(input())
items = OrderedDict()

for _ in range(n):
    name, price = input().rsplit(' ', 1)
    price = int(price)
    items[name] = items.get(name, 0) + price

for item, total in items.items():
    print(item, total)

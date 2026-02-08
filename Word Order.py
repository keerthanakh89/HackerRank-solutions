from collections import Counter

n = int(input())
words = []

for _ in range(n):
    words.append(input().strip())

count = Counter(words)

print(len(count))
print(*count.values())

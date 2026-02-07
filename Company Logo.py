from collections import Counter

if __name__ == '__main__':
    s = input().strip()

    # Count character frequencies
    counter = Counter(s)

    # Sort by frequency descending, then alphabetically
    for char, count in sorted(counter.items(), key=lambda x: (-x[1], x[0]))[:3]:
        print(char, count)

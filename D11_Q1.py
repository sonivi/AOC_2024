from collections import Counter

def transform(counts):
    new_counts = Counter()
    for s, cnt in counts.items():
        if s == "0":
            # Rule 1
            new_counts["1"] += cnt
        else:
            digits = len(s)
            if digits % 2 == 0:
                # Even number of digits => split
                half = digits // 2
                left_part = str(int(s[:half]))
                right_part = str(int(s[half:]))
                new_counts[left_part] += cnt
                new_counts[right_part] += cnt
            else:
                # Odd number of digits => multiply by 2024
                val = int(s) * 2024
                new_counts[str(val)] += cnt
    return new_counts

def main():
    with open("inp.txt", "r") as f:
        stones = f.read().strip().split()

    counts = Counter(stones)

    # Apply 75 transformations
    for i in range(75):
        counts = transform(counts)
        if i==25-1:
            # Print the number of stones after 25 transformations
            print(f"part1 answer= {sum(counts.values())}")
        if i==75-1:
            # Print the number of stones after 75 transformations
            print(f"part1 answer= {sum(counts.values())}")

if __name__ == "__main__":
    main()

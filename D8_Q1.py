def read_input(file="inp.txt"):
    """Reads the grid input from inp.txt."""
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]

def find_antennas(grid):
    """Find all antennas and their frequencies."""
    antennas = {}
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char.isalnum():  # Valid antenna frequencies
                antennas.setdefault(char, []).append((x, y))
    return antennas

def calculate_antinodes(grid):
    """Calculate the number of unique antinodes in the grid."""
    antennas = find_antennas(grid)
    antinodes = set()

    for freq, positions in antennas.items():
        n = len(positions)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = positions[i]
                x2, y2 = positions[j]

                # Calculate midpoints
                dx, dy = x2 - x1, y2 - y1

                # Midpoint in one direction
                mx1, my1 = x1 - dx, y1 - dy
                if 0 <= mx1 < len(grid[0]) and 0 <= my1 < len(grid):
                    antinodes.add((mx1, my1))

                # Midpoint in the other direction
                mx2, my2 = x2 + dx, y2 + dy
                if 0 <= mx2 < len(grid[0]) and 0 <= my2 < len(grid):
                    antinodes.add((mx2, my2))

    return len(antinodes)

def solve():
    """Solve the problem using inp.txt."""
    grid = read_input("inp.txt")
    return calculate_antinodes(grid)

if __name__ == "__main__":
    result = solve()
    print(f"The number of unique locations containing antinodes is: {result}")
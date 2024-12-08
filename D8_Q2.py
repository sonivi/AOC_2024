import math
from itertools import combinations

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
        # Add all antenna positions as antinodes
        antinodes.update(positions)

        # Calculate all straight-line antinodes for the given frequency
        for p1, p2 in combinations(positions, 2):
            x1, y1 = p1
            x2, y2 = p2

            # Compute the step direction for the line
            dx, dy = x2 - x1, y2 - y1
            gcd = abs(dx) if dy == 0 else abs(dy) if dx == 0 else abs(math.gcd(dx, dy))
            dx //= gcd
            dy //= gcd

            # Extend in both directions along the line
            x, y = x1, y1
            while 0 <= x < len(grid[0]) and 0 <= y < len(grid):
                antinodes.add((x, y))
                x -= dx
                y -= dy

            x, y = x2, y2
            while 0 <= x < len(grid[0]) and 0 <= y < len(grid):
                antinodes.add((x, y))
                x += dx
                y += dy

    return len(antinodes)

def solve():
    """Solve the problem using inp.txt."""
    grid = read_input("inp.txt")
    return calculate_antinodes(grid)

if __name__ == "__main__":
    result = solve()
    print(f"The number of unique locations containing antinodes is: {result}")

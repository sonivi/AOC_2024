from collections import deque

with open('inp.txt', 'r') as file:
    stones = deque(map(int, file.read().strip().split()))

def optimized_blink(stones, total_blinks):
    for _ in range(total_blinks):
        new_stones = deque()
        while stones:
            stone = stones.popleft()
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                mid = len(str(stone)) // 2
                left, right = int(str(stone)[:mid]), int(str(stone)[mid:])
                new_stones.extend([left, right])
            else:
                new_stones.append(stone * 2024)
        stones = new_stones
    return len(stones)

total_stones = optimized_blink(stones, 75)
print(total_stones)

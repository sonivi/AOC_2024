def parse_input(input_data):
    sections = input_data.strip().split("\n\n")
    rules = [tuple(map(int, line.split("|"))) for line in sections[0].splitlines()]
    updates = [list(map(int, line.split(","))) for line in sections[1].splitlines()]
    return rules, updates

def is_correct_order(update, rules):
    positions = {page: i for i, page in enumerate(update)}
    for x, y in rules:
        if x in positions and y in positions:
            if positions[x] > positions[y]:  # x must appear before y
                return False
    return True

def calculate_middle_sum(rules, updates):
    total = 0
    for update in updates:
        if is_correct_order(update, rules):
            middle_index = len(update) // 2
            total += update[middle_index]
    return total

def main():
    with open("inp.txt", "r") as f:
        input_data = f.read()

    rules, updates = parse_input(input_data)
    result = calculate_middle_sum(rules, updates)
    print(f"Sum of middle page numbers: {result}")

if __name__ == "__main__":
    main()